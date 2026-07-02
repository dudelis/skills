# Tracker — Invariants (the guardrails)

Every `tracker-*` skill must obey these. They are the design's safety model.

1. **Folder location is scope; `status` is nuance.** `Active/` vs `Closed/` is the coarse gate;
   the `status:` enum expresses nuance within `Active/`.

2. **Single writer of frontmatter:** only `tracker-project-update` writes `project.md`
   frontmatter (and `tracker-project-new` / `tracker-project-close` for their scaffolding and
   stamping). **`tracker-sweep` writes notes only — never frontmatter.**

3. **Read skills never mutate.** `tracker-status` and `tracker-customer-status` are always
   safe. "Show me status" must never change a file. (The one exception: `tracker-status`
   overwrites the derived `Dashboard/Overview.md`, which is not source of truth.)

4. **Nothing is written until an explicit write-skill invocation.** Discuss first, commit
   deliberately. Never pre-emptively write files because it "seems helpful."

5. **`project.md` frontmatter wins** over any derived view (`Overview.md`) or `notes/` entry
   when they disagree.

6. **`last_updated` is always automatic**, reflecting real activity (latest note or frontmatter
   change). Never hand-entered.

7. **Every frontmatter change leaves a `[manual]` note** explaining *why* — preserves the
   "how did it get here" audit trail.

8. **Notes are append-only, source-tagged, one lazily-created file per active day.** Never
   rewrite or delete existing note entries.

## Confirm-before-write

Write skills (`-update`, `-new`, `-close`) **show the diff / planned change and confirm with
the user before committing**. Moves (`-close`) confirm before moving the folder. OneDrive
version history is the safety net, not a licence to write carelessly.
