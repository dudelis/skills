# Tracker — Customer Schema

## `customer.md` — reference context (NOT scanned daily)

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

## Field notes

- **Required:** `customer`. Everything else is enrichment and can be filled over time.
- **`relationship_status`** closed set: `healthy` | `at-risk` | `strategic`.
- **Sweep-matching keys** (`domains`, `aliases`, `key_contacts`) are how `tracker-sweep`
  builds its Graph query net for mail/Teams. Keep them current for good sweep hit rates.

## How it is used

- Read **only** for enrichment (e.g. pulling a sponsor name into a status card) and to drive
  sweep matching.
- **Never** in the daily scan hot path — `tracker-status` does not open `customer.md`.
