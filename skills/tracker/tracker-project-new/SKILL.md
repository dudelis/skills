---
name: tracker-project-new
description: 'Scaffold a new project in the Tracker system under an existing customer''s Active/ folder. Creates project.md with required frontmatter, an empty Context body, a first [manual] note, and an empty materials/ folder. Use for "new project for Contoso", "add a project", "scaffold <project>", or when tracker-sweep discovers work with no home yet. The customer must already exist.'
argument-hint: '<customer> plus project details (name, next action, owner)'
disable-model-invocation: true
---

# tracker-project-new (write)

Scaffold a new project. The customer **must already exist** — if not, run
`tracker-customer-new` first. See
[../tracker-shared/STORAGE.md](../tracker-shared/STORAGE.md),
[PROJECT-SCHEMA.md](../tracker-shared/PROJECT-SCHEMA.md).

## Procedure

1. **Resolve the customer** fuzzily. If the customer folder does not exist, stop and tell the
   user to run `tracker-customer-new` first.
2. Gather (prompt for, or accept pasted text):
   - **Project name** (becomes the human-readable folder name; spaces allowed).
   - **Required fields:** `status` (default `active`), `next_action`, `next_action_owner`.
   - `priority` (default `normal`). Other optional fields left blank.
3. **Show what will be created and confirm.**
4. Scaffold under `Customers/<Customer>/Active/<Project>/`:
   - `project.md` — required frontmatter + `last_updated` = today + an empty `## Context`.
   - `notes/<today>.md` — first entry: `[manual] Project created`.
   - `materials/` — empty folder.

## Guardrails

- Never create a project outside an existing customer.
- Use the closed-set `status` values; default `active`.
- Auto-stamp `last_updated`; do not ask the user to type a date.
- Half-filled is fine — capture fast, enrich later via `tracker-project-update`.
