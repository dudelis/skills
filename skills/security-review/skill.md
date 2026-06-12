# Security Review

## Description

Identifies security vulnerabilities in code and suggests concrete remediations. Covers common vulnerability classes including injection, authentication flaws, insecure data handling, and dependency risks.

## Instructions

When performing a security review:

1. **Review the attack surface** — Identify all entry points: HTTP endpoints, CLI arguments, file inputs, environment variables, inter-service calls, and database queries.
2. **Check for common vulnerabilities** — Systematically evaluate against the OWASP Top 10 and relevant language-specific risks:
   - **Injection** (SQL, command, LDAP, XPath, template injection)
   - **Broken authentication** (weak passwords, missing MFA, insecure session management)
   - **Sensitive data exposure** (secrets in code, unencrypted storage or transit, verbose error messages)
   - **Broken access control** (missing authorization checks, IDOR, path traversal)
   - **Security misconfiguration** (default credentials, open CORS, debug mode enabled)
   - **Insecure deserialization** (untrusted data passed to deserialization functions)
   - **Known vulnerable dependencies** (outdated packages with CVEs)
   - **Insufficient logging** (missing audit logs for security-relevant actions)
3. **Assign severity** — Label each finding `critical`, `high`, `medium`, or `low` using CVSS-based reasoning.
4. **Provide a remediation** — For every finding, give a specific, actionable fix with a code example where applicable.
5. **Avoid false positives** — Only report confirmed or highly probable vulnerabilities. If something is suspicious but not definitively a vulnerability, note it as a recommendation rather than a finding.

### Guidelines

- Prioritize findings by severity — address `critical` and `high` items first.
- Consider the deployment context (public internet vs internal tool) when assessing severity.
- Flag hardcoded credentials or secrets immediately as `critical`, regardless of other context.
- Check that cryptographic functions use appropriate algorithms and key lengths (e.g. avoid MD5/SHA-1 for security purposes).

### Out of Scope

- Do not perform a general code quality review; focus exclusively on security.
- Do not run external tools or scanners; review the code directly.

## Example Usage

**Prompt:**
> Review `src/api/users.js` for security vulnerabilities.

**Expected output:**
> **[critical] SQL injection on line 34** — The `userId` parameter is interpolated directly into the SQL query string. An attacker can craft a malicious `userId` to read or modify arbitrary data.
>
> Fix:
> ```javascript
> // Before (vulnerable)
> const query = `SELECT * FROM users WHERE id = ${userId}`;
>
> // After (safe)
> const query = 'SELECT * FROM users WHERE id = ?';
> db.query(query, [userId]);
> ```
>
> **[high] Missing authorization check on line 58** — The `/users/:id` endpoint returns user data without verifying that the authenticated user is allowed to access that `id`. Add an ownership or role check before returning data.
