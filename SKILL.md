---
name: codex-instruction-auditor
description: Audit and safely streamline Codex global instructions, Skills, and prompt surfaces when asked to organize Codex; preserve runtime contracts, safety boundaries, and task completion criteria.
metadata:
  short-description: Audit and streamline Codex instructions
---

# Codex instruction auditor

Use this skill when the user asks to clean up, organize, shorten, or review Codex instructions. The goal is smaller, more precise context without deleting behavior that protects permissions, verification, delivery, or runtime operation.

## Scope

- Inspect the user-maintained `AGENTS.md`, `skills/*/SKILL.md`, and, when useful, prompt/agent metadata.
- Treat `config.toml`, credentials, databases, sessions, logs, and runtime state as out of scope unless the user explicitly asks for them.
- Preserve managed markers, frontmatter, invocation policy, working references, and model/permission boundaries.

## Workflow

1. Run `scripts/audit_codex.py --root <codex-root>` to make a compact inventory and candidate list.
2. Classify findings as stale, duplicate, over-broad trigger, unconditional detail, or required contract. Do not rewrite solely because a file is long.
3. Before edits, create a timestamped, non-overwriting backup and record hashes. Stop the affected slice if a source changed concurrently.
4. Keep entrypoints short and route conditional detail to existing references. Remove repetition only when the preserved behavior is clear.
5. Validate frontmatter, references, markers, and the actual Codex skill scan. Report changed files, checks, and any untouched risk.

For detailed review criteria, read [references/review-policy.md](references/review-policy.md). For the edit and verification checklist, read [references/cleanup-checklist.md](references/cleanup-checklist.md).

Do not claim that a saved configuration is active without runtime readback. Do not change model, provider, account, credential, or production settings as part of an instruction cleanup unless that change is separately requested.
