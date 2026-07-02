# Tracker — Storage & Hierarchy

Single dedicated folder at the **OneDrive root**: **`/Tracker/`**.

> **Anchor to the OneDrive root, not `Documents/`.** The folder must live at the top level of
> OneDrive (`/Tracker/`), *not* inside `Documents/` or any other subfolder. When creating or
> resolving the folder via Graph / Scout, use the drive root path (`/Tracker/…` →
> `root:/Tracker/…`). If a `Documents/Tracker/` was created by mistake, move it to the root.

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

## Rules

- **Folder location = scope.** `Active/` vs `Closed/` is the coarse gate. Daily/status scans
  only glob `Tracker/Customers/*/Active/*/project.md`. `customer.md` and everything under
  `Closed/` are **outside the hot path** and are never touched by the daily scan.
- **`status:` field = nuance** within `Active/` (see [PROJECT-SCHEMA.md](./PROJECT-SCHEMA.md)).
- **Per-customer** `Active/`/`Closed/` (not global) — everything about a customer stays
  co-located. Closing a project never crosses customer boundaries.
- **Human-readable folder names** — spaces allowed (e.g. `Data Platform Migration`). No slugs
  to maintain.

## Name resolution (customer / project arguments)

Skills receive names as arguments (e.g. `Contoso/Data Platform Migration`). Resolve them
**case-insensitively and fuzzily** against:

1. Folder names under `Tracker/Customers/`
2. The `customer:` / `project:` frontmatter fields
3. Customer `aliases:` in `customer.md`

**If a name is ambiguous or matches nothing, ask the user to pick** — never guess and act on
the wrong folder. When a customer resolves but the project does not, list that customer's
active projects and ask.

## The hot path vs. cold storage

| Path | Scanned by `tracker-status`? | Read by other skills? |
|------|------------------------------|-----------------------|
| `Customers/*/Active/*/project.md` | Yes (the glob) | Yes |
| `Customers/*/Active/*/notes/` | No | On demand (customer-status, sweep, update) |
| `Customers/*/customer.md` | No | Enrichment + sweep matching only |
| `Customers/*/Closed/**` | No | Only if explicitly asked |
