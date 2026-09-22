# Logo Atelier 1.0

**帮助设计师做决策，让Agent来替你实现。**

Logo Atelier 是面向设计师的 Logo 与 App Icon 设计 Skill，将 Agent 的探索能力与 Figma 的可编辑工作台结合。从需求理解、参考研究到方案精修与交付，Agent 负责展开设计可能性，设计师始终掌握方向与最终决策。

整个流程通常围绕 **6 个主要决策点**展开。每一轮，Agent 基于上一轮结论生成方案、提出选择问题，由你收敛方向，再进入下一轮。方案直接在 Figma 中以可编辑 SVG 矢量绘制，主体、表情、背景与材质可以独立调整、自由组合。

你可以通过**方案编号**指定选择，也可以直接在 Figma 方案旁留下 **Comment**，让反馈进入下一轮修改，持续迭代直到满意。普通偏好暂未回复时，Agent 会在合理等待后说明自己的暂选并继续推进；最终定稿由你明确确认。

这套工作流提炼自实际 Logo 项目的参考研究、方案筛选与多轮精修，将有效的设计方法沉淀为可复用流程，并根据每个新产品的需求重新展开。

## 核心能力

### 从产品需求，提炼品牌意象

读取需求文档，理解产品功能、品牌名字和你想传达的感觉，提炼 2–3 个视觉方向。比如键盘产品可以从一个按键、键盘结构或表情入手；品牌名字也可以成为图形或首字母设计的灵感。

### 以参考为依据，逐步展开设计方向

从 App Store、Pinterest、Logosystem 等可访问来源研究同类产品与相关视觉意象，按方向整理到 Figma 中。每个方向约 30 张参考，供你选择 2–3 张作为后续探索依据，也支持导入自己的截图或草图。

先看 6–12 个差异明显的初稿，留下 2–3 个方向，再围绕选中的方向细化。几何探索通常每个方向约 25 款，配色与材质探索通常每个选中形体约 25 款；已有明确偏好时可以直接精修。

### 分层探索，让方案可以组合与复用

主体、表情、背景、辅助图形、颜色和材质分别展示，方便比较与组合。你可以直接说：

> 用 A 的背景、B 的形状和 C 的表情，再试几种蓝色。

也可以只改一个部分，例如换键盘颜色，同时保留原来的渐变、透明度和形状。

### 用编号与评论，推动每一轮精修

每个方案都有编号。告诉它“选 03，表情换成 07”，或在 Figma 方案旁留下 Comment，它会读取评论与回复，逐条修改，并保留之前的版本供比较。

每轮围绕当前需要解决的问题集中选择，保留已经认可的部分。局部修改直接进入对应阶段，无需重新走完整流程。

### 在使用场景中，检验图标表现

选中的图标会放入设备样机，与少量系统图标一起比较，名称使用你的产品名。后续修改源图标时，会在同一轮任务中更新对应样机，并检查小尺寸下的比例、居中和辨识度。

### 从可编辑母版，到交付与模版沉淀

设计保留为可编辑矢量。定稿后，按目标平台和交付要求导出 SVG、PNG 等文件，也可以打包到桌面。最终方案连同分层、配色和材质存入项目或你指定的私有模版库，方便以后继续使用。

## 设计流程

**读需求 → 选参考 → 选形体 → 试颜色与材质 → 评论精修与样机预览 → 定稿导出**

通常有约 6 个主要选择点。需要时继续迭代，满意时即可定稿。配色已确定可以跳过探索；只想改某个图标，也可以从那里开始。

[查看完整工作流程](skills/logo-atelier/references/workflow-1.0.md)

## 开始使用

1. 在 Codex 中安装或加载 Logo Atelier。
2. 连接具备编辑能力的 Figma 工具，准备一个可编辑的 Figma 项目链接。
3. 提供需求文档、参考图或一段产品介绍，然后告诉它：

> 使用 Logo Atelier。这是我的产品需求：[链接或附件]，这是 Figma：[链接]。先帮我找几个设计方向，我会通过编号或评论选择，再继续细化。

如果你已有设计，也可以这样开始：

> 读取这个 Section 里的评论，在下方新建一轮方案，并更新选中款的手机样机。

> 保留这个图标的形状和透明度，试几版深灰、黑色和蓝色。

<details>
<summary>手动安装与本地工具</summary>

克隆仓库，将 `skills/logo-atelier` 文件夹放入 `~/.codex/skills/`，然后在新任务中使用。已有同名 Skill 时先保留自己的改动。仓库也可作为本地 Codex 插件源使用。

SVG 设计不要求配置图像模型。可选本地校验需要 Python 3；PNG 渲染需要 Node.js 和 `sharp`。在仓库根目录运行：

```sh
python3 skills/logo-atelier/scripts/atelier.py doctor
python3 skills/logo-atelier/scripts/atelier.py validate skills/logo-atelier/assets/demo-mark.svg
npm install
node skills/logo-atelier/scripts/render.cjs skills/logo-atelier/assets/demo-mark.svg ./proof-demo
```

渲染输出目录应为新目录。可选图像模型的配置与费用说明见[模型接口](skills/logo-atelier/references/models.md)。

</details>

## 使用前了解

- 这是由 Codex 执行的 Skill，需要可用的 Figma 连接；不提供独立 Figma 侧栏。
- 评论在任务执行时读取，样机在任务内更新，不会在后台持续监听。
- 在线找参考取决于来源是否可访问；参考作品保留来源，不作为原创设计直接复制。
- 保留已有审美规则、图标风格库和几何检查方法；不提供商标可注册性判断。
- 客户文档、评论和设计文件不会自动发布到公开仓库。

## 更多资料

[Skill 入口](skills/logo-atelier/SKILL.md) · [完整流程](skills/logo-atelier/references/workflow-1.0.md) · [参考研究](skills/logo-atelier/references/reference-board.md) · [分层混搭](skills/logo-atelier/references/modular-design.md) · [评论迭代](skills/logo-atelier/references/comment-driven-iteration.md)

## 来源与许可

部分设计方法参考了 Taste Skill 与 Company Logos：[Taste 说明](skills/logo-atelier/references/taste-integration.md)、[Taste MIT 许可](skills/logo-atelier/references/taste-license.txt)、[Company Logos MIT 许可](skills/logo-atelier/references/company-logos-license.txt)。第三方 App 图标归各自权利人所有，不随仓库分发。

其余原创内容暂未指定统一开源许可证；公开可见不代表额外授予商业使用或再分发许可。
