#!/usr/bin/env python3
"""Inventory Codex instruction surfaces without reading secrets or runtime state."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def frontmatter(text: str) -> tuple[str | None, str | None]:
    if not text.startswith("---"):
        return None, None
    block = text.split("---", 2)
    if len(block) < 3:
        return None, None
    name = re.search(r"^name:\s*([^\n]+)", block[1], re.M)
    desc = re.search(r"^description:\s*(.+)", block[1], re.M)
    return (name.group(1).strip() if name else None, desc.group(1).strip() if desc else None)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.home() / ".codex")
    args = parser.parse_args()
    root = args.root.expanduser().resolve()

    agents = root / "AGENTS.md"
    skills_root = root / "skills"
    entries = []
    for entry in sorted(skills_root.iterdir()) if skills_root.exists() else []:
        if not entry.is_symlink() and not entry.is_dir():
            continue
        target = entry.resolve(strict=False)
        skill_file = entry / "SKILL.md"
        broken = entry.is_symlink() and not target.exists()
        if not skill_file.exists():
            entries.append({"path": str(entry), "symlink": entry.is_symlink(), "broken": broken, "has_skill": False})
            continue
        text = skill_file.read_text(encoding="utf-8", errors="replace")
        name, desc = frontmatter(text)
        rel_refs = sorted(set(re.findall(r"\]\(([^)]+\.md)(?:#[^)]+)?\)", text)))
        missing = [ref for ref in rel_refs if not ref.startswith(("http://", "https://", "/")) and not (skill_file.parent / ref).exists()]
        entries.append(
            {
                "path": str(skill_file),
                "symlink": entry.is_symlink(),
                "broken": broken,
                "has_skill": True,
                "bytes": len(text.encode("utf-8")),
                "lines": text.count("\n") + 1,
                "name": name,
                "description_chars": len(desc or ""),
                "references": len(rel_refs),
                "missing_references": missing,
                "candidates": [
                    reason
                    for reason, condition in (
                        ("large_entrypoint", len(text) > 12000),
                        ("long_description", len(desc or "") > 240),
                        ("missing_frontmatter", name is None or desc is None),
                        ("broken_reference", bool(missing)),
                    )
                    if condition
                ],
            }
        )

    report = {
        "root": str(root),
        "scope": ["AGENTS.md", "skills/*/SKILL.md", "skill symlinks"],
        "excluded": ["config.toml", "credentials", "databases", "sessions", "logs", "runtime state"],
        "agents": {
            "exists": agents.exists(),
            "bytes": agents.stat().st_size if agents.exists() else 0,
            "lines": agents.read_text(encoding="utf-8", errors="replace").count("\n") + 1 if agents.exists() else 0,
        },
        "skill_entries": len(entries),
        "broken_symlinks": sum(e.get("broken", False) for e in entries),
        "skill_files": sum(e.get("has_skill", False) for e in entries),
        "candidates": sum(bool(e.get("candidates")) for e in entries),
        "entries": entries,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
