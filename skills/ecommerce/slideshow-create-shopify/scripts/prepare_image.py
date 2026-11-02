"""Crop-resize the slide image in a slide folder to 1536x1024 and name it <handle>.<ext>.

Usage: python prepare_image.py <slide-folder> [--image <path>]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from PIL import Image, ImageOps

TARGET = (1536, 1024)
# Source suffix -> (output extension, Pillow format). The original format is kept.
FORMATS = {
    ".png": (".png", "PNG"),
    ".jpg": (".jpg", "JPEG"),
    ".jpeg": (".jpg", "JPEG"),
    ".webp": (".webp", "WEBP"),
}


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


class SlideImageError(Exception):
    """A problem the user has to fix; the message says what to do."""


def find_source(folder: Path, handle: str) -> Path:
    """Return the one image dropped into the folder, ignoring the processed <handle>.<ext>."""
    files = [p for p in folder.iterdir() if p.is_file() and p.stem != handle]
    candidates = [p for p in files if p.suffix.lower() in FORMATS]
    if not candidates and any(p.suffix.lower() == ".svg" for p in files):
        raise SlideImageError(
            "WARNING: only an SVG was found. SVG is probably a mistake for a photographic "
            "slide and cannot be crop-resized; export it as PNG, JPG, or WebP."
        )
    if len(candidates) != 1:
        found = ", ".join(p.name for p in candidates) or "none"
        raise SlideImageError(
            f"Expected exactly one PNG, JPG, or WebP image in {folder} (found: {found}). "
            "Pass the image explicitly with --image <path>."
        )
    return candidates[0]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path, help="slide folder containing brief.md")
    parser.add_argument("--image", type=Path, help="image outside the folder to use instead")
    args = parser.parse_args(argv)

    handle = read_front_matter(args.folder).get("handle", "")
    try:
        if not handle:
            raise SlideImageError(f"No `handle` in the front matter of {args.folder / 'brief.md'}.")
        source = args.image or find_source(args.folder, handle)
        if source.suffix.lower() not in FORMATS:
            raise SlideImageError(f"Unsupported image type {source.suffix}: use PNG, JPG, or WebP.")
    except SlideImageError as error:
        print(error, file=sys.stderr)
        return 1
    extension, image_format = FORMATS[source.suffix.lower()]
    target = args.folder / f"{handle}{extension}"
    with Image.open(source) as image:
        # ImageOps.fit scales by the larger factor, so the source must cover both target sides.
        scale = max(TARGET[0] / image.width, TARGET[1] / image.height)
        if scale > 1:
            print(
                f"WARNING: source {image.width}x{image.height} was upscaled {scale:.2f}x; "
                "check it for softness or ask the generator for a larger image."
            )
        fitted = ImageOps.fit(image, TARGET, Image.Resampling.LANCZOS)
        if image_format == "JPEG":
            fitted = fitted.convert("RGB")
        fitted.save(target, image_format, quality=90)
    print(f"OK {target} {TARGET[0]}x{TARGET[1]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
