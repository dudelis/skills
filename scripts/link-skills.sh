#!/usr/bin/env bash
set -euo pipefail

# Symlinks all skills into ~/.copilot/skills (GitHub Copilot CLI) and
# ~/.claude/skills (Claude Code) for local development.
# Run this once after cloning; edits to skill files take effect immediately.
#
# Usage:
#   bash scripts/link-skills.sh              # links to both tools
#   bash scripts/link-skills.sh --copilot    # Copilot CLI only
#   bash scripts/link-skills.sh --claude     # Claude Code only

REPO="$(cd "$(dirname "$0")/.." && pwd)"

COPILOT_DEST="$HOME/.copilot/skills"
CLAUDE_DEST="$HOME/.claude/skills"

# Determine which targets to link based on flags
TARGETS=()
case "${1:-}" in
  --copilot) TARGETS+=("$COPILOT_DEST") ;;
  --claude)  TARGETS+=("$CLAUDE_DEST") ;;
  *)         TARGETS+=("$COPILOT_DEST" "$CLAUDE_DEST") ;;
esac

# Guard: if a destination is itself a symlink pointing into this repo,
# bail out to avoid writing symlinks back into the source tree.
for DEST in "${TARGETS[@]}"; do
  if [ -L "$DEST" ]; then
    resolved="$(readlink -f "$DEST")"
    case "$resolved" in
      "$REPO"|"$REPO"/*)
        echo "error: $DEST is a symlink into this repo ($resolved)." >&2
        echo "Remove it (rm \"$DEST\") and re-run." >&2
        exit 1
        ;;
    esac
  fi
  mkdir -p "$DEST"
done

# Find every SKILL.md, skip deprecated / in-progress / personal / node_modules
find "$REPO/skills" -name SKILL.md \
  -not -path '*/node_modules/*' \
  -not -path '*/deprecated/*' \
  -not -path '*/in-progress/*' \
  -not -path '*/personal/*' \
  -print0 |
while IFS= read -r -d '' skill_md; do
  src="$(dirname "$skill_md")"
  name="$(basename "$src")"

  for DEST in "${TARGETS[@]}"; do
    target="$DEST/$name"
    # Remove a non-symlink at the target path before (re)creating the symlink.
    if [ -e "$target" ] && [ ! -L "$target" ]; then
      rm -rf "$target"
    fi
    ln -sfn "$src" "$target"
    echo "linked $name → $target"
  done
done
