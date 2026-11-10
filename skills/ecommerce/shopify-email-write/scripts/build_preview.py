#!/usr/bin/env python3
"""Render preview.html: mock inbox line + native header + block(s) + native footer.

Usage: python build_preview.py <email-folder> [--lang de|en]
Liquid is replaced with sample values so the page opens in any browser.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

from emailfiles import block_files, read_front_matter

SAMPLE_FIRST_NAME = "Anna"

PAGE = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Preview – {subject}</title>
</head>
<body style="margin:0;padding:0;background:#E9E6E3;font-family:Arial,Helvetica,sans-serif;">
<div style="max-width:600px;margin:0 auto;padding:16px 0;">
  <div style="background:#FFFFFF;border:1px solid #D8D2CD;border-radius:8px;padding:12px 16px;margin:0 8px 16px;">
    <div style="font-size:12px;color:#81746D;">YuliSkin · Posteingang</div>
    <div style="font-size:15px;font-weight:700;color:#292724;margin-top:4px;">{subject}</div>
    <div style="font-size:13px;color:#75685F;margin-top:2px;">{preheader}</div>
  </div>
  <div style="background:#FFFFFF;text-align:center;padding:22px 0;font-size:22px;letter-spacing:3px;color:#292724;border-bottom:1px solid #EADFD8;">
    YULISKIN <span style="font-size:11px;letter-spacing:1px;color:#81746D;">(native header)</span>
  </div>
{body}
  <div style="background:#FFFFFF;text-align:center;padding:22px 12px;font-size:11px;line-height:1.6;color:#81746D;">
    Native footer: shop address · social icons · <u>Abmelden</u>
  </div>
</div>
</body>
</html>
"""

COUNTDOWN = """  <div style="background:#FFFFFF;text-align:center;padding:18px 12px;">
    <div style="display:inline-block;border:2px dashed #AD6745;padding:14px 24px;color:#955D3F;font-size:14px;font-weight:700;">
      Native Countdown section · ends {end}
    </div>
  </div>
"""


def render_liquid(source: str) -> str:
    """Replace Liquid with sample output; highlight anything not simulated."""
    source = re.sub(r"\{%-?.*?-?%\}", "", source, flags=re.DOTALL)

    def output(match: re.Match[str]) -> str:
        expr = match.group(1).strip()
        if expr.startswith("customer.first_name"):
            return SAMPLE_FIRST_NAME
        return (
            '<span style="background:#FFE58A;color:#292724;font-size:12px;">'
            f"[Liquid: {html.escape(expr)}]</span>"
        )

    return re.sub(r"\{\{-?(.*?)-?\}\}", output, source, flags=re.DOTALL)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", type=Path)
    parser.add_argument("--lang", choices=["de", "en"], default="de")
    args = parser.parse_args()

    meta = read_front_matter(args.folder)
    files = block_files(args.folder, args.lang)
    if not files:
        print(f"error: no email block found for --lang {args.lang} in {args.folder}", file=sys.stderr)
        return 1

    suffix = "" if args.lang == "de" else "_en"
    chunks = []
    for index, path in enumerate(files):
        if index > 0:
            end = html.escape(meta.get("countdown_end", "(countdown_end missing in brief.md)"))
            chunks.append(COUNTDOWN.format(end=end))
        chunks.append(render_liquid(path.read_text(encoding="utf-8")))

    page = PAGE.format(
        lang=args.lang,
        subject=html.escape(meta.get(f"subject{suffix}", "(subject missing)")),
        preheader=html.escape(meta.get(f"preheader{suffix}", "(preheader missing)")),
        body="\n".join(chunks),
    )
    out = args.folder / ("preview.html" if args.lang == "de" else "preview-en.html")
    out.write_text(page, encoding="utf-8")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
