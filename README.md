# Codex Instruction Auditor

一个用于审计和整理 Codex 全局指令、Skills 与提示词入口的 Skill。

它针对一个常见问题：随着模型能力增强，项目里容易积累过长、重复、过宽或相互冲突的 `AGENTS.md`、Skill 描述和任务提示词。这个 Skill 帮助把入口变短、触发条件变清楚，并把低频内容放到按需读取的 references 中。

## 能做什么

- 盘点 `AGENTS.md`、`skills/*/SKILL.md` 和 Skill 符号链接
- 找出失效链接、过长入口、过宽描述和断开的本地引用
- 在编辑前创建备份并记录哈希
- 保留权限边界、验收标准、停止条件、运行时 marker 和 frontmatter
- 通过 Skill 校验和 Codex app-server 扫描验证结果

## 使用

将这个目录放入 Codex 的用户 Skills 目录，然后在整理 Codex 指令时使用：

```text
使用 $codex-instruction-auditor 审计并整理我的 Codex 指令。
```

也可以直接运行只读审计脚本：

```bash
python3 scripts/audit_codex.py --root ~/.codex
```

脚本默认只读取 `AGENTS.md`、`skills` 和 Skill 引用，不读取凭证、数据库、会话、日志或运行时状态。

## 设计原则

- 入口只保留触发条件、核心约束、主流程和完成标准
- 详细流程、示例和诊断资料按需放入 `references/`
- 不因为文件较长就自动删除内容
- 配置、模型、Provider 和凭证变更需要单独授权

## 目录

- `SKILL.md`：入口规则和工作流
- `scripts/audit_codex.py`：确定性审计脚本
- `references/`：审查标准和清理检查表
- `agents/openai.yaml`：Codex UI 元数据

## 验证

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py .
```

## License

本项目按个人用途提供。使用、修改和再分发时请保留来源说明。
