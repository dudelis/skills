# Skills Repository

A collection of reusable skills for AI tools (GitHub Copilot, coding agents, etc.) that can be applied across multiple projects.

## What are Skills?

Skills are reusable instruction sets for AI agents. Each skill provides focused guidance for a specific task, such as reviewing code, generating tests, or writing documentation. They can be referenced in AI tool configurations to customize agent behavior.

## Available Skills

| Skill | Description |
|-------|-------------|
| [Code Review](./skills/code-review/skill.md) | Performs thorough code reviews focusing on bugs, security, and maintainability |
| [Test Generation](./skills/test-generation/skill.md) | Generates comprehensive unit and integration tests for existing code |
| [Documentation](./skills/documentation/skill.md) | Writes and improves code documentation, comments, and READMEs |
| [Security Review](./skills/security-review/skill.md) | Identifies security vulnerabilities and suggests remediations |
| [Refactoring](./skills/refactoring/skill.md) | Suggests and applies code refactoring to improve readability and structure |

## Usage

### GitHub Copilot Coding Agent

Reference a skill in your repository's `.github/copilot-instructions.md` or in the `available_skills` configuration:

```xml
<available_skills>
  <skill>
    <name>code-review</name>
    <description>Performs thorough code reviews focusing on bugs, security, and maintainability</description>
    <location>https://raw.githubusercontent.com/dudelis/skills/main/skills/code-review/skill.md</location>
  </skill>
</available_skills>
```

### Direct Reference

Copy or link the skill file content directly into your project's AI tool configuration.

## Adding a New Skill

1. Copy the [skill template](./templates/skill-template.md) to `skills/<skill-name>/skill.md`
2. Fill in the template with the skill's instructions
3. Add an entry to the table above in this README
4. Submit a pull request

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidelines.
