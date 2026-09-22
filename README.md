# Logo Atelier

**把产品想法变成可拆分、可混搭、可追溯的 Logo 与 App Icon。**

Logo Atelier 是面向 Codex 的设计 Skill / 插件。它将需求解析、参考研究、Figma 分层探索、可编辑 SVG、配色实验与 mock 展示组织成一条设计流程，让设计师把精力放在判断与选择上。

当前快照：**v0.1 · 2026-09-22**。流程由 Agent 配合 Figma 工具执行；仓库包含 Skill、参考规则、示范构建脚本和本地校验工具。

[开始使用](#开始使用) · [功能清单](#现有功能) · [目录结构](#目录结构) · [能力边界](#当前能力边界)

## 现有功能

### 01 / 解析需求，找到产品自己的小巧思

读取上传的需求文档、文档链接或口述 brief，提炼产品功能与品牌调性。已知信息直接整理，缺失信息再问，围绕五个方向展开：

| 解析方向 | 产出 |
| --- | --- |
| 核心功能 | 产品解决什么问题，哪些物件、动作或反馈值得转成图形 |
| 品牌名字 | 准确名字与可视化意象，区分原始含义和设计联想 |
| 感受与风格 | 希望传达的感受，以及形状、线条、颜色和材质如何实现它 |
| 交付内容 | 根据项目确定标志、App 图标、字标、配色、母版、mock 或导出资产 |
| 首字母延展 | 从实际名字的字形、缩写与负形中寻找构形机会，可选择不使用字母 |

创意选项从需求生成，每项说明 **产品特点 → 如何画出来 → 传达什么感受**。例如键盘产品可以聚焦单个按键、改变键位的表现方法，或让按键带上表情；这些是方法示例，不是所有项目都套用的元素。

### 02 / 参考与草图，先看清方向

- 接收设计师提供的截图、参考链接与 sketch，在 Figma 中建立独立 Reference Section。
- 按品类研究真实 App 图标，结合 Logosystem、Pinterest、小红书、App Store 和官方奖项来源；访问受限时记录实际缺口。
- 默认先整理 **24 个真实图标**，归纳 **3–4 个有图例的风格方向**；选定方向后，定向补充到总计 **100 个**。数量与是否跳过可按用户要求调整。
- 支持设计师直接在 Figma 删选、移动参考；继续时读取最新选择，不恢复用户已经删除的内容。
- 提炼可借鉴的轮廓、负形、构图、色彩和材质原则，保存来源，不整枚复制参考商标。

### 03 / 在 Figma 中建立可混搭的设计工作台

把适用的设计角色分别放进可见的 Section，展示可编辑选项；不适用的角色不强加。

| Section | 用来比较什么 |
| --- | --- |
| Background / 背景 | 底形、圆角、空间层次与背景效果 |
| Shape / 主体形态 | 主图标轮廓、字母、物件与负形 |
| Expression / 表情 | 眼睛、嘴、情绪和人格表达 |
| Supporting Motif / 辅助图形 | 键盘等承托、辅助或功能元素 |
| Material / 材质 | 平面、渐变、玻璃、浅浮雕、立体等处理 |
| Presentation / 展示 | 设备 mock 与使用场景 |

另设 **Palette / 配色** 与 **Composition / Final / 组合与最终方案**。设计师可以直接指定“用 A 的背景、B 的形态和 C 的表情”，由 Agent 组合并检查比例与层级。

原生图层支持手动拖动、重排和改色；“交换前后景”会区分交换颜色与交换图层角色。

### 04 / 先找偏好，再展开变体

**6–12 个差异明显的方向 → 保留 2–3 个 → 展开共 12–18 个精细变体 → 最终组合。**

- 初轮比较构形思路，不把换颜色计作新造型。
- 精修轮按比例、表情、配色或材质等维度逐项比较，避免同时改动所有东西。
- 可以按需求增加方案，也可以先快速比较两款。
- 已有明确选择时直接继续，局部修改不重新跑整套流程。

### 05 / 独立配色与材质实验

- 从选定参考提炼三种有区别的背景风格，并制作可编辑 SVG 母版。
- 绘制 **10 组品牌色板**，用原生色块与一致的预览供选择。
- 将颜色与材质参数分开：可以只替换键盘颜色，同时保留渐变位置、方向、透明度、描边和阴影。
- 支持深浅配色、黑白版本和局部颜色对比；材质深度随 brief 调整。

### 06 / 精修几何与视觉关系

围绕选定方向检查比例、光学居中、曲线、圆角、留白、透视、遮挡和明暗分界。主体、表情、辅助图形分别编辑；修改前读取当前 Figma 内容，保留无关属性和设计师的手动改动。

矢量母版与位图材质探索分开管理。位图参考需要重新构建几何后才可作为可编辑矢量，不能仅改后缀冒充 SVG。

### 07 / 最终方案与 mock 对应更新

- 记录原方案、组合和 mock 图标槽位的节点映射。
- 在已授权范围内，每轮源图标修改后更新对应 mock，并检查实际显示。
- 保留手机布局与其他内容；需要时同步指定 Section 的最终方案。
- 新建资产适合时使用组件实例；已有矢量可通过 Agent 在本轮任务中同步。

**这是任务内联动，不是后台实时监听。** 默认保留范围外的对比稿；用户要求“只保留当前方案”时才清理对应多余 mock。

### 08 / 验收、交付与复用

- 检查真实 SVG 结构与导出结果，渲染 16 / 24 / 32 / 64 / 128 / 1024 px 诊断图。
- 在实际小尺寸、浅底和深底检查识别度、边缘、对比和裁切。
- 根据约定交付可编辑母版、变体、PNG、Figma 图层与 mock；诊断尺寸不等同于完整平台上架资源。
- 项目保存 brief、来源、母版版本、节点映射和验收记录。通用方法可以沉淀回 Skill，客户的具体偏好留在项目内。

## 开始使用

### 环境

- 可加载 Skill 的 Codex 环境。
- 需要写入 Figma 时，连接具备编辑能力的 Figma 工具并提供可编辑的项目链接。仓库本身不提供 Figma 连接服务。
- Python 3 用于本地项目初始化、SVG 校验与模型适配器；Node.js + `sharp` 用于可选的 PNG 渲染。
- 不需要图像模型即可进行 SVG 设计。可选 Gemini 位图探索需要自行配置凭据，当前仓库未包含密钥。

### 加载 Skill

克隆仓库后，将 `skills/logo-atelier` 放入本机的 Codex skills 目录，例如 `~/.codex/skills/logo-atelier`，然后在新任务中调用。已有同名 Skill 时先保留自己的改动，再决定合并或替换。

仓库也包含 `.codex-plugin/plugin.json`，可作为本地 Codex 插件源使用；它不是独立的 Figma 插件安装包。

### 一个完整任务

> 使用 Logo Atelier。这是我的需求文档：[链接或附件]，这是项目 Figma：[链接]。先解析功能、品牌调性和可视化巧思，确认交付范围；建立参考区和分层工作台，先探索 6–12 个方向，我选 2–3 个后继续精修，最后更新对应 mock 并检查小尺寸效果。

### 也可以只改一部分

> 保留这几个图标的几何、渐变和透明度，只把键盘换成深灰、黑色与蓝色，在下方新增比较。

> 用 A 的背景、B 的气泡和 C 的表情组合；调整光学居中，然后更新这个最终方案对应的 mock。

> 只解析文档，给我几种有依据的小巧思，暂时不要画图。

### 本地工具

在仓库根目录运行：

```sh
python3 skills/logo-atelier/scripts/atelier.py doctor
python3 skills/logo-atelier/scripts/atelier.py init ./my-project --name '品牌名'
python3 skills/logo-atelier/scripts/atelier.py validate skills/logo-atelier/assets/demo-mark.svg

# 可选：安装本地渲染依赖，输出目录应为新目录
npm install
node skills/logo-atelier/scripts/render.cjs skills/logo-atelier/assets/demo-mark.svg ./proof-demo

# 单元测试使用模拟响应，不发送付费图像请求
python3 -m unittest discover -s skills/logo-atelier/tests
```

模型配置位于 [`config/models.json`](skills/logo-atelier/config/models.json)。生成默认 dry-run；真实请求需设置 `GEMINI_API_KEY` 并显式使用 `--execute`，可能产生提供商费用。详见 [模型接口](skills/logo-atelier/references/models.md)。

## 目录结构

```text
.codex-plugin/plugin.json       Codex 插件入口
skills/logo-atelier/
  SKILL.md                     主工作流
  references/                  解析、调研、配色、分层、Figma 与验收规则
  scripts/                     项目初始化、SVG 校验、渲染与模型接口
  figma/                       示例构建记录与项目状态入口
  assets/                      示例矢量母版
  config/                      模型与 token 配置
  tests/                       本地工具测试
```

关键文档：[需求解析](skills/logo-atelier/references/parse.md) · [参考研究](skills/logo-atelier/references/reference-board.md) · [分层设计](skills/logo-atelier/references/modular-design.md) · [配色](skills/logo-atelier/references/palette-board.md) · [视觉验收](skills/logo-atelier/references/review.md)。

`figma/build-*.js` 是早期示范模板的构建记录，不是幂等脚本或一键安装器；在真实项目里由 Agent 按当前 Skill 建立工作台。公开快照不附带个人 Figma 文件、节点映射或客户项目。

## 当前能力边界

| 能力 | 当前状态 |
| --- | --- |
| 需求解析、分层探索、变体与 mock 工作流 | 已写入 Skill，由 Agent 与可用工具执行 |
| SVG 校验、项目初始化、本地渲染 | 已提供脚本与测试 |
| Gemini 位图接口 | 已实现适配器与 dry-run；真实凭据下的连通性仍待验证 |
| Figma 独立侧栏、拖拽混搭界面 | 未提供；使用 Figma 原生图层与 Agent 操作 |
| 跨应用后台实时双向同步 | 未提供 |
| Pinterest / 小红书自动采集 API | 未提供；调研取决于可访问来源与工具 |
| 自动商标查重、商标可注册性判断 | 未提供 |
| 设备模拟器或完整上架资源验收 | 未提供 |

## 来源与许可说明

部分设计方法参考了 Taste Skill 与 Company Logos，相关来源及许可随仓库保留：[Taste 说明](skills/logo-atelier/references/taste-integration.md)、[Taste MIT 许可](skills/logo-atelier/references/taste-license.txt)、[Company Logos MIT 许可](skills/logo-atelier/references/company-logos-license.txt)。第三方 App 图标用于项目研究时仍归各自权利人所有，不随此仓库分发。

本快照尚未为其余原创内容指定统一开源许可证；公开可见不代表额外授予商业使用或再分发许可。
