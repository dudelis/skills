"""Crop-resize the slide image in a slide folder to 1536x1024 and name it <handle>.<ext>.

Usage: python prepare_image.py <slide-folder> [--image <path>]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from PIL import Image, ImageOps

WIDTH, HEIGHT = 1536, 1024
# Source suffix -> (output extension, Pillow format). The original format is kept.
FORMATS = {
    ".png": (".png", "PNG"),
    ".jpg": (".jpg", "JPEG"),
    ".jpeg": (".jpg", "JPEG"),
    ".webp": (".webp", "WEBP"),
}
SVG_WARNING = (
    "WARNING: {name} is an SVG, which is probably a mistake for a photographic slide "
    "and cannot be crop-resized; export it as PNG, JPG, or WebP."
)


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


def is_svg(path: Path) -> bool:
    return path.suffix.lower() == ".svg"


def check_explicit(image: Path) -> Path:
    if is_svg(image):
        raise SlideImageError(SVG_WARNING.format(name=image.name))
    if image.suffix.lower() not in FORMATS:
        raise SlideImageError(f"Unsupported image type {image.suffix}: use PNG, JPG, or WebP.")
    return image


def find_source(folder: Path, handle: str) -> Path:
    """Return the one image dropped into the folder, ignoring the processed <handle>.<ext>."""
    files = [p for p in folder.iterdir() if p.is_file() and p.stem != handle]
    candidates = [p for p in files if p.suffix.lower() in FORMATS]
    svgs = [p for p in files if is_svg(p)]
    if not candidates and svgs:
        raise SlideImageError(SVG_WARNING.format(name=svgs[0].name))
    if len(candidates) != 1:
        found = ", ".join(p.name for p in candidates) or "none"
        raise SlideImageError(
            f"Expected exactly one PNG, JPG, or WebP image in {folder} (found: {found}). "
            "Pass the image explicitly with --image <path>."
        )
    for svg in svgs:
        print(f"WARNING: ignored {svg.name} (SVG cannot be crop-resized); using {candidates[0].name}.")
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
        source = check_explicit(args.image) if args.image else find_source(args.folder, handle)
    except SlideImageError as error:
        print(error, file=sys.stderr)
        return 1
    extension, image_format = FORMATS[source.suffix.lower()]
    output_path = args.folder / f"{handle}{extension}"
    with Image.open(source) as image:
        # ImageOps.fit scales by the larger factor, so the source must cover both target sides.
        scale = max(WIDTH / image.width, HEIGHT / image.height)
        if scale > 1:
            print(
                f"WARNING: source {image.width}x{image.height} was upscaled {scale:.2f}x; "
                "check it for softness or ask the generator for a larger image."
            )
        fitted = ImageOps.fit(image, (WIDTH, HEIGHT), Image.Resampling.LANCZOS)
        if image_format == "PNG":
            fitted.save(output_path, image_format)
        else:
            fitted.convert("RGB").save(output_path, image_format, quality=90)
    print(f"OK {output_path} {WIDTH}x{HEIGHT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
