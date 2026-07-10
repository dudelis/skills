---
name: tdd
description: Apply test-driven development through agreed public seams using small red-green cycles. Use when implementing features or fixes test-first, choosing behavioral tests, or when the user mentions TDD, red-green, or integration tests.
---

# Test-Driven Development

Tests specify observable behavior through public interfaces. They should survive internal refactoring.

## Before The Loop

1. Read relevant context documents, ADRs, standards, and nearby tests.
2. Use `codebase-design` to identify the public seam where behavior is observable.
3. Record the seams under test. Reuse seams approved in the source spec; otherwise confirm new seams with the user before writing tests.
4. Choose the narrowest test command that exercises the behavior.

## Red-Green Loop

For one vertical slice at a time:

1. Write one behavior-focused test with expected values from an independent source of truth.
2. Run it and confirm it fails for the intended reason.
3. Write only enough production code to pass.
4. Run the focused test and confirm it passes.
5. Continue with the next behavior informed by the previous cycle.

Run focused typechecking and tests regularly. Run the broader relevant suite after the slices are complete.

## Guardrails

- Do not test private methods or mock internal collaborators.
- Do not assert through a side channel when the public interface can be used.
- Avoid tautological expectations that reproduce the implementation.
- Do not write all tests before all implementation; keep each slice executable.
- Do not add speculative cases or abstractions.
- Leave structural refactoring for the review stage unless it is necessary to make the current behavior possible.