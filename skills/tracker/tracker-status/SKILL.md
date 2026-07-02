---
name: tracker-status
description: 'Portfolio overview of all active customer projects in the Tracker system — grouped by customer, tabular, with staleness flags. Reads project.md files and overwrites Dashboard/Overview.md. Use for "tracker status", "portfolio overview", "where am I across all customers", the morning glance, or an end-of-week review. Read-only over source of truth.'
argument-hint: '(no argument — scans the whole portfolio)'
disable-model-invocation: true
---

# tracker-status (read)

Portfolio heartbeat: a single glanceable grid of everything in flight. **Read-only** over the
source of truth. See [../tracker-shared/STORAGE.md](../tracker-shared/STORAGE.md),
[PROJECT-SCHEMA.md](../tracker-shared/PROJECT-SCHEMA.md), and
[INVARIANTS.md](../tracker-shared/INVARIANTS.md).

## Procedure

1. **Glob the hot path only:** `Tracker/Customers/*/Active/*/project.md`. Do **not** open
   `customer.md` or anything under `Closed/`.
2. Parse frontmatter for each project: `project`, `status`, `next_action`, `next_action_owner`,
   `last_updated`, `priority`.
3. **Compute relative age** of `last_updated` against today (e.g. `12d ago`).
4. **Group by customer.** Within each customer, render a table with columns:
   **Initiative/Project · Status · Next action · Owner · Last updated (age) · Priority**.
5. **Staleness is inline annotation + sort key, not a separate nag section:**
   - `owner: me` + old → ⚠️ flag (the user is the blocker).
   - `owner: them` + old → "consider nudging."
   - Sort within a customer so the most stale / highest-priority rows surface first.
6. Print the grouped tables in chat.
7. **Overwrite `Tracker/Dashboard/Overview.md`** with the same tables (mobile-glanceable;
   OneDrive versioning keeps history). This is the only write, and it targets a *derived* file
   — never a `project.md`.

## Guardrails

- Never modify any `project.md`, `notes/`, or `customer.md`.
- Never invent a `status` value; render exactly what the file says.
- If a required field is missing, show it as `—` rather than guessing.
