---
name: wayfinder
description: Map a large, uncertain effort as GitHub decision issues and review one frontier decision at a time until the route is clear. Use when work exceeds one agent session, important decisions remain unknown, or the user asks to chart or review an effort.
disable-model-invocation: true
---

# Wayfinder

Wayfinder plans and reviews; it never invokes `implement` or delivers the destination. Each session either charts a map or advances one decision.

Work in a Git repository with an authenticated `gh` CLI. Read-only map review does not authorize remote writes.

## Map Model

The parent GitHub issue is the map and the canonical low-resolution index. Child issues hold individual questions. Use names and links in user-facing text, not bare issue numbers.

The map contains:

- **Destination**: what must be clear when wayfinding is complete.
- **Notes**: domain context, relevant skills, and standing constraints.
- **Decisions so far**: links to resolved questions with one-line outcomes.
- **Not yet specified**: in-scope uncertainty that cannot yet be phrased as a precise question.
- **Out of scope**: explicitly excluded work.

Use no workflow labels other than `ready-for-agent`. An open, unblocked, unassigned child issue is on the frontier; assignment is the claim. Prefer GitHub sub-issues and native dependencies when available, with linked body references as fallback.

## Chart A Map

1. Use `grill-with-docs` to establish the destination and breadth-first frontier.
2. If the entire route is already clear and fits one session, explain that no map is needed and stop.
3. Draft the parent map, currently precise child questions, and dependency operations. Leave uncertain future questions in `Not yet specified`.
4. Show every proposed GitHub write and ask for one explicit approval.
5. After approval, create the map and children, then wire dependencies. Stop without resolving a child.

## Review A Map

1. Load the parent issue and query its open children without eagerly loading every body.
2. Review the destination, resolved decisions, frontier, blockers, and remaining uncertainty.
3. If the user names a child, review that question. Otherwise recommend the first unblocked, unassigned decision and explain why. Do not start it without confirmation.
4. Resolve at most one decision per session using research or `grill-with-docs`; do not implement product work.
5. Draft the resolution, closure, map update, new children, dependency changes, and any scope corrections.
6. Ask for explicit approval before assigning, commenting, closing, creating, or editing anything on GitHub. Apply the approved operations together.

The map is complete when no unresolved decision or meaningful fog remains. Hand the clarified result back to the user; do not transition automatically to `to-spec`, `to-tickets`, or `implement`.