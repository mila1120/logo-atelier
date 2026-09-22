await figma.loadFontAsync({family:'Noto Sans SC',style:'Regular'});
const vars=await figma.variables.getLocalVariablesAsync(),styles=await figma.getLocalTextStylesAsync();
const v=n=>vars.find(x=>x.name===n),created=[];const add=n=>(created.push(n.id),n);
const fill=(n,c)=>{n.fills=[figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:0,g:0,b:0}},'color',v(c))];};
async function txt(parent,content,kind='Body'){const t=add(figma.createText());t.fontName={family:'Noto Sans SC',style:'Regular'};await t.setTextStyleIdAsync(styles.find(s=>s.name==='Atelier / '+kind).id);t.characters=content;parent.appendChild(t);t.layoutSizingHorizontal='FILL';t.textAutoResize='HEIGHT';fill(t,'color/foreground');return t;}
const board=add(figma.createAutoLayout('VERTICAL'));board.name='04 / Proof · 尺寸与反白';board.x=3060;board.y=120;board.resize(1440,100);board.counterAxisSizingMode='FIXED';board.primaryAxisSizingMode='AUTO';board.paddingLeft=64;board.paddingRight=64;board.paddingTop=64;board.paddingBottom=64;board.itemSpacing=48;board.setBoundVariable('itemSpacing',v('space/lg'));fill(board,'color/canvas');
await txt(board,'04 / 缩小之后，还成立吗？','Heading');await txt(board,'以下是实际尺寸实例。请在 100% 缩放检查，并导出 PNG 验证。\n深浅背景各检查一次；尺寸预览不代表已完成 iOS 真机验收。');
const master=await figma.getNodeByIdAsync('3:2');
const cols=await figma.variables.getLocalVariableCollectionsAsync();const colors=cols.find(c=>c.name==='Atelier / Color');
for(const mode of ['Light','Dark']){
 const row=add(figma.createAutoLayout('HORIZONTAL'));row.name=mode+' / Native sizes';row.resize(1312,220);row.primaryAxisSizingMode='FIXED';row.counterAxisSizingMode='FIXED';row.paddingLeft=24;row.paddingRight=24;row.paddingTop=24;row.paddingBottom=24;row.itemSpacing=48;row.setBoundVariable('itemSpacing',v('space/lg'));fill(row,'color/canvas');row.setExplicitVariableModeForCollection(colors.id,colors.modes.find(m=>m.name===mode).modeId);board.appendChild(row);
 for(const size of [16,24,32,64,128]){const col=add(figma.createAutoLayout('VERTICAL'));col.name=size+'px';col.resize(180,172);col.primaryAxisSizingMode='FIXED';col.counterAxisSizingMode='FIXED';col.itemSpacing=16;col.fills=[];row.appendChild(col);await txt(col,size+' px','Label');const i=add(master.createInstance());col.appendChild(i);i.setProperties({'Show background#3:0':false});i.rescale(size/1024);created.push(...i.findAll(()=>true).map(n=>n.id));}
}
await txt(board,'验收记录 / 每次修改几何后重新检查','Body');await txt(board,'□ 轮廓可识别   □ 负空间未闭合   □ 无意外裁切   □ 黑白成立\n□ 用户修改已保留   □ SVG 与渲染一致   □ 平台导出已核验\n当前状态：模板示范，未针对真实项目验收。','Label');
return {createdNodeIds:created,board:board.id};
