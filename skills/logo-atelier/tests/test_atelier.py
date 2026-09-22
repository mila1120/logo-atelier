import base64
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('atelier',ROOT/'scripts/atelier.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
GOOD=(ROOT/'assets/demo-mark.svg').read_text()
PNG=base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQIHWP4z8DwHwAFgAI/ScLttAAAAABJRU5ErkJggg==')
RESPONSE={'candidates':[{'content':{'parts':[{'inlineData':{'mimeType':'image/png','data':base64.b64encode(PNG).decode()}}]}}]}
class WorkflowTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
  self.prompt=self.root/'prompt.txt';self.prompt.write_text('Make a paper material study from the supplied master.')
  self.config=ROOT/'config/models.json'
 def test_good_is_not_visual_approval(self):
  result=a.validate_svg(GOOD);self.assertTrue(result['passed']);self.assertEqual(result['visual_review'],'pending')
 def test_unsafe_and_bitmap_rejected(self):
  for element in ['<script/>','<image href="data:image/png;base64,xx"/>','<foreignObject/>','<path onclick="x"/>','<path fill="url(https://example.com/a)"/>']:
   with self.subTest(element=element):self.assertFalse(a.validate_svg(GOOD.replace('</svg>',element+'</svg>'))['passed'])
 def test_invalid_viewbox(self):
  for box in ['0 0 0 512','0 0 nan 512','0 0 inf 512','0 0 -1 512']:
   with self.subTest(box=box):self.assertFalse(a.validate_svg(GOOD.replace('0 0 512 512',box))['passed'])
 def test_local_references(self):
  self.assertFalse(a.validate_svg(GOOD.replace('fill="#182823"','fill="url(#missing)"'))['passed'])
  self.assertTrue(a.validate_svg(GOOD.replace('<g id=', '<defs><linearGradient id="ink"><stop offset="0" stop-color="#000"/></linearGradient></defs><g id=').replace('fill="#182823"','fill="url(#ink)"'))['passed'])
 def test_init_no_overwrite(self):
  target=self.root/'project';a.initialize(target,'星火');self.assertEqual(json.loads((target/'brief.json').read_text())['brand_name'],'星火')
  with self.assertRaises(FileExistsError):a.initialize(target,'overwrite')
 def test_dry_run_never_network(self):
  with patch.object(a,'send_gemini',side_effect=AssertionError('network')):
   r=a.generate(self.config,'explore',self.prompt,self.root/'runs');self.assertEqual(r['status'],'dry_run')
 def test_missing_key_before_request(self):
  with patch.dict(os.environ,{},clear=True),patch.object(a,'send_gemini',side_effect=AssertionError('network')):
   with self.assertRaises(ValueError):a.generate(self.config,'explore',self.prompt,self.root/'runs',execute=True)
  self.assertFalse((self.root/'runs').exists())
 def test_host_not_svg_image_adapter(self):
  self.assertEqual(a.generate(self.config,'svg',self.prompt,self.root/'runs')['status'],'needs_host_execution')
  with self.assertRaises(ValueError):a.generate(self.config,'svg',self.prompt,self.root/'runs',execute=True)
 def test_response_validation(self):
  self.assertEqual(a.unpack_images(RESPONSE)[0][1],PNG)
  with self.assertRaises(ValueError):a.unpack_images({})
  bad=json.loads(json.dumps(RESPONSE));bad['candidates'][0]['content']['parts'][0]['inlineData']['mimeType']='image/jpeg'
  with self.assertRaises(ValueError):a.unpack_images(bad)
 def test_reference_validation(self):
  bad=self.root/'bad.png';bad.write_text('not image')
  with self.assertRaises(ValueError):a.gemini_payload({},'prompt',[bad],1000)
 def test_partial_failure_keeps_output_without_key(self):
  with patch.dict(os.environ,{'GEMINI_API_KEY':'secret-test-only'}),patch.object(a,'send_gemini',side_effect=[RESPONSE,RuntimeError('offline')]):
   with self.assertRaises(RuntimeError):a.generate(self.config,'explore',self.prompt,self.root/'runs',count=2,execute=True)
  run=next((self.root/'runs').iterdir());record=json.loads((run/'manifest.json').read_text());self.assertEqual(record['status'],'failed_or_partial');self.assertEqual(len(record['outputs']),1)
  self.assertNotIn('secret-test-only',(run/'manifest.json').read_text())
 def test_candidate_budget(self):
  with self.assertRaises(ValueError):a.generate(self.config,'explore',self.prompt,self.root/'runs',count=7)
if __name__=='__main__':unittest.main()
