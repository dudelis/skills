---
name: tracker-sweep
description: 'Triage a customer''s recent mail and Teams activity into the Tracker notes ledger. Uses customer.md domains/aliases/contacts to query Graph, then walks items one at a time asking which project each belongs to. Writes notes only — never frontmatter or status. Use for "sweep Contoso", "triage my mail for <customer>", or before engaging a customer when mail may have moved something.'
argument-hint: '<customer> (e.g. Contoso)'
disable-model-invocation: true
---

# tracker-sweep (write: notes only)

Triage mail/Teams for one customer into `notes/`. **Never touches frontmatter or status** —
that is `tracker-project-update`'s job (INVARIANT 2). See
[../tracker-shared/CUSTOMER-SCHEMA.md](../tracker-shared/CUSTOMER-SCHEMA.md),
[PROJECT-SCHEMA.md](../tracker-shared/PROJECT-SCHEMA.md),
[INVARIANTS.md](../tracker-shared/INVARIANTS.md).

## Procedure

1. **Resolve `<customer>`** fuzzily; ask if ambiguous.
2. **Build the net:** read `customer.md` `domains`, `key_contacts`, `aliases`. Query Graph for
   mail + Teams messages matching those in a time window (default: since the customer's most
   recent note; confirm the window with the user).
3. **Interactive triage loop — one item at a time.** For each item summarise it, then ask
   "which project?":
   - **Assign to existing project** → append an `[email]` / `[teams]` entry to that project's
     `notes/<today>.md` (create the file lazily if it is the first entry today; prepend within
     the day, newest at top).
   - **Skip / ignore** → write nothing.
   - **New project** → hand off to `tracker-project-new`, then file the note there.
   - **Park for later** → hold in an in-memory unfiled list; do not force a decision.
4. **Closing summary:** e.g. "filed 4 items across 2 projects, 1 parked, 2 ignored." List the
   parked items so the user can decide later.

## Guardrails

- **Notes only.** Never change `status`, `next_action`, `priority`, or any frontmatter field.
  If triage reveals a status change is needed, note it and tell the user to run
  `tracker-project-update`.
- Append-only, source-tagged entries. Never rewrite existing notes.
- Do not auto-file ambiguous items — ask.
