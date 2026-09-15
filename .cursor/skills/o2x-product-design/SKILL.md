---
name: o2x-product-design
description: O2X Product Design skill entry for One2X/Medeo. Use for One2X design system work, Medeo UI implementation or review, Figma MCP writing, Figma variable binding, full-page Figma assembly, design tokens, typography, components, or animation. Routes the agent to the right sibling skills in order.
---

# O2X Product Design skill

## 唯一来源与路径解析

本仓库是 O2X Skill、`design.md` 和 `tokens/` 的唯一维护来源。通过 Codex / Cursor 全局入口加载时，先解析当前 `SKILL.md` 的符号链接真实路径，再以真实文件所在目录解析本文所有相对路径；不可直接从全局入口目录计算 `../../../`。

配套 O2X Skill 与仓库自带的 Figma、动效 Skill 按真实路径加载。额外技能（如 `design-feedback-judge`、`emil-design-engineering`）从当前环境技能目录发现，不假设它们位于仓库内。消费项目的组件与实现配置仍遵循该项目约束；产品专属差异不能自动改写仓库的品牌规范。

## 自动反馈评审与技能改进

执行本技能的设计、视觉调整或实现对稿任务前，从当前环境的技能目录加载 `design-feedback-judge`（如已安装），可用时按任务建立评审记录；交付前、收到用户修订意见后自动评审并给简短回执，无需用户另外要求记录。普通问答与纯文档维护不触发作品评审。多个设计技能联用只保留一份记录；已有独立视觉评审直接复用，不增加另一套打分。

先修本次作品，再区分单期偏好、执行遗漏与可复用方法缺口；有依据才更新负责的技能，保存差异并验证。保持本技能的参考材料、先审后改、设计系统及操作授权要求。One2X 团队规范和已发布库不因单次反馈自动改变。


Use this as the default entry for One2X / Medeo design work. It is an orchestrator skill: read this file first, then load the required sibling skills before acting.

## Always Do First

1. Read `../../../design.md` from the skill pack root.
2. If the task touches implementation tokens, read `../../../tokens/README.md` from the skill pack root.
3. Pick the route below and load the listed skills in order.

Path resolution:

- If this skill is installed inside a project, `../../../design.md` means that project's root `design.md`.
- If this skill is loaded globally through a symlink under `~/.cursor/skills` or `~/.codex/skills`, resolve the symlink target first and use the cloned skill pack root that contains `.cursor/skills/o2x-product-design/`.
- If the target project also has its own `design.md` / `tokens/`, prefer the target project for implementation details and use the skill pack copy as the One2X baseline.

Motion supplement: when `emil-design-engineering` is installed, load it from the environment skill catalog alongside the bundled `web-animation-design`.

## Routes

### Code Implementation Or Review

Use when building, reviewing, fixing, or refactoring One2X / Medeo frontend UI.

Load:

1. `../o2x-design-system/SKILL.md`
2. `../web-animation-design/SKILL.md` when the task involves hover, transition, entrance/exit motion, easing, loading states, touch interaction, or `prefers-reduced-motion`.

Rules:

- When a Figma URL or selected Figma node is the implementation source, follow the mandatory Figma-to-code workflow in `o2x-design-system`; do not implement from the screenshot alone.
- Fetch both structured design context and a screenshot before editing code. Fetch variable definitions for token-sensitive work and inspect the target repository's existing components and tokens before creating anything.
- Build a short evidence map from Figma component/style/variable names to existing project components and `tokens.css` variables. Unmapped values are exceptions to resolve, not permission to hardcode.
- Use `tokens/tokens.css` names for color, typography, spacing, radius, and font family.
- Avoid naked hex, arbitrary `font-size`, arbitrary spacing, and non-token radius values.
- Use existing project components before creating new UI primitives.
- Icons must come from the One2X icon library `@one2x/o2x-icons` (component `<XxxIcon />` or font className `o2x-icons-<Name>`, color via `currentColor`); never hand-roll SVGs, pull in third-party icon sets (Material Symbols / Lucide / Iconfont, etc.), or use emoji as icons. See `design.md` §6.1.
- Validate the rendered result against the same Figma node at the target viewport before completion.

### Figma MCP Write Or Edit

Use when creating, editing, syncing, inspecting, or fixing Figma nodes, components, variables, styles, Auto Layout, or screenshots through MCP.

Load:

1. `../figma-use/SKILL.md`
2. `../o2x-figma-workflow/SKILL.md`
3. `../figma-generate-design/SKILL.md` only for full-page, screen, modal, drawer, panel, or multi-section assembly from code or description.
4. `../web-animation-design/SKILL.md` if motion or transition behavior is being designed.

Rules:

- Never call `use_figma` before loading `figma-use`.
- Reuse published One2X variables, text styles, and components. Do not create duplicate local `One2X · Color` or `Shape` collections in consumer files.
- Bind all `fills`, `strokes`, and text fills to published One2X `Color` variables. Low-emphasis strokes default to `Surface/On Surface Variant` at `0.5px`; use `Schemes/*` for primary, error, and other semantic roles; use palette variables only when no semantic variable exists.
- Bind `padding*` and `itemSpacing` to `Shape/Space/s*`.
- Bind `topLeftRadius`, `topRightRadius`, `bottomLeftRadius`, and `bottomRightRadius` to `Shape/Radius/*`.
- Any rounded element must keep a concentric relationship with adjacent inner/outer rounded elements: `inner radius = outer radius - gap/padding`.
- Set `cornerSmoothing = 0.6` for non-zero rounded nodes to match One2X's default corner-shape / superellipse rendering. If a component needs standard round corners instead, annotate `corner-shape: round`.
- After writing Figma components, run the Color and Shape binding checks from `o2x-figma-workflow`.

### Design Token Or Skill Pack Maintenance

Use when updating `design.md`, `tokens/`, skill docs, or the design skill pack itself.

Load:

1. `../o2x-design-system/SKILL.md`
2. `../o2x-figma-workflow/SKILL.md` if the change affects Figma variables, components, or MCP behavior.

Rules:

- Keep Figma naming and Web naming aligned: `Radius/*` maps to `--shape-radius-*`; `Space/s*` maps to `--space-s*`.
- `Space/s*` names are scale steps, not pixel values.
- Update README guidance when the recommended usage changes.

## Quick Trigger Phrases

These should route here:

- "use One2X design system"
- "Medeo UI"
- "One2X Figma"
- "write to Figma"
- "bind variables"
- "design token"
- "tool call UI"
- "make this follow One2X"

## Completion Checks

- For code: design context and screenshot were captured when Figma was the source; Figma variables/styles/components were mapped to project tokens/components; no naked color, spacing, radius, typography, or font tokens remain unless an explicit exception exists; the rendered result was visually compared with the reference.
- For Figma: required sibling skills were loaded before tool calls, DS variables/components were reused, Color bindings and Shape bindings were verified, and rounded nodes use One2X corner smoothing.
- For docs: installation and usage instructions still point users to this stack as the default entry.
