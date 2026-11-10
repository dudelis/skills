#!/usr/bin/env node
// Removes every skill the `skills` CLI installed globally from dudelis/skills, leaving other sources alone.
//
// Usage (from a clone of this repo; works in bash, zsh, PowerShell, and cmd):
//   node scripts/remove-dudelis-skills.mjs --dry-run   # only list what would be removed
//   node scripts/remove-dudelis-skills.mjs             # remove them from every agent
//
// Reads the CLI's global lock file: $XDG_STATE_HOME/skills/.skill-lock.json when XDG_STATE_HOME is set,
// otherwise ~/.agents/.skill-lock.json.
import { existsSync, readFileSync } from "node:fs";
import { homedir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";

const SOURCE = "dudelis/skills";
const dryRun = process.argv.slice(2).includes("--dry-run");

const stateHome = process.env.XDG_STATE_HOME;
const lockPath = stateHome
  ? join(stateHome, "skills", ".skill-lock.json")
  : join(homedir(), ".agents", ".skill-lock.json");

const skills = existsSync(lockPath) ? JSON.parse(readFileSync(lockPath, "utf8")).skills || {} : {};

const names = [];
for (const [name, entry] of Object.entries(skills)) {
  if (entry?.source !== SOURCE) continue;
  // Names are passed to a shell, so only accept the characters a skill folder name may contain.
  if (!/^[a-z0-9-]+$/.test(name)) {
    console.warn(`Skipping unexpected skill name: ${JSON.stringify(name)}`);
    continue;
  }
  names.push(name);
}

if (names.length === 0) {
  console.log(`No skills from ${SOURCE} installed (lock file: ${lockPath}).`);
  process.exit(0);
}

console.log(`${dryRun ? "Would remove" : "Removing"} ${names.length} skill(s) from ${SOURCE}:`);
for (const name of names) console.log(`  ${name}`);
if (dryRun) process.exit(0);

// One command string with shell: true (no args array): npx is npx.cmd on Windows and needs a shell,
// and passing args together with shell: true is deprecated in Node 24 (DEP0190).
const command = `npx -y skills@latest remove -g -y ${names.map((n) => `--skill ${n}`).join(" ")}`;
const result = spawnSync(command, { stdio: "inherit", shell: true });
if (result.error) console.error(result.error.message);
process.exit(result.status ?? 1);
