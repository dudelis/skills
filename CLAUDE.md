Skills are organized into bucket folders under `skills/`:

- `engineering/` — daily code work
- `productivity/` — daily non-code workflow tools
- `misc/` — kept around but rarely used
- `personal/` — tied to my own setup, not promoted
- `in-progress/` — drafts not yet ready to ship
- `deprecated/` — no longer used

Every skill in `engineering/`, `productivity/`, or `misc/` must have a reference in the top-level `README.md` and an entry in `.claude-plugin/plugin.json`. Skills in `personal/`, `in-progress/`, and `deprecated/` must not appear in either.

Each bucket folder has a `README.md` that lists every skill in the bucket with a one-line description, with the skill name linked to its `SKILL.md`.

## Skill structure

```
skills/<bucket>/<skill-name>/
├── SKILL.md        # Required. YAML frontmatter + Markdown body.
├── REFERENCE.md    # Optional. Long-form docs linked from SKILL.md.
├── EXAMPLES.md     # Optional. Usage examples.
└── scripts/        # Optional. Helper scripts referenced by SKILL.md.
```

## SKILL.md frontmatter

```yaml
---
name: skill-name          # lowercase, hyphens, matches directory name
description: >            # max 1024 chars; third person; "Use when [triggers]"
  What the skill does. Use when [specific keywords or context].
---
```

## Adding a skill checklist

- [ ] Create `skills/<bucket>/<skill-name>/SKILL.md`
- [ ] Add a row to `skills/<bucket>/README.md`
- [ ] Add the path to `README.md` (top-level reference table)
- [ ] Add the path to `.claude-plugin/plugin.json` `skills` array
- [ ] Run `bash scripts/link-skills.sh` locally to verify it links correctly
