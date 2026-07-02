# Customer/Project Status Tracker — Design Brief

**Purpose:** A personal system to track status across many customers and their projects, so I always know "where am I right now" instead of drowning in email/Teams.

**Tooling:** Microsoft Scout / M365 Copilot only to start (has Graph access to my mail/Teams/files). Fallback later: GitHub Copilot CLI as a second "structure" arm if Scout falls short.

**Source of truth:** Markdown files in OneDrive. No git — OneDrive version history is the safety net/audit trail.

---

## 1. Storage & Hierarchy

Single dedicated folder at the **OneDrive root**: **`/Tracker/`** (top level of OneDrive, **not** inside `Documents/`).

```
/Tracker/
  Dashboard/
    Overview.md                       ← rolling portfolio snapshot (derived, overwritten)
  Customers/
    <Customer>/
      customer.md                     ← general customer info (NOT scanned daily)
      Active/
        <Project>/
          project.md                  ← YAML frontmatter + free markdown body
          notes/
            <YYYY-MM-DD>.md            ← one file per ACTIVE day (created lazily)
          materials/                  ← SOWs, decks, attachments
      Closed/
        <Project>/                    ← wrapped projects (whole folder moved here)
          project.md
          notes/
          materials/
```

**Key rules:**
- **Folder location = scope.** `Active/` vs `Closed/` is the coarse gate. Daily/status scans only glob `Tracker/Customers/*/Active/*/project.md`. `customer.md` and `Closed/` are outside the hot path.
- **`status:` field = nuance** within Active (see enum below).
- **Per-customer** Active/Closed (not global) — everything about a customer stays co-located; closing never crosses customer boundaries.
- **Human-readable folder names** (spaces allowed, e.g. `Data Platform Migration`). Skills resolve args case-insensitively/fuzzily against folder + frontmatter names; **if ambiguous, Scout asks you to pick.** No slugs to maintain.

---

## 2. Schemas

### 2a. `project.md` — YAML frontmatter + free markdown body

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

- **Required fields:** `customer`, `project`, `status`, `next_action`, `next_action_owner`, `last_updated`.
- **Optional:** `priority`, `key_dates`, `contacts`, `tags`. Half-filled files are valid so new projects can be captured fast.
- **`last_updated`** = date of the most recent `notes/` entry OR frontmatter change (last *real activity*). Always auto-stamped by any skill that writes.

### 2b. `status:` enum (closed set — Scout must not invent values)

| Value | Meaning |
|---|---|
| `active` | Moving, I'm working it |
| `blocked` | Stalled on an internal/technical dependency (not the customer) |
| `waiting-on-customer` | Ball's in their court; I'm waiting on their input/sign-off |
| `closed` | Wrapped; set automatically on move to `Closed/` |

No snooze / no `proposed` state. Everything in `Active/` stays visible until explicitly closed.

### 2c. `customer.md` — reference context (NOT scanned daily)

```yaml
---
customer: Contoso
account_owner: me
relationship_status: healthy         # healthy | at-risk | strategic
primary_industry: Manufacturing
# --- sweep matching keys ---
domains: [contoso.com, contoso-eu.com]
aliases: ["Contoso Ltd", "Project Titan"]
key_contacts:
  - name: Jane Doe
    role: CIO
    email: jane@contoso.com
---

## About
Account history, org notes, "how they like to work."
```

Read only for enrichment (e.g. sponsor name) and to drive sweep matching. Never in the daily scan hot path.

### 2d. `notes/` — the activity ledger

- **One file per active day, created lazily.** First update on a day creates `notes/<YYYY-MM-DD>.md`; later updates that day append to it. Idle days get no file — a gap in filenames means nothing happened.
- **Append-only**, reverse-chronological within a file.
- **Source-tagged entries:** `[email]`, `[teams]`, `[meeting]`, `[manual]`.

```markdown
## 2026-07-01 14:30 — [email] Jane Doe re: SOW
Jane approved scope with one change: add phase-2 option.

## 2026-07-01 09:15 — [teams] Delivery standup
Blocker on data access resolved by IT.
```

Notes are how the truth *got here*; `project.md` frontmatter is the *current* truth. If they disagree, **frontmatter wins**.

---

## 3. The Skills (namespace: `tracker-`)

| Skill | Arg | Type | Purpose |
|---|---|---|---|
| `tracker-status` | — | read | Portfolio overview: all customers, grouped, tabular. Writes `Dashboard/Overview.md`. |
| `tracker-customer-status` | `<customer>` | read | Customer deep-dive: narrative cards per project. Chat-only. |
| `tracker-sweep` | `<customer>` | write (notes only) | Triage mail/Teams for the customer → append to `notes/`. |
| `tracker-project-update` | `<customer>/<project>` | write (frontmatter) | **Only** writer of frontmatter. Appends `[manual]` note. |
| `tracker-project-new` | project data provided | write | Scaffold a new project (customer must exist). |
| `tracker-project-close` | `<customer>/<project>` | write | Move `Active/ → Closed/`, stamp closed. |
| `tracker-customer-new` | customer data provided | write | Scaffold a new customer. |

**Core safety model (applies everywhere):** read → pull mail / discuss in chat → *then* an explicit write skill commits. Nothing is written to files until I explicitly invoke a write skill. **Read skills never mutate. `tracker-project-update` is the single writer of the source-of-truth frontmatter.**

### 3a. `tracker-status` (read)
- Globs `Customers/*/Active/*/project.md`.
- Output: **grouped by customer**, tabular. Columns: **Initiative/Project · Status · Next action · Owner · Last updated (with relative age, e.g. `12d ago`) · Priority**.
- Staleness is an **inline annotation + sort key**, not a separate nag section. `owner: me` + old = ⚠️ flag; `owner: them` + old = "consider nudging."
- Also overwrites `Dashboard/Overview.md` with the same table (mobile-glanceable; OneDrive versioning = history).

### 3b. `tracker-customer-status <customer>` (read, chat-only)
- Customer header + short context (from `customer.md`), then one **card per active project**.
- Card = full frontmatter + **last 3 notes entries** (default, overridable) with a "…older in `notes/`" pointer.
- Chat-only; nothing written unless I later say `tracker-project-update`.

Card shape:
```markdown
# Contoso
> Manufacturing · Account: healthy · CIO: Jane Doe (jane@contoso.com)

## Data Platform Migration
**Status:** waiting-on-customer · **Priority:** high · **Last updated:** 2026-07-01 (today)
**Next action:** Send revised SOW draft — *owner: me*
**Key dates:** 2026-07-08 Steering review · 2026-07-15 SOW signature target
**Contacts:** Jane Doe (Sponsor), Bob Smith (Tech lead)
**Recent activity:**
- 2026-07-01 [email] Jane approved scope, wants phase-2 option
- 2026-06-28 [meeting] Kickoff; data access blocker raised
```

### 3c. `tracker-sweep <customer>` (write: notes only — never frontmatter)
- **Customer filter (the net):** uses `customer.md` `domains` / `key_contacts` / `aliases` to query Graph for mail/Teams in a time window.
- **Interactive triage loop, one item at a time.** For each item Scout asks "which project?":
  1. **Assign to existing project** → append `[email]`/`[teams]` note to that project's `notes/<today>.md`.
  2. **Skip/ignore** → nothing written.
  3. **New project** → hand off to `tracker-project-new`, then file there.
  4. **Park for later** → held in an unfiled list; not forced to decide mid-sweep.
- **Sweep NEVER changes status/frontmatter.** It only writes notes. Status changes are always a separate deliberate `tracker-project-update`.
- **Closing summary** at the end: e.g. "filed 4 items across 2 projects, 1 parked, 2 ignored."

### 3d. `tracker-project-update <customer>/<project>` (write: the only frontmatter writer)
- Consumes **accumulated conversation context** (discussion, pulled emails, pasted meeting notes) — not just a single blob. Flow: converse → then say `tracker-project-update Contoso/Data-Platform` → Scout serializes the discussion into files.
- Can set: `status`, `next_action`, `next_action_owner`, `priority`, `key_dates`, `contacts`, `tags`.
- **Always auto-stamps `last_updated`.**
- **Always appends a short `[manual]` note** recording *why* (preserves the "how did it get here" audit trail).
- Confirms the diff before writing.

### 3e. `tracker-project-new` (write)
- Requires the customer to already exist (create via `tracker-customer-new` first).
- Prompts for / accepts pasted text to fill: project name + required fields (`status` default `active`, `next_action`, `next_action_owner`, `priority` default `normal`). Optional fields left blank.
- Scaffolds `Active/<Project>/project.md` (+ empty `## Context`), `notes/<today>.md` (first `[manual]` "Project created" entry), and empty `materials/`.

### 3f. `tracker-project-close <customer>/<project>` (write)
- Moves the whole folder `Active/<Project>/ → Closed/<Project>/` (project.md, notes/, materials/ travel together, history intact).
- Stamps `status: closed`, adds `closed_date: <today>`, auto-updates `last_updated`.
- Appends a `[manual]` closing note with the reason.
- Confirms before moving. Scout performs the OneDrive move directly (OneDrive versioning = safety net).
- **No reopen skill** — rare; move the folder back manually if it happens.

### 3g. `tracker-customer-new` (write)
- Focused flow to scaffold `Customers/<Customer>/customer.md` + empty `Active/` and `Closed/`.
- Captures sweep-matching keys: `domains`, `aliases`, `key_contacts`.

---

## 4. Usage Rhythm (manual — nothing automated yet)

Suggested ritual, not enforced by the system:
- **Morning (~2 min):** `tracker-status` — glance at the grid; spot owner=me and stale items.
- **Ad-hoc during the day:** `tracker-project-update` at the moment of a decision; `tracker-customer-status` when working a customer.
- **Per customer, as needed:** `tracker-sweep <customer>` before engaging that customer / when you suspect mail moved something. **Not** a blanket daily sweep of everyone.
- **End of week (~5 min):** `tracker-status`, sweep the 2–3 hottest customers, close anything wrapped.

Heartbeat = `tracker-status` (cheap, read-only, frequent). Targeted = `tracker-sweep` (per-customer). Writes = at the moment of decision. **No scheduling/automation for now.**

---

## 5. Key Invariants (the design's guardrails)

1. **Folder location is scope; `status` is nuance.**
2. **Single writer of frontmatter:** only `tracker-project-update` (and `-new`/`-close` for their scaffolding/stamping). `tracker-sweep` writes notes only.
3. **Read skills never mutate.** "Show me status" is always safe.
4. **Nothing written until an explicit write-skill invocation.** Discuss first, commit deliberately.
5. **`project.md` frontmatter wins** over any derived view (`Overview.md`) or notes.
6. **`last_updated` is always automatic**, reflecting real activity.
7. **Every frontmatter change leaves a `[manual]` note** explaining why.
8. **Notes are append-only, source-tagged, one lazily-created file per active day.**
