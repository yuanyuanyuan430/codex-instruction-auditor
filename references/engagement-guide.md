# 说明文案的钩子、反转、高潮与爽点 / Hooks, Reversals, Payoff, and CTA

这份指南是本项目对文档表达方式的补充，不是 OpenAI 官方文章的额外规范。OpenAI 官方文章负责提供工程原则；本指南负责把这些原则讲得更容易理解、更容易被采用。

This guide is an editorial layer added by this project. It is not an additional requirement from OpenAI. The official OpenAI article provides the engineering principles; this guide makes those principles easier to understand and adopt.

## 四段结构 / Four-part structure

### 1. 钩子：先说读者正在承受的代价

不要从“这是一个 Python 脚本”开始。先让读者认出自己的问题：Skill 越装越多、全局规则越来越长、同一个任务被不同提示词反复要求。

Do not begin with “this is a Python script.” Start with the cost the reader already recognizes: more Skills, longer global rules, and repeated instructions for the same task.

可用句式：

- “如果你的 Codex 已经记不住哪些规则真正重要，这个 Skill 会先把它们盘点出来。”
- “When your Codex setup has accumulated more rules than you can explain, start with an inventory instead of another prompt.”

### 2. 反转：拆掉一个常见但危险的直觉

反转要建立在事实或边界上，不靠夸张。这个项目的核心反转是：“清理”不等于“把文件删短”；真正目标是减少噪声，同时保留权限、验证、停止条件和运行时契约。

A reversal should challenge a common assumption without exaggeration. Here the reversal is: cleanup does not mean deleting until files are short; it means reducing noise while keeping permission, verification, stop, and runtime contracts.

可用句式：

- “文件更短，不代表上下文更好；删掉验收标准，反而会让结果更不可靠。”
- “Shorter files are not automatically better context; removing completion criteria can make delivery less reliable.”

### 3. 高潮：给出可验证的转折结果

高潮不是形容词，而是读者可以检查的变化。说明中要把“发现问题 → 做最小修改 → 读取真实状态 → 验证结果”写成一条完整路径。

The payoff is not an adjective. It is a result the reader can check: find the issue, make the smallest change, read the real state, and validate the outcome.

推荐展示：

```text
整理前：<实际扫描得到的失效 Skill 链接数量>
整理后：<重新扫描得到的失效 Skill 链接数量>，入口保留核心契约
```

这是示例格式，不代表新安装环境的固定结果。Use evidence such as file counts, scan output, validation results, and public links. Never invent a before/after number for a new installation.

### 4. 爽点与行动：让读者马上获得一个小胜利

“爽点”在工具文档里应当是低风险、可重复的小胜利：一条只读命令、一份清晰报告、一个可回滚备份，或一个已经公开可访问的示例。最后给出下一步命令，而不是只留下口号。

In technical documentation, the payoff should be a low-risk, repeatable win: a read-only command, a clear report, a recoverable backup, or a public example. End with the next command instead of a slogan.

```text
python3 scripts/audit_codex.py --root ~/.codex
```

## 写作模板 / Reusable template

```markdown
## 你会先看到什么 / What you get first

[钩子] 说明读者遇到的具体混乱。
[反转] 说明为什么“简单删短”不是正确答案。
[高潮] 给出可核验的流程和结果字段。
[爽点] 给出一条只读命令或最小可用示例。
[边界] 明确哪些内容不会自动修改。
[来源] 链接权威文章，并区分来源原则与本项目实现。
```

## 真实性检查 / Truthfulness check

- 钩子描述真实痛点，不制造恐惧或承诺“自动变聪明”。
- 反转必须对应项目中的安全边界或验证规则。
- 高潮必须有文件、命令、扫描结果或链接作为证据。
- 爽点必须能由读者在自己的环境中复现。
- 权威来源、个人实现和当前环境结果分开标注。
- 中英文内容表达相同边界，不用英文夸大中文没有承诺的能力。
