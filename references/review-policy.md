# Review policy

Judge an instruction surface by whether it changes decisions for the requests it actually serves.

- Keep a description when it has a precise trigger and a distinct capability. Narrow broad triggers such as “anything about databases” to the concrete workflow, such as “adding, changing, or reviewing a migration.”
- Keep safety, authorization, acceptance evidence, stop conditions, output requirements, and non-obvious operational invariants even when shortening prose.
- Move mode-specific procedures, schemas, examples, and provider details to references. Link them from the entrypoint and load them only for the matching mode.
- Remove repeated generic advice, stale model-specific handholding, and unconditional “read every document” rules when task-scoped routing preserves the same outcome.
- Treat runtime overlays and generated markers as contracts. Do not flatten or regenerate them casually.
- A long file is a candidate, not proof of a problem. Prefer evidence from overlap, contradiction, unconditional loading, or an over-broad trigger.
