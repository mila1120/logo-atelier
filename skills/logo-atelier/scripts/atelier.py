#!/usr/bin/env python3
"""Logo Atelier local workflow + replaceable model adapters. Standard library only."""
import argparse
import base64
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys
import urllib.error
import urllib.request
import uuid
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
SVG_NS = 'http://www.w3.org/2000/svg'
ALLOWED = {'svg','g','defs','path','rect','circle','ellipse','polygon','polyline','line',
           'title','desc','clipPath','mask','linearGradient','radialGradient','stop'}

def write_json(path, data):
    path = Path(path)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

def validate_svg(text):
    """Strict portable master profile, not an all-purpose SVG sanitizer or aesthetic judge."""
    errors = []
    if len(text.encode()) > 2_000_000:
        return {'passed': False, 'errors': ['SVG exceeds 2 MB profile limit']}
    if re.search(r'<!DOCTYPE|<!ENTITY|<\?', text, re.I):
        errors.append('Remove declarations, entities and processing instructions')
    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        return {'passed': False, 'errors': ['Invalid XML: ' + str(exc)]}
    if root.tag != '{'+SVG_NS+'}svg':
        errors.append('Root must be SVG with the SVG namespace')
    try:
        box = [float(v) for v in re.split(r'[\s,]+', root.attrib['viewBox'].strip())]
        if len(box)!=4 or not all(math.isfinite(v) for v in box) or min(box[2:])<=0:
            raise ValueError()
    except (ValueError, KeyError):
        errors.append('viewBox must contain four finite numbers with positive dimensions')
    ids, refs = set(), []
    for node in root.iter():
        tag = node.tag.split('}')[-1]
        if not node.tag.startswith('{'+SVG_NS+'}') or tag not in ALLOWED:
            errors.append('Unsupported master element: ' + tag)
        if 'id' in node.attrib:
            if node.attrib['id'] in ids: errors.append('Duplicate id: '+node.attrib['id'])
            ids.add(node.attrib['id'])
        for key, value in node.attrib.items():
            local = key.split('}')[-1].lower()
            if local.startswith('on') or local in {'href','style','base'}:
                errors.append('Unsupported attribute: '+key)
            for match in re.finditer(r'url\((.*?)\)', value, re.I):
                ref = match.group(1).strip().strip('\'"')
                if not ref.startswith('#'): errors.append('External paint/resource reference')
                else: refs.append(ref[1:])
            if '\\' in value or re.search(r'@import|javascript:|data:|https?://|file:', value, re.I):
                errors.append('Nonportable attribute value: '+key)
    for ref in refs:
        if ref not in ids: errors.append('Missing local reference: '+ref)
    if not any(n.tag.split('}')[-1] in {'path','rect','circle','ellipse','polygon','polyline','line'} for n in root.iter()):
        errors.append('No vector geometry')
    return {'passed': not errors, 'errors': sorted(set(errors)),
            'visual_review': 'pending', 'profile': 'portable-vector-master-v1'}

def initialize(directory, name):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=False)
    for folder in ['source','concepts','master','variants','exports','proof','runs']:
        (directory/folder).mkdir()
    write_json(directory/'brief.json', {'brand_name':name, 'sources':[], 'audience':None,
        'product_purpose':None, 'desired_perception':[], 'hard_constraints':[],
        'references':[], 'must_preserve':[], 'usage_surfaces':[], 'assumptions':[],
        'direction_status':'unconfirmed'})
    write_json(directory/'project.json', {'schema_version':1, 'phase':'discovery',
        'figma':{'file_key':None,'nodes':{}}, 'master':None,'reviews':[],
        'platform':{'ios_minimum':None,'xcode_version':None,'icon_route':None}})
    return {'project':str(directory.resolve()),'status':'initialized'}

def config_role(config, role):
    data=json.loads(Path(config).read_text())
    if data.get('schema_version') != 1: raise ValueError('Unsupported config schema')
    spec=data['roles'][role]
    expected='svg' if role=='svg' else 'image'
    if spec.get('output')!=expected: raise ValueError('Role/output mismatch')
    if spec.get('adapter') not in {'host','gemini'}: raise ValueError('Unknown adapter; implement it before selecting it')
    if spec['adapter']=='gemini' and expected!='image': raise ValueError('Gemini image adapter cannot deliver SVG')
    if not re.fullmatch(r'[A-Za-z0-9._-]+',spec['model']): raise ValueError('Invalid model identifier')
    return data,spec

def image_mime(data):
    if data.startswith(b'\x89PNG\r\n\x1a\n'): return 'image/png'
    if data.startswith(b'\xff\xd8\xff'): return 'image/jpeg'
    if data[:4]==b'RIFF' and data[8:12]==b'WEBP': return 'image/webp'
    raise ValueError('Reference/output must be PNG, JPEG or WebP')

def gemini_payload(spec, prompt, references, byte_limit):
    parts=[{'text':prompt}]
    hashes=[]
    if len(references)>4: raise ValueError('v1 supports at most four reference images')
    for filename in references:
        path=Path(filename)
        if path.stat().st_size>byte_limit: raise ValueError('Reference exceeds configured byte limit')
        content=path.read_bytes(); mime=image_mime(content)
        parts.append({'inlineData':{'mimeType':mime,'data':base64.b64encode(content).decode()}})
        hashes.append({'name':path.name,'sha256':hashlib.sha256(content).hexdigest()})
    ratio=spec.get('aspect_ratio','1:1')
    if ratio not in {'1:1','2:3','3:2','3:4','4:3','4:5','5:4','9:16','16:9','21:9'}:
        raise ValueError('Unsupported aspect ratio in v1 adapter')
    return {'contents':[{'parts':parts}], 'generationConfig':{
        'responseModalities':['TEXT','IMAGE'], 'responseFormat':{'image':{'aspectRatio':ratio}}}},hashes

def send_gemini(spec,payload,timeout):
    key=os.environ.get(spec.get('api_key_env','GEMINI_API_KEY'))
    if not key: raise ValueError('Missing configured API key environment variable; no request sent')
    request=urllib.request.Request(
        'https://generativelanguage.googleapis.com/v1/models/'+spec['model']+':generateContent',
        data=json.dumps(payload).encode(), headers={'Content-Type':'application/json','x-goog-api-key':key},method='POST')
    try:
        with urllib.request.urlopen(request,timeout=timeout) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        raise RuntimeError('Gemini HTTP '+str(exc.code)+'; not retried (avoid duplicate charges)') from None
    except (urllib.error.URLError, TimeoutError):
        raise RuntimeError('Gemini connection/timeout failure; outcome may be unknown; not retried') from None

def unpack_images(response):
    images=[]
    for candidate in response.get('candidates',[]):
        for part in candidate.get('content',{}).get('parts',[]):
            if part.get('thought'): continue
            inline=part.get('inlineData',part.get('inline_data'))
            if inline:
                data=base64.b64decode(inline['data'],validate=True)
                actual=image_mime(data)
                if inline.get('mimeType',inline.get('mime_type'))!=actual:
                    raise ValueError('Model output MIME/signature mismatch')
                images.append((actual,data))
    if not images: raise ValueError('Provider returned no image; review prompt/filter or model availability')
    return images

def generate(config,role,prompt_file,out,references=(),count=1,execute=False):
    data,spec=config_role(config,role)
    limit=data.get('limits',{})
    if not 1<=count<=limit.get('max_candidates',6): raise ValueError('Candidate count outside budget')
    prompt=Path(prompt_file).read_text()
    if not prompt.strip(): raise ValueError('Prompt is empty')
    payload,hashes=gemini_payload(spec,prompt,references,limit.get('max_reference_bytes',10485760)) if spec['adapter']=='gemini' else (None,[])
    if spec['adapter']=='host' and references: raise ValueError('Host references must be attached/read by the agent')
    if execute and spec['adapter']=='host': raise ValueError('Host route: current agent must write SVG; CLI cannot switch or invoke host models')
    if execute and not os.environ.get(spec.get('api_key_env','GEMINI_API_KEY')):
        raise ValueError('Missing configured API key environment variable; no request sent')
    run=Path(out)/('run-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')+'-'+uuid.uuid4().hex[:8])
    run.mkdir(parents=True,exist_ok=False)
    (run/'prompt.txt').write_text(prompt)
    record={'schema_version':1,'role':role,'adapter':spec['adapter'],'model':spec['model'],
        'status':'prepared','output':spec['output'],'requested_candidates':count,'references':hashes,
        'settings':{'aspect_ratio':spec.get('aspect_ratio')},'outputs':[],
        'visual_review':'pending','live_request_sent':False}
    write_json(run/'manifest.json',record)
    if not execute:
        return {'run':str(run.resolve()),'status':'needs_host_execution' if spec['adapter']=='host' else 'dry_run','model':spec['model']}
    try:
        for index in range(count):
            record['live_request_sent']=True
            record['status']='requesting'
            write_json(run/'manifest.json',record)
            response=send_gemini(spec,payload,limit.get('timeout_seconds',120))
            for sub,(mime,content) in enumerate(unpack_images(response)):
                ext={'image/png':'png','image/jpeg':'jpg','image/webp':'webp'}[mime]
                filename=f'candidate-{index+1:02d}-{sub+1:02d}.{ext}'
                (run/filename).write_bytes(content)
                record['outputs'].append({'file':filename,'sha256':hashlib.sha256(content).hexdigest()})
            record['status']='partial'
            write_json(run/'manifest.json',record)
        record['status']='generated_unreviewed'
    except Exception as exc:
        record['status']='failed_or_partial'
        record['error']=str(exc)
        write_json(run/'manifest.json',record)
        raise
    write_json(run/'manifest.json',record)
    return {'run':str(run.resolve()),'status':record['status'],'outputs':record['outputs']}

def main():
    p=argparse.ArgumentParser(description=__doc__); sub=p.add_subparsers(dest='command',required=True)
    init=sub.add_parser('init');init.add_argument('directory');init.add_argument('--name',required=True)
    check=sub.add_parser('validate');check.add_argument('svg');check.add_argument('--report')
    doctor=sub.add_parser('doctor');doctor.add_argument('--config',default=str(ROOT/'config/models.json'))
    gen=sub.add_parser('generate');gen.add_argument('--role',choices=['svg','explore','presentation'],required=True)
    gen.add_argument('--config',default=str(ROOT/'config/models.json'));gen.add_argument('--prompt',required=True)
    gen.add_argument('--out',required=True);gen.add_argument('--reference',action='append',default=[])
    gen.add_argument('--count',type=int,default=1);gen.add_argument('--execute',action='store_true')
    a=p.parse_args()
    if a.command=='init': result=initialize(a.directory,a.name)
    elif a.command=='validate':
        result=validate_svg(Path(a.svg).read_text())
        if a.report: write_json(a.report,result)
        print(json.dumps(result,ensure_ascii=False,indent=2));return 0 if result['passed'] else 1
    elif a.command=='doctor':
        result={}
        for role in ['svg','explore','presentation']:
            _,spec=config_role(a.config,role)
            result[role]={'adapter':spec['adapter'],'model':spec['model'],
                'credential_configured':bool(os.environ.get(spec.get('api_key_env',''))) if spec['adapter']=='gemini' else None,
                'live_connection':'not_tested'}
    else: result=generate(a.config,a.role,a.prompt,a.out,a.reference,a.count,a.execute)
    print(json.dumps(result,ensure_ascii=False,indent=2));return 0

if __name__=='__main__':
    try: sys.exit(main())
    except (ValueError,RuntimeError,OSError,KeyError) as exc:
        print('Error: '+str(exc),file=sys.stderr);sys.exit(1)
