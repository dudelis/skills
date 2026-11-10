# Copilot Instructions

This repository stores personal AI skills — reusable, self-contained prompt/instruction sets installed into GitHub Copilot CLI and Claude Code.

## Repository Structure

```
skills/
  blog/           # Technical blog articles and videos (distributed)
  ecommerce/      # Ecommerce product research (distributed)
  engineering/    # Daily code work (distributed)
  productivity/   # Non-code workflow tools (distributed)
  tracker/        # Customer/project status tracker (distributed)
  misc/           # Rarely used (distributed)
  personal/       # Not distributed
  in-progress/    # Drafts — not distributed
  deprecated/     # No longer used — not distributed
scripts/
  install.mjs     # npx installer — copies skills to tool directories
  link-skills.sh  # Local dev — symlinks skills (edits are live)
.claude-plugin/
  marketplace.json  # One plugin per distributed bucket, listing its skill folders
```

## Skill Conventions

- Every skill lives in `skills/<bucket>/<skill-name>/` with a required `SKILL.md`.
- `SKILL.md` frontmatter requires `name` (lowercase, hyphens, must match directory name) and `description` (≤1024 chars, third person, "Use when [triggers]").
- Skills in `blog/`, `ecommerce/`, `engineering/`, `productivity/`, `tracker/`, and `misc/` are distributed and should appear in `README.md` and in `.claude-plugin/marketplace.json`, under the plugin named after their bucket.
- Skills in `personal/`, `in-progress/`, `deprecated/` are never installed, and must not appear in `README.md` or `marketplace.json`.

## Install Destinations

| Tool | Path |
| ---- | ---- |
| GitHub Copilot CLI | `~/.copilot/skills/` |
| Claude Code | `~/.claude/skills/` |

## When Adding a Skill

1. Create `skills/<bucket>/<skill-name>/SKILL.md`.
2. Add row to `skills/<bucket>/README.md`.
3. Add row to top-level `README.md`.
4. Add the skill folder path (`./skills/<bucket>/<skill-name>`) to the `skills` array of the bucket's plugin in `.claude-plugin/marketplace.json` (add a plugin named after the bucket if it has none yet).
5. Run `bash scripts/link-skills.sh` locally to verify.

## Commands

```bash
bash scripts/link-skills.sh        # symlink all skills locally (both tools)
bash scripts/link-skills.sh --copilot  # Copilot CLI only
bash scripts/link-skills.sh --claude   # Claude Code only
npx github:dudelis/skills          # install from GitHub (copies, not symlinks)
```
