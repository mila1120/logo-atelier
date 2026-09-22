await figma.loadFontAsync({family:'Noto Sans SC',style:'Regular'});
const vars=await figma.variables.getLocalVariablesAsync(),styles=await figma.getLocalTextStylesAsync();
const v=n=>vars.find(x=>x.name===n),created=[];const add=n=>(created.push(n.id),n);
const fill=(n,c)=>{n.fills=[figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:0,g:0,b:0}},'color',v(c))];};
async function txt(parent,content,kind='Body'){const t=add(figma.createText());t.fontName={family:'Noto Sans SC',style:'Regular'};await t.setTextStyleIdAsync(styles.find(s=>s.name==='Atelier / '+kind).id);t.characters=content;parent.appendChild(t);t.layoutSizingHorizontal='FILL';t.textAutoResize='HEIGHT';fill(t,'color/foreground');return t;}
const b=add(figma.createAutoLayout('VERTICAL'));b.name='05 / Material & App icon';b.x=3060;b.y=1400;b.resize(1440,100);b.counterAxisSizingMode='FIXED';b.primaryAxisSizingMode='AUTO';b.paddingLeft=64;b.paddingRight=64;b.paddingTop=64;b.paddingBottom=64;b.itemSpacing=48;b.setBoundVariable('itemSpacing',v('space/lg'));fill(b,'color/canvas');
await txt(b,'05 / 材质可以变，识别不能丢。','Heading');await txt(b,'左：母版的 App 图标组合示范。右：材质探索留白区。\n生成图用于探索与展示；最终几何始终回到可编辑矢量。');
const row=add(figma.createAutoLayout('HORIZONTAL'));row.name='App icon / Material study';row.fills=[];row.itemSpacing=48;row.setBoundVariable('itemSpacing',v('space/lg'));row.primaryAxisSizingMode='AUTO';row.counterAxisSizingMode='AUTO';b.appendChild(row);
const master=await figma.getNodeByIdAsync('3:2');const i=add(master.createInstance());i.name='App icon · 512 preview of 1024 master';row.appendChild(i);i.rescale(.5);created.push(...i.findAll(()=>true).map(n=>n.id));
const study=add(figma.createAutoLayout('VERTICAL'));study.name='Material study · image goes here';study.resize(752,512);study.primaryAxisSizingMode='FIXED';study.counterAxisSizingMode='FIXED';study.paddingLeft=48;study.paddingRight=48;study.paddingTop=48;study.paddingBottom=48;study.itemSpacing=24;study.setBoundVariable('itemSpacing',v('space/md'));fill(study,'color/accent');row.appendChild(study);
await txt(study,'MATERIAL STUDY','Label');await txt(study,'[等待真实项目与模型调用]');await txt(study,'方向 / 扁平 · 纸张 · 3D · 其他\n参考 / 从当前母版渲染\n检查 / 轮廓、比例、负空间是否改变\n状态 / 生成不等于验收','Body');
await txt(b,'iOS 交付','Body');await txt(b,'保留 1024 × 1024 方形源稿，圆角裁切用于预览，不烘焙进源文件。\n按项目的 iOS / Xcode 版本选择 Asset Catalog 或 Icon Composer。\n此板不模拟系统效果；设备与实际导出验证留待真实项目。','Label');
return {createdNodeIds:created,board:b.id,icon:i.id,materialSlot:study.id};
