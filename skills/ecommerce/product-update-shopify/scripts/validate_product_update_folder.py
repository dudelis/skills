#!/usr/bin/env python3
"""Validate product-research files before update-only Shopify writes."""

from __future__ import annotations

import re
import sys
from pathlib import Path


METADATA_BANNERS = [
    "shopify.product_id",
    "shopify.product_url",
    "shopify.match_confidence",
]

DE_BANNERS = METADATA_BANNERS + [
    "title",
    "descriptionHtml",
    "handle",
    "productType",
    "vendor",
    "variants[0].title",
    "variants[0].price",
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

EN_BANNERS = METADATA_BANNERS + [
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

REQUIRED_DE_UPDATE_VALUES = [
    "descriptionHtml",
    "metafields.custom.application",
    "metafields.custom.effect",
    "metafields.custom.ingredients",
    "seo.title",
    "seo.description",
]

BANNER_RE = re.compile(r"^===\s*(.*?)\s*===\s*$", re.MULTILINE)
PRODUCT_GID_RE = re.compile(r"^gid://shopify/Product/\d+$")
NUMERIC_ID_RE = re.compile(r"^\d+$")
SEQUENTIAL_IMAGE_RE = re.compile(r"-\d{2}\.(?:jpe?g|png|webp)$", re.IGNORECASE)


def parse_banners(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    matches = list(BANNER_RE.finditer(text))
    values: dict[str, str] = {}
    for index, match in enumerate(matches):
        name = match.group(1).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[start:end]
        lines = [line for line in block.splitlines() if not line.lstrip().startswith("#")]
        values[name] = "\n".join(lines).strip()
    return values


def is_empty(value: str | None) -> bool:
    return value is None or not value.strip() or value.strip().lower() == "unknown"


def validate_file(
    path: Path,
    expected: list[str],
    required_values: list[str],
) -> tuple[dict[str, str], list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not path.exists():
        return {}, [f"Missing file: {path}"], []

    banners = parse_banners(path)
    if not banners:
        errors.append(f"{path.name}: no banners found")
        return banners, errors, warnings

    actual = list(banners)
    missing = [name for name in expected if name not in banners]
    if missing:
        errors.append(f"{path.name}: missing banner(s): {', '.join(missing)}")

    unknown = [name for name in actual if name not in expected]
    if unknown:
        warnings.append(f"{path.name}: unknown banner(s): {', '.join(unknown)}")

    expected_order = [name for name in expected if name in banners]
    actual_expected_order = [name for name in actual if name in expected]
    if actual_expected_order != expected_order:
        warnings.append(f"{path.name}: expected banners appear out of order")

    for name in required_values:
        if name not in banners:
            errors.append(f"{path.name}: required update banner {name!r} is missing")
        elif is_empty(banners[name]):
            errors.append(f"{path.name}: required update banner {name!r} is empty")

    description = banners.get("descriptionHtml", "")
    if "<h1" in description.lower():
        errors.append(f"{path.name}: descriptionHtml contains <h1>")

    seo_title = banners.get("seo.title", "")
    if not is_empty(seo_title) and len(seo_title) > 70:
        errors.append(f"{path.name}: seo.title is {len(seo_title)} chars, max 70")

    seo_description = banners.get("seo.description", "")
    if not is_empty(seo_description) and len(seo_description) > 160:
        errors.append(
            f"{path.name}: seo.description is {len(seo_description)} chars, max 160"
        )

    product_id = banners.get("shopify.product_id", "")
    if not is_empty(product_id) and not (
        PRODUCT_GID_RE.match(product_id) or NUMERIC_ID_RE.match(product_id)
    ):
        errors.append(
            f"{path.name}: shopify.product_id must be a Product GID, numeric ID, or Unknown"
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
        print("Usage: validate_product_update_folder.py <Products/Company/Product folder>")
        return 2

    folder = Path(argv[1]).expanduser().resolve()
    if not folder.exists() or not folder.is_dir():
        print(f"Product folder does not exist: {folder}")
        return 2

    errors: list[str] = []
    warnings: list[str] = []

    brief = folder / "brief.txt"
    if not brief.exists():
        errors.append(f"Missing file: {brief}")

    _, de_errors, de_warnings = validate_file(
        folder / "shopify-de.txt",
        DE_BANNERS,
        REQUIRED_DE_UPDATE_VALUES,
    )
    _, en_errors, en_warnings = validate_file(
        folder / "shopify-en.txt",
        EN_BANNERS,
        ["descriptionHtml", "metafields.custom.application", "metafields.custom.effect", "metafields.custom.ingredients", "seo.title", "seo.description"],
    )
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
    print(f"- Product folder: {folder}")
    print(f"- Sequential image files: {len(images)}")
    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
