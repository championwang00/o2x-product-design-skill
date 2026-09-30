---
name: o2x-design-system
description: >-
  Applies One2X (📖One2X Design System) Figma tokens, typography (Manrope,
  Nohemi), Material-aligned components, and UI patterns. Use when building or
  reviewing Medeo/One2X interfaces, matching Figma exports, or when the user
  mentions One2X Design System, One2X DS, or the company design file. For
  transitions, motion, easing, or animation implementation/review, also load
  web-animation-design (sibling skill in .cursor/skills/).
---

# O2X Design System skill

## 唯一来源与路径解析

本仓库是 O2X Skill、`design.md` 和 `tokens/` 的唯一维护来源。通过 Codex / Cursor 全局入口加载时，先解析当前 `SKILL.md` 的符号链接真实路径，再以真实文件所在目录解析本文所有相对路径；不可直接从全局入口目录计算 `../../../`。

配套 O2X Skill 与仓库自带的 Figma、动效 Skill 按真实路径加载。额外技能（如 `design-feedback-judge`、`emil-design-engineering`）从当前环境技能目录发现，不假设它们位于仓库内。消费项目的组件与实现配置仍遵循该项目约束；产品专属差异不能自动改写仓库的品牌规范。

## 自动反馈评审与技能改进

执行本技能的设计、视觉调整或实现对稿任务前，从当前环境的技能目录加载 `design-feedback-judge`（如已安装），可用时按任务建立评审记录；交付前、收到用户修订意见后自动评审并给简短回执，无需用户另外要求记录。普通问答与纯文档维护不触发作品评审。多个设计技能联用只保留一份记录；已有独立视觉评审直接复用，不增加另一套打分。

先修本次作品，再区分单期偏好、执行遗漏与可复用方法缺口；有依据才更新负责的技能，保存差异并验证。保持本技能的参考材料、先审后改、设计系统及操作授权要求。One2X 团队规范和已发布库不因单次反馈自动改变。

用户要求把反馈提炼进规范时，同时审查现有正文能否被这次提炼改进：收紧模糊的规则，改掉已被推翻的旧表述，补上缺失的交叉引用，把放错位置或重复的段落归位合并，并把新检查补进 `design.md` §11 Do / Don't、§13.3 与本文「完成验收」。规则正文写进 `design.md`，本文只留执行要点和指向；不要只在末尾追加新段落。


## When to use

- User or task references **One2X**、**One2X Design System**、**📖One2X Design System**，或 Figma 文件 `wHNBqjzSQZM8a4DlyBIDqW`。
- 需要与设计稿一致的 **颜色、圆角、间距、字体、按钮/图标按钮/菜单/列表** 行为。
- 从 Figma MCP 导出代码后，需要收敛到项目技术栈并保持视觉一致。
- **动效 / 过渡 / 入场出场 / hover 微交互 / 动效 Review**：除本 skill 外，**必读** **[web-animation-design](../web-animation-design/SKILL.md)**（Emil Kowalski / animations.dev 体系：缓动、时长、`prefers-reduced-motion`、仅 animating `transform`/`opacity` 等）。**层次**：视觉与 Token 仍服从 **`design.md`** 与 **`tokens.css`**；动效语义与可访问性按 **web-animation-design**。
- **工作台列表页**（分区标题、工具栏、网格 / 列表切换、置顶灰底面板、hover 操作、弹出菜单、骨架加载）的对齐与交互细节：见下文「密集工作区页面（执行要点）」与 `design.md` §7.6。
- **要在 Figma 里改稿 / 用 `use_figma` 写入**时：改用打包入口 **[o2x-figma-workflow](../o2x-figma-workflow/SKILL.md)**（先 `figma-use`，整页再 `figma-generate-design`，并固定 One2X `fileKey`）。

## Required: read the canonical spec

1. **打开并遵循** 工作区根目录下的 [`design.md`](../../../design.md)（相对本文件：`../..` 到 `.cursor`，再 `..` 到工作区根）。
2. 若 `design.md` 路径不同，在用户工作区根目录查找 **`design.md`** 文件并以其为准。

全文规范（Token 表、组件清单、布局配方——§7.5 紧凑面板、§7.6 密集工作区页面及 Medeo 参考值、Share/VideoShareDialog 模式、代码映射）均在 `design.md` 中；本 skill 只保留执行要点。页面级数值表和长规格写进 `design.md`，这里只留检查点和指向。

## Figma 到代码：强制工作流

当实现来源是 Figma URL、Figma 节点或 Figma 截图时，必须按以下顺序执行。截图只能校验外观，不能替代结构与变量证据。

1. **锁定来源**：解析 `fileKey` 与 `nodeId`；没有具体节点时先取得当前选择或请用户提供 node-specific URL。记录目标 viewport、主题和需要覆盖的状态。
2. **同时获取结构与视觉证据**：调用 `get_design_context` 和 `get_screenshot`。复杂节点若上下文截断，先用 `get_metadata` 找出主要子节点，再逐个获取 `get_design_context`；不要根据截图猜 Auto Layout、约束或组件层级。
3. **读取规范证据**：对 token 敏感节点调用 `get_variable_defs`；用 `search_design_system` 查对应 One2X 组件、变量和样式。读取目标项目的 `design.md`、`tokens/tokens.css`、已有 UI 组件及其变体。
4. **先做映射，再写代码**：形成简短映射清单，至少覆盖 `Figma component -> project component/variant`、`Figma variable/style -> CSS token/text style`、`asset -> supplied asset source`。找不到映射时先查库和项目；仍不存在才新增 token/variant 或记录明确例外。
5. **按项目约定实现**：把 MCP 输出当设计结构证据，不直接照抄生成的 React/Tailwind。复用现有组件、状态和响应式模式；使用 Figma 返回的资源，不引入替代图标包或占位素材。
6. **渲染并对稿**：在目标 viewport 运行页面并与同一节点截图对比。优先修正结构、尺寸、间距、字体、颜色、圆角、描边、资产和交互状态；每轮从最大视觉差异开始。
7. **通过门槛后完成**：运行项目测试/构建，并完成下方验收。未进行实际渲染对比时，不得声称 1:1、pixel-perfect 或已完全匹配。

### 映射与冲突优先级

按以下顺序裁决，避免“设计稿优先”和“设计系统优先”互相打架：

1. **语义与组件身份**：One2X 已发布组件、变量、文字样式及 `design.md`。
2. **该节点的明确设计意图**：Figma 实例属性、变体、约束和视觉参考。
3. **项目实现约定**：现有组件 API、路由、状态、响应式和可访问性模式。
4. **局部补偿**：只在前三者不能表达设计时使用，并记录原因。

若 Figma 数值与已命名 One2X token 不一致，先判断是实例变体、过期设计还是缺失 token。不要静默取最近值，也不要直接硬编码。必要时采用设计稿值完成视觉修复，同时明确指出应同步更新的 `design.md` / `tokens.css` / Figma 库。走查中设计师直接给出的数值（如「间距 1px」）属于第 2 级「明确设计意图」：照做，不吸附到最近的 token 档；没听清先复述确认，不要换成同类元素的现有值。不在 `Space/s*` 档内的 1–3px 光学微调，代码里就近注释来源（`design.md` §4.5）。

### 完成验收

- [ ] 已获取目标节点的 `get_design_context` 与 `get_screenshot`；截断内容已拆分读取。
- [ ] token 敏感实现已检查 `get_variable_defs`，并完成 Figma 到项目的组件/token 映射。
- [ ] 已复用项目组件和 One2X 语义 token；新增 primitive、variant 或 token 有明确理由。
- [ ] 没有用裸 hex / `rgba()`、任意字号/行高/间距/圆角替代已有 token；颜色都随明暗主题切换，已在深色模式下看过一遍；例外均有注释或交付说明。
- [ ] 默认、hover、active、focus、disabled、loading 等设计中存在的状态已实现；点开菜单后触发按钮回到 default（展开只用 `aria-expanded` 表达）；状态切换不改变盒子尺寸；同页 loading 用同一种骨架（`design.md` §4.3、§7.6）。
- [ ] 响应式行为来自 Figma constraints/Auto Layout 与项目断点，不是只匹配单张静态截图。
- [ ] 已在目标 viewport 实际渲染并对比参考图；布局、排版、颜色、资产和圆角描边无明显偏差。对齐与间距按**可视边缘**实测（不按热区或盒子），改动后在所有分区、所有视图（网格 / 列表）下复量，不只看刚改的元素；组件变体实际生效的尺寸、颜色、圆角读浏览器计算值。
- [ ] 勾选框、选中态、选择模式、生效中的筛选按钮符合 `design.md` §4.3 / §6 / §7.6；hover 才出现的操作仍默认隐藏；改过的圆角已连同内层一起复算同心。
- [ ] 构建、类型检查和相关测试通过；无法执行的检查已明确说明。

## Agent workflow

1. **优先对齐 Token**：`Surface/*`；**`Shape`** 集合内 **`Radius/*`** / **`--shape-radius-*`**（名=px）、**`Space/s*`** / **`--space-s*`**（**s**=阶梯档，≠px）；字样式 **`--type-*`** 与 **`--font-family-*`**；以及 `State Layers/*`、`Schemes/*`（见 `design.md`、`tokens/tokens.css`）。
2. **网页 / 静态页（强制）——「颜色与文字都用变量」**
   - 若仓库有 **`tokens/tokens.css`**，**颜色**一律 **`var(--color-…)`**；**字号/行高/字间距**一律 **`var(--type-…)`**（及 **`--font-family-*`**）；**间距** **`--space-s*`**、**圆角** **`--shape-radius-*`**（或项目中等效 token 名）。  
   - **禁止**：裸 hex、任意 `font-size: 14px` / `margin: 12px` 等与 token 无关的魔法数，除非 **`design.md` 写明特例**。
   - **颜色一律用随明暗主题切换的 token（强制）**：文字、图标、填充、描边、蒙层、阴影颜色、TS 颜色常量都用深色模式下会重新取值的语义 token（Medeo：`var(--Surface-*, #fallback)`、`var(--State-Layers-*-Opacity-NN, rgba(...))`），不写裸 hex / `rgba()` / `white`；`Inverse Surface` 按钮上的蒙层用 `Inverse On Surface` 档；只有图片 / 视频上的遮罩与白字、视频黑边、品牌渐变可保留字面值，并在同一行注释声明原因（`design.md` §4.6）。
   - **间距与圆角尽可能用变量**：值落在档位上就用变量（Medeo 代码：`var(--Space-S-n, Npx)`、`var(--Radius-N, Npx)`），负值写 `calc(-1 * var(…))`，同心内层写 `calc(var(--Radius-8, 8px) - 2px)`；只有不在档位上的 1–3px 光学微调写字面值并注释（`design.md` §4.5、§4.6）。  
   - 与 **`design.md` § Design scale「团队约定」**、**`o2x-figma-workflow`** 中「设计稿全变量」**对表**：设计侧用 Figma 变量 + Text style，代码侧用 **`tokens.css`**。
2.1 **Material 颜色角色配对（强制，见 `design.md` §4.2）**：`Schemes/*` 必须按 **Role / On Role / Container / On Container** 成对使用。
   - **高强调底**：`Schemes/<Role>` 只作为对应角色的高强调色面；其上文字 / 图标只能用 `Schemes/On <Role>`。
   - **低强调容器**：`Schemes/<Role> Container` 只作为对应角色的柔和容器；其上文字 / 图标只能用 `Schemes/On <Role> Container`。
   - **禁止跨配对**：不要把 `On Primary` 放在 `Surface`、`Primary Container` 或 `Secondary` 上；不要把 `On Primary Container` 放在 `Primary` 上；其他 Role 同理。
   - **One2X 双主色**：默认主按钮仍用 `Surface/Inverse Surface` + `Inverse On Surface`；`Schemes/Primary` + `On Primary` 只给最高强调的品牌动作，每屏 0–1 个。`Secondary` / `Secondary Container` 不能替代主品牌 CTA。
2.2 **Surface 两套层级（强制，见 `design.md` §4.1）**：不要把所有 Surface 当成一条梯子。
   - **页面/大分区底色明度**：用 `Surface/Surface Dim`、`Surface/Surface`、`Surface/Surface Bright`。Dim 更沉，Surface 默认，Bright 更亮。
   - **容器强调层级**：用 `Surface/Surface Container Lowest` → `Low` → `Container` → `High` → `Highest`。用于 Card、Sheet、Menu、Panel、输入区块等 contained area；`Surface Container` 是常规默认，Lowest/Low 降低强调，High/Highest 提高强调。浮出菜单 / 下拉面板例外，用 `Surface Container Lowest`（`design.md` §4.1、§8）。
   - **禁止混用**：不要把 `Surface Bright` 当作最高容器；不要从 `Surface Container Low` 开始漏掉 `Surface Container Lowest`；嵌套容器靠 Container 层级 + `Outline Variant` / `On Surface Variant` 0.5px 分隔。
3. **描边（默认）**：低强调容器、卡片、输入框、列表分隔和图标容器的描边，优先用 **`Surface/On Surface Variant`**（代码侧 `--color-surface-on-surface-variant`）+ **`0.5px`**。只有需要更弱层级、禁用态、分隔线层级或设计稿明确指定时，才改用 `Outline` / `Outline Variant` / 1px。Compact 档（弹出菜单、下拉、托盘面板）的容器边框与分隔线改用 `Outline Variant`（`design.md` §2.1）。
4. **Figma 组件写入（强制）——「不是只看数值，要看变量绑定」**
   - 写入或更新 One2X 组件时，Auto Layout 的 **`padding*` / `itemSpacing`** 必须绑定 Figma **`Shape/Space/s*`** 变量；四角半径必须绑定 **`Shape/Radius/*`** 变量。  
   - 只把数值设成 8、12、16、999 等，不算完成；右侧面板要能看到变量绑定。胶囊圆角用 **`Radius/Full`**，不要保留裸 `999px`。  
   - 具体 `use_figma` 绑定方式和验收脚本见 **[`o2x-figma-workflow`](../o2x-figma-workflow/SKILL.md)** 的 **Shape 绑定检查**。
5. **组件语义（代码侧也要「组件化」）**：优先使用 **与设计系统对齐的 UI 原语**（项目里已有的 Button、Field、封装好的区块），**不要**为每个页面手写一整块无复用的「假组件」。按钮层级（Filled vs Outlined vs IconButton）、菜单 **0 Density**、列表项变体以 Figma 为准；**主行动按钮（双主色，见 `design.md` §3.1）**：**默认**用 **Filled** + **`Surface/Inverse Surface`**（`--color-surface-inverse-surface`）+ **`Inverse On Surface`**（`--color-surface-inverse-on-surface`）的**黑色**主按钮；**只有最高强调**那一个才升级到 **`Schemes/Primary`**（`--color-schemes-primary`）+ **`On Primary`**（紫色，每屏 0–1 个，**非常克制**）。
5.1 **图标（强制，见 `design.md` §6.1）**：所有图标统一调用 One2X 图标库 **`@one2x/o2x-icons`**（medeo-fe `packages/o2x-icons`，字体图标，数量以 `info.json` 为准）——组件 **`<XxxIcon />`** 或字体 className **`o2x-icons-<名>`**，颜色用 **`currentColor`**，常用 **18/20/24px**（Compact 参考：工具栏 18、卡片角标 16、菜单项 14）。实现任何语义图标前都先查 `info.json` / 可视化预览「图标」区：主题切换用 **`LightModeIcon` / `DarkModeIcon`**，仪表盘用 `DashboardIcon`，搜索用 `SearchIcon` 等；只要库里已有，就必须复用。**禁止**临时画 SVG、用 CSS 拼图标、引第三方图标库（Material Symbols / Lucide / Iconfont 等）或用 emoji 占位。**设计指定的图标名库里没有时，不拿语义相近的图标顶替**（指定 `TableEyeIcon` 就不用 `VisibilityIcon`）：先查 One2X Figma 图标页（node `60839:470`）是否已有、只是没同步，按 `design.md` §6.1「缺图标」同步（有 `FIGMA_TOKEN` 用 `pnpm sync`，没有则按包 README 手动补）。
5.2 **先查设计系统组件与变体（强制，见 `design.md` §6）**：写 Tooltip、按钮、图标之前，先找 `@one2x/o2x-design` 里现成的组件和变体，不自写同类组件，也不把一个变体改造成另一个变体的样子。Medeo 例子：Tooltip 用库 `Tooltip`；浮在封面上的轻按钮用 `kind="text"` 浅色方案加浅底，不自创深色毛玻璃底；实底按钮用 `kind="filled"`，不用 `kind="text"` 再涂黑。
   - **变体会覆盖你写的值**：`IconButton size="small"` 把图标压到 14px；组件默认前景是 `On Surface`，不继承父级颜色。交付前在浏览器里读图标尺寸和颜色的计算值。
   - **只保留一层状态底色**：组件自带 state layer 又在外层叠了 hover 底时，只留一层，圆角跟随按钮外形（`design.md` §4.3）。
   - **状态层要在实际底色上看得出**：反色实底按 `design.md` §4.3「特殊表面例外」提高档位，并在浏览器里比对亮度。
6. **实现**：映射到 **`tokens/tokens.css`** 已有变量；禁止无约定地硬编码与设计冲突的值。
7. **冲突处理**：按上方“映射与冲突优先级”裁决；不得用一句“Figma 为源”跳过 One2X 组件与 token 语义。
8. **Figma MCP（设计稿实现时强制）**：使用 `get_design_context`、`get_screenshot`、`get_variable_defs`、`search_design_system`（One2X `fileKey`: `wHNBqjzSQZM8a4DlyBIDqW`）。只有不以 Figma 为输入的纯代码任务才可跳过。
9. **动效**（有则执行）：阅读 **[web-animation-design](../web-animation-design/SKILL.md)**；需要细节时见同目录 **[PRACTICAL-TIPS.md](../web-animation-design/PRACTICAL-TIPS.md)**。Review 动效问题时按该 skill 要求使用 **Before / After 表格**输出。动效不替代 Token：例如 `transition` 的 `color` / `background-color` 仍用 **`var(--color-…)`**。库组件自带的动效与延迟（如 `Tooltip` 的偏移与冷 / 暖延迟）直接沿用，不另定数值。
10. **走查微调（设计师选中元素提意见时）**：样式类反馈（菜单规格、外框阴影、按钮默认态、骨架、图标颜色、勾选框、圆角）同步到同页所有同类元素（含同页不同分区，如 Createspace 的创作与素材），不等逐个指出。默认只在本页范围内覆盖；设计师说明是通用组件、要求统一时才改共享组件，并在交付时列出被波及的其它页面（如编辑器素材面板）。位置类反馈只动被点名的元素本身（不连带移动它所在的面板或布局），若因此偏离共同起点线，交付时说明并询问是否整体同步。只说「大一点 / 小一点」时小步调整，并报出改前 → 改后的数值。走查中的协作方式见下文「走查协作方式」。

## 走查协作方式

设计师走查时通常是「选中元素 + 截图 + 一句话」。下面是反复出现过的做法，照这个节奏配合能少走几轮：

- **先量再改，改完再量**：动手前读浏览器计算值（尺寸、间距、圆角、颜色），改完在同一视口复量，回复里报「改前 → 改后」。「看起来不对」多半是可视边缘没对齐，按可视边缘量（`design.md` §4.5）。
- **问「现在是多少」时列表回答**：按元素逐行给出计算值、来源变量和换算（如 `--Radius-8` → 10px），标明哪些是实测、哪些按 CSS 推断。
- **圆角、间距一改就查一圈**：任何圆角改动顺带复算贴着它的内层是否同心、四周可视间距是否相等（勾选框、角标、缩略图、⋯ 按钮），不等设计师逐个指出。
- **「这是通用组件」= 同类一起改**：同一个共享组件渲染的地方一起统一，交付时列出影响范围。
- **问「有什么建议」时先给方案**：给现状、问题和推荐做法，等设计师说「改」再动手；说「都优化」就把建议全部落地，做不到的（如需后端配合）先说明。
- **试了又改回，以最终值为准**：同一处来回调整过（如勾选框填充 Background 90 → Scrim 40 → 改回 Background 90），代码和规范里只留最后定下的值。
- **设计师说「我写过规则」时先查**：先在本 skill、`design.md` 和环境里的其它设计 skill 里找原文（如 Geist Mono 的 `ss09`），找到就照做并告诉对方出处；确实没有再按现象排查。
- **保持既有交互**：hover 才出现的操作、从右锚定等已定交互不因顺手改样式而丢；发现被别人的提交改掉时先指出是谁、何时改的，再按设计师意见恢复。
- 用中文回复，数值用表格或短列表，不堆长段落。

## 描边 / Stroke

描边默认是轻边界，不是装饰线。除非组件规范或设计稿另有说明：

- 颜色优先用 **`Surface/On Surface Variant`**；代码侧用 `var(--color-surface-on-surface-variant)`。**Compact 档例外**（`design.md` §2.1）：弹出菜单、下拉、托盘面板的容器边框与分隔线用 `Surface/Outline Variant`，可交互的 Outlined 按钮 / 输入框用 `Surface/Outline`。
- 宽度优先用 **`0.5px`**；Figma 写入时设置 `strokeWeight = 0.5`，并把 `strokes` 的 paint 绑定到对应 Color 变量。
- 对容器类节点优先用 `strokeAlign: inside`，避免描边改变外部几何尺寸。
- 如果 0.5px 在目标渲染环境过淡或不可见，可以升到 1px，但要有明确原因；不要把 1px 当默认值。
- **描边被裁掉就改 ring**：按钮或容器自身（或组件内部某层）设了 `overflow: hidden` 时，`border` 与外扩的 `outline` 可能根本不显示。先在浏览器里确认线是否被裁，再改用 `box-shadow: inset 0 0 0 0.5px var(…)` 或负 `outline-offset` 的 outline；同时在深色模式下看线色（`Outline` 在深色下是一根浅色线，与浅色模式观感不同）。
- **可拖拽分栏线（resizer）用中性色**：hover、键盘聚焦、拖动中显示的线用 `Surface/Outline`，不用 `Schemes/Primary`；品牌紫只留给最高强调（`design.md` §3.1）。

```css
.surface-card {
  border: 0.5px solid var(--color-surface-on-surface-variant);
}
```

## 视觉补偿 / Optical Alignment

几何对齐不总是视觉对齐。遇到标题、label、hint、辅助说明与圆角矩形（Card、Input、Select、Media frame、Toolbar、Dialog surface）相邻时，不要只把文字左边缘和容器外边缘做 `x` 值相等；要根据圆角做少量内缩，让文字看起来和圆角形体的视觉重心对齐。对齐以**肉眼可见的内容边缘**为准（文字、封面、缩略图、可视按钮底），不以带内边距的卡片外框、按钮热区或容器盒子为准：卡片自带 4px 内边距时，标题对齐封面左缘，而不是卡片外框。

### 圆角矩形外部文字

当文字位于圆角容器上方或下方，并且表达上属于该容器时：

- **默认规则**：文字向内缩进约 `radius * 0.5`，再吸附到 `--space-s*` token；常见上限为 `12px`，避免标题看起来脱离卡片。
- **小圆角**：`Radius/0`、`Radius/4`、`Radius/6` 通常不需要补偿，或最多 `--space-s1`。
- **中等圆角**：`Radius/8`、`Radius/12` 通常用 `--space-s1`（4px）；如果是输入框 label、hint，且圆角明显，可以用 `--space-s2`（8px）。
- **大圆角**：`Radius/16` 通常用 `--space-s2`（8px）；`Radius/20`、`Radius/24` 通常用 `--space-s2` 到 `--space-s3`（8-12px）。
- **胶囊 / Full radius**：不要按 `1000px` 计算。按实际高度估算，取 `min(height * 0.1, 12px)`，再吸附到最近的 `--space-s*`。

示例：

```css
.field-label {
  margin-inline-start: var(--space-s2); /* 16px radius input -> 8px optical inset */
}
```

```tsx
<section>
  <h2 className="ml-[var(--space-s2)]">Upcoming sessions</h2>
  <div className="rounded-[var(--shape-radius-16)]">...</div>
</section>
```

### 何时不要补偿

- 文字属于页面网格，而不是某个圆角容器，例如页面主标题、列表大分组标题。
- 卡片本身已经有同一列的内部文字锚点，应优先对齐内部内容，而不是外轮廓。
- 多个相邻容器圆角不同，且标题控制一整个区域时，标题应对齐区域内容网格。
- 设计稿已明确使用几何对齐，或 Figma 主组件已有固定变量绑定。
- 页面有统一左起点线时（如工作台列表页）：分区标题、Pinned、列表表头都对齐这条线，不按置顶灰底的圆角另做内缩（`design.md` §7.2、§7.6）。

### 辅助信息块内部布局

Prompt、Hint、Note、Code snippet 等辅助信息块如果同时包含标签、正文与操作按钮，不要默认做三栏横排。窄卡片里三栏会让左侧标签占掉过多宽度，正文被挤成很窄的多行。

- 默认做两行：第一行左侧短标签、右上角轻操作（复制 / 展开 / 更多）；第二行正文独占整行。
- 正文区域 `min-width: 0`，允许自然换行；只有长代码、命令或不可断开的 token 才使用水平滚动。
- 标签只承担分类提示，不要给标签固定大列宽，也不要让标签参与正文列宽分配。
- 复制按钮这类轻操作放在角落，不要夹在正文中间；若操作位于正文行右侧，正文需要给按钮预留宽度。
- 角落按钮到相邻两条容器边的距离必须一致（用同一个 inset token 控制）。例如右下角按钮的右边距与下边距相同；并按同心圆角计算：`action radius = outer radius - inset`。不要让角落按钮贴边（「不贴边」指两条边都留出相等、可见的间距，不要求大留白；密集网格卡片的 hover 角标可收到约 2px，见 `design.md` §7.6），也不要给它一个与外框无关的圆角。

### 圆角同心关系

任何元素只要使用圆角，就要检查它与内层、外层相邻圆角元素的同心关系。圆角元素嵌套时，内层不要直接复用外层圆角；为了让角落间距看起来均匀，使用同心圆角：

```css
.card {
  --card-radius: var(--shape-radius-24);
  --card-padding: var(--space-s2);
  border-radius: var(--card-radius);
  padding: var(--card-padding);
}

.card-media {
  border-radius: max(0px, calc(var(--card-radius) - var(--card-padding)));
}
```

规则：`inner radius = outer radius - gap/padding`。如果 padding 大于 radius，内层圆角归零。Figma 里同理：外层 `Radius/24` + 内距 `Space/s2` 时，内层优先用接近 16px 的 radius，而不是继续用 24px。

执行要求：

- 内层图片、媒体框、按钮组、输入框、浮层内容区、菜单项、分段控件选中块、卡片角标按钮等，只要贴近外层圆角容器，都按同心圆角计算（Medeo 参考：分段控件外框 4px、内距 1px → 选中块 3px；菜单项圆角 = 面板圆角 − 容器 padding）。
- 外层包裹层若只是为了裁切内容，可以只在外层设置圆角并使用 `overflow: hidden` / `clip`，避免重复设置不一致的内层圆角。
- 多层嵌套时逐层计算，不要把最外层 radius 直接传给所有子元素。
- Figma 写入时同样要检查：外层 radius、padding、内层 radius 三者要能解释为同心关系。
- **外层半径以用户看到的轮廓为准**：卡片 hover 时有贴边描边（如 `outline-offset: -1px`）的，按这条描边的半径计算内层元素，不按内部封面或盒子计算。
- **单独改嵌套元素的圆角时，先查同心**：给定数值与同心值不一致时，先指出差异并建议同心值（Medeo：卡片 hover 外框 6px，角标 inset 2px → 4px，勾选框 inset 3px → 3px）。反过来，外框圆角一改，贴着它的内层（角标、勾选框、缩略图、菜单项）全部一起复算。
- **控件同心，封面可由设计指定**：内容主体（封面、图片）可以按设计给出比同心值更大的圆角（Createspace 卡片 6、内边距 4，设计定封面 4px 而不是 2px），照做并注释说明是有意不同心（`design.md` §4.4）。
- **圆角要落在可见像素上**：方形框里放非方形图片时，不要把 `img` 撑满再用 `object-fit: contain`，那样圆角只落在透明盒子上。让 `img` 按自身比例显示（`width/height: auto`，`max-width/max-height: 100%`，父框尺寸确定），圆角作用在图片本体上。
- **Token 与字面 px 不要混算**：Medeo `--Radius-N` 的计算值不等于名中数字（如 `--Radius-8` → 10px，换算见 `design.md` §4.6）。外层尽量用变量，内层写 `calc(var(--Radius-8, 8px) - 2px)` 引用同一个变量；只有外层确实不在档位上时内外层才都用字面 px（Medeo 没有计算为 6px 的 `--Radius-N`：6px 的菜单面板、卡片与列表行外框写字面值，内层 4 / 3 / 2px 同样写字面值）。核对时读浏览器计算值。

## Typography 使用语义（实现侧速查）

对齐 One2X 当前字阶时，按语义选层级，不按“看起来接近”手动改字号：

- `display/*`：营销/品牌级大标题（Hero、活动 KV）；不要用于常规业务弹窗与表单。
- `headline/*`：页面或章节级标题（信息结构层）；不要用于按钮文本。
- `title/*`：组件和区块标题（Dialog、Card、List Section）；是日常业务界面主力标题层。
- `body/*`：阅读内容（正文、说明、元信息）；不要承担主操作强调。
- `label/*`：交互标签（Button、Tab、Chip、Field label）；不要用于正文段落。
- `*-prominent`：同语义加权（主 CTA/关键操作）；避免整屏普遍使用导致层级失真。

### Geist Mono 数字与千分位逗号

- 计数、积分、时长等数字采用 Geist Mono 时，默认保持整串 `letter-spacing: 0`，不要为修正逗号而压缩所有数字间距。
- 使用千分位逗号时，将逗号包成独立元素，只对逗号做光学间距调整：收紧左侧数字到逗号的空隙，同时单独保留逗号到右侧数字的呼吸空间。必须同时检查逗号两侧，不能只看整串宽度。
- 间距值需按字号与实际 Geist Mono 字形目测校准。Medeo 顶栏 12px 的参考值为逗号 `left: -2px`、`margin-right: 1px`；此值是光学补偿，不作为所有字号的通用 token。
- 使用该项目仅提供 400 字重的 Geist Mono 时，数字设 `font-weight: 400`，不要依赖浏览器合成 500/600。
- Geist Mono 默认使用斜杠零；需要无斜杠 `0` 时，使用 `font-feature-settings: 'ss09' 1`。不要同时启用 `font-variant-numeric: slashed-zero` 或 OpenType `zero` 特性（`'zero' 1`），否则会重新显示斜杠。
- 检查最终承载数字的元素，而不只检查外层标签：滚动数字、格式化数字等子组件可能自行设置 `font-variant-numeric: slashed-zero` 和 `'zero' 1`，覆盖父级。此时在使用场景的子组件根节点显式设置 `font-variant-numeric: tabular-nums; font-feature-settings: 'tnum' 1, 'zero' 0, 'ss09' 1;`，再用浏览器计算样式确认 `zero` 为 `0`、没有 `slashed-zero`。

### Medeo 组件/页面快速映射

- 营销 Hero：`display/large` 或 `display/medium`。
- 页面主标题：`headline/medium`（强章节可用 `headline/large`）。
- Dialog/Drawer 标题：`title/medium`；小区块标题：`title/small`。
- 正文与说明：`body/medium`；辅助注释/时间戳：`body/small` 或 `body/extra small`。
- 交互文案默认：`label/large`；主 CTA：`label/large - prominent`；紧凑工具条、弹出菜单项：`label/medium`。

## Menu Bar 锚点弹窗

- Menu Bar 中由图标按钮或头像触发的弹窗统一使用 100ms 展开、100ms 退出，按按钮所在边缘设置 `transform-origin`，从触发位置缩放与淡入，不做额外位移。
- 定位与缩放不能写在同一个 `transform` 上；定位使用 `top` / `left` 等坐标，弹窗自身只动画 `scale` 与 `opacity`，避免展开起点反向或位置跳动。
- 相邻入口切换时立即隐藏前一个弹窗，再显示新弹窗；指针从按钮移入其弹窗时保持打开。`prefers-reduced-motion: reduce` 下取消过渡。
- Menu Bar 里的列表型菜单与图标按钮，同样遵守下文「密集工作区页面（执行要点）」里的弹出菜单、触发按钮回到 default 与 Tooltip 规则（正文见 `design.md` §4.3、§6、§8）；积分卡这类不是菜单的悬浮卡片，只按本节的定位和动效处理。

## 密集工作区页面（执行要点）

工作台列表页：分区标题、工具栏、网格 / 列表切换、置顶灰底面板、hover 操作、弹出菜单、骨架加载。规则正文与 Medeo Createspace 参考值见 `design.md` §7.6；其中菜单、触发按钮与 Tooltip 的规则对所有页面都适用（正文在 `design.md` §4.3、§6、§8）。

- **点开菜单后，触发按钮回到 default（强制）**：图标按钮和 Sort / Filter / Group 这类文字下拉按钮都不保留 selected / pressed 底色，展开只用 `aria-expanded` 表达；模式开关（Select）和分段控件的当前项例外。
- **整页一条左起点线**：分区标题、Pinned、表头、封面、缩略图在所有分区、网格 / 列表两种视图下落在同一 `x`，按肉眼可见的内容左缘量；整体平移改共享滚动容器的 padding，所有起点一起动，已约定的留白（灰底距视口）不能丢；工具栏、灰底推近视口边时留小而固定的可见间距，同类控件右缘上下对齐，不出现横向滚动。
- **工具栏从右锚定**：按内容 / 数据 / 视图分区，视图切换在最右不动；切视图、换排序、展开搜索时锚点及其右侧不动，搜索展开把左侧操作往左推。文字按钮 hug 文案，不按最长文案写死宽度。
- **工具栏样式统一（局部覆盖）**：同一条工具栏同一 `gap`、同一圆角（分段选中块按同心），图标同尺寸，未选中前景 `On Surface Variant`、选中 `On Surface`；只在工具栏范围内覆盖，不改共享组件在别处的样式。
- **弹出菜单**：全页一套紧凑规格（项高 24、`label/medium`、图标 14）和一组面板 token；只有直接包含菜单项的那一层有描边 / 底色 / 阴影；菜单与触发按钮的距离按**可视**边缘量（Createspace 为 4px）；首列是图标时与按钮图标同轴（`crossAxis` 公式见 `design.md` §7.6），首列是文字时文字左缘对齐按钮图标左缘；距视口至少 4px；打开期间菜单位置固定（`design.md` §6）。
- **纯图标按钮配库 `Tooltip`**：沿用组件默认（上方、4px、500 / 100ms），带文字的按钮和菜单展开时不显示；列表 / 卡片里批量出现的行内按钮不逐个挂实例，改用共享的单个提示层。
- **hover 操作不占位**：按钮绝对定位叠在内容右端，内容用 `mask-image` 渐隐让位（只在按钮可见时加），不盖带底色的遮罩；它的任一菜单打开期间按钮保持显示。
- **置顶灰底面板**：内边距按可见内容量（左、下相等）；完整包住内部控件，加宽后确认没被祖先 `overflow` 裁掉；标题在文档流里独占一行；窄面板设最小宽度，放不下时默认显示标题、hover 或聚焦时换成控件。
- **从属间距极小（Createspace 定为 1px）**：标题栏与灰底、标题行与内容、表头与灰底读作一组；`margin` 与容器 `gap` 会叠加，改完量实际值。
- **整页一套扫光骨架**：每个异步区域都有形状匹配的占位；加载中不显示默认封面（默认封面只表示确认没有封面）。
- **保持 hover 才出现**：控制栏、置顶区视图切换、翻页箭头不改成常驻；列表行 ⋯ 在行内垂直居中，上 / 下 / 右到 hover 外框等距。
- **网格内容贴顶、列表外框居中**：网格卡片封面到外框上 / 左 / 右等距（多出的行高留在文字下方）；列表 hover 外框距视口左右相等；面板内分组标题文字对齐面板标题文字，展开箭头与文字同色。
- **横向滚动行**：两端 64px 渐隐只在可滚方向出现；裁切点贴相邻面板右缘与视口右缘；翻页箭头 hover 才出现、贴边，翻页用约 240ms ease-out 的滚动动画并可被滚轮打断（`design.md` §7.6）。
- **选择模式**：Select 原位展开成灰底工具组（全选 / 批量操作 / 取消），把左侧按钮推开，不用浮在内容上的底部条；同页只激活一个分区；全选三态，部分选中点击补全、全选点击清空，文案「全选（N）· 已选择 M 项」；全选记为状态（新加载条目自动选中）；支持 Shift 连选；选中条目只靠勾选框表达（`design.md` §4.3、§7.6）。
- **勾选框统一**：网格 / 列表 / 全选一套样式（未选 Background 90 + 0.5px On Surface 16 的 `outline`，选中 Primary），位置和圆角按所在外框同心、四周等距（`design.md` §6）。
- **生效中的筛选 / 分组**：Primary 08 底 + Primary 图标，与菜单展开的 default 态区分（`design.md` §4.3）。
- **分组视图不显示空分组**：没内容的分组连标题一起隐藏，全空时显示整体空状态。

## Out of scope

- 不替代产品 PRD 或无障碍专项审计；a11y 在遵循设计系统基础上按平台规范补强。
- 产品信息架构决定（如哪个 Tab 作首页、入口迁到哪个菜单）不写进本 skill，放 PRD 或导航文档。
- 不自动同步 Figma；大版本变更需人工或流水线更新 `design.md`。
