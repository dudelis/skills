---
name: to-tickets
description: Break a plan, spec, or conversation into GitHub issues using tracer-bullet vertical slices and explicit blocking edges. Use when the user asks to create implementation tickets, split a spec into issues, or prepare agent-ready GitHub work.
disable-model-invocation: true
---

# To Tickets

Turn the available context into independently implementable GitHub issues. This skill drafts and publishes tickets; it never invokes `implement`.

## Prerequisites

- Work in a Git repository with an authenticated `gh` CLI.
- Read `CONTEXT.md`, `CONTEXT-MAP.md`, and relevant ADRs when present.
- Use only the `ready-for-agent` workflow label.

## Workflow

1. Read the referenced spec, issue body, and comments. Otherwise use the current conversation.
2. Inspect enough of the codebase to use its domain language and identify realistic seams.
3. Draft tracer-bullet slices in dependency order. Each slice must deliver a narrow, complete, independently verifiable behavior through every affected layer.
4. Treat wide mechanical refactors as expand-migrate-contract sequences when no green vertical slice is possible.
5. Present the proposed titles, blockers, and delivered behavior. Revise until the user approves.
6. Show the exact GitHub issues, dependency links or `Blocked by` references, and label operations that will be performed. Ask for one explicit approval covering all remote writes.
7. After approval, create missing `ready-for-agent` label if needed, publish blockers first, and connect dependencies using GitHub's native relationships when available. Otherwise record issue links in `Blocked by`.

Do not publish, edit, label, or close any GitHub issue before approval. Do not modify or close a parent issue. Publishing tickets does not authorize implementation.

## Ticket Template

```markdown
## Parent

<Parent issue link, when one exists>

## What to build

<End-to-end behavior from the user's perspective>

## Acceptance criteria

- [ ] <Observable criterion>

## Blocked by

<Blocking issue links, or "None - can start immediately">
```

Avoid file paths and implementation snippets because they become stale. Include a compact decision-bearing prototype excerpt only when prose would lose essential precision.