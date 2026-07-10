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

### Ecommerce

Skills for ecommerce product research workflows.

| Skill                                                                | Description                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[product-research](./skills/ecommerce/product-research/SKILL.md)** | Researches one skincare or dermocosmetics product, compiles a structured YuliSkin brief, and downloads 2 to 5 main product images into the same product folder with sequential names.                                                                      |
| **[product-create-shopify](./skills/ecommerce/product-create-shopify/SKILL.md)** | Creates one new draft Shopify product from a product-research folder, using German default fields, best-effort English translations, existing metafields, handle generation, sequential product images, and duplicate-stop safety checks. |
| **[product-update-shopify](./skills/ecommerce/product-update-shopify/SKILL.md)** | Updates existing Shopify products from regenerated research files with dry-run diffing, guarded bilingual content updates, and append-only media handling. |
| **[company-research](./skills/ecommerce/company-research/SKILL.md)** | Researches one skincare or dermocosmetics brand, produces a Shopify-ready collection-page brief in German and English, downloads the brand logo, and discovers products from the brand site into a manifest ready for parallel `product-research` fan-out. |

### Engineering

Skills for daily code work.

<!-- Add rows as you create skills: | **[name](./skills/engineering/name/SKILL.md)** | description | -->

| Skill                                                                | Description                                                                                                                                                                       |
| -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[codebase-design](./skills/engineering/codebase-design/SKILL.md)** | Guide architecture toward deep modules, stable interfaces, explicit seams, and local knowledge.                                                                                  |
| **[code-review](./skills/engineering/code-review/SKILL.md)**         | Review committed or uncommitted changes independently against repository standards and the originating specification.                                                           |
| **[grill-me](./skills/engineering/grill-me/SKILL.md)**               | Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree.                                           |
| **[grill-with-docs](./skills/engineering/grill-with-docs/SKILL.md)** | Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documentation (CONTEXT.md, ADRs) inline as decisions crystallise. |
| **[implement](./skills/engineering/implement/SKILL.md)**             | Implement explicit work locally with focused validation, TDD where appropriate, and final code review, leaving changes uncommitted.                                             |
| **[tdd](./skills/engineering/tdd/SKILL.md)**                         | Apply test-driven development through agreed public seams using small red-green cycles.                                                                                           |
| **[to-spec](./skills/engineering/to-spec/SKILL.md)**                 | Synthesize an agreed discussion and codebase context into a specification published as a GitHub issue.                                                                           |
| **[to-tickets](./skills/engineering/to-tickets/SKILL.md)**           | Break a plan or spec into GitHub issues using tracer-bullet vertical slices and explicit blocking edges.                                                                          |
| **[wayfinder](./skills/engineering/wayfinder/SKILL.md)**             | Map a large uncertain effort as GitHub decision issues and review one frontier decision at a time.                                                                                |

The engineering workflow is explicitly driven: `grill-with-docs` → `to-spec` → `to-tickets` → `implement`. Use `wayfinder` for large uncertain efforts; `codebase-design`, `tdd`, and `code-review` are reusable supporting skills. No stage automatically invokes the next.

### Productivity

General workflow tools, not code-specific.

| Skill                                                             | Description                                                                                                  |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **[write-a-skill](./skills/productivity/write-a-skill/SKILL.md)** | Create new agent skills with proper structure, progressive disclosure, and bundled resources.                |
| **[teach-me](./skills/productivity/teach-me/SKILL.md)**           | Teach the user a new skill or concept over multiple sessions, with lessons, learning records, and a mission. |

### Misc

Skills kept around but rarely used.

| Skill | Description |
| ----- | ----------- |

### Tracker

A personal customer/project status tracker over markdown files in OneDrive, driven by Microsoft Scout / M365 Copilot. See [skills/tracker/README.md](./skills/tracker/README.md) and the [design brief](./skills/tracker/tracker-design-brief.md).

| Skill | Description |
| ----- | ----------- |
| **[tracker-shared](./skills/tracker/tracker-shared/SKILL.md)** | Reference library: storage hierarchy, project/customer schemas, and safety invariants shared by every tracker skill (not a slash command). |
| **[tracker-status](./skills/tracker/tracker-status/SKILL.md)** | Read-only portfolio overview across all customers; overwrites `Dashboard/Overview.md`. |
| **[tracker-customer-status](./skills/tracker/tracker-customer-status/SKILL.md)** | Read-only, chat-only deep-dive on one customer with a card per active project. |
| **[tracker-sweep](./skills/tracker/tracker-sweep/SKILL.md)** | Triage a customer's mail/Teams into the notes ledger. Writes notes only. |
| **[tracker-project-update](./skills/tracker/tracker-project-update/SKILL.md)** | The single writer of `project.md` frontmatter; auto-stamps and adds a `[manual]` note. |
| **[tracker-project-new](./skills/tracker/tracker-project-new/SKILL.md)** | Scaffold a new project under an existing customer. |
| **[tracker-project-close](./skills/tracker/tracker-project-close/SKILL.md)** | Move a project `Active/ → Closed/` and stamp it closed. |
| **[tracker-customer-new](./skills/tracker/tracker-customer-new/SKILL.md)** | Scaffold a new customer with sweep-matching keys. |

## Adding a skill

1. Create `skills/<bucket>/<skill-name>/SKILL.md` with YAML frontmatter (`name`, `description`) and Markdown body.
2. Add a row to `skills/<bucket>/README.md` and to the table above.
3. Add the path to `.claude-plugin/plugin.json`.
4. Run `bash scripts/link-skills.sh` to test locally.

See [CLAUDE.md](./CLAUDE.md) for the full conventions.
