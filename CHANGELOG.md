# Changelog

All notable changes to this skill pack should be recorded in this file.

## Unreleased

- 2026-09-29 `design.md` / `o2x-design-system`：新增两条强制规则——间距与圆角尽可能用变量（档位值、负值、`calc()` 项、同心内层都用变量，只有不在档位上的 1–3px 光学微调写字面值并注释），颜色一律用随明暗主题切换的 token（蒙层、阴影、TS 颜色常量同样适用；图片上的遮罩、视频黑边、品牌渐变需在同一行注释声明）；§7.6 参考值表的工具栏、菜单项、卡片角标圆角改为变量写法（来源：Createspace 走查追加反馈）
- 2026-09-29 `design.md` / `o2x-design-system`：新增 design.md §7.6 密集工作区页面（工具栏、hover 操作、弹出菜单、置顶灰底面板、扫光骨架与 Medeo 参考值）；§2.1 密度按区域判定，§2.2 团队约定成节并补组件条款；§4.3 / §4.4 / §4.5 / §4.6 / §6 / §6.1 / §7.2 / §8 补状态层、同心圆角、可视边缘量法、Medeo 变量换算、组件与图标规则；修正 §4.1 菜单底色、§7.1 s1 档、§10 主行动按钮颜色三处矛盾；o2x-design-system 新增「密集工作区页面（执行要点）」与 Agent workflow 5.2 / 10，补描边 Compact 例外、resizer 中性色、圆角同心四条与完成验收（来源：Medeo Createspace 页面走查复盘）
- 2026-09-14 `design.md`：新增 §2.1 密度档（Default / Compact）、§3.1 主按钮四形态表、§5.4 Compact 字阶行、§7.1 Compact 间距、§7.5 紧凑面板配方（Medeo 托盘面板定稿参考帧 + 骨架）；§11 / §13 同步。来源：Medeo 桌面端「同步文件夹」托盘面板 Agent 首版 vs 设计师定稿对比复盘。
- 2026-09-14 `o2x-figma-workflow`：加载顺序增「密度档判定」；新增「从 PRD 到设计稿」规格前置要求与 Compact 可 import 库组件 key 表。

## v0.1.0

- 初始发布。
- 补齐 `design.md`，作为 One2X 设计系统唯一正文规范。
- 增加 `tokens/tokens.css` 与 `tokens/README.md`，落盘 Web Token。
- 打包官方 `figma-use`、`figma-generate-design`。
- 增加 `o2x-design-system`，用于前端实现 / Review。
- 增加 `o2x-figma-workflow`，用于 Figma MCP 写回流程。
- 增加 `web-animation-design`，作为动效补充规则。
