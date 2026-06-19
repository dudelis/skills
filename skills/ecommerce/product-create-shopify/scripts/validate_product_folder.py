#!/usr/bin/env python3
"""Validate product-research banner files before Shopify writes.

The create skill blocks only on the minimum needed to create a draft product.
Everything else is reported as a warning so Shopify writes can continue best-effort.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


DE_BANNERS = [
    "title",
    "descriptionHtml",
    "productType",
    "vendor",
    "variants[0].title",
    "variants[0].sku",
    "variants[0].barcode",
    "variants[0].weight",
    "metafields.shopify.country_of_origin",
    "metafields.shopify.harmonized_system_code",
    "variants[0].metafields.dhlapp.customsItemDescription",
    "metafields.shopify--discovery--product_recommendation.related_products",
    "metafields.custom.application",
    "metafields.custom.effect",
    "metafields.custom.ingredients",
    "metafields.custom.skin_application_areas",
    "metafields.custom.skin_problem",
    "metafields.custom.skin_type",
    "seo.title",
    "seo.description",
    "media[].alt",
]

OPTIONAL_DE_BANNERS = ["handle"]

EN_BANNERS = [
    "title",
    "descriptionHtml",
    "productType",
    "variants[0].title",
    "metafields.custom.application",
    "metafields.custom.effect",
    "metafields.custom.ingredients",
    "seo.title",
    "seo.description",
]

BANNER_RE = re.compile(r"^===\s*(.*?)\s*===\s*$", re.MULTILINE)
SEQUENTIAL_IMAGE_RE = re.compile(r"-\d{2}\.(?:jpe?g|png|webp)$", re.IGNORECASE)


def parse_banners(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    matches = list(BANNER_RE.finditer(text))
    values: dict[str, str] = {}

    for index, match in enumerate(matches):
        name = match.group(1)
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[start:end]
        lines = [line for line in block.splitlines() if not line.lstrip().startswith("#")]
        values[name] = "\n".join(lines).strip()

    return values


def validate_file(
    path: Path,
    expected: list[str],
    *,
    required_values: list[str] | None = None,
    optional_banners: list[str] | None = None,
) -> tuple[dict[str, str], list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not path.exists():
        return {}, [f"Missing file: {path}"], []

    banners = parse_banners(path)
    actual = list(banners)
    optional = set(optional_banners or [])
    allowed = set(expected) | optional

    if not banners:
        errors.append(f"{path.name}: no banners found")

    missing = [name for name in expected if name not in banners]
    if missing:
        warnings.append(f"{path.name}: missing expected banner(s): {', '.join(missing)}")

    unknown = [name for name in actual if name not in allowed]
    if unknown:
        warnings.append(f"{path.name}: unknown banner(s): {', '.join(unknown)}")

    expected_order = [name for name in expected if name in banners]
    actual_expected_order = [name for name in actual if name in expected]
    if actual_expected_order != expected_order:
        warnings.append(
            f"{path.name}: expected banners appear out of order. "
            f"Expected relative order: {expected_order}; actual: {actual_expected_order}"
        )

    for name in required_values or []:
        if name not in banners:
            errors.append(f"{path.name}: required banner {name!r} is missing")
        elif not banners[name]:
            errors.append(f"{path.name}: required banner {name!r} has no value")

    for name in expected:
        if name not in banners:
            continue
        if not banners[name]:
            warnings.append(f"{path.name}: banner {name!r} has no value")

    description = banners.get("descriptionHtml", "")
    if "<h1" in description.lower():
        warnings.append(f"{path.name}: descriptionHtml contains <h1>")

    seo_title = banners.get("seo.title", "")
    if len(seo_title) > 70:
        warnings.append(f"{path.name}: seo.title is {len(seo_title)} chars, max 70")

    seo_description = banners.get("seo.description", "")
    if len(seo_description) > 160:
        warnings.append(
            f"{path.name}: seo.description is {len(seo_description)} chars, max 160"
        )

    return banners, errors, warnings


def image_files(folder: Path) -> list[Path]:
    return sorted(
        path
        for path in folder.iterdir()
        if path.is_file() and SEQUENTIAL_IMAGE_RE.search(path.name)
    )


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: validate_product_folder.py <Products/Company/Product folder>")
        return 2

    folder = Path(argv[1]).expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not folder.exists() or not folder.is_dir():
        print(f"Product folder does not exist: {folder}")
        return 2

    _, de_errors, de_warnings = validate_file(
        folder / "shopify-de.txt",
        DE_BANNERS,
        required_values=["title", "vendor", "descriptionHtml"],
        optional_banners=OPTIONAL_DE_BANNERS,
    )
    _, en_errors, en_warnings = validate_file(folder / "shopify-en.txt", EN_BANNERS)
    errors.extend(de_errors)
    errors.extend(en_errors)
    warnings.extend(de_warnings)
    warnings.extend(en_warnings)

    images = image_files(folder)
    if not images:
        warnings.append("No sequential product image files found")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        if warnings:
            print("Warnings:")
            for warning in warnings:
                print(f"- {warning}")
        return 1

    print("Validation passed.")
    print(f"- German file: {folder / 'shopify-de.txt'}")
    print(f"- English file: {folder / 'shopify-en.txt'}")
    print(f"- Sequential image files: {len(images)}")
    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
