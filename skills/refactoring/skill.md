# Refactoring

## Description

Suggests and applies targeted code refactoring to improve readability, reduce complexity, eliminate duplication, and make code easier to maintain — without changing external behaviour.

## Instructions

When refactoring code:

1. **Verify behaviour is preserved** — The refactored code must have identical external behaviour to the original. If tests exist, confirm they still pass after changes.
2. **Apply one refactoring at a time** — Make small, incremental changes with a clear rationale for each. Avoid rewriting large sections in a single step.
3. **Choose appropriate refactoring techniques** — Apply well-known refactoring patterns as appropriate:
   - **Extract function/method** — Pull repeated or complex logic into a named function.
   - **Rename** — Use descriptive, intention-revealing names for variables, functions, and classes.
   - **Remove duplication** — Replace copy-pasted logic with shared abstractions.
   - **Simplify conditionals** — Replace complex boolean logic with guard clauses or well-named predicates.
   - **Decompose large functions** — Split functions that do too many things into focused, single-purpose functions.
   - **Replace magic numbers/strings** — Use named constants for hardcoded literal values.
   - **Introduce parameter objects** — Replace long parameter lists with a single structured object.
4. **Explain each change** — Briefly describe what was changed and why (e.g. "Extracted `validateEmail` to reduce duplication across three call sites").
5. **Keep changes minimal** — Only refactor code that is directly related to the requested change or clearly benefits from improvement. Do not refactor unrelated code.

### Guidelines

- Do not change function signatures unless explicitly asked, as it may break callers.
- Preserve all existing comments that remain relevant after the refactoring.
- If a refactoring would require updating tests, note this explicitly and provide updated test code.
- Prefer standard language idioms over clever one-liners.

### Out of Scope

- Do not introduce new features or fix bugs while refactoring (unless a bug is directly caused by the code being refactored).
- Do not change formatting or style unless it materially improves readability.

## Example Usage

**Prompt:**
> Refactor the `processOrder` function in `src/orders.ts` to improve readability.

**Expected output:**
> The function was doing three distinct things in a single 60-line body. I extracted each into a named helper:
>
> ```typescript
> // Before
> function processOrder(order: Order) {
>   // 60 lines of mixed validation, pricing, and notification logic
> }
>
> // After
> function processOrder(order: Order) {
>   validateOrder(order);
>   const total = calculateTotal(order);
>   notifyCustomer(order, total);
> }
>
> function validateOrder(order: Order) { /* ... */ }
> function calculateTotal(order: Order): number { /* ... */ }
> function notifyCustomer(order: Order, total: number) { /* ... */ }
> ```
>
> Each function now has a single responsibility and can be tested independently.
