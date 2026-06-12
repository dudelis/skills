#!/usr/bin/env node
// @ts-check
/**
 * npx installer for dudelis-skills.
 * Copies skills into ~/.copilot/skills (GitHub Copilot CLI)
 * and/or ~/.claude/skills (Claude Code).
 *
 * Usage:
 *   npx github:dudelis/skills
 *   npx dudelis-skills
 */

import { readdir, copyFile, mkdir, rm } from 'fs/promises';
import { existsSync } from 'fs';
import { join, dirname } from 'path';
import { homedir } from 'os';
import { fileURLToPath } from 'url';
import { createInterface } from 'readline';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = join(__dirname, '..');

const TARGETS = {
  copilot: {
    label: 'GitHub Copilot CLI',
    path: join(homedir(), '.copilot', 'skills'),
  },
  claude: {
    label: 'Claude Code',
    path: join(homedir(), '.claude', 'skills'),
  },
};

// These bucket directories are not distributed as skills themselves.
const SKIP_DIRS = new Set(['deprecated', 'in-progress', 'personal', 'node_modules', '.git']);

/**
 * Recursively find all skill directories (those containing a SKILL.md).
 * Skips SKIP_DIRS.
 */
async function findSkills(root) {
  const skills = [];

  async function walk(dir) {
    let entries;
    try {
      entries = await readdir(dir, { withFileTypes: true });
    } catch {
      return;
    }
    for (const entry of entries) {
      if (!entry.isDirectory()) continue;
      if (SKIP_DIRS.has(entry.name)) continue;
      const child = join(dir, entry.name);
      if (existsSync(join(child, 'SKILL.md'))) {
        skills.push(child);
      } else {
        await walk(child);
      }
    }
  }

  await walk(root);
  return skills;
}

/** Recursively copy a directory. */
async function copyDir(src, dest) {
  await rm(dest, { recursive: true, force: true });
  await mkdir(dest, { recursive: true });
  const entries = await readdir(src, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = join(src, entry.name);
    const destPath = join(dest, entry.name);
    if (entry.isDirectory()) {
      await copyDir(srcPath, destPath);
    } else {
      await copyFile(srcPath, destPath);
    }
  }
}

function ask(rl, question) {
  return new Promise((resolve) => rl.question(question, resolve));
}

async function main() {
  const rl = createInterface({ input: process.stdin, output: process.stdout });

  const skillsRoot = join(REPO_ROOT, 'skills');
  if (!existsSync(skillsRoot)) {
    console.error(`\nNo skills/ directory found at ${skillsRoot}`);
    rl.close();
    process.exit(1);
  }

  const skills = await findSkills(skillsRoot);

  console.log('\n🛠  dudelis-skills installer\n');

  if (skills.length === 0) {
    console.log('No skills found (skills/ directory exists but contains no SKILL.md files).');
    rl.close();
    return;
  }

  console.log('Skills found:');
  for (const s of skills) {
    const rel = s.replace(REPO_ROOT, '').replace(/^[\\/]/, '');
    console.log(`  • ${rel}`);
  }

  console.log('\nInstall targets:');
  Object.values(TARGETS).forEach((t, i) => {
    console.log(`  ${i + 1}. ${t.label}  →  ${t.path}`);
  });
  console.log('  3. Both (recommended)');

  const answer = await ask(rl, '\nWhere to install? [1/2/3, default: 3]: ');
  const choice = answer.trim() || '3';

  const selectedKeys =
    choice === '1' ? ['copilot'] : choice === '2' ? ['claude'] : ['copilot', 'claude'];

  for (const key of selectedKeys) {
    const target = TARGETS[key];
    console.log(`\nInstalling to ${target.label} (${target.path})...`);
    await mkdir(target.path, { recursive: true });

    for (const skillDir of skills) {
      const name = skillDir.split(/[\\/]/).pop();
      const dest = join(target.path, name);
      await copyDir(skillDir, dest);
      console.log(`  ✓ ${name}`);
    }
  }

  console.log(`\n✅ Installed ${skills.length} skill(s) to ${selectedKeys.length} target(s).`);
  console.log('   Run /skills reload in your AI tool to pick up the changes.\n');
  rl.close();
}

main().catch((err) => {
  console.error('\nInstall failed:', err.message);
  process.exit(1);
});
