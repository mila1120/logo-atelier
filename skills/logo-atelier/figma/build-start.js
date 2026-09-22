await figma.loadFontAsync({family:'Noto Sans SC',style:'Regular'});
const vars=await figma.variables.getLocalVariablesAsync(),styles=await figma.getLocalTextStylesAsync();
const v=n=>vars.find(x=>x.name===n),created=[];
const add=n=>(created.push(n.id),n);
const fill=(n,c)=>{n.fills=[figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:0,g:0,b:0}},'color',v(c))];};
function stack(name,width){const f=add(figma.createAutoLayout('VERTICAL'));f.name=name;f.resize(width,100);f.counterAxisSizingMode='FIXED';f.primaryAxisSizingMode='AUTO';f.itemSpacing=24;f.setBoundVariable('itemSpacing',v('space/md'));f.fills=[];return f;}
async function txt(parent,content,kind='Body',color='color/foreground'){const t=add(figma.createText());t.fontName={family:'Noto Sans SC',style:'Regular'};await t.setTextStyleIdAsync(styles.find(s=>s.name==='Atelier / '+kind).id);t.characters=content;parent.appendChild(t);t.layoutSizingHorizontal='FILL';t.textAutoResize='HEIGHT';fill(t,color);return t;}
const board=stack('00 / Start · 品牌工作台',1440);board.x=120;board.y=120;board.paddingLeft=64;board.paddingRight=64;board.paddingTop=64;board.paddingBottom=64;board.itemSpacing=48;board.setBoundVariable('itemSpacing',v('space/lg'));fill(board,'color/canvas');
await txt(board,'LOGO ATELIER     /     V0.1     /     EDITABLE BY DESIGN','Label','color/muted');
await txt(board,'从品牌意图，\n到经得起使用的标志。','Heading');
await txt(board,'一套可以持续迭代的设计工作台。\n先确定要传达什么，再构建母版，最后用真实尺寸检验。');
const stripe=stack('流程',1312);fill(stripe,'color/background');stripe.paddingLeft=24;stripe.paddingRight=24;stripe.paddingTop=24;stripe.paddingBottom=24;board.appendChild(stripe);stripe.layoutSizingHorizontal='FILL';
await txt(stripe,'01  理解品牌     →     02  比较意象     →     03  编辑母版     →     04  渲染验收','Body');
const brief=stack('01 / Brand brief',1312);board.appendChild(brief);brief.layoutSizingHorizontal='FILL';
await txt(brief,'01 / 在这里开始','Heading');
await txt(brief,'产品与用户  /  [填写产品功能、核心用户与使用场景]\n期望感受  /  [用 3 个词描述，希望被怎样记住]\n必须保留  /  [已有符号、草图特征、颜色或品牌限制]\n交付场景  /  [品牌标志 / iOS 图标 / 网站 / 印刷]\n来源链接  /  [需求文档、参考与草图；区分事实和假设]');
await txt(board,'使用方式','Heading');
await txt(board,'复制文件用于真实项目。右侧母版可直接编辑矢量与图层。\nShow background / Show accent 控制显示；Light / Dark 切换配色。\n模板的纸色、深绿与示范几何仅用于展示编辑能力。');
await txt(board,'完成标准  /  结构有效 ≠ 视觉通过 ≠ 用户确认。每一步分别记录。','Label','color/muted');
return {createdNodeIds:created,board:board.id,brief:brief.id};
