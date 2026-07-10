---
name: code-review
description: Review committed or uncommitted changes against repository standards and the originating specification. Use when the user requests a code review, wants changes checked since a fixed point, or when an implementation workflow needs a final independent review.
---

# Code Review

Review without editing. Keep standards and specification conformance as separate axes so one cannot hide failures in the other.

Work in a Git repository. Use an authenticated `gh` CLI when the specification source is a GitHub issue.

## Establish The Change Set

Use the fixed point supplied by the caller. For uncommitted implementation work, include staged and unstaged changes and use the implementation session's recorded baseline to distinguish pre-existing edits. If no defensible change set can be identified, ask for a commit, branch, tag, or explicit file scope.

Confirm the reference resolves and the resulting change set is non-empty before reviewing.

## Gather Sources

- Find the originating GitHub issue, spec, or PRD. Ask if none can be identified.
- Read repository instructions, coding standards, context documents, and relevant ADRs.
- Ignore concerns already enforced by successful automated tooling unless the tool output itself shows a failure.

## Review In Two Independent Axes

Run both reviews independently, in parallel when subagents are available:

1. **Standards**: identify concrete repository-rule violations and well-supported maintainability risks. Use `codebase-design` for architectural concerns. Distinguish hard violations from judgment calls.
2. **Spec**: identify missing or partial requirements, incorrect behavior, and unrequested scope. Tie each finding to the source requirement.

Report findings first, ordered by severity within each axis, with file and line references plus a concrete remedy. Do not modify files, rerank across axes, or close/update GitHub issues.

## Output

```markdown
## Standards

<Findings or "No findings.">

## Spec

<Findings or "No findings.">

## Validation gaps

<Checks that could not be performed and residual risk.>
```