# Code Review

## Description

Performs thorough code reviews focusing on correctness, bugs, security vulnerabilities, performance issues, and maintainability. Surfaces only actionable issues with clear explanations and suggested fixes.

## Instructions

When performing a code review:

1. **Understand context** — Read the diff or changed files in full before commenting. Understand the intent of the change.
2. **Identify real issues** — Focus on bugs, logic errors, security vulnerabilities, performance problems, and API misuse. Do not comment on style or formatting unless it causes a functional issue.
3. **Explain clearly** — For each issue found, explain what the problem is, why it matters, and how to fix it with a concrete code example when helpful.
4. **Prioritize severity** — Label each finding as `critical`, `high`, `medium`, or `low` based on its potential impact.
5. **Acknowledge strengths** — Briefly note what the change does well before listing issues, to provide balanced feedback.

### Guidelines

- Always provide a suggested fix alongside each issue, not just a description of the problem.
- Group related findings together rather than listing them item by item across the same file.
- Consider the broader codebase context — a change that looks wrong in isolation may be intentional.
- Check for: null/undefined dereferences, off-by-one errors, incorrect error handling, hardcoded credentials, injection vulnerabilities, race conditions, and missing input validation.

### Out of Scope

- Do not flag style issues such as indentation, spacing, or naming conventions (unless they violate a documented project standard).
- Do not suggest refactoring unrelated to the changed code.
- Do not rewrite entire functions when a small targeted fix is sufficient.

## Example Usage

**Prompt:**
> Review the changes in this pull request for bugs and security issues.

**Expected output:**
> **Summary:** The change adds a new user authentication endpoint. The logic is sound overall, but there are two findings:
>
> **[high] Missing input validation on `username` parameter** — The `username` value is passed directly to the database query without sanitization, which could allow SQL injection. Sanitize or use a parameterized query:
> ```python
> cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
> ```
>
> **[low] Unnecessary logging of sensitive data** — Line 42 logs the full request body which may contain passwords. Remove or redact sensitive fields before logging.
