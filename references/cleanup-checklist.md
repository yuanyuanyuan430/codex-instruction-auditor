# Cleanup checklist

Before editing:

- Confirm the target is user-maintained and outside secrets/runtime databases.
- Record file hashes and make a timestamped non-overwriting backup.
- Check for concurrent writers or managed marker blocks.

After editing:

- Parse YAML frontmatter and verify lowercase skill names, descriptions, and preserved metadata.
- Resolve relative Markdown links from every changed skill.
- Check that required managed markers still occur in the same logical sections.
- Run the Codex skill scan or app-server `skills/list` when available.
- Re-read the changed files and report exact scope, validation evidence, and remaining limits.
