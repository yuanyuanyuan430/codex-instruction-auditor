# Codex Instruction Auditor

一个用于审计和整理 Codex 全局指令、Skills 与 Prompt 入口的个人开源 Skill。

> 先把你的 Codex 指令变成一张可核查的地图，再决定删什么。  
> Map your Codex instruction surface before deciding what to remove.

这是一个**基于 OpenAI Developers 官方文章的工程化实现**：它把文章中关于“减少上下文膨胀、缩短 Skill 描述、采用渐进式披露、按任务读取文档、明确完成标准”的建议，落成一个可以在本地运行的审计工作流。

> This is a personal implementation inspired by an official OpenAI Developers article. It is not an OpenAI-maintained product or an official OpenAI package.

## 权威来源 / Authoritative source

- [OpenAI Developers — Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)

文章讨论了 Codex 项目中常见的三类指令面：Skills、`AGENTS.md` 和任务提示词。文章的核心判断是：模型能力增强以后，过去为了“手把手引导”模型而积累的长规则、重复约束和过度具体的操作剧本，可能导致上下文膨胀、触发误判、规则冲突和过早停止。

## 文章观点如何落地 / How the article becomes a tool

| OpenAI 文章原则 | 本 Skill 的对应实现 |
| --- | --- |
| Skill 描述要短而精准 | 检查描述长度，并提示过宽的触发条件 |
| 渐进式披露 | 建议把低频流程、示例和诊断资料放入 `references/` |
| `AGENTS.md` 要按任务读取文档 | 将全局入口与任务专属资料分开审计 |
| 减少旧模型时代的过度手把手规则 | 把重复、无条件加载和过时指令列为候选 |
| 重新检查权限边界 | 保留授权、验证、停止条件和运行时契约 |
| 明确真正的完成标准 | 要求整理后重新扫描、读取和验证实际状态 |

这不是把文件越短越好，而是在减少上下文噪声的同时保留真正改变模型决策的约束。

## 能做什么 / What it does

- 盘点 `AGENTS.md`、`skills/*/SKILL.md` 和 Skill 符号链接
- 找出失效链接、过长入口、过宽描述和断开的本地引用
- 标记可能重复、过时或无条件加载的指令
- 在编辑前创建非覆盖式备份并记录哈希
- 保留权限边界、验收标准、停止条件、运行时 marker 和 frontmatter
- 通过 Skill 校验和 Codex app-server 扫描验证结果

## 使用方式 / Usage

将这个目录放入 Codex 用户 Skills 目录，然后在需要整理指令时调用：

```text
使用 $codex-instruction-auditor 审计并整理我的 Codex 指令。
```

也可以直接运行只读审计脚本：

```bash
python3 scripts/audit_codex.py --root ~/.codex
```

脚本默认只读取 `AGENTS.md`、`skills` 和 Skill 引用，不读取凭证、数据库、会话、日志或运行时状态。

## 工作流程 / Workflow

1. **Inventory**：盘点入口、描述、引用和符号链接。
2. **Classify**：区分失效、重复、过宽触发、无条件细节和必须保留的契约。
3. **Backup**：编辑前创建带时间戳的备份并记录哈希。
4. **Refactor**：缩短入口，把条件性内容放入按需引用；不因为文件长就自动删除。
5. **Validate**：检查 frontmatter、引用、marker，并运行 Codex Skill 扫描。
6. **Report**：区分观察结果、实际修改、验证证据和仍存在的限制。

## 怎样把说明写得让人愿意使用 / How the docs earn adoption

工程规则需要准确，也需要让读者快速看懂价值。本项目提供一个可选的四段式表达层：**钩子 / hook** 先说读者正在承受的混乱；**反转 / reversal** 说明清理不是盲目删短；**高潮 / payoff** 展示可以检查的前后变化；**爽点 / call to action** 给出一条低风险命令，让读者马上得到一个小胜利。

Technical documentation must be accurate and easy to act on. This project adds an optional four-part editorial layer: a **hook** names the reader’s current pain; a **reversal** corrects the “just delete until it is short” instinct; a **payoff** shows a checkable before-and-after; and a **call to action** gives the reader a low-risk first command.

例如，不写“它会让 Codex 变聪明”，而是写清楚：整理前有哪些失效链接，整理后保留了哪些契约，运行哪条只读命令可以复核结果。完整的中英文模板和真实性检查见 [`references/engagement-guide.md`](references/engagement-guide.md)。

For example, do not claim that the tool “makes Codex smarter.” Show which broken links existed, which contracts were preserved, and which read-only command verifies the result. The full bilingual template and truthfulness checklist are in [`references/engagement-guide.md`](references/engagement-guide.md).

## 设计边界 / Scope boundaries

这个 Skill 专注于 Codex 指令、Skills 和 Prompt 配置的整理。

它不会自动：

- 修改业务代码或生产环境
- 改动模型、Provider、账号、凭证或支付设置
- 保存密码、Token、Cookie、订阅链接或机器绑定运行时文件
- 因为“文件较大”就删除有效的安全、验收或权限规则

任何配置变更都应先确认范围、保留可恢复路径，并用实际状态验证结果。

## 项目结构 / Project structure

```text
codex-instruction-auditor/
├── SKILL.md
├── agents/openai.yaml
├── scripts/audit_codex.py
├── references/review-policy.md
├── references/cleanup-checklist.md
├── references/engagement-guide.md
└── README.md
```

- `SKILL.md`：入口规则和工作流
- `scripts/audit_codex.py`：确定性审计脚本
- `references/`：审查标准、清理检查表和中英文说明模板
- `agents/openai.yaml`：Codex UI 元数据

## 验证 / Validation

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py .
python3 scripts/audit_codex.py --root ~/.codex
```

本项目的审计脚本已经在 macOS Codex 环境中验证，能够识别失效 Skill 链接、入口文件规模、frontmatter 和本地 Markdown 引用。

## 来源与实现的关系 / Source and implementation

OpenAI 官方文章提供原则和方向；本仓库提供个人环境中的审计脚本、Skill 入口和检查表。仓库中的实现、README 和验证结果由作者维护，不能代表 OpenAI 的官方支持、承诺或发布计划。

## 作者 / Author

[cliff / yuanyuanyuan430](https://github.com/yuanyuanyuan430) 专注于 Codex、AI Agent 工具、自动化工作流和证据驱动的交付实践。
