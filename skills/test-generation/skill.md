# Test Generation

## Description

Generates comprehensive, well-structured unit and integration tests for existing code. Tests are idiomatic to the language and framework in use, cover happy paths, edge cases, and error conditions.

## Instructions

When generating tests:

1. **Analyse the code** — Read the function, class, or module to be tested. Understand its inputs, outputs, side effects, and failure modes.
2. **Use the existing test framework** — Identify which testing library and conventions are already used in the project (e.g. Jest, pytest, JUnit, Go testing) and follow the same patterns.
3. **Cover all cases** — Write tests for:
   - Happy path (expected inputs producing expected outputs)
   - Edge cases (empty input, boundary values, maximum values)
   - Error/failure paths (invalid input, exceptions, rejected promises)
4. **Write descriptive test names** — Test names should clearly describe the scenario being tested, e.g. `should return empty array when input list is empty`.
5. **Keep tests independent** — Each test should be able to run in isolation without depending on other tests' state.
6. **Mock external dependencies** — Replace network calls, database access, and file I/O with mocks or stubs so tests run quickly and deterministically.

### Guidelines

- Prefer small, focused tests over large tests that assert many things at once.
- Do not duplicate production logic inside tests; test behaviour, not implementation.
- Aim for meaningful coverage, not 100% line coverage at the expense of test quality.
- Include setup and teardown where needed to avoid test pollution.

### Out of Scope

- Do not generate tests for code that has no observable behaviour (e.g. pure configuration files).
- Do not modify existing production code to make it more testable unless explicitly asked.

## Example Usage

**Prompt:**
> Generate tests for the `calculateDiscount` function in `src/pricing.ts`.

**Expected output:**
> ```typescript
> describe('calculateDiscount', () => {
>   it('should apply 10% discount for silver tier customers', () => {
>     expect(calculateDiscount(100, 'silver')).toBe(90);
>   });
>
>   it('should apply 20% discount for gold tier customers', () => {
>     expect(calculateDiscount(100, 'gold')).toBe(80);
>   });
>
>   it('should return original price for unknown tier', () => {
>     expect(calculateDiscount(100, 'unknown')).toBe(100);
>   });
>
>   it('should return 0 when price is 0', () => {
>     expect(calculateDiscount(0, 'gold')).toBe(0);
>   });
>
>   it('should throw when price is negative', () => {
>     expect(() => calculateDiscount(-1, 'gold')).toThrow('Price must be non-negative');
>   });
> });
> ```
