# Contributing

Thank you for contributing to this skills repository! Follow these guidelines to keep skills consistent and high quality.

## Adding a New Skill

1. **Create the skill directory:**
   ```
   skills/<skill-name>/
   └── skill.md
   ```

2. **Use the template:** Copy [`templates/skill-template.md`](./templates/skill-template.md) to `skills/<skill-name>/skill.md` and fill it in.

3. **Follow the skill format:**
   - **Description** — One or two sentences summarising the skill.
   - **Instructions** — Numbered steps with clear directives the agent should follow.
   - **Guidelines** — Bullet-point rules that apply throughout the skill.
   - **Out of Scope** — Explicitly list what the skill should NOT do.
   - **Example Usage** — At least one example prompt and expected output.

4. **Update the README:** Add a row to the skills table in [`README.md`](./README.md).

5. **Submit a pull request** with a clear title and description.

## Updating an Existing Skill

- Keep changes focused and explain the reasoning in your pull request.
- Do not rename skills without updating all references (README, any dependent configurations).
- Test the skill against representative prompts before submitting.

## Skill Quality Checklist

Before submitting, verify that your skill:

- [ ] Has a clear, single-sentence description
- [ ] Provides specific, actionable instructions (not vague guidance)
- [ ] Defines what is out of scope to keep the skill focused
- [ ] Includes at least one realistic example with expected output
- [ ] Is free of spelling and grammatical errors
- [ ] Is listed in the README skills table

## Naming Conventions

- Skill directory names: lowercase, hyphen-separated (e.g. `code-review`, `test-generation`)
- Skill file: always named `skill.md` inside the skill directory
- Skill title (H1 in `skill.md`): Title Case, human-readable (e.g. `Code Review`)
