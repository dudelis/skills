#!/usr/bin/env python3
"""Validate a Shopify Email Custom Liquid block before hand-over.

Usage: python validate_email.py <email-folder> [--lang de|en] [--check-urls]

Errors block the hand-over; warnings are reported for review.
Checks: subject/preheader length, block size (50 KB limit), leftover
placeholders, scripts, image alt text and formats, link language and
discount-code consistency, and optionally that every URL loads.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import ssl
import subprocess
import sys
import unicodedata
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

from emailfiles import block_files, read_front_matter

MAX_BYTES = 50 * 1024
WARN_BYTES = 45 * 1024
SUBJECT_MAX = 50
PREHEADER_RANGE = (40, 90)
BAD_IMAGE_FORMATS = {"svg", "webp"}
SHOP_HOST = "yuliskin.de"
USER_AGENT = "Mozilla/5.0 (email-validator)"


class TagCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.images: list[dict[str, str | None]] = []
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "img":
            self.images.append(values)
        elif tag == "a" and values.get("href"):
            self.links.append(values["href"] or "")


def char_len(text: str) -> int:
    return len(unicodedata.normalize("NFC", text))


def image_format(src: str) -> str | None:
    parsed = urlparse(src)
    forced = parse_qs(parsed.query).get("format")
    if forced:
        return forced[0].lower()
    suffix = Path(parsed.path).suffix.lower().lstrip(".")
    return suffix or None


def check_copy(meta: dict[str, str], lang: str, errors: list[str]) -> None:
    suffix = "" if lang == "de" else "_en"
    subject = meta.get(f"subject{suffix}", "")
    preheader = meta.get(f"preheader{suffix}", "")
    if not subject:
        errors.append(f"brief.md: subject{suffix} missing")
    elif char_len(subject) > SUBJECT_MAX:
        errors.append(f"subject{suffix} has {char_len(subject)} chars (max {SUBJECT_MAX})")
    if not preheader:
        errors.append(f"brief.md: preheader{suffix} missing")
    elif not PREHEADER_RANGE[0] <= char_len(preheader) <= PREHEADER_RANGE[1]:
        errors.append(
            f"preheader{suffix} has {char_len(preheader)} chars "
            f"(expected {PREHEADER_RANGE[0]}-{PREHEADER_RANGE[1]})"
        )


def check_link_language(href: str, lang: str, name: str, errors: list[str], warnings: list[str]) -> None:
    parsed = urlparse(href)
    if parsed.hostname not in (SHOP_HOST, f"www.{SHOP_HOST}"):
        return
    is_en = parsed.path == "/en" or parsed.path.startswith("/en/")
    redirect = unquote(parse_qs(parsed.query).get("redirect", [""])[0])
    if lang == "de" and is_en:
        errors.append(f"{name}: German block links to English URL {href}")
    if lang == "en" and not is_en:
        errors.append(f"{name}: English block links without /en: {href}")
    if lang == "en" and redirect and not redirect.startswith("/en"):
        warnings.append(f"{name}: English discount redirect without /en: {href}")


def check_block(path: Path, lang: str, code: str, errors: list[str], warnings: list[str]) -> set[str]:
    name = path.name
    source = path.read_text(encoding="utf-8")
    size = len(source.encode("utf-8"))
    if size > MAX_BYTES:
        errors.append(f"{name}: {size} bytes exceeds the 50 KB Custom Liquid limit")
    elif size > WARN_BYTES:
        warnings.append(f"{name}: {size} bytes is close to the 50 KB limit; strip whitespace")

    for match in re.finditer(r"\[\[[^\]]*\]\]", source):
        errors.append(f"{name}: unfilled placeholder {match.group(0)}")
    if re.search(r"<script\b", source, re.IGNORECASE):
        errors.append(f"{name}: <script> does not run in email clients")
    if re.search(r"<style\b", source, re.IGNORECASE):
        warnings.append(f"{name}: <style> block; keep styles inline for Gmail/Outlook")
    if re.search(r"background(-image)?\s*:[^;\"]*url\(", source, re.IGNORECASE):
        warnings.append(f"{name}: CSS background image is unreliable in Shopify Email")

    collector = TagCollector()
    collector.feed(source)
    urls: set[str] = set()

    for img in collector.images:
        src = (img.get("src") or "").strip()
        if not (img.get("alt") or "").strip():
            errors.append(f"{name}: image without alt text: {src or '(no src)'}")
        if "{{" in src:
            continue
        if not src.startswith("https://"):
            errors.append(f"{name}: image src is not an absolute https URL: {src}")
            continue
        fmt = image_format(src)
        if fmt in BAD_IMAGE_FORMATS:
            errors.append(f"{name}: {fmt.upper()} image not supported by all email clients: {src}")
        urls.add(src)

    for href in collector.links:
        href = href.strip()
        if "{{" in href or href.startswith("mailto:"):
            continue
        if not href.startswith("https://"):
            errors.append(f"{name}: link is not an absolute https URL: {href}")
            continue
        check_link_language(href, lang, name, errors, warnings)
        discount = re.search(r"/discount/([^/?#]+)", urlparse(href).path)
        if discount:
            used = unquote(discount.group(1))
            if not code:
                errors.append(f"{name}: discount link {used} but brief.md has no discount_code")
            elif used != code:
                errors.append(f"{name}: discount link uses {used}, brief.md says {code}")
        if re.search(r"[?&]utm_", href):
            warnings.append(f"{name}: UTM parameters present (default is none): {href}")
        urls.add(href)

    if code and code not in source:
        warnings.append(f"{name}: discount code {code} does not appear in the block text")
    return urls


def fetch_with_curl(url: str) -> tuple[int, str] | None:
    """Fallback when Python's CA bundle rejects a certificate the OS trusts."""
    if not shutil.which("curl"):
        return None
    result = subprocess.run(
        ["curl", "-sL", "-o", os.devnull, "-A", USER_AGENT, "--max-time", "20",
         "-w", "%{http_code} %{content_type}", url],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        return None
    code, _, content_type = result.stdout.partition(" ")
    return int(code), content_type


def check_urls(urls: set[str], images: set[str], errors: list[str]) -> None:
    for url in sorted(urls):
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                status = response.status
                content_type = response.headers.get("Content-Type", "")
        except urllib.error.HTTPError as exc:
            errors.append(f"URL returns HTTP {exc.code}: {url}")
            continue
        except Exception as exc:  # network errors are reported, never swallowed
            fallback = fetch_with_curl(url) if isinstance(getattr(exc, "reason", None), ssl.SSLError) else None
            if fallback is None:
                errors.append(f"URL not reachable ({exc}): {url}")
                continue
            status, content_type = fallback
        if status >= 400:
            errors.append(f"URL returns HTTP {status}: {url}")
        if url in images and not re.match(r"image/(png|jpe?g|gif)", content_type):
            errors.append(f"image is served as {content_type or 'unknown type'}: {url}")


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", type=Path)
    parser.add_argument("--lang", choices=["de", "en"], default="de")
    parser.add_argument("--check-urls", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    meta = read_front_matter(args.folder)
    if not meta:
        errors.append("brief.md missing or without front matter")
    check_copy(meta, args.lang, errors)

    files = block_files(args.folder, args.lang)
    if not files:
        errors.append(f"no email block for --lang {args.lang}")
    if len(files) > 1 and not meta.get("countdown_end"):
        errors.append("split block (countdown) but brief.md has no countdown_end")

    code = meta.get("discount_code", "")
    urls: set[str] = set()
    images: set[str] = set()
    for path in files:
        found = check_block(path, args.lang, code, errors, warnings)
        urls |= found
        collector = TagCollector()
        collector.feed(path.read_text(encoding="utf-8"))
        images |= {(img.get("src") or "").strip() for img in collector.images}

    if args.check_urls:
        check_urls(urls, images, errors)

    for line in warnings:
        print(f"WARN  {line}")
    for line in errors:
        print(f"ERROR {line}")
    checked = ", ".join(p.name for p in files) or "nothing"
    print(f"{len(errors)} error(s), {len(warnings)} warning(s) — checked {checked}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
