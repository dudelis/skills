---
name: implement
description: Implement work from an explicit GitHub issue, specification, or ticket using focused validation, TDD where appropriate, and final code review. Use when the user explicitly asks to implement a defined piece of work.
disable-model-invocation: true
---

# Implement

Implement only the work explicitly named by the user. This skill changes local files; it never commits, pushes, comments on, labels, or closes GitHub issues.

Work in a Git repository. When the source is a GitHub issue, require an authenticated `gh` CLI for read-only retrieval.

## Workflow

1. Read the full source issue or specification and its comments. A directly supplied open issue does not need `ready-for-agent`.
2. Read repository instructions, status, relevant context documents, ADRs, code, and tests. Record the initial worktree state and preserve pre-existing changes.
3. Translate acceptance criteria into observable checks. Resolve a genuinely blocking ambiguity with the user; do not silently expand scope.
4. Use `codebase-design` for interface and seam decisions. Use `tdd` where practical at seams already agreed in the source, confirming any new seam first.
5. Work in small vertical slices. After the first substantive edit, run the cheapest focused check that can falsify it. Keep focused tests and typechecking green as work proceeds.
6. Run the broader relevant validation once implementation is complete.
7. Invoke `code-review` against the source and repository standards. Fix actionable findings, rerun validation, and review again, for at most three review passes.
8. Stop with uncommitted changes. Report acceptance-criteria coverage, commands run, review outcome, unresolved findings, and any manual validation still required.

Do not overwrite unrelated changes or weaken tests to obtain green results. Do not claim completion when required validation failed or could not run.