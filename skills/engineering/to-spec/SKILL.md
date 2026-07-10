---
name: to-spec
description: Synthesize the current discussion and codebase context into a specification published as a GitHub issue. Use when the user asks to turn an agreed design, plan, or conversation into a spec or PRD.
disable-model-invocation: true
---

# To Spec

Produce a specification from decisions already made. Do not restart the interview and do not invoke `to-tickets`.

Work in a Git repository with an authenticated `gh` CLI. Read-only GitHub access does not authorize remote writes.

## Workflow

1. Read the current conversation and any referenced GitHub issue, including comments.
2. Inspect the relevant code, `CONTEXT.md` or `CONTEXT-MAP.md`, ADRs, and repository standards.
3. Use `codebase-design` to identify existing or proposed public interfaces. Prefer the highest existing seam and the fewest new seams.
4. Use `tdd` as the testing reference. Record which observable behaviors and seams should be tested, using nearby tests as prior art.
5. Draft the specification below. Resolve contradictions from existing context; ask only when a missing decision prevents an honest spec.
6. Show the complete issue title, body, and proposed `ready-for-agent` label. Ask for explicit approval covering all GitHub writes.
7. After approval, verify authenticated `gh`, create the label if missing, and publish the issue.

Never create, modify, or label a GitHub issue before approval. Publishing the spec does not authorize ticket creation or implementation.

## Specification Template

```markdown
## Problem statement

## Solution

## User stories

1. As a <role>, I want <capability>, so that <benefit>.

## Implementation decisions

## Testing decisions

## Out of scope

## Further notes
```

Keep decisions behavioral and architectural. Avoid file paths and code snippets unless a compact prototype excerpt is the clearest durable expression of a decision.