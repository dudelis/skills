---
name: tracker-shared
description: 'Shared conventions, schemas, and guardrails for the customer/project Tracker system (OneDrive markdown source of truth). Reference library used by every tracker-* skill. Use when working with the Tracker/ folder, project.md or customer.md files, notes ledgers, or any tracker-status / tracker-sweep / tracker-project-* / tracker-customer-* workflow, to understand file structure, the status enum, and the safety model.'
user-invocable: false
---

# Tracker — Shared Conventions

The **Tracker** is a personal system for tracking status across many customers and their
projects. The source of truth is a tree of **markdown files in OneDrive** under a single root
`Tracker/`. There is no git — OneDrive version history is the audit trail and safety net.

Every `tracker-*` skill shares the conventions in this folder. Read the relevant reference
before acting:

| Reference | What it defines |
|-----------|-----------------|
| [STORAGE.md](./STORAGE.md) | Folder hierarchy, `Active/` vs `Closed/` scope, the daily hot path, name resolution |
| [PROJECT-SCHEMA.md](./PROJECT-SCHEMA.md) | `project.md` frontmatter, the `status:` enum, the `notes/` activity ledger |
| [CUSTOMER-SCHEMA.md](./CUSTOMER-SCHEMA.md) | `customer.md` reference context and sweep-matching keys |
| [INVARIANTS.md](./INVARIANTS.md) | The guardrails every skill must obey (read/write safety model) |

## The skill set

| Skill | Arg | Type | Purpose |
|-------|-----|------|---------|
| `tracker-status` | — | read | Portfolio overview across all customers; writes `Dashboard/Overview.md` |
| `tracker-customer-status` | `<customer>` | read | Customer deep-dive, narrative cards (chat-only) |
| `tracker-sweep` | `<customer>` | write (notes only) | Triage mail/Teams for a customer into `notes/` |
| `tracker-project-update` | `<customer>/<project>` | write (frontmatter) | The **only** writer of frontmatter |
| `tracker-project-new` | project data | write | Scaffold a new project |
| `tracker-project-close` | `<customer>/<project>` | write | Move `Active/ → Closed/`, stamp closed |
| `tracker-customer-new` | customer data | write | Scaffold a new customer |

## Non-negotiable safety model

Read → pull mail / discuss in chat → **then** an explicit write skill commits. Nothing is
written to files until the user explicitly invokes a write skill. See [INVARIANTS.md](./INVARIANTS.md)
for the full list. When in doubt, do not write — show the user what you would do and wait.

## Dates

Always use the **actual current date** for `last_updated`, `closed_date`, note filenames, and
relative-age calculations. Never hardcode or guess a date.
