---
name: tracker-customer-status
description: 'Deep-dive on a single customer in the Tracker system — a header of context plus one narrative card per active project (full frontmatter + recent notes). Chat-only, writes nothing. Use for "customer status", "show me Contoso", "what is going on with <customer>", or when about to engage a specific customer and needing the full picture.'
argument-hint: '<customer> (e.g. Contoso)'
disable-model-invocation: true
---

# tracker-customer-status (read, chat-only)

Narrative deep-dive on one customer. **Writes nothing** — output is chat only. See
[../tracker-shared/STORAGE.md](../tracker-shared/STORAGE.md),
[PROJECT-SCHEMA.md](../tracker-shared/PROJECT-SCHEMA.md),
[CUSTOMER-SCHEMA.md](../tracker-shared/CUSTOMER-SCHEMA.md).

## Procedure

1. **Resolve `<customer>`** fuzzily against folder names + `customer:` + `aliases:`. If
   ambiguous or not found, ask the user to pick.
2. Read `Customers/<Customer>/customer.md` for the header context (industry, relationship,
   key contact).
3. Glob `Customers/<Customer>/Active/*/project.md` and read each project's frontmatter plus the
   **last 3 `notes/` entries** (default — overridable if the user asks for more).
4. Render a **customer header** then **one card per active project** (shape below).
5. End of each card's activity list: a "…older in `notes/`" pointer if more entries exist.

## Card shape

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

## Guardrails

- Chat-only. Never write to any file. If the user wants to record a change afterward, direct
  them to `tracker-project-update`.
- Omit `Closed/` projects unless the user explicitly asks for them.
