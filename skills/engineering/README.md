# Engineering Skills

Skills for daily code work.

| Skill | Description |
| ----- | ----------- |
| [codebase-design](codebase-design/SKILL.md) | Guide architecture toward deep modules, stable interfaces, explicit seams, and local knowledge. |
| [code-review](code-review/SKILL.md) | Review committed or uncommitted changes independently against repository standards and the originating specification. |
| [grill-me](grill-me/SKILL.md) | Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. |
| [grill-with-docs](grill-with-docs/SKILL.md) | Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documentation (CONTEXT.md, ADRs) inline as decisions crystallise. |
| [implement](implement/SKILL.md) | Implement explicit work locally with focused validation, TDD where appropriate, and final code review, leaving changes uncommitted. |
| [tdd](tdd/SKILL.md) | Apply test-driven development through agreed public seams using small red-green cycles. |
| [to-spec](to-spec/SKILL.md) | Synthesize an agreed discussion and codebase context into a specification published as a GitHub issue. |
| [to-tickets](to-tickets/SKILL.md) | Break a plan or spec into GitHub issues using tracer-bullet vertical slices and explicit blocking edges. |
| [wayfinder](wayfinder/SKILL.md) | Map a large uncertain effort as GitHub decision issues and review one frontier decision at a time. |

## Workflow

The usual sequence is `grill-with-docs` → `to-spec` → `to-tickets` → `implement`. Each stage is invoked explicitly; no skill automatically advances to the next one. Use `wayfinder` separately when an effort is too uncertain or too large for one agent session.

`codebase-design`, `tdd`, and `code-review` are reusable supporting skills. They can be invoked directly and may be consulted by the explicit workflow skills. GitHub writes require approval, and `implement` leaves code changes uncommitted and issues open for manual validation.
