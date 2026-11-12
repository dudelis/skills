"""Crop-resize a slide's two images: <handle>.<ext> at 1536x1024 and <handle>-mobile.<ext> at 1536x864.

The mobile source is the dropped image whose file name ends in -mobile; the other one is the desktop source.

Usage: python prepare_image.py <slide-folder> [--image <path>] [--mobile-image <path>]
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageOps

MOBILE_SUFFIX = "-mobile"


@dataclass(frozen=True)
class Variant:
    """One of the slide's two images: its target size, output suffix, CLI option, and name in messages."""

    size: tuple[int, int]
    suffix: str
    option: str
    label: str


DESKTOP = Variant((1536, 1024), "", "--image", "desktop image")
MOBILE = Variant((1536, 864), MOBILE_SUFFIX, "--mobile-image", f"mobile image (file name ending in {MOBILE_SUFFIX})")
# A source more than 20 % off its target's aspect ratio (portrait, square) loses visible content in the
# center crop. 3:2 for the 16:9 mobile image stays below it: ChatGPT offers no wider landscape size.
SHAPE_TOLERANCE = 0.20
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


def is_mobile(path: Path) -> bool:
    return path.stem.lower().endswith(MOBILE_SUFFIX)


def dropped_files(folder: Path, handle: str) -> list[Path]:
    """Files in the slide folder, ignoring the processed <handle> and <handle>-mobile outputs."""
    outputs = {handle, f"{handle}{MOBILE_SUFFIX}"}
    return [p for p in folder.iterdir() if p.is_file() and p.stem not in outputs]


def find_source(files: list[Path], folder: Path, variant: Variant) -> Path:
    """Return the one dropped image for variant: named *-mobile for MOBILE, any other name for DESKTOP."""
    group = [p for p in files if is_mobile(p) == (variant is MOBILE)]
    candidates = [p for p in group if p.suffix.lower() in FORMATS]
    svgs = [p for p in group if is_svg(p)]
    if not candidates and svgs:
        raise SlideImageError(SVG_WARNING.format(name=svgs[0].name))
    if len(candidates) != 1:
        found = ", ".join(p.name for p in candidates) or "none"
        raise SlideImageError(
            f"Expected exactly one PNG, JPG, or WebP {variant.label} in {folder} (found: {found}). "
            f"Pass it explicitly with {variant.option} <path>."
        )
    for svg in svgs:
        print(f"WARNING: ignored {svg.name} (SVG cannot be crop-resized); using {candidates[0].name}.")
    return candidates[0]


def prepare(source: Path, size: tuple[int, int], output_stem: Path) -> None:
    """Center-crop and resize source to size, saved as <output_stem>.<ext> in its own format."""
    extension, image_format = FORMATS[source.suffix.lower()]
    output_path = output_stem.with_name(output_stem.name + extension)
    width, height = size
    with Image.open(source) as image:
        if abs((image.width / image.height) / (width / height) - 1) > SHAPE_TOLERANCE:
            print(
                f"WARNING: {source.name} is {image.width}x{image.height}, far from the {width}x{height} shape; "
                f"the center crop may cut off products. Check {output_path.name} or regenerate."
            )
        # ImageOps.fit scales by the larger factor, so the source must cover both target sides.
        scale = max(width / image.width, height / image.height)
        if scale > 1:
            print(
                f"WARNING: source {image.width}x{image.height} was upscaled {scale:.2f}x; "
                "check it for softness or ask the generator for a larger image."
            )
        fitted = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
        if image_format == "PNG":
            fitted.save(output_path, image_format)
        else:
            fitted.convert("RGB").save(output_path, image_format, quality=90)
    print(f"OK {output_path} {width}x{height}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path, help="slide folder containing brief.md")
    parser.add_argument("--image", type=Path, help="desktop image to use instead of the dropped one")
    parser.add_argument("--mobile-image", type=Path, help="mobile image to use instead of the dropped *-mobile one")
    args = parser.parse_args(argv)

    handle = read_front_matter(args.folder).get("handle", "")
    try:
        if not handle:
            raise SlideImageError(f"No `handle` in the front matter of {args.folder / 'brief.md'}.")
        files = dropped_files(args.folder, handle)
        sources = {
            variant: check_explicit(explicit) if explicit else find_source(files, args.folder, variant)
            for variant, explicit in ((DESKTOP, args.image), (MOBILE, args.mobile_image))
        }
    except SlideImageError as error:
        print(error, file=sys.stderr)
        return 1
    for variant, source in sources.items():
        prepare(source, variant.size, args.folder / f"{handle}{variant.suffix}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
