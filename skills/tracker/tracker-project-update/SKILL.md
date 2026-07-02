---
name: tracker-project-update
description: 'The single writer of project.md frontmatter in the Tracker system. Serializes accumulated conversation (discussion, pulled emails, pasted meeting notes) into a project''s frontmatter, auto-stamps last_updated, and appends a [manual] note recording why. Use for "update Contoso/Data Platform", "set status to blocked", "change next action", or committing a decision reached in chat. Confirms the diff before writing.'
argument-hint: '<customer>/<project> (e.g. Contoso/Data Platform Migration)'
disable-model-invocation: true
---

# tracker-project-update (write: the ONLY frontmatter writer)

Commits decisions from the conversation into a project's source of truth. This is the **only**
skill that writes `project.md` frontmatter (INVARIANT 2). See
[../tracker-shared/PROJECT-SCHEMA.md](../tracker-shared/PROJECT-SCHEMA.md),
[INVARIANTS.md](../tracker-shared/INVARIANTS.md).

## Flow

Converse first → then invoke `tracker-project-update <customer>/<project>` → serialize the
discussion into files. The skill consumes **accumulated conversation context** (discussion,
pulled emails, pasted notes), not just a single blob.

## Procedure

1. **Resolve `<customer>/<project>`** fuzzily; ask if ambiguous.
2. Read the current `project.md` frontmatter.
3. From the conversation, determine which fields to set: `status`, `next_action`,
   `next_action_owner`, `priority`, `key_dates`, `contacts`, `tags`.
   - `status` must be one of the closed-set values — never invent one.
4. **Auto-stamp `last_updated` = today.** Never ask the user to type it.
5. **Show the diff** (old → new for each changed field) and the `[manual]` note you will add.
   **Confirm before writing.**
6. On confirmation:
   - Write the updated frontmatter.
   - **Append a short `[manual]` note** to `notes/<today>.md` recording *why* the change was
     made (INVARIANT 7). Create the day file lazily if needed.

## Guardrails

- Only this skill writes frontmatter. Do not use it to file raw mail/Teams items — that is
  `tracker-sweep`.
- Never set `status: closed` here — use `tracker-project-close` (it also moves the folder).
- Preserve the free-form `## Context` body unless the user asks to edit it.
