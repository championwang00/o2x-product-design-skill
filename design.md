# One2X Design System

> 规范仅此文件；技能说明见 `.cursor/skills/README.md`。（macOS 上勿用 `DESIGN.md` 当第二文件名，易与 `design.md` 冲突。）

**谁用**：团队共用的一份「事实来源」——你自己、同事、以及 Cursor 里的 Agent 都应对齐它；给同事拷贝仓库时带上本文件与 `tokens/`、`.cursor/skills/` 即可（详见 `.cursor/skills/README.md` §2）。

**两个带 One2X 的 Cursor skill 分别干什么**（不是「DISPATCH / WORKFLOW」两套规范）：`**o2x-design-system`** 管写代码/对稿；`**o2x-figma-workflow`** 管用 MCP 在 Figma 里改稿时叠加官方 `figma-use` / `figma-generate-design` 与本文档。若你在 Figma 左侧看到 **DISPATCH**、**WORKFLOW** 之类页面名，那是设计文件里的 **Page 命名**，和本 Markdown 里的章节标题不是同一套东西；本文件只列「尺度」与节选结构，**不会**逐页解释每个业务页名。

**Figma 源文件**（同一 `fileKey`，任选其一打开即可）：

- **整文件入口**（无 `node-id`，从目录/首页进入）：[📖One2X Design System](https://www.figma.com/design/wHNBqjzSQZM8a4DlyBIDqW/%F0%9F%93%96One2X-Design-System?m=auto&t=B0QwV6M00Yh5Mpct-6)
- **定位到某一帧**（URL 中带 `node-id`）：例如 [Share 区块](https://www.figma.com/design/wHNBqjzSQZM8a4DlyBIDqW/%F0%9F%93%96One2X-Design-System?node-id=79433-33267)、[🌈Styles](https://www.figma.com/design/wHNBqjzSQZM8a4DlyBIDqW/%F0%9F%93%96One2X-Design-System?node-id=49823-12141)

`fileKey`: `wHNBqjzSQZM8a4DlyBIDqW`。`?m=auto`、`t=` 等为 Figma 网页端参数，**不会**在链接里附带 Token 或组件数据；内容仍以云端文件为准。

**说明**：带 `node-id` 的链接只决定**默认聚焦哪一帧**；整文件含 Foundation、Components、Medeo 产品页等。**完整 Page 枚举见 [附录 A](#附录-afigma-文件结构全部-page-一览)**。**Figma 文件命名、图层与组件属性、Figma2code 协作、i18n 与字阶稿内规则见 [附录 C](#附录-cfigma-设计稿使用规范)**。实现界面时应对照对应页面与变量，而非仅依赖单一节点导出。

**MCP 若 504**：勿在超大文件里全 Page `findAll`；只用变量 API 或单页查询。详见 `.cursor/skills/README.md` §5。

---

## 目录

- [1. 视觉气质与关键特征](#1-视觉气质与关键特征)
- [2. One2X 尺度体系（Design scale）](#2-one2x-尺度体系design-scale)
- [3. 设计原则与参考](#3-设计原则与参考)
- [4. 设计 Token（Figma Variables）](#4-设计-tokenfigma-variables)
- [5. 字体排印（Typography）](#5-字体排印typography)
- [6. 核心组件](#6-核心组件)
- [7. 布局原则](#7-布局原则)
- [8. 深度与层级](#8-深度与层级)
- [9. 模式参考：Share / VideoShareDialog](#9-模式参考share--videosharedialog)
- [10. 代码映射与工程接入](#10-代码映射与工程接入)
- [11. Do's and Don'ts](#11-dos-and-donts)
- [12. 响应式与字阶模式](#12-响应式与字阶模式)
- [13. Agent Prompt Guide](#13-agent-prompt-guide)
- [附录 A：Figma 文件结构（全部 Page 一览）](#附录-afigma-文件结构全部-page-一览)
- [附录 C：Figma 设计稿使用规范](#附录-cfigma-设计稿使用规范)
- [附录 B：修订记录](#附录-b修订记录)

---

## 1. 视觉气质与关键特征

Medeo / One2X 产品界面建立在 **Material Design 3** 的组件语义之上，但品牌识别来自 **中性表面（Surface）上的少量紫色主行动点**：大面积灰白阶与清晰层级，让 `**Schemes/Primary`** 在关键操作上保持高辨识度。字面上是「工具型」效率界面，而非强装饰营销站——营销与 Hero 场景再交给 `**display/*` + Nohemi** 等档位完成叙事。

**Key characteristics**

- **双字族**：正文与 UI 用 **Manrope（Plain）**；品牌展示标题用 **Nohemi（Brand）**，与 Typescale 绑定。
- **双主色**：常规主按钮用 `**Surface/Inverse Surface`**（黑）+ `**Inverse On Surface`**；只有**最高强调**的那一个用 `**Schemes/Primary`**（紫）+ `**On Primary`**。紫色**非常克制**，每屏通常 0–1 个（见 §3.1）。
- **变量驱动**：颜色、字阶、圆角、间距均来自 Figma **📖One2X** 变量；Web 以 `**tokens/tokens.css`** 的 `**--color-*`、`--type-*`、`--space-s*`、`--shape-radius-*`** 为准。
- **圆角 vs 间距命名**：圆角 `**Radius/{数字}`** = 半径 **px**；间距 `**Space/s0`…`s10`** = **阶梯档**，不等于数字本身即 px（见 §4.4–§4.5）。
- **多模式 Color**：Medeo 产品以 **Medeo light / Medeo dark** 为主；Mebox 为另一套 Color 模式；实现时跟随主题与 `tokens.css`。
- **工程纪律**：避免裸 hex、魔法数字字号与间距；列表与表单优先 **库组件实例**（Figma）与 **token**（代码）。

---

## 2. One2X 尺度体系（Design scale）

把 Figma 里的变量与组件组织成可执行的「尺度」：写代码或 `use_figma` 时按层级选用。**固定文件**：`fileKey` `**wHNBqjzSQZM8a4DlyBIDqW`**（📖One2X Design System）。


| 层级  | 集合 / 来源                        | 要点                                                                                                                                                 |
| --- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| 色彩  | `Color`（Medeo / Mebox 各 Mode）  | Medeo 产品用 **Medeo light / dark**；语义色 `**Schemes/*`**、表面 `**Surface/*`**、`**State Layers/***`。品牌感主要靠少量 `**Schemes/Primary` + `On Primary**`（见 §3.1） |
| 字族  | `Typeface`                     | **Manrope（Plain）**、**Nohemi（Brand）**                                                                                                               |
| 字阶  | `Typescale`（Baseline / mobile） | 响应式对齐两套模式                                                                                                                                          |
| 形状  | `Shape`（Baseline）              | `**Radius/*`** 按**半径 px** 命名（`Radius/0`、`Radius/4` … `Radius/40`、`Radius/6`、`Radius/Full`），见 §4.4                                                  |
| 间距  | `**Shape`** 集合内 `**Space/s*`** | **阶梯代号** `Space/s0`…`Space/s10`（**非**像素名），见 §4.5                                                                                                   |
| 组件  | `Components`、Medeo 各页          | 优先 **库内组件实例**，见 §6                                                                                                                                 |


### 2.1 密度档（Density）——开工前先判定

同一套 token 在不同容器里的「用法」不同。**先判定密度档，再选字阶、间距、按钮形态**；判错档位是 Agent 生成稿「看起来像网页、不像工具」的首要原因。**密度按区域判定，不按整页**：工作台页面里的工具栏、弹出菜单、列表密集区和置顶 / 分组灰底面板按 Compact 处理；密集列表工作台的页面边距也可以低于 Default 的 `s4`–`s6`（Medeo Createspace：内容起点距视口 12px、置顶灰底距视口 4px，见 §7.6）。


| 密度档 | 适用容器 | 外边距 / 行内边距 | 行高 | 主字阶 / 次字阶 | 主操作形态 |
| --- | --- | --- | --- | --- | --- |
| **Default（业务页）** | 工作台页面、Dialog、Drawer、Card、表单 | `s4`–`s6` / `s3`–`s4` | 48–56 | `body/medium` / `body/small` | Filled Button 40（详见 §3.1） |
| **Compact（工具面板）** | 托盘 / 菜单栏面板（340×480）、下拉菜单、侧栏、浮出面板、列表密集区 | **`s2`（8px）** / **`[2, 8]`** | **24（标题行）· 32（状态条）· 41–45（列表行）· 33（传输行）** | **`label/medium`（12） / `label/small`（11）** | **紧凑黑钮 24 高 `Radius/6`**，放在分组标题行右侧（§3.1） |


Compact 档的关键规则（2026-09 由 Medeo 桌面端托盘面板定稿归纳，参考帧见 §7.5）：

- **层级靠不透明度，不靠换 token**：主文 `Surface/On Surface` 100%；次要文本 `Surface/On Surface Variant` **60%**；分组标题 / 邮箱等三级信息 `On Surface Variant` **40%**；图标随文本同色、同不透明度。**不要**为了做层级把 12px 升到 14px，也不要引入第三种颜色 token。**交互控件前景不走这套降级**：工具栏里未选中的按钮（纯图标与带文字）图标和文字统一 `On Surface Variant` 100%，`On Surface` 只给选中态（§4.1、§6.1）。
- **只用两档字号**：12 / 11。`title/medium`（16）只给 Dialog 与登录视图标题；`label/large`（14）只给通栏按钮与空态提示。**禁止**在 Compact 列表行里用 `label/large - prominent` 做行名。
- **描边一律 0.5px**：容器边框、分隔线、图标按钮描边用 `Surface/Outline Variant`；可交互的 Outlined 按钮 / 输入框用 `Surface/Outline`；浮出于页面之上的 Dialog 才用 `Surface/On Surface Variant`（深一档，配 Elevation）。
- **分组标题行 = 24 高**：`label/medium` @40% 左对齐，右侧放该分组的唯一操作（紧凑黑钮或 20px IconButton）。分组之间不用大留白，靠标题行 + 一条 `HorizontalDivider` 分段。标题行在文档流里独占一行，不用绝对定位压在内容上；标题行与它所属的内容之间只留 1–4px，让两者读作一组，不套用区块间距（Medeo 定稿值见 §7.6）。
- **进度条单色**：`Progress` 组件，轨道 `On Surface` 10%、进度 `On Surface` 40%、4px 高；**不用**蓝色 `Secondary Container` 做进度。
- **状态徽标 = 库内实心图标**：`CheckCircleIcon` / `ClockLoader60Icon` / `ErrorFillIcon` 等 10px，放在 24px 文件夹图形右下角、外包一圈 `Surface Container Lowest` 白圈；不手绘圆点。
- **头像 32 圆角 `Radius/8`**，不用圆形。

### 2.2 团队约定（设计稿 + 代码都要对齐变量与组件）

- **设计稿（Figma）**  
  - **颜色**：图层填色/描边绑 **📖One2X 的 Color 变量**（消费稿用库变量 `import` / 面板绑定，勿自建一套重复集合）。  
  - **字阶**：正文/标题用主库 **Text style**（`title/medium`、`label/large` 等），承接 **Typescale**；勿手写零散字号当长期方案。  
  - **形状与间距**：圆角用 **Shape**；间距用 **spacing** 或 Auto layout，与设计变量一致。  
  - **结构**：**能用组件就不用裸 Frame 冒充**——按钮、输入、列表等一律 **库组件实例**；详见 `**o2x-figma-workflow`**。
- **前端（Web）**  
  - **颜色与排版**：以 `**tokens/tokens.css`** 的 `**--color-*`、`--type-*`、`--space-s*`、`--shape-radius-*`、`--font-*`** 为准；**禁止**裸 hex、无 token 的裸 `font-size` / 间距（细则见 `**o2x-design-system`**）。
  - **组件**：先用 `@one2x/o2x-design` 里现成的组件与变体，不自写同类组件（§6）。

---

## 3. 设计原则与参考

- **组件语义**：与 **Material Design 3** 对齐处，遵循 Figma 组件描述中的用法（例如 [Buttons](http://m3.material.io/components/buttons/overview)、[Icon buttons](https://m3.material.io/components/icon-buttons/overview)）。
- **强调层级**：主要操作用 **Filled Button**；次要/并列操作用 **Outlined** 或 **IconButton**；成组图标按钮保持同一密度与圆角。同一条工具栏里的文字按钮、下拉按钮、分段切换外框和展开后的搜索框也用同一个 `gap` 与圆角（工作台工具栏见 §7.6，属工具栏范围内的局部覆盖，不改 §3.1 紧凑黑钮）。
- **文案与数字**：排版样式中启用 `font-feature-settings: 'zero' 1`（零宽数字等）时与设计稿一致。

### 3.1 双主色与主按钮（核心规则）

One2X 有**两个主色**，按强调层级分工，**紫色要非常克制**。整页以中性灰阶为底，黑色承担日常主行动，紫色只在最需要突出处点睛。


| 层级        | 填充                                  | 文字 / 图标                              | 用在哪                                                          |
| --------- | ----------------------------------- | ----------------------------------- | ------------------------------------------------------------ |
| **默认主按钮** | `Surface/Inverse Surface`（黑）        | `Surface/Inverse On Surface`（白）     | **大多数主要操作**：确认、提交、Copy link 等。这是日常主行动的**默认**承载。              |
| **最高强调**  | `Schemes/Primary`（品牌紫）              | `Schemes/On Primary`（白）             | 只给**最需要突出**的那一个行动 / 品牌强调点。每屏通常 **0–1 个**。                     |


- **先想用黑，再想用紫**：默认主按钮用 `Inverse Surface`（黑）；只有这一个行动需要特别强调时，才升级到 `Primary`（紫）。
- **网页**：黑色主按钮 `background: var(--color-surface-inverse-surface); color: var(--color-surface-inverse-on-surface)`；紫色强调 `background: var(--color-schemes-primary); color: var(--color-schemes-on-primary)`（图标同色）。代码里实底按钮用库 `Button` 的 `kind="filled"`，**不**用 `kind="text"` 再覆盖成黑底：`text` 的 hover 蒙层按浅底配色，落在黑底上看不出变化（§4.3）。
- **为何重要**：紫色用量越少越醒目；若把紫当默认主按钮色到处用，品牌焦点被稀释，反而读不出层级。**勿**用 `Secondary Container`（蓝）替代这两个主色。

**主按钮的四种形态（按容器选，颜色规则不变）**


| 形态 | 尺寸 | 圆角 | 用在哪 | 反例 |
| --- | --- | --- | --- | --- |
| **紧凑黑钮** | 高 **24**，`hasStart` 图标 18 + `label/medium`，pad `[0, 8, 0, 6]` | `Radius/6` | Compact 面板的分组标题行右侧（如「Sync folders · 3 ［＋ Add file］」）；列表内唯一主操作 | ❌ 在列表中间放一个通栏 48 高黑钮 |
| **通栏黑钮** | 高 **40**，宽 240–280，`label/large` | `Radius/12` | 空态引导（居中）、登录视图、单一行动页 | ❌ 正常列表状态下也保留通栏钮 |
| **Dialog 双钮** | 高 **44**，两钮等宽平分（gap `s2`）：左 Outlined（`Surface/Outline` 0.5px）取消，右 Filled 黑确认 | `Radius/12` | 系统确认框（360 宽，pad `[12]`，`Radius/16`，顶部 40px Logo，标题 `title/medium` 居中，正文 `body/small` 居中） | ❌ 单个全宽确认钮；❌ 红色危险钮（危险语义只在正文与图标里表达） |
| **行内 Outlined 对** | 高 **24**，两钮等宽，`Surface/Outline` 0.5px，`Radius/6`，左缩进对齐行内文本（pad-left 40） | 出错行下方的〔Retry〕〔Re-select〕等行级动作 | ❌ 把动作做成红色文字链塞在状态句后面 |


第三方登录按钮是唯一例外：**Google = `Schemes/Secondary Container` 蓝 + `On Secondary Container`；Apple = `Surface/On Surface` 黑 + `Inverse On Surface`**，均 280×40 `Radius/12`、`hasStart` 品牌图标（`SocialMediaIcon`）；两者之间不再出现紫色 Primary。

---

## 4. 设计 Token（Figma Variables）

Figma 本地变量按 **Collection** 组织；下列与稿内 **Variables** 面板一致（`fileKey`: `wHNBqjzSQZM8a4DlyBIDqW`）。

### 4.0 变量集合一览


| 集合            | 模式（Modes）                                     | 变量数     | 类型构成                                                            |
| ------------- | --------------------------------------------- | ------- | --------------------------------------------------------------- |
| **Color**     | Medeo light、Medeo dark、Mebox light、Mebox dark | **320** | COLOR **319** + STRING **1**                                    |
| **Typeface**  | Baseline、Wireframe                            | **5**   | STRING **5**                                                    |
| **Typescale** | Baseline、mobile                               | **88**  | FLOAT **51** + STRING **37**                                    |
| **Shape**     | Baseline                                      | **24**  | FLOAT **24**（`**Radius/*`** 圆角 + `**Space/s*`** 间距，见 §4.4–§4.5） |


- **Medeo 界面**以 **Medeo light / Medeo dark** 为准；Mebox 为另一套 Color 模式。

### 4.1 Surface（表面色）

Material 3 的 Surface 不是一条单一“越上越亮”的梯子，而是两套相关但用途不同的角色：

- **Surface Dim / Surface / Surface Bright**：页面与大分区的**底色明度范围**。Dim 更沉，Surface 默认，Bright 更亮；它们用于决定大面积底色的整体亮度。
- **Surface Container Lowest → Highest**：容器的**强调层级**。用于 Card、Sheet、Menu、Panel、输入区块等 contained area；`Surface Container` 是默认容器色，Lowest/Low/High/Highest 用于降低或提高容器强调。浮出菜单 / 下拉面板例外，用 `Surface Container Lowest`（见下表与 §8）。

不要把 `Surface Bright` 当作最高容器，也不要漏掉 `Surface Container Lowest`。两套体系可组合：页面底可用 `Surface Dim / Surface / Surface Bright`，其上的卡片/浮层再用 `Surface Container *`。

**Surface 明暗范围**

| Token | 典型用途 | Medeo light |
| --- | --- | --- |
| `Surface/Surface Dim` | 更沉的页面/分区底色，降低整体亮度 | `#e4e4e7` |
| `Surface/Surface` | 默认页面/分区底色 | `#f4f4f5` |
| `Surface/Surface Bright` | 更亮的页面/分区底色，适合需要更轻、更亮的大面积背景 | `#fafafa` |

**Surface Container 强调层级**

| Token | 典型用途 | Medeo light |
| --- | --- | --- |
| `Surface/Surface Container Lowest` | 最低强调容器、顶层白卡、模态底；浮出菜单 / 下拉面板（配 0.5px `Outline Variant` 描边与轻阴影，§8） | `#ffffff` |
| `Surface/Surface Container Low` | 低强调容器、轻分组 | `#fafafa` |
| `Surface/Surface Container` | 默认容器色，Card / Sheet / Panel 的常规选择（浮出菜单 / 下拉面板例外，用 Lowest） | `#f4f4f5` |
| `Surface/Surface Container High` | 更高强调容器，强调分组或嵌套层 | `#e4e4e7` |
| `Surface/Surface Container Highest` | 最高强调容器，最强的中性容器对比 | `#d4d4d8` |

**内容与分隔**

| Token                              | 典型用途         | Medeo light       |
| ---------------------------------- | ------------ | --------- |
| `Surface/On Surface`               | 主文本/图标（亮色表面）；控件选中态前景 | `#09090b` |
| `Surface/On Surface Variant`       | 次要文本、未选中 Tab；工具栏未选中控件的图标与文字（100%） | `#3f3f46` |
| `Surface/Outline`                  | 主边框、分隔；可拖拽分栏线（resizer）的 hover / 聚焦 / 拖动线（不用 `Schemes/Primary`） | `#d4d4d8` |
| `Surface/Outline Variant`          | 轻边框（如图标按钮容器）；浮出菜单面板与菜单内分隔线（0.5px） | `#e4e4e7` |
| `Surface/Inverse Surface`          | 深色填充按钮、反色条   | `#09090b` |
| `Surface/Inverse On Surface`       | 深色按钮上的文字/图标  | `#ffffff` |


### 4.2 Schemes（语义色，Material 角色契约）

`Schemes/*` 按 Material Design 的 **Role / On Role / Container / On Container** 成对使用。核心规则是：**底色 token 与文字/图标 token 不可跨角色混搭**。

| Token 类型 | 用法 | 禁止 |
| -------- | --- | --- |
| `Schemes/{Role}` | 高强调色面：Filled 按钮、强状态、关键焦点。 | 不把 `{Role}` 当文字色直接放在 `Surface` 上；不把多个 Role 同时当主层级。 |
| `Schemes/On {Role}` | 只用于对应 `{Role}` 底色上的文字 / 图标。 | 不放在 `Surface`、`{Role} Container` 或其他角色底色上。 |
| `Schemes/{Role} Container` | 低强调容器：Tonal 按钮、选中背景、信息性提示块、柔和强调面。 | 不作为主品牌 CTA 色；不与其他角色的 `On *` 搭配。 |
| `Schemes/On {Role} Container` | 只用于对应 `{Role} Container` 底色上的文字 / 图标。 | 不放在 `{Role}` 高强调底上，也不跨角色使用。 |

| 角色 | 高强调底 + 内容 | 低强调容器 + 内容 | One2X 使用方式 |
| --- | --- | --- | --- |
| Primary | `Primary` + `On Primary` | `Primary Container` + `On Primary Container` | 品牌紫。只给最高强调行动 / 品牌焦点，每屏通常 0–1 个。 |
| Secondary | `Secondary` + `On Secondary` | `Secondary Container` + `On Secondary Container` | 次级强调、信息性强调、选中态；不替代主 CTA。 |
| Tertiary | `Tertiary` + `On Tertiary` | `Tertiary Container` + `On Tertiary Container` | 第三强调、徽标、少量点缀；不抢主行动层级。 |
| Error | `Error` + `On Error` | `Error Container` + `On Error Container` | 错误、删除、校验失败、危险提示。 |

> 口语里的「Primalist 紫」一般对应变量 `**Schemes/Primary`**，不是 `Secondary Container` 的蓝。

主行动 **Filled** 按钮（**双主色**，见 §3.1）：**常规**用 `Surface/Inverse Surface`（黑）+ `Inverse On Surface`；**最高强调**那一个才用 `Schemes/Primary`（紫）+ `On Primary`。**勿**用 `Secondary` / `Secondary Container` 充当主品牌色。

### 4.3 State layers（状态蒙层）

交互态（hover / focus / pressed / dragged）**不是换一个颜色**，而是在底色上**叠一层半透明蒙层**。One2X 的默认做法是**全局统一叠 `Surface/On Surface`**，再用 **Blend Mode** 适配明暗，而**不是**为每个组件单独挑各自的 `On X` 色：


| 模式              | 蒙层色                  | Blend Mode（Figma）                  | 效果      |
| --------------- | -------------------- | ---------------------------------- | ------- |
| 浅色（Medeo light） | `Surface/On Surface` | **Plus Darker**（API `LINEAR_BURN`）  | 在底色上变暗 |
| 深色（Medeo dark）  | `Surface/On Surface` | **Plus Lighter**（API `LINEAR_DODGE`） | 在底色上变亮 |


- **透明度档**：hover **8%**、focus / pressed **12%**、dragged **16%**。
- **特殊表面例外**：反色条、Error 容器等少数表面，才按需改叠对应的 `Inverse On Surface` / `On Error Container` 等；其余一律 `On Surface` + Blend。**档位要在实际底色上看得出**：`Inverse Surface` 实底上叠默认 8% 几乎看不出（Medeo 顶栏登录钮 `#09090b` 只亮到约 `#1c1b1e`），应提高档位，并在浏览器里比对亮度（Medeo 参考：hover 16%、按下 24%，Agent 定值、设计未单独确认；24% 不在 8 / 12 / 16 档内）。
- **变量位置**：仍在 `State Layers/*` 集合（如 `State Layers/On Surface/Opacity-08`、`Opacity-12`、`State Layers/On Surface Variant/*`）。
- **Web 实现**：在底色上叠一层 `On Surface` 的半透明层，`mix-blend-mode: plus-darker`（浅）/ `plus-lighter`（深）；或用项目中等效的 `color-mix` / 专用 state token。
- **只留一层状态底色**：组件自带 state layer（如 `IconButton` 内层方角那层）又在外层叠了 hover 底时，只保留一层，圆角跟随按钮外形；两层叠加会比同排文字按钮更深，还会露出直角（Medeo 工具栏保留外层圆角层、关掉内层）。
- **展开不算状态**：点开菜单 / 弹层后，触发按钮回到 default，不保留 selected / pressed 底色，只有真实 hover 或按下才叠蒙层；展开用 `aria-expanded` 表达，`:focus-visible` 照常显示。例外：模式开关（如 Select 模式）与分段控件的当前项保留选中样式。
- **状态不改尺寸**：状态切换只改颜色与蒙层。只在选中态出现的边框，要在默认态预留同宽透明边框，或改用 `outline` / inset `box-shadow`，否则相邻元素会跳动（Medeo 顶栏 Tab 曾因 0.5px 选中边框在切换时跳动）。
- **生效中 ≠ 展开**：筛选条件、按类型分组这类「条件正在生效」的持续状态，触发按钮用 `State Layers/Primary` Opacity-08 底 + `Schemes/Primary` 图标（Medeo `var(--State-Layers-Primary-Opacity-08, …)` + `var(--Schemes-Primary, …)`），和「菜单展开回到 default」、工具栏「选中用 `On Surface`」区分开，用户一眼能看出列表正被过滤。它是低强调的状态指示，不算 §3.1 的紫色主按钮。同一处所有能「生效」的按钮（筛选、分组）用同一套，不只改被点名的那个（Medeo 编辑器素材面板已用；Createspace 工具栏的 Filter / Group 文字按钮仍是中性选中底，待同步）。
- **多选中的条目只靠勾选框表达**：选择模式下被选中的卡片 / 列表行不加紫色外框、不加底色，只让勾选框进入选中态；外框和底色留给 hover，否则满屏选中时整页都是紫框。勾选框规格见 §6。

### 4.4 圆角（Shape 集合）

`**Shape`** 集合中同时包含 `**Radius/*`**（本节）与 `**Space/s***`（§4.5）。**命名规则与间距不同**：圆角 **名中数字 = 半径 px**；间距 **名中 `s0`…`s10` = 阶梯档，≠ px**（见 §4.5 表）。

Figma（`**Shape`** · **Baseline**）圆角变量分组名为 `**Radius/*`**；Web 侧以 `**--shape-radius-*`** 对齐。Figma 变量作用域分类仍为 Corner radius（面板/作用域名，与分组前缀 `Radius` 不同）。名称**不**与组件高度（H24、H40 等）绑定，避免同心嵌套时产生误导。


| Figma 变量      | CSS 变量                | 半径                               |
| ------------- | --------------------- | -------------------------------- |
| `Radius/0`    | `--shape-radius-0`    | 0                                |
| `Radius/4`    | `--shape-radius-4`    | 4px                              |
| `Radius/6`    | `--shape-radius-6`    | 6px（保留原档，非 4 步进）                 |
| `Radius/8`    | `--shape-radius-8`    | 8px                              |
| `Radius/12`   | `--shape-radius-12`   | 12px                             |
| `Radius/16`   | `--shape-radius-16`   | 16px                             |
| `Radius/20`   | `--shape-radius-20`   | 20px                             |
| `Radius/24`   | `--shape-radius-24`   | 24px                             |
| `Radius/28`   | `--shape-radius-28`   | 28px                             |
| `Radius/32`   | `--shape-radius-32`   | 32px                             |
| `Radius/36`   | `--shape-radius-36`   | 36px                             |
| `Radius/40`   | `--shape-radius-40`   | 40px                             |
| `Radius/Full` | `--shape-radius-full` | 全圆角（胶囊；`tokens.css` 中为 `1000px`） |


**同心嵌套**：内层圆角 = 外层圆角 − 两者间距（padding / inset），间距大于外层圆角时内层归零，多层逐层计算。外层以用户看到的轮廓为准，hover 时贴边的描边也算（Medeo Createspace：网格卡片与列表行的 hover 外框 6px → 卡片角标、列表缩略图、列表 ⋯ inset 2px 为 4px，网格勾选框 inset 3px 为 3px，列表勾选框 inset 4px 为 2px；弹出菜单面板 6px → 菜单项 4px；编辑器时间轴 clip 6px，内部元素按同心算）。**控件严格同心，内容主体可由设计指定**：角标、勾选框、缩略图、菜单项这类控件按公式算；封面 / 图片属于内容主体，设计可以指定比同心值更大的圆角（Createspace 卡片 6、内边距 4，同心算出 2，设计定封面 4px），照设计值做并在代码注释里写明是有意不同心。改外框圆角时，把所有贴着它的内层一起复算。圆角要落在可见像素上：方框里的非方形图片不要撑满再 `object-fit: contain`，否则圆角只落在透明盒子上。Medeo 代码里 `--Radius-N` 的计算值不等于名中数字，见 §4.6；执行细则见 `**o2x-design-system**`「圆角同心关系」。

**历史**：此前稿内曾用 `**Corner/*`** 前缀（与上表同一套 px / Full）；已统一为 `**Radius/*`**。旧高度档名对照仍见 `**tokens.css**` 里 `**--shape-corner-***` 别名。另见旧稿中的 `dimensions/radius/rounded-sm` 等，以节点绑定为准。

### 4.5 间距（`Shape` 集合内的 `Space/s*`）

与 **§4.4 圆角**刻意区分：**圆角**用 `**Radius/{px}`**，名字里的数字 就是 像素；间距用 阶梯代号 `**s0`…`s10`**，名字 **不是** 像素，避免把档名误认为 px（例如旧 `**spacing/4` = 16px**，与「4px」无关）。

变量与圆角同在 `**Shape`** 集合（**Baseline**），面板中 `**Space/`** 分组；网页侧对应 token 为 `**--space-s0`** … `**--space-s10`**。


| Figma（阶梯）   | 实际值  | 网页侧 CSS           |
| ----------- | ---- | ----------------- |
| `Space/s0`  | 0    | `**--space-s0**`  |
| `Space/s1`  | 4px  | `**--space-s1**`  |
| `Space/s2`  | 8px  | `**--space-s2**`  |
| `Space/s3`  | 12px | `**--space-s3**`  |
| `Space/s4`  | 16px | `**--space-s4**`  |
| `Space/s5`  | 20px | `**--space-s5**`  |
| `Space/s6`  | 24px | `**--space-s6**`  |
| `Space/s7`  | 32px | `**--space-s7**`  |
| `Space/s8`  | 40px | `**--space-s8**`  |
| `Space/s9`  | 48px | `**--space-s9**`  |
| `Space/s10` | 64px | `**--space-s10**` |


**间距与圆角尽可能用变量（强制）**：`gap` / `padding` / `margin` / `inset` 以及角标这类位置偏移，值落在 `Space/s*` 档上就一律用 `**var(--space-s*)**`（Medeo 代码 `var(--Space-S-n, Npx)`，带 px 兜底），不裸写 `16px`；负值写 `calc(-1 * var(--Space-S-1, 4px))`，`calc()` 里的档位值也换成变量（如 `calc(100% + var(--Space-S-1, 4px))`）。圆角同理（设计指定确切渲染 px、`--Radius-N` 补偿后会偏离时写字面值，见 §4.4 / §4.6）。**只有**不在档位上、也没有推导关系的 1–3px 光学微调（如工具栏控件 gap 2px、角标 inset 2px、表头与置顶灰底 1px）才写字面值，并就近注释来源；不要为凑变量写 `calc(var(--Space-S-1) / 2)` 这类表达式。**量法**：间距与对齐都按**可视边缘**量，不按热区或盒子（热区 24、可视 20 时，「距 4px」要扣掉 2px 内缩）；`margin` 与父容器 `gap` 会叠加，改完量实际值。

### 4.5.1 圆角容器标题的视觉补偿

标题、label、hint、辅助说明如果位于圆角卡片、输入框、媒体框、Toolbar、Dialog surface 的上方或下方，并且表达上属于这个容器，不要只做几何左对齐。文字应按圆角稍微向内缩进，让标题和圆角形体的视觉重心对齐。

- **默认规则**：向内缩进约 `radius * 0.5`，再吸附到最近的 `Space/s*`；常见上限为 `12px`，避免标题看起来脱离卡片。
- **小圆角**：`Radius/0`、`Radius/4`、`Radius/6` 通常不需要补偿，或最多用 `Space/s1`。
- **中等圆角**：`Radius/8`、`Radius/12` 通常用 `Space/s1`；`Radius/16` 通常用 `Space/s2`。
- **大圆角**：`Radius/20`、`Radius/24` 通常用 `Space/s2` 到 `Space/s3`。
- **Full radius**：不要按 `1000px` 计算；按实际高度估算，取 `min(height * 0.1, 12px)` 后吸附到 `Space/s*`。

不需要补偿的情况：标题属于页面整体网格，而不是某个圆角容器；卡片内部已有明确文字锚点；多个不同圆角容器共用一个大分组标题；或 Figma 主组件已明确采用几何对齐。工作台列表页的统一左起点线属于第一种（§7.2）。

### 4.6 网页侧变量（与 Figma 对齐）

- **颜色**：Figma `**Color`** 共 **320** 项；网页 `**--color-*`**；**浅色 `:root`**，**深色** `prefers-color-scheme: dark` 或 `data-theme`。
- **颜色一律用随明暗主题切换的 token（强制）**：文字、图标、填充、描边、hover / 按下蒙层、阴影颜色、渐变色、TS 里的颜色常量，除非有明确声明，都用会在深色模式重新取值的语义 token（`Surface/*`、`Schemes/*`、`State Layers/*`；Medeo 代码 `var(--Surface-On-Surface-Variant, #3f3f46)`、`var(--State-Layers-On-Surface-Opacity-08, rgba(9, 9, 11, 0.08))`），不写裸 hex / `rgba()` / `white`。`var()` 里的 fallback 值不算违规。先确认 token 在深色主题下确实重新定义过（不随主题切换的色板变量不算）。
  - **半透明蒙层按所在底色选角色**：普通表面叠 `On Surface` / `On Surface Variant` 的 Opacity 档；`Inverse Surface` 实底按钮叠 `Inverse On Surface` 的档（深色主题下 Inverse Surface 是浅紫，写死白色蒙层会看不见）。
  - **阴影**：颜色用 `State Layers/Shadow` 的 Opacity 档（如 `0 4px 16px var(--State-Layers-Shadow-Opacity-12, …)`），只保留几何值字面。
  - **SVG 填色**：presentation attribute 里不能写 `var()`，用 `currentColor`，由元素的 CSS `color` 取 token。
  - **明确声明的例外**：压在图片 / 视频上、两种主题都要一样的遮罩与白字、视频黑边、品牌渐变，保留字面值并在同一行注释声明原因（medeo-fe 用 `theme-chrome: allow — 原因`）；`mask-image` 的渐变色只起透明度作用，不算颜色。
- **圆角**：Figma `**Shape`** · `**Radius/*`**；网页 `**--shape-radius-***`。`tokens.css` 中 `**--shape-corner-***` 仅为与旧高度档/旧 `**Corner/***` 名对照的别名，新稿以 `**Radius/{px}**` 与 `**--shape-radius-{px}**` 为准（§4.4）。
- **字阶 / 字族**：`**--font-family-*`**、`**--type-*`**，或组合类 `**.o2x-type-***`（见 `tokens.css`）。
- **间距**：Figma `**Shape`** · `**Space/s*`**；网页 `**--space-s***`（§4.5）；**勿**与 `**Radius/{px}`** 的「名=像素」规则混用。
- **Medeo 代码（medeo-fe）**：变量来自 `apps/medeo-web/src/web/components/theme/variables.readonly.css`（Web），命名为 `--Surface-*`、`--Schemes-*`、`--State-Layers-*`、`--Radius-N`，与本仓库 `tokens.css` 的 `--color-*` / `--shape-radius-*` 对应同一批 Figma 变量（如 `Surface/Outline` → `--Surface-Outline`），但不同名。在支持 `corner-shape` 的浏览器里，`--Radius-N` 按 superellipse 补偿放大约 1.27 倍（`--Radius-4` → 5px、`--Radius-6` → 8px、`--Radius-8` → 10px；附录 C.7），**名中数字 ≠ 计算值**。圆角**尽可能用变量**：值落在 `Radius/*` 档上一律写 `var(--Radius-N, Npx)`（胶囊 `var(--Radius-Full, 1000px)`），同心的内层写 `calc(var(--Radius-8, 8px) - 2px)`，与外层引用同一个变量。**例外是设计师指定了确切的渲染 px**，而 `--Radius-N` 的补偿（4→5、6→8、8→10）会渲染成别的值：这时写字面 px 并就近注释原因（Medeo：工具栏 4px；弹出菜单面板、网格卡片与列表行的 hover 外框 6px，也没有哪个 `--Radius-N` 算出 6px），贴着它的同心内层也写字面值（分段选中块 3px；菜单项与角标 4px，勾选框网格 3px、列表 2px），不拿字面 px 去减变量。间距变量 `--Space-S-0`…`--Space-S-10`（0、4、8、12、16、20、24、32、40、48、64px）是固定值，不放大。核对时读浏览器计算值。

全文变量表见 `**tokens/tokens.css`**、`**tokens/README.md**`。

---

## 5. 字体排印（Typography）

### 5.1 Typeface 集合（Figma Variables）


| Token             | 值（Baseline，STRING） |
| ----------------- | ------------------ |
| `Brand`           | Nohemi             |
| `Plain`           | Manrope            |
| `Weight/Medium`   | Medium             |
| `Weight/Semibold` | SemiBold           |
| `Weight/Bold`     | Bold               |


另有 **Wireframe** 模式；以稿内为准。

### 5.2 字阶样式（节选）

**Plain**：**Manrope**。**Brand**：**Nohemi**。


| 样式名                          | 字重           | 字号   | 行高   | 字间距（约） |
| ---------------------------- | ------------ | ---- | ---- | ------ |
| **label/medium**             | Medium 500   | 12px | 17px | 0.2px  |
| **label/medium - prominent** | SemiBold 600 | 12px | 17px | 0.2px  |
| **label/large**              | Medium 500   | 14px | 20px | 0.1px  |
| **label/large - prominent**  | SemiBold 600 | 14px | 20px | 0.1px  |
| **title/medium**             | SemiBold 600 | 16px | 24px | 0.15px |
| **body-medium**（导出中使用的变量名）   | SemiBold 600 | 14px | 20px | 0.1px  |


**展示/营销标题**：部分模块使用 **Nohemi**（如 `headline-small`）。**Typescale** 共 **88** 个变量（Baseline / mobile）；上表为常用节选。

### 5.3 字阶语义与场景映射（Medeo）

以下映射用于统一设计与实现选型。优先按语义选字阶，不按“视觉看起来接近”临时改字号。


| 层级           | 当前档位（主库）                                                       | 推荐场景                                  | 不建议                |
| ------------ | -------------------------------------------------------------- | ------------------------------------- | ------------------ |
| `display/*`  | `display/large`、`display/medium`、`display/small`               | 营销页 Hero 主标题、活动 KV、品牌叙事入口             | 常规业务弹窗标题、表单标题、正文段落 |
| `headline/*` | `headline/large`、`headline/medium`、`headline/small`            | 页面主标题、章节开场标题、内容区一级分组标题                | 按钮文案、长段正文          |
| `title/*`    | `title/large`、`title/medium`、`title/small`                     | Dialog/Drawer 标题、Card/Panel 标题、列表分组标题 | Hero 大标题、超小注释文本    |
| `body/*`     | `body/large`、`body/medium`、`body/small`、`body/extra small`     | 正文、说明、帮助文案、元信息/时间戳（extra small）       | 主 CTA 文案、主导航标签     |
| `label/*`    | `label/Extra Large`、`label/large`、`label/medium`、`label/small` | Button、Tab、Chip、Field label、紧凑工具条文案   | 段落正文、营销大标题         |


`prominent` 仅用于同层强调，不替代层级：

- `label/large - prominent`：主行动（Primary CTA）。
- `label/medium - prominent`：紧凑空间中的关键操作。
- `label/Extra Large prominent`：超大按钮场景下的最高强调。

### 5.4 Medeo 常见页面举例（可直接套用）


| 场景                                       | 推荐字阶                                             | 备注                     |
| ---------------------------------------- | ------------------------------------------------ | ---------------------- |
| 营销落地页 Hero 主标题                           | `display/large`（或 `display/medium`）              | 品牌叙事优先                 |
| 活动页区块开场标题                                | `headline/large`                                 | 比 `display` 收敛，仍保持强层级  |
| 工作台页面主标题（Projects / Templates）           | `headline/medium`                                | 信息结构一级标题               |
| Dialog 标题（Share / Export / Notification） | `title/medium`                                   | 通用弹窗默认档                |
| Card/Panel 标题（Library 等）                 | `title/small` 或 `title/medium`                   | 按信息密度选择                |
| 表格正文 / 列表项主文案                            | `body/medium`                                    | 默认阅读层                  |
| 辅助说明 / 时间戳 / 元信息                         | `body/small` 或 `body/extra small`                | 低层级信息                  |
| 主按钮文案（主 CTA）                            | `label/large - prominent`                        | 默认配 `Inverse Surface`；最高强调才配 `Schemes/Primary` |
| 次要按钮 / Tab / 输入标签                        | `label/large`                                    | 默认交互文案                 |
| 紧凑工具条按钮 / 小 Chip                         | `label/medium`（关键操作用 `label/medium - prominent`） | 密集区域的平衡选择              |
| **Compact · 弹出菜单项**（下拉 / 更多 / 右键，含 Default 页面里的菜单） | `label/medium`（12） | 项高 24、图标 14；全页同一档（§7.6） |
| **Compact 面板 · 列表行主文案**（文件夹名、文件名、账号名） | `label/medium`（12，Medium） | 不用 prominent，不升到 14 |
| **Compact 面板 · 行内元信息**（「306 files · 38.2 GB · Up to date」、速率、百分比、邮箱） | `label/small`（11）@ `On Surface Variant` **60%**（邮箱等三级信息 40%） | 用不透明度做层级 |
| **Compact 面板 · 分组标题**（「Sync folders · 3」「Transfer activity · Uploading · 3」「Recent · 20」） | `label/medium` @ `On Surface Variant` **40%** | 与行主文案同字号，靠 40% 退后 |
| **Compact 面板 · 状态条文案**（「Syncing: 3 to upload」「1 errors」） | `label/medium`（错误态填色 `Schemes/Error`，条底 `Schemes/Error Container`） | 速率用 `label/small` @60% 跟在后面 |
| **Compact 面板 · 空态提示**（「Folder not synced yet」） | `label/large` @ `On Surface Variant` 60% | 配 48px 灰文件夹图形 40% + 通栏黑钮 |
| 登录视图 / 系统确认框标题 | `title/medium` 居中 | 正文 `body/small` @ `On Surface Variant` 居中 |
| 紧凑黑钮 / 行内 Outlined 钮文案 | `label/medium` | 24 高按钮唯一档 |


执行约束：

1. 同一页面内，同一语义角色固定同一档位，避免局部“看着调”。某类元素的字阶一旦定下（如弹出菜单项改为 `label/medium`），**同步到同页所有同类元素**（排序 / 筛选下拉、卡片更多、右键、Tab 菜单），不等逐个指出。
2. `prominent` 仅给关键操作，避免全局滥用导致主次失效。
3. 组件内部文字优先沿用库内样式，不在实例里逐个手改。

**网页实现（必读）**：新建页面时 `**font-family`** 须为 `**var(--font-family-plain)`** 或 `**var(--font-family-brand)**`；**字号 / 行高 / 字间距 / 字重** 须来自 `**tokens.css`** 里对应 `**--type-*`**（或直接使用 `**.o2x-type-***` 组合类），**禁止**随意写 `font-size: 14px` 等魔法数字。页面需 **加载 Manrope、Nohemi**（如 Google Fonts），否则变量仍会回退到系统字体。

---

## 6. 核心组件

实现 UI 时应优先复用或对照 Figma 中同名组件变体。代码侧先查 `@one2x/o2x-design`（medeo-fe `packages/o2x-design`）里现成的组件与变体（如 `Tooltip`、`Button` / `IconButton` 的 `kind` 与 `size`），不自写同类组件；**不要把一个变体改造成另一个变体的样子**（如 `kind="text"` 涂黑当 filled，状态层会失效）。库变体缺所需密度时，只在所在容器范围内覆盖并注明，是否回收到库另议。列表 / 卡片里批量重复的元素因性能改用共享 CSS 的原生元素时，外观与状态层照搬对应库变体（Medeo 卡片 ⋯ 复刻 `text` 方案）。变体的默认尺寸与颜色可能压过页面样式，交付前读浏览器计算值（执行要点见 `**o2x-design-system**` Agent workflow 5.2）。

- **操作**：`Button`、`IconButton`、`IconButtonToggleable`、`InlineButton`、`ButtonBar`、`ButtonInCard`、`Clip button`、`generateButton` 等。
- **选择**：`Radio buttons`、`FilterChip`。
- **菜单**：`Menu`、`inlineButtonDropDownMenu`、`MoreDropDownMenu` 及各类业务 `*DropDownMenu`（密度多为 **0 Density**）。弹出菜单属 Compact 档（§2.1）：同页所有下拉 / 更多 / 右键菜单**共用一套紧凑规格和一组面板 token**，只保留一层可见面板（§8）；菜单与触发按钮的间距按按钮**可视边缘**量、同页一致（Createspace 为下方 4px）；切换型菜单项用成对图标（§6.1）。工作台页数值见 §7.6。
  - **水平对齐**：菜单首列以图标开头时，首图标与触发按钮的图标中心同轴；首列只有文字（图标只在文字后面，如选中对勾）时，首段文字左缘对齐触发按钮图标的左缘。空间不够才被推回视口，且距视口左右至少 4px。
  - **打开期间位置固定**：菜单里的控件（如缩放滑杆）改变了面板宽度、带动触发按钮移动时，菜单不跟着走；关闭后下次打开再重新对齐。
  - **菜单内分组标题**：12px、与菜单项同字重、`On Surface Variant` @40%。视图选项这类控件直接放进菜单、排成一行，不在面板里另展开一行占位。
- **列表**：`List item/List Item: 0 Density`。
- **表单**：`Field`、`TextFieldsIcon`、`buildingBlocks/promptDialog`。单行输入的文字垂直居中靠 `line-height` 等于输入区内容高度，不靠 padding 凑（Medeo 命令框紧凑态：14px `Body-Medium` 字号、28px 行高）；字号换档时行高仍跟输入区高度走。
- **勾选框（Checkbox）**：同页所有勾选框（网格卡片、列表行、工具栏全选）一套样式。未选：`State Layers/Background` Opacity-90 填充 + 0.5px `State Layers/On Surface` Opacity-16 描边，描边用 `outline` + `outline-offset: -0.5px`，不用 `border`（不改变尺寸，也不会被内部裁切吃掉）；选中 / 部分选中：`Schemes/Primary` 填充 + `On Primary` 对勾 / 横杠。列表行与工具栏 16px（对勾 12px），网格卡片 18px（对勾 14px）；圆角按所在外框同心算（§4.4）。网格放卡片左上角、距 hover 外框 2px；列表行里垂直居中，左侧与上下的可视间距一致（选择模式下行左内边距相应加大）。
- **标签溢出**：表示「还有更多」的省略点（`··`）按一个字符占位，和文字同一行、同一对齐方式参与排版，不额外把文字往一侧挤（否则整组看起来没居中）。
- **进度 / 容量条**：值大于 0 时至少显示 5% 的填充，避免看起来是空的。
- **结构与导航**：`BuildingBlocks/TopActions`、`BuidldingBlocks/ScrollButton` 等。
- **提示**：`Tooltip`（`@one2x/o2x-design` Overlays/Floatings）。**纯图标按钮必配**；带可见文字的按钮不加，按钮自己的菜单展开时不显示。沿用组件默认行为（上方出现、偏移 4px、冷 / 暖延迟 500 / 100ms），不自写提示层。列表 / 卡片里批量出现的行内按钮不逐个挂实例（Medeo 曾因此卡死页面），改用共享的单个提示层（Medeo 卡片 ⋯ 目前未配提示）。

**组件描述要点（节选）**：

- **Button**：用于 Dialog、Modal、Form、Card、Toolbar 等处的可点击操作；详见 M3 Buttons。**主行动按钮遵守双主色**（§3.1）：常规主按钮用 **Filled + `Surface/Inverse Surface` + `Inverse On Surface`**；只有最高强调的那一个才用 **Filled + `Schemes/Primary` + `On Primary`**，每屏 0–1 个。Tonal / Container 按钮遵守 §4.2 的 Material 配对规则。同一排并列的按钮高度、圆角一致，不叠 inner shadow（Medeo 编辑器顶栏 Share / Export：24 高、4px 圆角）。
- **IconButton**：紧凑操作；可成组或单独使用。自带 state layer，外层另有 hover 底时只留一层；点开菜单后回到 default 态（§4.3）。`size="small"` 会把图标压到 14px；组件默认前景是 `On Surface`，不继承父级颜色；和同排按钮不一致时在所在容器范围内覆盖，并读计算值核对。
- **Outlined IconButton**：中等强调，常与 Filled 搭配表示替代操作。
- **Button / IconButton `kind` 按底色明暗选**：实底按钮（含黑色 `Inverse Surface` 主按钮）用 `kind="filled"`（§3.1）；浮在封面或图片上的轻按钮用 `kind="text"` 的浅色方案，再垫一层浅底（Medeo 卡片 ⋯：`Surface/Background` 约 90%、图标 `On Surface Variant`、hover 8% / 按下 12%），不自创深色毛玻璃底或渐变 scrim。

### 6.1 图标库（Icons · `@one2x/o2x-icons`，核心规则）

**所有图标必须调用 One2X 自有图标库 `@one2x/o2x-icons`**（medeo-fe `packages/o2x-icons`，字体图标；清单与数量以 `src/fonts/info.json` 为准）。**不要**临时画 SVG、不要从第三方库（Material Symbols / Lucide / Iconfont / Font Awesome 等）引入、不要用 emoji 占位。

- **代码用法（二选一）**：
  - **组件**：`import { AddIcon } from '@one2x/o2x-icons'` → `<AddIcon />`（命名 = `componentName`，PascalName + `Icon` 后缀）。
  - **字体 className**：引入字体后用 `o2x-icons-<ComponentName>`，或字族 `font-family: 'o2x-icons'` + 对应字符（PUA 码位见 `info.json` 的 `encodedCode` / `unicode`）。
- **找图标**：图标清单与映射在 `packages/o2x-icons/src/fonts/info.json`（`componentName` / `snakeName` / `className` / `encodedCode`），或在可视化预览「图标」区搜索后点选复制组件名。
- **先查再画**：只要库里已有对应语义图标，就必须复用库图标；例如主题切换使用 `LightModeIcon` / `DarkModeIcon`。不要用 CSS 手画太阳、月亮、箭头等已有图标。设计指定了具体图标名时按名字使用，**语义接近不算已有**：要 `TableEyeIcon` 时不能用 `VisibilityIcon` 顶替，库里没有就先同步（见「缺图标」）。切换型状态用成对图标（`PinIcon` / `PinOffIcon`）。
- **尺寸**：常用 **18 / 20 / 24px**（随同级文字字号）；Compact 区另有 **14**（菜单项、面板行尾图标）与 **16**（卡片角标、状态图标），24 高工具栏按钮里用 **18**。同一条工具栏里纯图标按钮与带文字按钮的图标**视觉尺寸一致**；组件变体可能改写图标尺寸（§6 IconButton），交付前读计算值。点击区域参照 §9 与组件规范（如 Share 网格 64×64）；热区可以大于可视底（如卡片角标可视 20、热区 24），间距按可视边缘量（§4.5）。
- **颜色**：用 `currentColor` 继承所在文本的 `On *` 颜色，**不要**给图标硬编码 hex。工具栏里未选中控件的前景统一 `Surface/On Surface Variant`，`On Surface` 只给选中态；组件默认前景（如 `IconButton` 的 `On Surface`）会压过继承色，要读计算值核对。
- **缺图标**：先查 One2X Figma 图标页（node `60839:470`），常见情况是 Figma 已有、仓库还没同步（如 `PinIcon` / `PinOffIcon` / `TableEyeIcon`）。标准流程是 `packages/o2x-icons` 的 `pnpm sync`（`pull` + `gen` + `build`，`pull` 即 `sync-figma-icons`，需要本机 `FIGMA_TOKEN`）；没有 token 时按该包 README 里「手动补普通图标时…」那段：用 Figma MCP 取矢量写成 `svgs/<Name>.svg`，再 `pnpm gen && pnpm build`。Figma 里也没有的图标，由设计补充后再用。**不要**在业务代码里散放一次性 SVG。

---

## 7. 布局原则

### 7.1 间距与节奏

- **基础阶梯**：`Space/s0`…`s10` 对应 0 → 64px 的离散档（见 §4.5）；**优先 4 的倍数**与 `**var(--space-s*)`**，与 Auto layout `gap` / `padding` 一致。
- **主信息区**：业务页常用 `**s4`–`s6`** 作为卡片内边距与区块间距起点；大留白用 `**s7`+**。
- **Compact 面板**（§2.1）：容器**零内边距**，所有内容行自己带 `[顶 2, 右 8, 底 2, 左 8]`；行间 gap 2–4（4 = `s1`；2 属 Compact 光学微调，见 §4.5）；头部 `[8]`；状态条 `[6, 8]`；分组标题行 `[0, 4, 0, 8]`。**不要**把业务页的 `s4`（16）搬进 340 宽的面板——它会吃掉 10% 宽度并把行撑到 52+。

### 7.2 栅格与容器

- 具体最大宽度以稿为准；复杂工作台以 **侧栏 + 主内容** 与 Figma **Medeo** 各页为准。
- **分段与分区**：用 **Surface** 层级与 **Outline** 分隔，而非额外装饰线（除非组件规范要求）。
- **单一左起点线**：页面网格里的分区标题、子分区标题、列表表头、网格封面、列表缩略图，按**肉眼可见的内容左缘**（不是卡片外框、热区或容器）落在同一个 `x`，所有分区、所有视图（网格 / 列表）都要成立；顶栏首个 Tab 的 logo 也对齐这条线。嵌套 padding 会层层累加，要逐项实测。整体平移时改共享滚动容器的 padding，让所有起点一起动。这类标题属于页面网格，不做 §4.5.1 的圆角补偿。页面实例见 §7.6。
- **靠边但不贴边**：密集页面可以把工具栏、辅助灰底、角标推近视口或容器边缘，但要留一段小而固定的可见间距，也不能产生横向滚动。多条工具栏、灰底里的同类控件，右缘上下对齐。

### 7.3 留白与层级

- **中性表面为主**：大面积 `**Surface/Surface`** / `**Surface Container Lowest`** 形成底色，再用字阶与双主色建立层级：默认主行动用黑色 `Inverse Surface`，最高强调才用 `Primary`（见 §1、§3.1）。
- **避免**：无 token 依据的随意 `margin`、与字阶不一致的临时 `font-size`。

### 7.4 辅助信息块与操作布局

Prompt、Hint、Note、Code snippet 等辅助信息块如果同时包含**标签、正文与操作按钮**，不要默认做「标签 / 正文 / 操作」三栏横排。窄卡片里三栏会让标签占掉过多宽度，使正文被挤成过窄的多行。

- **默认结构**：第一行放短标签（如 `PROMPT`）与右上角操作（如复制）；第二行让正文独占整行。
- **正文优先**：正文列 `min-width: 0`，允许自然换行；长代码或命令才使用水平滚动。
- **标签克制**：标签只承担分类，不参与正文列宽分配；不要给标签固定大列宽。
- **操作位置**：复制、展开、更多等轻操作放在角落；不要把它夹在正文中间。若操作位于正文行右侧，正文需要给按钮预留宽度。
- **角落操作的视觉平衡**：角落按钮到相邻两条容器边的距离应相同；例如右下角按钮的右边距与下边距都用同一个 `--prompt-inset` 控制。按钮圆角按同心关系计算，`action radius = outer radius - inset`，不要让角落按钮贴边或使用无关圆角。「不贴边」指两条边留出相等、可见的间距，不要求大留白（密集网格卡片的 hover 角标可收到 2px）；`outer radius` 取用户看到的外轮廓（含 hover 时贴边的描边），不取内部封面或盒子。

### 7.5 紧凑面板配方（托盘 / 菜单栏 / 浮出面板 · 定稿模板）

**参考帧（唯一事实来源）**：文件 `vEJRRdbQhziklOs3apEfxi`（🌐 Medeo · Web · Responsive）页「✨ 88 · Brewing」→ section「桌面端 Beta · 同步文件夹托盘面板」→ 帧 `01 · 主视图 · mac · 浅色`（node **`6974:114850`**）；登录 `6128:90672`、空态 `7070:221796`、错误 `7070:222395`、确认框 `6128:91315`。生成任何 Compact 面板前，Agent 先 `get_design_context` / `get_metadata` 读这几帧，再按下面骨架搭。

```
Panel 340×480  VERTICAL pad 0 gap 0  fill Surface Container Lowest  stroke Outline Variant 0.5 INSIDE  Radius/12  smooth .6  clip
├ header            H 49  HORIZONTAL pad[8] gap s2 alignCENTER
│  ├ avatar 32×32 Radius/8（图片）
│  ├ identity  VERTICAL FILL：name label/medium OnSurface · email label/small OnSurfaceVariant @40%
│  └ IconButton 20（MoreHoriz，stroke Outline Variant 0.5，Radius/6）        ← 头部只留 ⋯；全局暂停放到状态条右侧
├ statusBand        H 32  HORIZONTAL pad[6,8] gap 4 alignCENTER  fill Surface/Surface
│  ├ 状态图标 16（ClockLoader20Icon / CheckCircleIcon / ErrorFillIcon，同文本色 @60%）
│  ├ statusText label/medium OnSurfaceVariant（错误态：fill Schemes/Error Container，文字 Schemes/Error）
│  ├ speed ×2 label/small @60%（"↑ 2.1 MB/s" "↓ 0.4 MB/s"）
│  └ IconButton 20（Pause / Play）
├ group · folders   VERTICAL pad[4,0,0,0] gap 2
│  ├ captionRow H 24  pad[0,4,0,8]：label/medium @40% "Sync folders · 3" ＋ 右侧 紧凑黑钮 24（AddNewFileIcon 18 + "Add file"）
│  └ folderRow ×n  H 41（同步中 45）HORIZONTAL pad[2,8] gap s2 alignCENTER
│      ├ folderGlyph 24：矢量 20×18 fill Surface Container Highest + stroke State Layers/On Surface/Opacity-12 1px；右下角 10px 白圈内放实心状态图标
│      ├ content VERTICAL FILL：name label/medium · meta label/small @60%（错误：Schemes/Error 100%）· [Progress 292×8]
│      ├ endIcon 14（ArrowRight，hover 显示）
│      └ IconButton 20 ⋯（hover 显示）
│      └ 错误行下方：buttonsRow H 24 pad[0,8,0,40] gap s2 → Outlined 24 ×2（Retry / Re-select）
├ group · transfer  VERTICAL pad[0,0,4,0]
│  ├ captionRow "Transfer activity · Uploading · 3"
│  └ transferRow ×n H 33 pad[4,8] gap s2：iconWrap 24 圆 fill Surface/Surface 内 ArrowUp 16 @40% · content(title 行：name + 右侧 % label/small @60%；Progress 292×8) · endIcon 14 · IconButton 20
├ HorizontalDivider（kind=fullwidth，Outline Variant 0.5）
└ group · recent    captionRow "Recent · 20" ＋ 右侧 IconButton 20（ChevronRight）；展开后 doneRow H 24：CheckCircleIcon 14 @40% + name label/small + 时间 label/small @40% 右对齐
```

配套视图：

- **登录（G0）**：content pad[24] gap 16 居中：Logo 48（`MedeologoIcon`，`Schemes/Primary` 紫是**全稿唯一紫色**）→ `title/medium` "Log in to Medeo Drive" → Google（蓝）/ Apple（黑）280×40 → "or" 分隔（`HorizontalDivider` ×2 + `body/medium` @40%）→ 手机号 `Field` 280×40 + 禁用态确认钮（`State Layers/On Surface/Opacity-12`）；底部 footer pad[16,24] `body/small` @40% "Beta 0.1.0"。
- **空态（G1）**：头部 + 状态条不变；列表区居中 gap 8：48px 灰文件夹图形 @40% → `label/large` @60% "Folder not synced yet" → 通栏黑钮 240×40 `Radius/12`（AddNewFileIcon + "Add sync folder"）。
- **确认框**：360 宽，pad[12] gap 8，`Radius/16`，stroke `On Surface Variant` 0.5：Logo 40 → `title/medium` 居中 → `body/small` @OnSurfaceVariant 居中 → 双钮 44（§3.1）。
- **深色模式**：同一骨架，帧上切 Color mode `Medeo dark`；不透明度层级不变。
- **文案语言**：Medeo 产品稿 UI 文案默认**英文**（"Sync folders · 3"、"Up to date"、"Can't find this folder"），中文只出现在 section 标题、注释与示意卡片；PRD 中文原句先译成短英文再上稿。

### 7.6 密集工作区页面（工作台列表页 · Medeo Createspace 定稿）

适用于有分区标题、工具栏、网格 / 列表切换、置顶灰底面板、hover 操作、弹出菜单和骨架加载的工作台列表页（参考实现：medeo-fe `apps/medeo-web/src/web/views/createspace`）。页面不是单一档位：工具栏、弹出菜单、列表密集区、置顶面板和页面边距都按 **Compact** 收紧（§2.1）。通用规则的正文在别处，本节只写这类页面怎么用：起点线与靠边见 §7.2，状态层见 §4.3，同心圆角见 §4.4，间距量法与 1–3px 微调见 §4.5，菜单 / Tooltip / 按钮组件见 §6，浮层外观见 §8。执行清单见 `**o2x-design-system**`「密集工作区页面（执行要点）」。

#### 起点线与边缘

- **哪些元素在线上**：分区标题、子分区标题（Pinned）、列表表头（Name）、网格封面、列表缩略图与图标，在所有分区、网格 / 列表两种视图里落在同一 `x`。卡片自带内边距时，标题对齐封面左缘，不对齐卡片外框。
- **置顶列表与主列表共用列几何**：行范围、行内边距、缩略图位置和各列 `x` 一致，置顶区只是多一层灰底。
- **顶栏首个 Tab 的 logo 左缘也在这条线上**：调 Tab 左右内边距实现，保持左右平衡，不只加大一侧；内容起点变了要复量 logo。
- **整体平移**：文字、封面、缩略图、列表图标一起动，两种视图都复核；灰底距视口这类已约定的留白不能因平移丢掉。
- **列表 hover 外框距视口左右相等**：列表行的紫色 hover 外框到可视区域左、右边缘的距离一致；右边明显更宽时加大列表可用宽度，不缩左边。
- **网格卡片内容贴顶**：网格行比卡片内容高时，多出的空间留在文字下方；封面到卡片外框的上、左、右间距一致，不把卡片内容垂直居中。
- **面板内分组标题对齐面板标题**：如编辑器素材面板的「视觉 / BGM」分组标题，文字左缘对齐面板标题「素材」的文字左缘，网格和列表两种视图都要复量；展开箭头与分组文字同色（文字带不透明度时箭头也带）。

#### 工具栏

- **按作用对象分区**，从左到右：内容操作（Add、Select）→ 数据操作（Search、Filter、Group、Sort）→ 视图槽 → 视图切换。缩放、字段展示这类视图入口共用紧贴视图切换的同一个槽位，按当前视图只显示其中一个，图标不变（Medeo 用 `TuneIcon`），靠 Tooltip 文案区分。
- **从右锚定**：视图切换是最右侧的固定锚点。切换视图、换排序、展开搜索时，锚点及其右侧都不动；搜索展开时槽位真实变宽，把左侧操作往左推，不盖住或淡出其它按钮。
- **文字按钮 hug 文案**：hug 优先于零位移，左侧控件随文案平移几像素可以接受（附录 C.5.1）。
- **样式统一**：同一条工具栏只用一个 `gap`，分区之间不另加间距；文字按钮、图标按钮、下拉按钮、分段外框和展开后的搜索框用同一个圆角，分段选中块按同心计算；图标同尺寸，未选中前景 `On Surface Variant`、选中 `On Surface`（§6.1）。这些都是工具栏范围内的局部覆盖，不改 §3.1 紧凑黑钮，也不改共享组件在别处的样式。弹出菜单不跟随工具栏圆角，保留面板圆角。

#### Hover 才出现的操作

- **不常驻留白**：Tab、列表行、表头都不为只在 hover 时出现的 ⋯ 加宽或预留占位列，按钮用绝对定位叠在内容右端。末列本身有富余（如日期列）时可以直接叠放，但要确认更长的语言不会伸进按钮下方（附录 C.5.4）。
- **渐隐用 `mask-image` 作用在内容本身**，不盖带底色的遮罩；只在按钮可见（hover、键盘聚焦、菜单打开）时加。以按钮可视左缘为基准：文字在它外侧 3–6px 处已完全透明，渐隐带约 20–30px。
- **卡片角标 ⋯**：外观按 `kind="text"` 浅色方案加浅底（§6），不自创深色毛玻璃底或渐变 scrim；到卡片外轮廓（含 hover 描边）上、右两边等距，圆角与外轮廓同心（§7.4）。列表行里的 ⋯ 不套用这套外观：它在行内垂直居中，到行 hover 外框的上、下、右可视间距相等（Createspace 20px 按钮在 24 高行内，三边 2px），不要贴右上角定位。
- **保持 hover 才出现**：控制栏、置顶区视图切换、横向翻页箭头这类 hover 操作不要改成常驻。合并别人的改动或调样式后，确认它们默认仍隐藏，并让浏览器测试覆盖「默认隐藏、hover / 聚焦出现」。
- **菜单打开期间保持可见**：hover 按钮或整排 hover 工具栏，只要它的任一菜单开着就保持显示，鼠标移进菜单不算离开。新增菜单都要接入这个条件。

#### 弹出菜单与触发按钮

- **全页一套**：所有下拉 / 更多 / 右键 / Tab 菜单共用同一套紧凑规格与一组面板 token（数值见下表，面板规则见 §8）；菜单项圆角 = 面板圆角 − 容器 padding（§4.4），全页一致（Createspace 面板 6px、菜单项 4px，都是字面值，原因见 §4.6）。
- **位置**：出现在触发按钮下方，距按钮**可视边缘** 4px；热区 24、可视 20 时，距热区 2px。
- **图标轴线对齐**：由图标按钮（如 ⋯）打开、首列带图标的菜单，首列图标中心与按钮图标中心同轴。`bottom-start` 时 `crossAxis = 按钮宽 / 2 − 首图标中心距菜单左缘`；Medeo 首图标中心距菜单左缘 15.5px（边框 0.5 + 容器 padding 2 + 菜单项左 padding 6 + 图标半宽 7），20px 按钮得 −5.5。菜单被推回视口时可以放弃对齐。
- **触发按钮**：点开后回到 default，展开只用 `aria-expanded` 表达（§4.3）；纯图标按钮配库 `Tooltip`，菜单展开时不显示（§6）。

#### 置顶灰底面板

- **内边距按可见内容量**：辅助灰底面板比主区紧，按「可见内容边缘到灰底边缘」量，左边与下边一致；先把嵌套元素自带的 padding 算进去，再反推容器 padding；右侧控件按控件到灰底边缘另算。
- **完整包住内部控件**：灰底里的控件与外部同类控件右缘对齐，同时留可见内边距，不截断、不贴边；加宽后在画面上确认没有被祖先元素的 `overflow` 裁掉。同页多块灰底左缘对齐，距视口同一个小间距。
- **标题在文档流里独占一行**（24 高，同 §2.1 分组标题行），内容整体下移；没有置顶内容时不占这一行。不需要收起的子分区标题做成静态文本：不带 chevron、不可点击、默认光标。
- **窄面板**：设最小宽度，最窄也能完整放下头部必需控件（如视图切换）；放不下「标题 + 控件」并排时默认只显示标题，hover 或键盘聚焦面板（`:focus-within`）时标题原位淡出、控件淡入（Medeo 参考 100ms）；宽度够时并排，不做互换。

#### 横向滚动行

- **两端渐隐**：左右各一条约 64px 的渐隐遮罩，只在该方向还能滚动时淡入，滚到头就消失。
- **裁切点贴边**：内容的消失点左侧贴近相邻置顶面板的右缘（留约 4px），右侧贴视口右缘，不停在面板内边距处。做法是把滚动容器向外扩出面板内边距，再用 padding 把首张卡片推回起点线。
- **翻页箭头**：hover 或区域内聚焦才出现，贴近左右边缘。点击按约 80% 可视宽度（最少 120px）翻页，用约 240ms ease-out 的横向滚动动画，看得出在滚动但要快；滚轮、触摸打断动画；`prefers-reduced-motion` 下直接到位（动效细则见 web-animation-design）。

#### 选择模式

- **原位展开**：点「选择」后，Select 按钮在工具栏原位展开成工具组：全选 → 批量操作（删除；回收站里是恢复与永久删除）→ 分隔线 → 取消，不另起浮在内容上的底部操作条。展开时宽度从 0 撑开（`grid-template-columns: 0fr → 1fr`，约 200ms ease-out），把左侧按钮往前推，符合工具栏从右锚定。
- **功能区块**：工具组整体一块灰底（`Surface/Background`，内距 2px，圆角 6px，内部按钮 4px 同心），按钮沿用工具栏 24 高 ghost 样式。选择模式期间工具栏常显，不受 hover 显隐影响。
- **同一时间只激活一个区域**：同页多个分区（创作 / 素材）只有一个处于选择模式，进入一个就退出另一个并清空它的选中项。
- **不冲突就不收起别的浮层**：工具组在工具栏里，底部命令框等浮层照常显示。
- **全选按钮**：勾选框三态（空 / 横杠部分选中 / 对勾全选）。空或部分选中时点击 = 全选，已全选时点击 = 清空（清空另有「取消」、Esc、点空白，所以部分选中时不拿这个按钮清空，免得一点就丢掉已挑的项）。文案固定「全选（总数）」，有选中时后接「· 已选择 N 项」（灰，约 60%），不在两种文案之间切换；搜索中改为「全选搜索结果（N）」。计数用 Geist Mono 等宽、`ss09` 无斜杠 0（执行要点见 `o2x-design-system` Typography）。
- **全选是一种状态**：记「全选 + 排除项」而不是一份固定 id 列表，之后滚动加载的新条目自动选中，取消勾选的记入排除；点空白清空时一并退出全选状态。要把未加载的条目也一起删，需要后端按条件批量操作；没有时只作用于已加载条目，并在文案里写明。
- **Shift 连选**：点一项作锚点，Shift 点另一项把中间整段加入选中；Shift 点击时阻止拉出文字选区。
- **批量删除的确认框写明数量**（「确定要删除选中的 N 个素材吗？」），只选一个时沿用单项文案。
- 选中条目的表达与勾选框规格见 §4.3、§6。

#### 分组与空状态

- **按类型分组时，空分组整组不显示**：连分组标题一起隐藏，不放「暂无背景音乐」这类占位；所有分组都为空时显示整个面板的空状态。

#### 加载骨架

- **整页一套骨架**：每个异步区域（各分区列表、置顶区、计数、封面、翻页尾部）都有形状匹配的占位，共用一个样式：灰底加斜向扫光，同色同节奏，恒速 `linear` 循环（web-animation-design 的 constant motion）；颜色取主题 token，明暗主题都看得见；`prefers-reduced-motion` 下静止。数据到达后用项目统一的渐显组件替换，不与脉冲骨架混用。
- **加载中不显示默认封面**：默认封面只表示「已确认没有封面」。无缩略图卡片的封面分三段：扫光 → 读到真实页面比例后显示比例正确的默认封面 → 缩略图到达后淡入真实封面；比例读取失败时按 16:9 直接显示默认封面，不卡在骨架。

**Medeo Createspace 参考值**（1653px 宽视口实测；换页面时保留原则，数值重新校准；1–3px 属 Compact 光学微调，见 §4.5）

| 项 | 参考值 |
| --- | --- |
| 内容起点（标题、表头、封面、缩略图） | `x = 12px`（列表视图实测；网格视图未单独复量） |
| 顶栏首个 Tab 的 logo 左缘 | 应对齐内容起点；内容起点在 8px 时已对齐，移到 12px 后**未复量** |
| 置顶灰底 | 距视口左右 4px；列表视图可见内边距左 / 下 8px；灰底内视图切换距灰底右缘 2px，右缘与工具栏视图切换对齐 |
| 工具栏 | 按钮 24×24、图标 18px；`gap` 2px；圆角 4px（字面值：设计指定渲染 4px，`--Radius-4` 补偿后是 5px，§4.6；Createspace 工具栏与编辑器素材面板标题栏统一），分段选中块 3px（4 − 1 同心，字面值）；搜索槽收起 24px、展开 200px |
| 弹出菜单 | 容器 padding 2px、min-width 96px（随内容撑开）；项高 24、padding `0 8px 0 6px`、`label/medium`、图标 14、图文间距 4；面板 0.5px `Outline Variant` + `Surface Container Lowest` + `0 4px 16px` 阴影（颜色用 `State Layers/Shadow` Opacity 12 档；选哪一档几何待定，见 §8） + 圆角 6px（字面值，§4.6），菜单项 4px（6 − 2 同心）；距触发按钮可视边缘 4px、距视口左右至少 4px |
| 卡片角标 ⋯ | 可视 20×20、热区 24×24，图标 16px，距卡片外轮廓 2px，圆角 4px（卡片外框 6 − 2） |
| 网格卡片 / 列表行 hover 外框 | 圆角 6px（字面值，§4.6），1px `Schemes/Primary` outline、`outline-offset: -1px`；网格封面 4px（设计指定，非同心），列表缩略图 4px |
| 列表行 ⋯ | 20×20，在 24 高行内垂直居中，距外框上 / 下 / 右各 2px，圆角 4px |
| 勾选框 | 未选 `Background` 90% + 0.5px `On Surface` 16% outline；选中 `Primary` + 白勾。列表 / 全选 16px、圆角 2px（行 6 − 内缩 4）；网格 18px、圆角 3px，距卡片边 3px（外框内 2px） |
| 选择工具组 | 灰底 `Surface/Background`、内距 2px、圆角 6px；展开 200ms；计数 Geist Mono + `ss09` |
| 横向滚动行 | 渐隐 64px；翻页 80% 可视宽（最少 120px），240ms ease-out |
| 命令框（Createspace 收起态） | 首页原尺寸 640×66 → Createspace 约 2/3（427×44），发送钮 42 → 28，文字 14px `Body-Medium`、行高 28px；两个方向切换都有过渡；占位文案固定「Create anything...」 |
| 从属间距 | 设计师指定 **1px**：分区标题栏 → 置顶灰底、Pinned 标题行 → 内容、列表表头（Name）→ 置顶灰底。Createspace 现状：前两处误做成 4px（待改回 1px），表头 → 灰底已是 1px |
| 作品封面图 | 圆角 4px，落在图片本体上 |
| 骨架扫光 | 1.6s 一轮，`linear` |

---

## 8. 深度与层级

- **Elevation Light/1**：多层 drop shadow（约 `0 1px`、`0 2px`、`0 4px`、`0 6px` 等组合，黑色低不透明度）。卡片与浮层与之一致（参见 §9 Share 模式）。
- **模糊**：`blur` — 背景模糊（如 `backdrop-blur`），用于浮层标题栏等需与设计数值一致。

**原则**：浅色 Medeo 上以 **细边框 + 轻阴影** 表达浮起；具体数值以节点与 `tokens.css` 为准，避免自造多层阴影栈。

- **同页浮层共用一组外观 token**：同一页面的弹出菜单（下拉 / 更多 / 右键 / Tab 菜单）共用同一描边（0.5px `Outline Variant`）、底色（`Surface Container Lowest`）、阴影档和圆角 token（阴影用哪档待定：Createspace 现用单层 `0 4px 16px`，与上文 Elevation Light/1 及库 `Menu` 多层阴影不一致）；新增菜单对齐已有那一档，不各写一套（Medeo Createspace 以排序菜单为准，数值见 §7.6）。
- **只有一层可见面板**：描边、底色、阴影、padding 只加在直接包含菜单项的那一层；弹层的定位容器保持透明、无边框、无 padding，避免框套框。

---

## 9. 模式参考：Share / VideoShareDialog

从当前节点导出可归纳以下模式（实现其他产品界面时类比）：

1. **容器**：白底、细边框（约 0.5px）、大圆角（如 24px）、轻阴影（Elevation Light/1）。
2. **分段控件（Tabs）**：轨道背景 `Surface/Surface`，选中项 `Surface Container Lowest` + `On Surface`；未选中项降低对比度（`On Surface Variant`、opacity）。选中块圆角与轨道同心（轨道圆角 − 轨道内距，§4.4；Medeo 工具栏 4 − 1 = 3px）；选中态不改变盒子尺寸（§4.3）。
3. **图标网格**：统一 **64×64** 点击区域、**12px** 圆角容器、`Outline Variant` 描边；下方 **label/medium** 平台名。
4. **主按钮（Copy link）**：`Inverse Surface` 填充 + `Inverse On Surface` 文字与图标；**12px** 圆角、`label/large`；左侧可放 **18px** 图标。
5. **加载态**：`title/medium` 标题 + 中央 **Spinner**（24px 区域）。

---

## 10. 代码映射与工程接入

本节不再重复维护另一份映射表。**实现侧单一数据源**为 `**tokens/tokens.css`**；Figma 命名与取值以 §4.4 圆角、**§4.5 间距**、**§4.6 网页侧变量**为准。

- **当前有效命名**：Figma 圆角为 `**Radius/*`**，间距为 `**Space/s*`**；Web 分别对应 `**--shape-radius-***`、`**--space-s***`。
- **历史名仅作兼容说明**：`**Corner/*`**、`**spacing/*`**、`**--shape-corner-***` 均不作为新稿或新实现命名依据。
- **新页面 / C2P 落地**：引入 `tokens.css`；字族与字阶使用 `**--font-family-*`**、`**--type-*`** 或 `**.o2x-type-***`；`gap` / `padding` / `margin` 用 `**var(--space-s*)**`；圆角用 `**var(--shape-radius-*)**`；默认主行动按钮用 `**--color-surface-inverse-surface**` + `**--color-surface-inverse-on-surface**`（`Button kind="filled"`），只有最高强调那一个才用 `**--color-schemes-primary**` + `**--color-schemes-on-primary**`（§3.1）。
- **图标**：统一用 `@one2x/o2x-icons`（组件 `<XxxIcon />` 或字体 className `o2x-icons-<名>`，§6.1），颜色继承 `currentColor`；禁止临时 SVG / 第三方图标库 / emoji 占位。
- **工程接入**：Tailwind / shadcn 可将 `tokens.css` 变量挂入 `theme.extend`（`colors`、`spacing`、`fontSize`、`borderRadius` 等）。
- **变更来源**：以 Figma 与 `tokens.css` 同步结果为准；`design.md` 负责说明，不再单独衍生第二套配置。

---

## 11. Do's and Don'ts

### Do

- 使用 `**tokens/tokens.css`** 中的 `**--color-*`、`--type-*`、`--space-s*`、`--shape-radius-*`、`--font-*`** 实现颜色、字阶、间距与圆角。
- 主路径 CTA 默认用 `**Surface/Inverse Surface**`（黑）+ `**Inverse On Surface**`；**最高强调**那一个才用 `**Schemes/Primary**` + `**On Primary**`（§3.1），并与 `**label/large - prominent**` 字阶搭配。
- 在 Figma 中绑定 **Color / Typescale / Shape** 变量；组件用 **库实例**。
- 按 **§5.3 / §5.4** 选择字阶；同一语义角色在同一页面内保持一致。
- 图标统一调用 `**@one2x/o2x-icons**`（`<XxxIcon />` 或 `o2x-icons-<名>`，颜色用 `currentColor`，§6.1）。
- Manrope 字阶按稿启用斜杠零（`**font-feature-settings: 'zero' 1`**）；Geist Mono 数字要无斜杠 0 时用 `'ss09' 1`，且不要同时开 `zero` / `slashed-zero`（执行要点见 `**o2x-design-system**` Typography）。
- 查阅 `**tokens/README.md`** 与 `**o2x-design-system**` skill 获取实现细则。
- **开工先判密度档**（§2.1）：托盘 / 菜单栏 / 浮出面板 / 下拉一律 Compact——12 / 11 两档字号、8px 外边距、24 高分组标题行、24 高紧凑黑钮、不透明度做层级；先读 §7.5 参考帧再搭。
- Compact 面板里用**库组件**：`Progress`（单色）、`HorizontalDivider`、`Spinner`、`IconButton` 20、`Button`（filled 24 / 40 / 44 三档）、`Field`、实心状态图标（`CheckCircleIcon` 等）。
- 对齐与间距按**可视边缘**量（文字、封面、可视按钮底），不量卡片外框、热区或盒子；改完一处，在所有分区、所有视图下复量（§4.5、§7.2）。
- **点开菜单后，触发按钮回到 default 态**（强制，§4.3）；模式开关与分段控件的当前项例外。
- 对某类元素定下的样式（菜单规格、面板外观、按钮默认态、骨架、图标颜色、勾选框、圆角）**同步到同页所有同类元素**，不等逐个指出。
- 勾选框全页一套：未选 `Background` 90% + 0.5px `On Surface` 16% 的 `outline`，选中 `Primary`；多选中的条目只靠勾选框表达（§4.3、§6）。
- 筛选 / 分组生效时用 `Primary` 08% 底 + `Primary` 图标，和菜单展开的 default 态区分（§4.3）。
- 多选用 Select 按钮原位展开的工具组，同页只激活一个分区；全选按钮部分选中时补全、全选时清空（§7.6）。

### Don't

- **不要**在代码中写裸 **hex** / `rgba()` / `white`（含蒙层、阴影、TS 颜色常量）：一律用随明暗主题切换的 token（§4.6）；确需恒定颜色（图片上的遮罩与白字、视频黑边、品牌渐变）时在同一行注释声明原因；稿与 token 尚未覆盖的临时情况也要注释并回写 token。
- **不要**用 `**Schemes/Secondary Container`** 充当主品牌 CTA 色（§4.2）。
- **不要**把 `**Radius/*` 的 px 命名规则**与 `**Space/s*`** 阶梯混淆（§4.4–§4.5）。
- **不要**把紫色 `**Schemes/Primary`** 当默认主按钮色到处用：默认主按钮用 `**Inverse Surface`**（黑），紫色只给最高强调，每屏 0–1 个（§3.1）；可拖拽分栏线（resizer）这类辅助 affordance 也不用紫色，用 `**Surface/Outline**`。
- **不要**在同一屏放多个同等视觉权重的紫色 Primary 主按钮（§3.1）。
- **不要**临时画 SVG、引第三方图标库（Material Symbols / Lucide / Iconfont 等）或用 emoji 当图标——一律走 `**@one2x/o2x-icons**`（§6.1）；设计指定的图标库里还没有时先同步补齐，不拿语义相近的图标顶替。
- **不要**自写库里已有的组件（如 `Tooltip`），也不要把一个变体改造成另一个变体的样子（如 `kind="text"` 涂黑当实底钮，状态层会失效）；同一按钮只留一层状态底色（§4.3、§6）。
- **不要**在超大 Figma 文件上对全文件 `**findAll`** 触发 MCP 过载（见文首 MCP 说明）。
- **不要**把业务页密度搬进工具面板：Compact 容器里禁止 `s4` 外边距、52+ 高列表行、`label/large - prominent` 行名、通栏 48 黑钮插在列表中间、蓝色进度条、彩色圆点徽标、圆形头像、红色危险按钮（§2.1 / §3.1 / §7.5）。
- **不要**用第三种颜色 token 做文本层级——Compact 面板只有 `On Surface` 与 `On Surface Variant` 两种，层级靠 100 / 60 / 40% 不透明度。
- **不要**用浮在内容上的底部操作条做多选工具，也不要给选中条目加紫色外框或底色（§4.3、§7.6）。
- **不要**把 hover 才出现的操作改成常驻，也不要在分组视图里展示空分组的「暂无…」占位（§7.6）。
- **不要**为只在 hover 时出现的按钮常驻留白或预留占位列（叠放在内容上，用 `mask-image` 渐隐让位，§7.6）；**不要**为防跳动按最长文案写死文字按钮宽度（hug 优先，附录 C.5.1）。

---

## 12. 响应式与字阶模式

- **Typescale** 提供 **Baseline** 与 **mobile** 等模式；组件与页面应在对应断点下选用稿内与 `**tokens.css`** 一致的字阶。
- **默认策略**：以 Medeo 产品稿为准；营销页可更多使用 `**display/*` + Nohemi**（§5.3）。
- 具体断点数值以实现框架与项目约定为准；**字阶切换**须仍对应 **Typescale / `--type-*`**，避免手写断点专属像素。
- **容器级响应**：可拖窄的面板、随宽度变化的工具栏，先设最小宽度，保证必需控件（如视图切换）完整显示；向视口边缘收紧时不得产生横向滚动（§7.2）。放不下时的处理示例见 §7.6 置顶面板（默认显示标题，hover / 聚焦时换成控件）。

---

## 13. Agent Prompt Guide

### 13.1 Quick reference（Medeo light 默认）


| 角色       | Token / 变量                                                       |
| -------- | ---------------------------------------------------------------- |
| 页面背景     | `Surface/Surface` → `--color-surface-surface`（以 `tokens.css` 为准） |
| 卡片/顶层表面  | `Surface/Surface Container Lowest`                               |
| 主文本      | `Surface/On Surface`                                             |
| 次要文本     | `Surface/On Surface Variant`                                     |
| 默认主按钮 · 背景 | `Surface/Inverse Surface` → `--color-surface-inverse-surface`   |
| 默认主按钮 · 文字 | `Surface/Inverse On Surface` → `--color-surface-inverse-on-surface` |
| 最高强调 · 背景 | `Schemes/Primary` → `--color-schemes-primary`（克制使用，每屏 0–1 个）    |
| 最高强调 · 文字 | `Schemes/On Primary` → `--color-schemes-on-primary`             |
| 圆角（示例）   | `Radius/12` → `var(--shape-radius-12)`                           |
| 间距（示例）   | `Space/s4` → `var(--space-s4)`                                   |
| 正文字体     | `var(--font-family-plain)`，字阶来自 `--type-*` 或 `.o2x-type-*`       |
| 图标       | `@one2x/o2x-icons` → `<XxxIcon />` 或 `o2x-icons-<名>`（颜色 `currentColor`） |
| 浮出菜单面板 | `Surface Container Lowest` + 0.5px `Outline Variant` + 同页一档阴影；菜单项 24 高、`label/medium`（§6、§8） |
| 未选中控件 / 图标 | `Surface/On Surface Variant`（100%）；选中态用 `On Surface` |
| 分栏线 / resizer | `Surface/Outline`（不用 `Schemes/Primary`） |


### 13.2 Example prompts

- 「在 Medeo light 下做一个 Dialog：白底容器用 `Surface Container Lowest`，标题 `title/medium`，默认主按钮 **Filled** + `Surface/Inverse Surface` / `Inverse On Surface`，次要操作为 Outlined；`gap` 与 `padding` 全部用 `var(--space-s*)`，圆角用 `var(--shape-radius-12)`。」
- 「做一列列表项：正文 `body/medium`，元信息 `body/small`，分隔线用 `Surface/Outline`；如果有主操作，默认用 `Inverse Surface` 黑色主按钮，紫色 Primary 每屏最多 0–1 个。」
- 「营销区块 Hero：`display/large` + `font-family: var(--font-family-brand)`，副标题 `body/large`；只有最高强调 CTA 才使用 `Schemes/Primary` + `On Primary`，不要用 Secondary Container 当品牌色。」
- 「做一个 340×480 的托盘面板（Compact 档，§2.1 / §7.5）：先读参考帧 `6974:114850`；头部 49 高（头像 32 `Radius/8` + `label/medium` 名 + `label/small` @40% 邮箱 + 20px ⋯），状态条 32 高 `Surface/Surface`，分组标题行 24 高 `label/medium` @40% 右侧放 24 高紧凑黑钮，列表行 41 高、行名 `label/medium`、元信息 `label/small` @60%，进度用单色 `Progress`，描边全部 `Outline Variant` 0.5px，文案英文。」
- 「做一个工作台列表页的工具栏和弹出菜单（§2.1 Compact 局部 / §7.6）：按内容（Add、Select）/ 数据（Search、Filter、Group、Sort）/ 视图（视图槽 + Grid｜List）分区，从右锚定；控件 24 高、`gap` 2px、圆角统一，图标 18px `On Surface Variant`，文字按钮 hug 文案；纯图标按钮配库 `Tooltip`；菜单 `Surface Container Lowest` + 0.5px `Outline Variant`，项高 24、`label/medium`、图标 14px，出现在触发按钮可视边缘下方 4px，点开后触发按钮回到 default。」

### 13.3 Iteration checklist

0. 密度档判对了吗（§2.1）？工具面板 / 下拉 / 侧栏 = Compact：12/11 字号、8px 边距、24 高标题行与紧凑钮、不透明度层级。工作台列表页不是整页 Default：工具栏、弹出菜单、置顶面板和页面边距按 Compact 收紧（§7.6）。
1. 颜色与间距是否均可映射到 `**--color-*`** 与 `**--space-s*`**？
2. 是否只有一个「主层级」的 Primary CTA（§3.1）？
3. 间距与圆角的档位值是否都用了变量（含负值、`calc()` 里的项、同心内层，§4.5 / §4.6），只剩注释过的 1–3px 光学微调，以及设计指定渲染 px 的圆角与其同心内层是字面值？圆角是否用了 `**--shape-radius-***`，且未与 `Space/s*` 混用规则？嵌套圆角是否与外轮廓同心（外轮廓以可见描边为准，§4.4）？token 与字面 px 有没有混算（Medeo `--Radius-8` 计算值为 10px，§4.6）？
4. 字阶是否落在 **§5.3** 的语义档位，而非临时 `font-size`？
5. Figma 侧是否优先 **实例化库组件**，而非手绘 Frame？
6. 图标是否全部来自 `**@one2x/o2x-icons**`，无临时 SVG / 第三方图标 / emoji（§6.1）？
7. 左起点线：所有分区、网格 / 列表两种视图下，标题、表头、封面、缩略图是否落在同一 `x`？间距是否按可视边缘量（§4.5、§7.2）？改完一处是否复量了整页（起点线、操作区右缘、灰底留白）？
8. 菜单与触发按钮：点开菜单后触发按钮是否回到 default（§4.3）？菜单与按钮的距离是否按**可视**边缘量、同页一致，是否只有一层面板（§6、§8）？hover 才出现的操作在菜单打开期间是否保持显示？状态切换是否改变了盒子尺寸？
9. 库组件与变体：Tooltip、按钮、图标是否用了库里现成的组件与变体？变体默认的尺寸 / 颜色（如 `IconButton size="small"` 的 14px 图标、组件默认的 `On Surface` 前景）是否读计算值核对过（§6）？
10. 同类样式是否已同步到同页所有同类元素（菜单、按钮默认态、骨架、图标颜色、勾选框、圆角）？
11. 选择模式：Select 是否原位展开、同页只有一个分区在选择模式？全选三态与「全选（N）· 已选择 M 项」文案、Shift 连选、全选后新加载的条目也选中？选中条目是否只靠勾选框表达（§4.3、§7.6）？
12. 勾选框：网格 / 列表 / 全选是否同一套样式？圆角是否与所在外框同心，四周可视间距是否一致（§4.4、§6）？
13. 横向滚动行：两端渐隐是否随可滚方向出现？裁切点是否贴相邻面板与视口？翻页箭头是否 hover 才出现、翻页有快速过渡（§7.6）？

---

## 附录 A：Figma 文件结构（全部 Page 一览）

以下内容通过 Figma MCP `use_figma`（Plugin API）读取 `figma.root` 下 **Page** 列表得到，便于与文件内左侧页签对照。名称含 **🚧** 表示该页在稿内标注为施工中 / 未就绪。


| 顺序  | 页面名                           |
| --- | ----------------------------- |
| 1   | Foundation                    |
| 2   | 📖Cover                       |
| 3   | 📄Table of contents           |
| 4   | 🌈Styles                      |
| 5   | ⭕️Icon                        |
| 6   | 🏗️Structure                  |
| 7   | 🔷State layer                 |
| 8   | 🎁Assets                      |
| 9   | ↳Illustrator                  |
| 10  | ↳One2X product logo           |
| 11  | 🚧表示施工中，not ready             |
| 12  | ----------                    |
| 13  | Components                    |
| 14  | ↳Alert                        |
| 15  | ↳Avartars🚧                   |
| 16  | ↳Badges🚧                     |
| 17  | ↳Buttons                      |
| 18  | ↳Checkbox🚧                   |
| 19  | ↳Chips🚧                      |
| 20  | ↳Dialog🚧                     |
| 21  | ↳Document                     |
| 22  | ↳Dividers                     |
| 23  | ↳Drawer                       |
| 24  | ↳Input field                  |
| 25  | ↳Menu🚧                       |
| 26  | ↳Media Cover🚧                |
| 27  | ↳Navigation🚧                 |
| 28  | ↳Lists🚧                      |
| 29  | ↳OTP Field                    |
| 30  | ↳Progress indicators🚧        |
| 31  | ↳Picture upload🚧             |
| 32  | ↳Radio buttons🚧              |
| 33  | ↳Tags🚧                       |
| 34  | ↳Tabs                         |
| 35  | ↳Tooltips                     |
| 36  | ↳Slider🚧                     |
| 37  | ↳Snackbars                    |
| 38  | ↳Spinner                      |
| 39  | ↳Suggestions🚧                |
| 40  | ↳Switch🚧                     |
| 41  | -----                         |
| 42  | Medeo                         |
| 43  | ↳💻Main pages                 |
| 44  | ↳AI style dialog              |
| 45  | ↳AI style cover               |
| 46  | ↳Audio Script Panel           |
| 47  | ↳Assets panel                 |
| 48  | ↳Clip edit dialog🚧           |
| 49  | ↳Chat panel                   |
| 50  | ↳Command box                  |
| 51  | ↳Drag indicator🚧             |
| 52  | ↳Feeds🚧                      |
| 53  | ↳Feed detail🚧                |
| 54  | ↳Library panel                |
| 55  | ↳Notification dialog          |
| 56  | ↳Queuing                      |
| 57  | ↳Onboarding dialog            |
| 58  | ↳Other dialogs                |
| 59  | ↳Player panel                 |
| 60  | ↳Pricing&Credit               |
| 61  | ↳Projects                     |
| 62  | ↳Property panel🚧             |
| 63  | ↳Recipe                       |
| 64  | ↳Sign in                      |
| 65  | ↳User profile dialog          |
| 66  | ↳Video Export & Share dialog  |
| 67  | ↳Video thumbnail              |
| 68  | ↳Timeline panel               |
| 69  | ↳Title bar                    |
| 70  | ↳Templates                    |
| 71  | ↳Variant tabs                 |
| 72  | ↳VIP level tags               |
| 73  | ↳Watermark                    |
| 74  | ↳Campaign                     |
| 75  | ↳ Medeo Rewards               |
| 76  | ---                           |
| 77  | Mebox                         |
| 78  | ↳Clip button                  |
| 79  | ↳Popup panel                  |
| 80  | Side panel                    |
| 81  | ↳Time stamp                   |
| 82  | --                            |
| 83  | 📥Archive                     |
| 84  | ↳微拟物设计探索                      |
| 85  | ↳new explore                  |
| 86  | ↳AI media panel （with custom） |
| 87  | ↳Command box（before v1.03）    |
| 88  | ↳Command box（before v2）       |
| 89  | ↳Variant tabs abandon🚫       |


---

## 附录 C：Figma 设计稿使用规范

本附录标准化 One2X 内 **Figma 设计稿的文件命名、图层与组件组织**，保证团队阅读一致，并使 **Figma2code** 同步到代码侧时符合开发阅读习惯。

**与正文关系**：本附录侧重 **稿面结构与协作**；视觉尺度、Token、字阶语义仍以 **§1–§5** 与 `**tokens/tokens.css`** 为准。字阶适用场景（**C.6**）与 **§5.3** 一致，可互为对照。

**强制性说明**：*本附录不是 Figma2code 工具使用的强制前置条件*，而是 **使用该工具时的最佳实践**。

### C.1 总则：命名与交互状态

- **文件 / Frame / 图层命名**：完整层级格式由团队在 **Figma 库内**统一执行；本仓库不另附「命名总览」表。
- **交互状态属性**：以组件中**已实际使用**的属性为准；新增状态须在团队约定的 **对象/Item 状态** 中取**唯一**取值，并同步到组件说明。
- **结构属性**：描述组件结构维度（如 `hasStart`、布局类型等）；与 Component Property 命名关系见 **C.2 补充规则 B**。

### C.2 组件图层结构规则

组件（Component）与变体（Variants）的构建规则如下。


| 规则名称                    | 规则详情                                                                                                                                                                             |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **最小图层数量**              | 用**最少图层**覆盖尽量多场景。低频且会显著增加图层时，优先用**外层 Frame 组合**承载，而非无限膨胀单一组件。                                                                                                                    |
| **变体间图层数量一致**           | 同一组件不同变体须**图层数量一致**；某变体不需要的元素应 **隐藏**，**不得**删图层导致结构不一致。若无法兼顾，应**拆成另一个组件**。                                                                                                       |
| **实例交换（Instance Swap）** | 对**可被替换**的子内容配置 **Property → Instance Swap**，便于 Figma2code 传递「可替换实例」；否则仅靠手改子图层，工具链难以同步给开发。不需要被替换的图层建议**锁定**。若 Boolean 名为 `hasXXX`，对应 Instance Swap 属性名一般为 `**XXX`**（无 `has` 前缀）。 |
| **文字属性（Text）**          | 可替换文案须配置 **Text** 属性（理由同上）。                                                                                                                                                      |


**补充规则 A：Component Property 类型选择**


| 内容类型              | Property 类型   | 适用场景                         | 示例                    |
| ----------------- | ------------- | ---------------------------- | --------------------- |
| 单个可替换组件（结构固定）     | Instance Swap | 图标、头像等从预设列表选择                | Button 的 start icon   |
| 可替换文字             | Text          | 标签、标题等                       | Button 的 label        |
| 可自由组装的内容区（结构不可预测） | Slot          | Dialog body、Drawer content 等 | Dialog 正文区            |
| 元素显隐              | Boolean       | 控制某图层是否显示                    | `hasStart`、`hasClose` |


- **Instance Swap vs Slot**：从预设里选一个 → **Instance Swap**；需自由组装 → **Slot**；仅显隐 → **Boolean**。

**补充规则 B：Boolean 命名**

- 统一 `**has` / `show` 前缀 + PascalCase**，如 `hasStart`、`hasClose`、`showRMBPrice`。
- 若 Boolean 控制某 Instance Swap 的显隐，且 Boolean 为 `hasXXX`，则对应 Instance Swap 名为 `**XXX`**（去掉 `has`）。  
  - ✅ `hasStart` + `start`  
  - ❌ `hasStart` + `startIcon`

**补充规则 C：Variant 属性值格式**

- 交互状态类（`state`、`selected`、`disabled`、`loading`）→ 全小写：`default`、`hovered`、`focused`、`pressed`、`true`、`false`。
- 布局 / 类型类（`type`、`layout`、`kind`）→ 全小写：`vertical`、`horizontal`、`filled`、`outline`。
- **禁止**同一 Variant 属性内大小写混用（如 `Default` 与 `hovered` 并存）。
- 布尔型 Variant → 使用 `**true` / `false`**，不用 `yes` / `no`。

**补充规则 D：拼写**

- 组件名、属性名、Variant 值须使用**正确英文**；发布前检查，避免 `increse`、`Iterm`、`currrent` 等错误进入库（修改成本极高）。

### C.3 组件命名与组织

**通用（基础 + 业务）**

- 组件名**全局唯一**；**PascalCase**：`ProfileDialog`、`ConfirmButton`。
- 子节点 **camelCase**，体现功能或角色，**不**用表现命名：✅ `confirmButton` ❌ `redButton`。

**基础组件（Atomic）**

- 子节点**严格唯一**，不可重复或模糊。  
- ✅ `Button` → `iconLeft`、`label`、`iconRight`  
- ❌ 多个同名 `icon`

**业务组件（Business）**

- 子节点可**语义化抽象**，但**禁止**拼接版本号式命名（如 `header_v1`）或重复同名子节点。  
- ✅ `ProfileDialog` → `header`、`body`、`confirmButton`、`cancelButton`  
- ❌ `header_v1`、`confirmButton_v1` 或三个 `confirmButton`

### C.4 Figma 文件与页面组织

**Page 命名**

- 基础组件子页：`↳` 前缀，如 `↳Buttons`、`↳Input field`。
- 施工中：名称后加 **🚧**，如 `↳Dialog🚧`。
- 分隔线：`----------` 或 `-----`。
- 产品页：产品名开头（如 `Medeo`、`Mebox`），子页用 `↳`。

**Page 内 Section**

- 用 **Section** 区分模块；名称语义化（如 `Credit`、`Pricing`）。
- 组件定义与 **demo/示例** 分区放置，避免混在一坨。

**Variant 数量**

- 基础组件（Button / Switch / Tag）：可用 Variants 管理交互状态，组合数可较多。
- 业务组件：Variant 维度建议 **≤ 3**；若组合 **> 12**，评估是否拆成多个组件。

### C.5 i18n 多语言设计规范

以下为设计稿侧规则（与产品侧本地化流程配合，架构细节以团队约定为准）。

#### C.5.1 文本容器弹性


| 英文源文案长度           | 预留膨胀  | 典型膨胀语言     |
| ----------------- | ----- | ---------- |
| ≤10 字符（短文案：按钮、标签） | +200% | 德语、芬兰语、希腊语 |
| 11–20 字符（菜单、Tab）  | +100% | 法语、俄语、葡萄牙语 |
| 21–70 字符（提示、描述片段） | +40%  | 大部分欧洲语言    |
| >70 字符（长文）        | +30%  | —          |


日语、韩语、中文常比英语短，但**不得以之为由缩小容器**——以**最长语言**为基准。

**落地规则**

- 禁止 **固定宽 + 固定高** 同时卡死（至少一维可自适应）。
- Button、Chip、Tab 等短文案：**auto width**（`min-width` + padding）。**hug 优先于零位移**：不要为避免切换文案（如排序项）时的位移，按最长文案写死宽度；相邻控件随之平移几像素可以接受。
- Toast、Alert body、Dialog body 等：**高度自适应**，允许多行。

#### C.5.2 组件级 i18n 标注

每个组件 Spec / Anatomy 区建议增加 **i18n constraints** 标注：


| 标注项                | 说明           | 示例                          |
| ------------------ | ------------ | --------------------------- |
| maxLength          | 源文案（英文）最大字符数 | max 24 chars (en)           |
| overflow           | 超长策略         | truncate、wrap、scale-down    |
| width              | 宽度策略         | auto (min 88px)、fixed 120px |
| lines              | 最大行数         | 1 line、unlimited            |
| icon-only fallback | 是否提供纯图标降级    | icon-only variant available |


**各组件建议值**（可按业务微调，稿内须明确）：


| 组件                | maxLength (en) | overflow           | width            | lines     |
| ----------------- | -------------- | ------------------ | ---------------- | --------- |
| Button            | 24             | truncate + tooltip | auto, min 88px   | 1         |
| Chips             | 20             | truncate           | auto, max 200px  | 1         |
| Tab               | 16             | truncate           | auto             | 1         |
| Input label       | 30             | wrap               | follow container | 2         |
| Input placeholder | 40             | truncate           | follow container | 1         |
| Input helper text | 60             | wrap               | follow container | 2         |
| Dialog title      | 40             | truncate           | follow container | 1         |
| Dialog body       | unlimited      | wrap               | follow container | unlimited |
| Dialog CTA        | 24             | 同 Button           | auto, min 88px   | 1         |
| Toast / Snackbar  | 80             | wrap               | fixed max-width  | 2         |
| Alert             | unlimited      | wrap               | follow container | unlimited |
| Navigation label  | 12             | truncate / wrap    | auto             | 2         |
| Tooltip           | 60             | wrap               | auto, max 240px  | unlimited |
| Tag               | 16             | truncate           | auto, max 120px  | 1         |
| Menu item         | 30             | truncate           | follow container | 1         |


#### C.5.3 设计稿文案

1. 源文案用**英文**；Text Property 默认值不用中文占位。
2. 文案有语义：避免无意义 `Label`、`Text`，用真实文案（如 Save changes、Cancel）。
3. 动态内容用 `{变量名}`，如 `Hello, {userName}`、`{count} items`。
4. 含文字需本地化的素材：图层名后加 **🌐**。

#### C.5.4 布局弹性检查清单（评审用）

- 文本容器至少一维可自适应？  
- 短文案组件是否 auto width？  
- 是否标注 maxLength 与 overflow？  
- 固定宽布局中文案区是否支持 truncate + tooltip？  
- 图标+文字是否可用 Auto Layout 预留 RTL 镜像？  
- 多行 Alert / Toast 是否高度自适应？  
- 含文字素材是否标 🌐？
- hover 才出现的叠放按钮（如 ⋯）下方的文案，换成最长语言时会不会伸进按钮下？（需渐隐 mask 或让位，§7.6）

### C.6 Typography 字阶稿内使用

与 **§5.3 字阶语义与场景映射**一致；下表便于在 Figma 选档时自查。


| Token 层级     | ✅ 适用                     | ❌ 不适用       |
| ------------ | ------------------------ | ----------- |
| `display/*`  | Landing Hero、Campaign KV | 表单标题、普通卡片标题 |
| `headline/*` | 页面主标题、章节起始               | 按钮文案、长段正文   |
| `title/*`    | Dialog / Drawer / 卡片标题   | Hero、脚注     |
| `body/*`     | 正文、说明、帮助                 | 主 CTA 文案    |
| `label/*`    | 按钮、Tab、Chip、输入标签         | 段落正文        |


`***-prominent`**：同一层级内强调主操作 / 高优先级；**同一视图内** prominent 宜控制在 **1–2 个**元素；超过 **3 个**须重新梳理信息架构。

### C.7 补充规则：corner-shape 圆角标注

项目默认启用 **corner-shape（superellipse）**；设计稿圆角按此渲染。若某组件需要**标准全圆角（pill / 半圆弧）**而非 superellipse，须在 Figma Dev Mode 注释或图层描述中标注 `**corner-shape: round`**。


| 组件     | 原因             |
| ------ | -------------- |
| Avatar | 圆形头像需标准 50% 圆弧 |
| Switch | 轨道需标准 pill 全圆角 |


其余组件用默认 corner-shape；新增场景在本表补充。

**代码侧换算**：Medeo Web `variables.readonly.css` 在支持 `corner-shape` 的浏览器里给所有元素设 `superellipse(1.4)`，并把 `--Radius-N` 放大约 1.27 倍（名中数字 ≠ 计算值，换算与同心写法见 §4.6）；字面 px 圆角只换形状、不放大。

### C.8 小结

**一句话**：约束产生一致性，一致性产生效率。

- **命名**：组件 PascalCase 全局唯一；子节点 camelCase、语义化。  
- **图层**：最少图层 + 变体间结构一致 + 不用的图层隐藏不删。  
- **属性**：可替换内容暴露为 Property（Swap / Text / Slot / Boolean），类型见 **C.2 补充规则 A**。  
- **Variant**：值全小写；布尔 `true`/`false`；禁止大小写混用。  
- **拼写**：发布前检查。  
- **文件组织**：Page 与 Section 规则见 **C.4**；i18n 见 **C.5**；字阶稿内见 **C.6**；与 **§5** 对齐。

---

## 附录 B：修订记录


| 日期         | 说明                                                                                                                                               |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2026-09-30 | **Medeo Createspace / 编辑器素材面板 UI polish 复盘**：**§4.3** 增「生效中 ≠ 展开」（筛选 / 分组生效用 Primary 08）、多选只靠勾选框表达；**§4.4** 更新 Medeo 同心实例（外框 6px 一组），增「控件严格同心，内容主体可由设计指定」；**§4.6** 增设计指定确切渲染 px、`--Radius-N` 补偿后会偏离时写字面值（工具栏 4px、外框 6px，同心内层同样字面）；**§6** 菜单水平对齐 / 打开期间固定 / 分组标题、勾选框统一规格、单行输入垂直居中、标签溢出点占位、进度条最小填充、同排按钮一致；**§7.6** 增列表 hover 外框距视口相等、网格内容贴顶、面板分组标题对齐、列表 ⋯ 居中等距、保持 hover 显隐，新增「横向滚动行」「选择模式」「分组与空状态」，参考值表把工具栏圆角改为字面 4px（分段选中块 3px，与编辑器素材面板标题栏统一）、改菜单与角标圆角并补外框 / 勾选框 / 选择工具组 / 横向滚动 / 命令框；**§11** 修正斜杠零写法（Manrope `zero` 与 Geist Mono `ss09` 分开）并补 Do / Don't；**§13.3** 增 11–13 |
| 2026-09-29 | **密集工作区页面**（来自 Medeo Createspace 工作台列表页走查复盘）：**新增 §7.6**（工具栏分区与从右锚定、hover 操作与 mask 渐隐、弹出菜单几何、置顶灰底面板、整页扫光骨架 + Medeo 参考值表）；**§7.2** 增单一左起点线、靠边但不贴边；**§4.3** 增只留一层状态底色、展开不算状态、状态不改尺寸、反色底档位可见；**§4.4** 增同心嵌套；**§4.5** 增 1–3px 光学微调与按可视边缘量；**§4.6** 增 Medeo 变量命名与 `--Radius-N` 补偿换算；**§2.1** 密度按区域判定（含密集工作台的页面边距例外）；**§2.2** 团队约定独立成节并补组件条款；**§4.1** 浮出菜单底色改为 `Surface Container Lowest`，补控件前景与 resizer 用途；**§6 / §6.1** 增组件先查库、Tooltip、Button kind、IconButton 变体、图标尺寸与缺图标同步流程；**§8** 同页浮层一档外观、单层面板；**§10** 修正主行动按钮颜色与 §3.1 的矛盾；§3、§3.1、§4.5.1、§5.4、§7.1、§7.4、§9、§11、§12、§13、附录 C.5 / C.7 同步 |
| 2026-09-14 | **密度档**：新增 **§2.1 Density**（Default / Compact），Compact 规则来自 Medeo 桌面端「同步文件夹」托盘面板定稿与 Agent 首版的对比复盘（首版按业务页密度生成：s4 边距、52 高行、`label/large - prominent` 行名、通栏黑钮、蓝色进度、彩色圆点徽标）；**§3.1** 增主按钮四种形态表（紧凑 24 / 通栏 40 / Dialog 双钮 44 / 行内 Outlined 对）与第三方登录钮例外；**§5.4** 增 Compact 面板字阶行（12/11 + 100/60/40% 不透明度层级）；**§7.1** 增 Compact 间距；**新增 §7.5 紧凑面板配方**（参考帧 node `6974:114850` 等 + 完整骨架 + 登录/空态/确认框/深色/英文文案约定）；§11、§13 同步 |
| 2026-04-06 | **结构**：按 Stitch 式重组（§1 视觉气质、目录、§7–§13、附录 A Page 表等）；**附录 C**：Figma 稿图层/Property、Figma2code 最佳实践、i18n、字阶稿内、corner-shape；已去掉对外部文档表格的依赖             |
| 2026-04-03 | Typography 增补 **§5.3 字阶语义与场景映射**、**§5.4 Medeo 常见页面举例**（原 §3.3 / §3.4），统一 `display/headline/title/body/label` 与 `prominent` 使用边界，避免 skill 与正文口径漂移 |
| 2026-03-31 | 精简 **代码映射**（现 §10）：去除与圆角/间距/`tokens.css` 重复的映射表描述，明确 `**tokens/tokens.css`** 为实现侧单一数据源；历史名仅作兼容说明                                                 |
| 2026-03-25 | 基于 Figma MCP：`get_variable_defs`（Share、Button 节点）、`search_design_system`、`get_design_context`（VideoShareDialog）与组件描述整理                           |
| 2026-03-25 | 补充整文件入口链接说明；用 `use_figma` 枚举全部 Page 页签写入「Figma 文件结构」表                                                                                            |
| 2026-03-25 | 增补变量集合一览、Shape 圆角全表、Typeface；**Design scale** 与 **fileKey** 强调；恢复误覆盖的正文                                                                          |
| 2026-03-25 | `**tokens.css`**：补齐 字阶 `--type-*`、字族、间距 `--space-*`、`**--shape-corner-*` 历史别名**、`**.o2x-type-*`** 组合类；间距与网页侧变量、Typography、代码映射明确新页面须用变量          |
| 2026-03-25 | 圆角 CSS 改为 `**--shape-radius-{px}`**（4px 网格至 40），与高度档命名脱钩；`tokens.css` 同步                                                                         |
| 2026-03-25 | 新增 **Primary 主按钮**（现 §3.1）：主 CTA 用 **Filled + Primary + On Primary** 体现品牌感；Schemes、核心组件 Button 呼应                                                |
| 2026-03-25 | **Figma `Shape`**：圆角分组曾历经 `**Radius/***` / `**Corner/***` 调整；**按 px 命名** 并补全 `**…/24`…`…/40`**；变量集合、圆角、代码映射同步                                    |
| 2026-03-31 | `**Shape`** 圆角变量：Figma 分组前缀改为 `**Radius/***`（替代 `**Corner/***`）；`design.md`、`tokens/*`、skills 与圆角表同步；Figma 作用域名 **Corner radius** 不变             |
| 2026-03-25 | **Figma `spacing`** 集合：`**spacing/0`…`spacing/16**`（11 项）与 `**--space-***` 对齐；Design scale、`tokens/README` 同步                                    |
| 2026-03-25 | `**spacing/***` 并入 `**Shape**` 集合（原独立 `**spacing**` 集合已删）；Design scale、`tokens/README`、`tokens.css` 头注释同步                                        |
| 2026-03-25 | **间距命名**：Figma `**Space/s0`…`Space/s10`**、CSS `**--space-s0`…`--space-s10`**（s = 阶梯，≠ px）；与圆角 `**{px}**` 名规则区分；`tokens.css`、示例页、skills 同步        |
| 2026-04-13 | **Shape 间距变量**：主库命名以 `**Space/s0`…`Space/s10`** 为准；移除 Shape 变量上的 **Code Syntax**，文档改为说明 Figma 命名与 Web token 对应，而不再把 Code Syntax 视为规范的一部分 |
