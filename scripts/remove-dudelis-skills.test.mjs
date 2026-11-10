// Run: node --test scripts/remove-dudelis-skills.test.mjs
// Every case uses a temporary XDG_STATE_HOME and --dry-run, so the real lock file is never touched.
import { test } from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { mkdtempSync, mkdirSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname, delimiter } from "node:path";
import { fileURLToPath } from "node:url";

const script = join(dirname(fileURLToPath(import.meta.url)), "remove-dudelis-skills.mjs");

function run(lock) {
  const state = mkdtempSync(join(tmpdir(), "remove-dudelis-skills-"));
  if (lock !== undefined) {
    mkdirSync(join(state, "skills"));
    writeFileSync(join(state, "skills", ".skill-lock.json"), JSON.stringify(lock));
  }
  const r = spawnSync(process.execPath, [script, "--dry-run"], {
    env: { ...process.env, XDG_STATE_HOME: state },
    encoding: "utf8",
  });
  return { status: r.status, stdout: r.stdout, stderr: r.stderr };
}

const listed = (stdout) => stdout.split(/\r?\n/).filter((l) => /^  \S/.test(l)).map((l) => l.trim());

test("lists only skills whose source is exactly dudelis/skills", () => {
  const r = run({
    version: 3,
    skills: {
      "product-research": { source: "dudelis/skills" },
      "company-research": { source: "dudelis/skills" },
      "fork-skill": { source: "dudelis/skills-fork" },
      tdd: { source: "mattpocock/skills" },
    },
  });
  assert.equal(r.status, 0);
  assert.deepEqual(listed(r.stdout).sort(), ["company-research", "product-research"]);
});

test("missing lock file is not an error", () => {
  const r = run(undefined);
  assert.equal(r.status, 0);
  assert.match(r.stdout, /No skills from dudelis\/skills installed/);
  assert.deepEqual(listed(r.stdout), []);
});

test("lock file without a skills key is not an error", () => {
  const r = run({ version: 3 });
  assert.equal(r.status, 0);
  assert.match(r.stdout, /No skills from dudelis\/skills installed/);
});

test("skips and warns about names outside [a-z0-9-]", () => {
  const r = run({
    skills: {
      "good-name": { source: "dudelis/skills" },
      "bad name; rm -rf ~": { source: "dudelis/skills" },
    },
  });
  assert.equal(r.status, 0);
  assert.deepEqual(listed(r.stdout), ["good-name"]);
  assert.match(r.stderr, /bad name; rm -rf ~/);
});

test("runs one npx remove command and propagates its exit code", () => {
  // A fake npx earlier on PATH records its arguments and exits 3, so no real skills are removed.
  const bin = mkdtempSync(join(tmpdir(), "fake-npx-"));
  writeFileSync(join(bin, "npx"), '#!/bin/sh\necho "fake-npx $*"\nexit 3\n', { mode: 0o755 });
  writeFileSync(join(bin, "npx.cmd"), "@echo fake-npx %*\r\n@exit /b 3\r\n");
  const state = mkdtempSync(join(tmpdir(), "remove-dudelis-skills-"));
  mkdirSync(join(state, "skills"));
  writeFileSync(
    join(state, "skills", ".skill-lock.json"),
    JSON.stringify({ skills: { "a-skill": { source: "dudelis/skills" }, "b-skill": { source: "dudelis/skills" } } }),
  );
  const pathKey = Object.keys(process.env).find((k) => k.toUpperCase() === "PATH") ?? "PATH";
  const r = spawnSync(process.execPath, [script], {
    env: { ...process.env, XDG_STATE_HOME: state, [pathKey]: bin + delimiter + process.env[pathKey] },
    encoding: "utf8",
  });
  assert.equal(r.status, 3);
  assert.match(r.stdout, /fake-npx -y skills@latest remove -g -y --skill a-skill --skill b-skill/);
  assert.doesNotMatch(r.stderr, /DEP0190/);
});
