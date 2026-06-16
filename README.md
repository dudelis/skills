# dudelis-skills

Personal AI skills for [GitHub Copilot CLI](https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli) and [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

## Quickstart

Install all skills with a single command:

```bash
npx skills@latest add dudelis/skills
```

Then run `/skills reload` in your AI tool to pick up the changes.

## Local development (symlinks)

Clone the repo and symlink skills so edits take effect immediately:

```bash
git clone https://github.com/dudelis/skills
bash skills/scripts/link-skills.sh             # links to both tools
bash skills/scripts/link-skills.sh --copilot   # Copilot CLI only
bash skills/scripts/link-skills.sh --claude    # Claude Code only
```

## Skills

### Engineering

Skills for daily code work.

<!-- Add rows as you create skills: | **[name](./skills/engineering/name/SKILL.md)** | description | -->

| Skill | Description |
| ----- | ----------- |
| **[grill-me](./skills/engineering/grill-me/SKILL.md)** | Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. |
| **[grill-with-docs](./skills/engineering/grill-with-docs/SKILL.md)** | Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documentation (CONTEXT.md, ADRs) inline as decisions crystallise. |
| **[to-issues](./skills/engineering/to-issues/SKILL.md)** | Break a plan, spec, or PRD into independently-grabbable issues on the project issue tracker using tracer-bullet vertical slices. |

### Productivity

General workflow tools, not code-specific.

| Skill | Description |
| ----- | ----------- |
| **[write-a-skill](./skills/productivity/write-a-skill/SKILL.md)** | Create new agent skills with proper structure, progressive disclosure, and bundled resources. |
| **[teach-me](./skills/productivity/teach-me/SKILL.md)** | Teach the user a new skill or concept over multiple sessions, with lessons, learning records, and a mission. |

### Misc

Skills kept around but rarely used.

| Skill | Description |
| ----- | ----------- |

## Adding a skill

1. Create `skills/<bucket>/<skill-name>/SKILL.md` with YAML frontmatter (`name`, `description`) and Markdown body.
2. Add a row to `skills/<bucket>/README.md` and to the table above.
3. Add the path to `.claude-plugin/plugin.json`.
4. Run `bash scripts/link-skills.sh` to test locally.

See [CLAUDE.md](./CLAUDE.md) for the full conventions.
