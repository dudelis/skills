---
name: tracker-project-close
description: 'Wrap a project in the Tracker system: move its whole folder from Active/ to Closed/, stamp status: closed and closed_date, and append a [manual] closing note. Use for "close Contoso/Data Platform", "wrap this project", or "archive <project>". Confirms before moving. There is no reopen skill — move the folder back manually if needed.'
argument-hint: '<customer>/<project> (e.g. Contoso/Data Platform Migration)'
disable-model-invocation: true
---

# tracker-project-close (write)

Wrap a project: move `Active/ → Closed/` with history intact. See
[../tracker-shared/STORAGE.md](../tracker-shared/STORAGE.md),
[PROJECT-SCHEMA.md](../tracker-shared/PROJECT-SCHEMA.md),
[INVARIANTS.md](../tracker-shared/INVARIANTS.md).

## Procedure

1. **Resolve `<customer>/<project>`** fuzzily; ask if ambiguous.
2. Ask for the **closing reason** (goes into the closing note).
3. **Confirm the move** with the user (show source → destination path).
4. On confirmation, in this order:
   - Stamp `status: closed`, add `closed_date: <today>`, update `last_updated: <today>` in
     `project.md`.
   - **Append a `[manual]` closing note** with the reason to `notes/<today>.md`.
   - **Move the whole folder** `Customers/<Customer>/Active/<Project>/ →
     Customers/<Customer>/Closed/<Project>/` — `project.md`, `notes/`, and `materials/` travel
     together. Perform the OneDrive move directly (versioning is the safety net).

## Guardrails

- The move is per-customer — closing never crosses customer boundaries.
- Confirm before moving. Never move without explicit confirmation.
- **No reopen skill.** Reopening is rare; if needed, tell the user to move the folder back to
  `Active/` manually and run `tracker-project-update` to reset status.
