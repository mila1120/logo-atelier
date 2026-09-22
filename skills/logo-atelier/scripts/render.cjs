#!/usr/bin/env node
// Render portable SVG and preserve an auditable proof. Never claims visual approval.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const {spawnSync} = require('node:child_process');
async function main(){
 const [input,out] = process.argv.slice(2);
 if(!input || !out) throw Error('Usage: node render.cjs <master.svg> <new-proof-directory>');
 const svg=fs.readFileSync(input);
 const checked=spawnSync(process.env.PYTHON || 'python3',[path.join(__dirname,'atelier.py'),'validate',input],{encoding:'utf8'});
 if(checked.status!==0) throw Error(checked.stdout || checked.stderr || 'SVG validation failed');
 let sharp; try {sharp=require('sharp');} catch {throw Error('Install sharp at plugin root, or set NODE_PATH to a directory containing sharp');}
 fs.mkdirSync(out,{recursive:false});
 const sizes=[16,24,32,64,128,1024], outputs=[];
 for(const size of sizes){
  const filename=`mark-${size}.png`;
  await sharp(svg,{density:288}).resize(size,size,{fit:'contain',background:{r:0,g:0,b:0,alpha:0}}).png().toFile(path.join(out,filename));
  outputs.push({file:filename,size,sha256:crypto.createHash('sha256').update(fs.readFileSync(path.join(out,filename))).digest('hex')});
 }
 const layers=[];
 const label=(text,width)=>Buffer.from(`<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="34"><text x="0" y="23" font-family="sans-serif" font-size="16" fill="#68756d">${text}</text></svg>`);
 for(let row=0;row<2;row++){
  layers.push({input:await sharp({create:{width:1100,height:240,channels:4,background:row?'#182823':'#f4f1e9'}}).png().toBuffer(),left:20,top:50+row*290});
  for(let i=0;i<5;i++){
   const x=50+i*210, y=50+row*290;
   layers.push({input:fs.readFileSync(path.join(out,`mark-${sizes[i]}.png`)),left:x+Math.floor((160-sizes[i])/2),top:y+Math.floor((210-sizes[i])/2)});
   layers.push({input:label(`${sizes[i]} px`,160),left:x,top:y+244});
  }
 }
 layers.push({input:label('Native pixels / light and dark backgrounds / visual review pending',1100),left:20,top:5});
 await sharp({create:{width:1140,height:640,channels:4,background:'#ffffff'}}).composite(layers).png().toFile(path.join(out,'proof.png'));
 fs.writeFileSync(path.join(out,'manifest.json'),JSON.stringify({master:path.resolve(input),master_sha256:crypto.createHash('sha256').update(svg).digest('hex'),renderer:'sharp',renderer_version:sharp.versions.sharp,created_at:new Date().toISOString(),sizes,outputs,structure_status:'passed',visual_review:'pending'},null,2)+'\n');
 fs.writeFileSync(path.join(out,'index.html'),'<!doctype html><meta charset="utf-8"><title>Logo proof — review pending</title><style>body{font:16px system-ui;background:#eee;padding:24px}img{max-width:none}.sample{display:inline-flex;flex-direction:column;gap:12px;padding:24px;background:white;margin:8px}</style><h1>Native-size logo proof</h1><p>Visual review pending. Dark-background visibility must be judged separately from a reverse-color variant.</p><img src="proof.png" width="1140" height="640">'+sizes.map(size=>`<div class="sample">${size} px<img src="mark-${size}.png" width="${size}" height="${size}"></div>`).join(''));
 console.log(JSON.stringify({directory:path.resolve(out),status:'rendered_unreviewed',outputs:outputs.length}));
}
main().catch(e=>{console.error(e.message);process.exitCode=1;});
