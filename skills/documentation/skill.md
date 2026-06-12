# Documentation

## Description

Writes and improves code documentation, including inline comments, docstrings, JSDoc/TSDoc annotations, and README files. Produces clear, accurate, and maintainable documentation that helps developers understand and use the code.

## Instructions

When writing or improving documentation:

1. **Understand the code first** — Read the implementation fully before writing any documentation. Documentation must be accurate; incorrect docs are worse than no docs.
2. **Choose the right format** — Use the documentation format standard for the language and project:
   - Python: Google-style or NumPy-style docstrings
   - JavaScript/TypeScript: JSDoc or TSDoc
   - Go: godoc comments
   - Java/Kotlin: Javadoc
   - Rust: rustdoc
3. **Document the what and why, not the how** — Describe what a function does and why it exists. The code itself shows how.
4. **Include parameters, return values, and exceptions** — For functions and methods, document all parameters, return values, and any exceptions or errors that can be thrown.
5. **Write for the reader** — Assume the reader is a competent developer who is unfamiliar with this specific code. Avoid jargon unless it is domain-standard.
6. **Keep docs up to date** — When updating existing code, update its documentation to match.

### Guidelines

- Keep inline comments concise; prefer self-documenting code with comments only for non-obvious logic.
- For README files, include: what the project does, how to install/set up, how to use, and how to contribute.
- Include usage examples in public API documentation where helpful.
- Do not restate what the code obviously does (e.g. `// increment i` above `i++`).

### Out of Scope

- Do not change code logic while adding documentation.
- Do not generate documentation for private/internal helpers unless explicitly asked.

## Example Usage

**Prompt:**
> Add docstrings to all public functions in `src/auth.py`.

**Expected output:**
> ```python
> def verify_token(token: str) -> dict:
>     """Verify a JWT token and return its decoded payload.
>
>     Args:
>         token: A signed JWT string to verify.
>
>     Returns:
>         A dictionary containing the decoded token claims.
>
>     Raises:
>         TokenExpiredError: If the token has passed its expiry time.
>         InvalidTokenError: If the token signature is invalid or the token is malformed.
>     """
> ```
