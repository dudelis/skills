"""Shared helpers: brief front matter and email block discovery."""

from __future__ import annotations

import re
from pathlib import Path


def read_front_matter(folder: Path) -> dict[str, str]:
    """Parse the flat `key: "value"` YAML front matter of brief.md."""
    brief = folder / "brief.md"
    if not brief.exists():
        return {}
    text = brief.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*(\n|$)", text, re.DOTALL)
    if not match:
        return {}
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        data[key.strip()] = value
    return data


def block_files(folder: Path, lang: str) -> list[Path]:
    """Return the paste-ready block(s) in order: single file or part-1/part-2."""
    prefix = "email" if lang == "de" else "email-en"
    single = folder / f"{prefix}.liquid"
    parts = sorted(folder.glob(f"{prefix}-part-*.liquid"))
    if single.exists():
        return [single]
    return parts
