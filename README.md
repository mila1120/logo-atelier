# Logo Atelier 1.0

**你来选方向，AI 把想法画出来。**

Logo Atelier 是一个配合 Codex 和 Figma 使用的 Logo 设计 Skill。给它一份产品需求，它会帮你找参考、画方案、试配色、修改细节，再把选中的设计放进手机样机里。你可以随时通过方案编号或 Figma 评论提出修改，最终由你决定用哪一版。

## 它能帮你做什么？

### 从产品里找到设计灵感

读取需求文档，理解产品功能、品牌名字和你想传达的感觉，提炼 2–3 个视觉方向。比如键盘产品可以从一个按键、键盘结构或表情入手；品牌名字也可以成为图形或首字母设计的灵感。

### 找参考，再出方案

从 App Store、Pinterest、Logosystem 等可访问来源寻找参考，按方向整理到 Figma 中。每个方向约 30 张，你只需挑出喜欢的 2–3 张，也可以提供自己的截图或草图。

先看 6–12 个差异明显的初稿，留下 2–3 个方向，再围绕选中的方向细化。几何探索通常每个方向约 25 款，配色与材质探索通常每个选中形体约 25 款；已有明确偏好时可以直接精修。

### 把喜欢的部分混搭起来

主体、表情、背景、辅助图形、颜色和材质分别展示，方便比较与组合。你可以直接说：

> 用 A 的背景、B 的形状和 C 的表情，再试几种蓝色。

也可以只改一个部分，例如换键盘颜色，同时保留原来的渐变、透明度和形状。

### 选编号，或直接留评论

每个方案都有编号。告诉它“选 03，表情换成 07”，或在 Figma 方案旁留下 Comment，它会读取评论与回复，逐条修改，并保留之前的版本供比较。

每轮先出方案，再集中让你选择。普通偏好暂未回复时，它会说明自己的暂选并继续；最终定稿仍由你确认。局部修改可以直接开始，不用重新走完整流程。

### 放进手机里，看真实效果

选中的图标会放入设备样机，与少量系统图标一起比较，名称使用你的产品名。后续修改源图标时，会在同一轮任务中更新对应样机，并检查小尺寸下的比例、居中和辨识度。

### 导出成品，积累自己的模版库

设计保留为可编辑矢量。定稿后，按目标平台和交付要求导出 SVG、PNG 等文件，也可以打包到桌面。最终方案连同分层、配色和材质存入项目或你指定的私有模版库，方便以后继续使用。

## 一次设计怎么进行？

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
