# Tracker

A personal customer/project status tracker. Source of truth is markdown files at the OneDrive
root under `/Tracker/` (top level of OneDrive, **not** inside `Documents/`); skills read and
write them via Microsoft Scout / M365 Copilot (Graph access to mail/Teams/files). See
[tracker-design-brief.md](./tracker-design-brief.md) for the full design.

Shared conventions, schemas, and guardrails live in
[tracker-shared](./tracker-shared/SKILL.md) and are referenced by every skill below.

| Skill | Description |
| ----- | ----------- |
| **[tracker-shared](./tracker-shared/SKILL.md)** | Reference library: storage hierarchy, project/customer schemas, and the read/write safety invariants shared by every tracker skill (not a slash command). |
| **[tracker-status](./tracker-status/SKILL.md)** | Read-only portfolio overview across all customers, grouped and tabular with staleness flags; overwrites `Dashboard/Overview.md`. |
| **[tracker-customer-status](./tracker-customer-status/SKILL.md)** | Read-only, chat-only deep-dive on one customer: header context plus a narrative card per active project with recent notes. |
| **[tracker-sweep](./tracker-sweep/SKILL.md)** | Triage a customer's recent mail/Teams into the notes ledger, one item at a time. Writes notes only — never frontmatter. |
| **[tracker-project-update](./tracker-project-update/SKILL.md)** | The single writer of `project.md` frontmatter: serializes conversation into fields, auto-stamps `last_updated`, appends a `[manual]` note. |
| **[tracker-project-new](./tracker-project-new/SKILL.md)** | Scaffold a new project under an existing customer's `Active/` folder. |
| **[tracker-project-close](./tracker-project-close/SKILL.md)** | Move a project `Active/ → Closed/`, stamp `closed`, append a closing note. |
| **[tracker-customer-new](./tracker-customer-new/SKILL.md)** | Scaffold a new customer with sweep-matching keys (domains, aliases, contacts). |
