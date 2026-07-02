---
name: tracker-customer-new
description: 'Scaffold a new customer in the Tracker system: create Customers/<Customer>/customer.md plus empty Active/ and Closed/ folders. Captures sweep-matching keys (domains, aliases, key_contacts) so tracker-sweep can find their mail/Teams. Use for "new customer", "add customer Contoso", or before creating the customer''s first project.'
argument-hint: '<customer> plus context (industry, domains, key contacts)'
disable-model-invocation: true
---

# tracker-customer-new (write)

Scaffold a new customer. See
[../tracker-shared/STORAGE.md](../tracker-shared/STORAGE.md),
[CUSTOMER-SCHEMA.md](../tracker-shared/CUSTOMER-SCHEMA.md).

## Procedure

1. Confirm the customer does not already exist (fuzzy check against folders + `aliases:`).
2. Gather (prompt for, or accept pasted text):
   - **Customer name** (human-readable folder name).
   - `account_owner` (default `me`), `relationship_status`, `primary_industry`.
   - **Sweep-matching keys:** `domains`, `aliases`, `key_contacts` — capture these well; they
     drive `tracker-sweep`'s Graph query.
3. **Show what will be created and confirm.**
4. Scaffold under `Customers/<Customer>/`:
   - `customer.md` — frontmatter + an `## About` body (can be brief).
   - `Active/` — empty.
   - `Closed/` — empty.

## Guardrails

- Only scaffolds the customer shell — creating projects is `tracker-project-new`.
- `customer.md` is reference context, never in the daily scan hot path.
- Half-filled is fine; enrich `domains`/`aliases` later to improve sweep hit rates.
