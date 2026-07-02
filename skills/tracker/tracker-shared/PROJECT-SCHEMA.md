# Tracker — Project Schema

## `project.md` — YAML frontmatter + free markdown body

```yaml
---
customer: Contoso
project: Data Platform Migration
status: waiting-on-customer          # active | blocked | waiting-on-customer | closed
next_action: "Send revised SOW draft"
next_action_owner: me                # me | them
last_updated: 2026-07-01             # AUTO-stamped, never hand-entered
# --- optional (enriched over time) ---
priority: high                       # high | normal | low
key_dates:
  - 2026-07-08: Steering committee review
  - 2026-07-15: SOW signature target
contacts:
  - name: Jane Doe
    role: Sponsor
    email: jane@contoso.com
tags: [delivery]                     # e.g. presales, delivery, escalation
closed_date: 2026-07-15              # stamped only on close
---

## Context
Free-form markdown: history, thinking, decisions.
```

- **Required fields:** `customer`, `project`, `status`, `next_action`, `next_action_owner`,
  `last_updated`.
- **Optional:** `priority`, `key_dates`, `contacts`, `tags`, `closed_date`. Half-filled files
  are valid — new projects can be captured fast.
- **`last_updated`** = date of the most recent `notes/` entry OR frontmatter change (the last
  *real activity*). Always auto-stamped by any skill that writes. Never hand-entered.

## `status:` enum — CLOSED SET (never invent values)

| Value | Meaning |
|-------|---------|
| `active` | Moving; the user is working it |
| `blocked` | Stalled on an internal/technical dependency (not the customer) |
| `waiting-on-customer` | Ball is in their court; waiting on their input/sign-off |
| `closed` | Wrapped; set automatically on move to `Closed/` |

No snooze, no `proposed` state. Everything in `Active/` stays visible until explicitly closed.

## `notes/` — the activity ledger

- **One file per active day, created lazily.** The first update on a day creates
  `notes/<YYYY-MM-DD>.md`; later updates that day **append** to it. Idle days get no file — a
  gap in filenames means nothing happened.
- **Append-only**, reverse-chronological within a file (newest entry at top).
- **Source-tagged entries:** `[email]`, `[teams]`, `[meeting]`, `[manual]`.

```markdown
## 2026-07-01 14:30 — [email] Jane Doe re: SOW
Jane approved scope with one change: add phase-2 option.

## 2026-07-01 09:15 — [teams] Delivery standup
Blocker on data access resolved by IT.
```

Notes are how the truth *got here*; `project.md` frontmatter is the *current* truth. **If they
disagree, frontmatter wins.**
