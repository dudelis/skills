# dudelis-skills

Personal AI skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code), Codex, [GitHub Copilot CLI](https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli), and any other agent supported by the [`skills` CLI](https://skills.sh/).

## Install

All commands use the `skills` CLI through `npx` (needs Node.js). `-g` installs for your user instead of the current project.

Pick skills interactively:

```bash
npx skills@latest add dudelis/skills -g
```

The picker groups skills by bucket folder (Blog, Ecommerce, Engineering, Productivity, Tracker). Selecting a group header selects every skill in it.

In the agent prompt, Codex, GitHub Copilot, Cursor, Gemini CLI and the other "universal" agents are always included: they all read the shared `~/.agents/skills` folder. You only pick additional tools with their own folder, such as Claude Code.

To skip the agent prompt, name the tools with `-a`. Naming one universal agent (here `codex`) covers all of them, because they share one folder:

```bash
npx skills@latest add dudelis/skills -g -a claude-code -a codex
```

Install specific skills by repeating `--skill`. Names must match exactly; wildcards such as `shopify-*` are not supported. The CLI has no group flag, so installing only the Ecommerce skills looks like this:

```bash
npx skills@latest add dudelis/skills -g --skill shopify-product-research --skill shopify-product-create --skill shopify-product-update --skill shopify-blog-write --skill shopify-email-write --skill shopify-slideshow-create --skill shopify-company-research --skill shopify-prices-compare
```

Then restart your AI tool or start a new session to pick up the changes. In GitHub Copilot CLI, `/skills reload` loads them without a restart.

## Update

```bash
npx skills@latest update -g   # refresh installed skills to their latest version
npx skills@latest list -g     # show what is installed
```

`update` only refreshes skills you already have. It never installs skills that are new or were renamed in this repo; install those with `add`.

## Renamed skills

The ecommerce skills now start with `shopify-`:

| Old name                   | New name                   |
| -------------------------- | -------------------------- |
| `product-research`         | `shopify-product-research` |
| `product-create-shopify`   | `shopify-product-create`   |
| `product-update-shopify`   | `shopify-product-update`   |
| `blog-write-shopify`       | `shopify-blog-write`       |
| `email-write-shopify`      | `shopify-email-write`      |
| `slideshow-create-shopify` | `shopify-slideshow-create` |
| `company-research`         | `shopify-company-research` |
| `company-compare-prices`   | `shopify-prices-compare`   |

`update` looks up each installed skill by its recorded folder path in this repo, then by name. A renamed skill matches neither, so `update` reports the old names as "deleted upstream". In an interactive terminal it offers to remove them; with `-y` or outside a terminal it skips that step. Either way it never installs the new names. Use `add` for those.

To start clean, remove every skill installed from `dudelis/skills` and install again. Skills from other sources are left alone. Run this from a clone of the repo; it works in bash, zsh, PowerShell, and cmd:

```bash
node scripts/remove-dudelis-skills.mjs --dry-run   # list what would be removed
node scripts/remove-dudelis-skills.mjs && npx skills@latest add dudelis/skills -g
```

[`scripts/remove-dudelis-skills.mjs`](./scripts/remove-dudelis-skills.mjs) reads the CLI's global lock file (`$XDG_STATE_HOME/skills/.skill-lock.json` when `XDG_STATE_HOME` is set, otherwise `~/.agents/.skill-lock.json`), picks the skills whose recorded source is exactly `dudelis/skills`, and removes them from every agent in one `npx skills@latest remove -g -y` call. `&&` runs the reinstall only if the removal succeeded. Windows PowerShell 5.1 has no `&&`: run the removal first, then run `npx skills@latest add dudelis/skills -g` once it succeeds.

Without a clone, run `npx skills@latest remove -g` with no skill names. It opens an interactive picker of every installed skill, from all sources, so tick the old names from the table above yourself. Then run `npx skills@latest add dudelis/skills -g`.

## Local development (symlinks)

Clone the repo and symlink skills so edits take effect immediately:

```bash
git clone https://github.com/dudelis/skills
bash skills/scripts/link-skills.sh             # links to both tools
bash skills/scripts/link-skills.sh --copilot   # Copilot CLI only
bash skills/scripts/link-skills.sh --claude    # Claude Code only
```

## Skills

### Blog

Skills for writing and maintaining Hack the Platform articles.

| Skill | Description |
| ----- | ----------- |
| **[write-blog-article](./skills/blog/write-blog-article/SKILL.md)** | Plans, researches, drafts, illustrates, and revises technical MDX articles in the established Hack the Platform style. |
| **[write-youtube-video](./skills/blog/write-youtube-video/SKILL.md)** | Turns an article or problem description into a recording-ready YouTube script, upload metadata, and thumbnail concept. |

### Ecommerce

Skills for ecommerce research and Shopify content workflows.

| Skill                                                                | Description                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[shopify-product-research](./skills/ecommerce/shopify-product-research/SKILL.md)** | Researches one skincare or dermocosmetics product, compiles a structured YuliSkin brief, and downloads 2 to 5 main product images into the same product folder with sequential names.                                                                      |
| **[shopify-product-create](./skills/ecommerce/shopify-product-create/SKILL.md)** | Creates one new draft Shopify product from a shopify-product-research folder, using German default fields, best-effort English translations, existing metafields, handle generation, sequential product images, and duplicate-stop safety checks. |
| **[shopify-product-update](./skills/ecommerce/shopify-product-update/SKILL.md)** | Updates existing Shopify products from regenerated research files with dry-run diffing, guarded bilingual content updates, and append-only media handling. |
| **[shopify-blog-write](./skills/ecommerce/shopify-blog-write/SKILL.md)** | Prepares complete German/English YuliSkin articles locally, then creates or updates Shopify drafts only after explicit confirmation, using supplied banners and existing associated collections. |
| **[shopify-email-write](./skills/ecommerce/shopify-email-write/SKILL.md)** | Plans German (optionally English) YuliSkin marketing emails with layout variants, subject lines, preview texts, and banner prompts, then writes paste-ready HTML/Liquid blocks for the Shopify Email Custom Liquid section. |
| **[shopify-slideshow-create](./skills/ecommerce/shopify-slideshow-create/SKILL.md)** | Prepares one German/English YuliSkin homepage slide locally in `ys-slides/`: intake, copy, prompts, generated desktop and mobile images, and alt text, with no Shopify writes. |
| **[shopify-company-research](./skills/ecommerce/shopify-company-research/SKILL.md)** | Researches one skincare or dermocosmetics brand, produces a Shopify-ready collection-page brief in German and English, downloads the brand logo, and discovers products from the brand site into a manifest ready for parallel `shopify-product-research` fan-out. |
| **[shopify-prices-compare](./skills/ecommerce/shopify-prices-compare/SKILL.md)** | Monitors one brand across competitor websites, capturing historical prices and promotions into one cumulative CSV file per competitor, compared against distributor recommended prices or YuliSkin.de prices. |

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
3. Add the skill folder path to its bucket's plugin in `.claude-plugin/marketplace.json`.
4. Run `bash scripts/link-skills.sh` to test locally.

See [CLAUDE.md](./CLAUDE.md) for the full conventions.
