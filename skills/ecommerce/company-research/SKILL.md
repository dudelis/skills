---
name: company-research
description: >
  Researches one skincare or dermocosmetics brand for YuliSkin, produces a Shopify-ready
  collection-page brief in German and English, downloads the brand logo, and discovers
  products from the brand site into a manifest for parallel product-research fan-out.
  Use when the user provides a brand/company name plus the company website URL and
  wants brand research, collection page copy, logo download, and a product list ready
  for product-research.
---

# Company Research

## Quick Start

Use this skill to research one skincare or dermocosmetics brand and produce Shopify-ready
collection-page content for `yuliskin.de`, download the brand logo, and discover the
brand's products into a manifest for parallel fan-out to the `product-research` skill.

Required input (both mandatory; ask the user if either is missing):

```text
Company name: [exact brand name]
Company URL:  [one or more official brand website URLs, comma-separated]
```

Output files:

```text
Collections/[CompanyName]/brief.txt                  # research + strategy + structured data reminder + discovered-products preview
Collections/[CompanyName]/shopify-de.txt              # German Shopify collection fields, banner-formatted for copy-paste
Collections/[CompanyName]/shopify-en.txt              # English Shopify collection fields, banner-formatted for copy-paste
Collections/[CompanyName]/products.csv                # discovered-products manifest for product-research fan-out
Collections/[CompanyName]/[CompanyName]-logo.[ext]    # SVG preferred, may be missing
```

The Shopify files use Shopify Admin GraphQL field paths as banners (e.g.
`=== descriptionHtml ===`, `=== handle ===`) so future Shopify automation can parse
them. Always write `brief.txt`, `shopify-de.txt`, and `shopify-en.txt` in the same run.

Folder/file naming: brand's own capitalization, ASCII-fold diacritics (`é→e`, `ö→o`,
`ß→ss`), strip apostrophes and periods, replace Windows-unsafe chars with `-`. Examples:
`L'Oréal Paris → LOreal Paris`, `Dr. Hauschka → Dr Hauschka`, `BABOR → BABOR`.

## Workflow

The skill runs three passes, then stops. It does not invoke `product-research` itself.

### Pass 1 — Brand research

Fetch the provided URL(s) plus these brand-info pages (German `/de` version preferred,
silently skip 404s, note found vs missing in Research Summary):

- `/about`, `/about-us`, `/our-story`, `/heritage`, `/ueber-uns`, `/unsere-geschichte`
- `/philosophy`, `/values`, `/manifesto`, `/mission`
- `/science`, `/research`, `/innovation`, `/wissenschaft`
- `/sustainability`, `/responsibility`, `/certifications`, `/nachhaltigkeit`
- `/professional`, `/experts`, `/dermatologist`
- `/contact`, `/imprint`, `/impressum`
- `/press`, `/media`, `/presse`
- 2–3 posts from `/blog/`, `/journal/`, `/magazine/` for tone of voice only

Use only the provided brand site. Do not crawl Instagram, LinkedIn, Wikipedia, or
competitor sites for brand facts. Verified facts vs unknown facts must be separated.

Then build the brief and Shopify files per [OUTPUT-CONTRACT.md](OUTPUT-CONTRACT.md):

- `Collections/[CompanyName]/brief.txt` — Research Summary, Keyword Research, Collection Strategy, Structured data reminder, Discovered Products.
- `Collections/[CompanyName]/shopify-de.txt` — 7 banner blocks (title, descriptionHtml, handle, image, image.altText, seo.title, seo.description).
- `Collections/[CompanyName]/shopify-en.txt` — 4 banner blocks (title, descriptionHtml, seo.title, seo.description).

The skill never fetches or verifies anything on yuliskin.de. YuliSkin (full name
YuliSkin Kosmetik Studio / YuliSkin Cosmetic Studio) is only the destination store
the copy is written for — name it in the copy, do not crawl it.

### Pass 2 — Logo download

Cascade until a usable logo is downloaded, stop at first success:

1. Brand homepage `<head>`: `<link rel="apple-touch-icon">`, `og:image`, `twitter:image`
2. JSON-LD `Organization.logo`
3. `/press`, `/media`, `/presse` pages
4. First `<img>` or inline `<svg>` in homepage `<header>` whose alt/filename/class
   contains `logo`, `brand`, or the company name
5. Wikipedia infobox image (last resort)
6. Graceful fail: leave file out, set `logo_status: missing` in Research Summary,
   tell the user. Do not download a placeholder.

Format priority: SVG → PNG (with transparency) → WebP → JPG. Reject images smaller
than 200×200 (SVG is exempt). Save as `Collections/[CompanyName]/[CompanyName]-logo.[ext]`
preserving source extension.

### Pass 3 — Product discovery (manifest)

Try these strategies in order, stop at first that yields ≥ 5 products:

1. `/sitemap.xml` and `/sitemap_products.xml` — filter URLs whose path looks like a
   product (`/product/`, `/products/`, `/shop/`, `/p/`).
2. JSON-LD `ItemList` / `Product` entities on homepage and main listing pages.
3. HTML scrape of `/shop`, `/products`, `/all-products`, `/store`, `/catalogue`,
   `/produkte`, `/boutique`.
4. Playwright fallback for JS-rendered sites.
5. If all fail: write empty `products.csv` (header only), set discovery status to
   `failed` in the brief, tell the user to paste product URLs manually.

Hard cap: **50 unique product URLs.** Normalize URLs before dedup (lowercase host,
strip trailing slash, strip tracking query params).

**Manifest exclusion list (drop these URLs at discovery time):**

| Pattern                  | Examples                                                           |
| ------------------------ | ------------------------------------------------------------------ |
| Gift cards / vouchers    | `gift-card`, `geschenkgutschein`, `voucher`, `e-gift`              |
| Free samples             | `sample`, `sachet`, `probe`, `try-me` (when sold separately)       |
| Services / consultations | `consultation`, `beratung`, `appointment`, `treatment-booking`     |
| Editorial                | `/blog/`, `/journal/`, `/magazine/`, `/news/`, `/article/`         |
| Brand pages              | `/about`, `/contact`, `/store-locator`, `/faq`, `/legal`, `/press` |
| Loyalty / accounts       | `/account`, `/login`, `/loyalty`, `/rewards`                       |
| Empty / placeholder      | Page title empty, contains "404", "page not found", "coming soon"  |
| Pure category landing    | URL ends in `/collections/...` with no product slug                |

**Kept but flagged in the brief.txt summary line:**

- Sets / kits / bundles (URL or title contains `set`, `kit`, `bundle`, `routine`, `duo`, `trio`)
- Size or shade variants of the same product (URL stem identical except trailing variant segment)

Write `Collections/[CompanyName]/products.csv` with header `product_name,product_url`.
CSV is the source of truth; the Markdown table inside `brief.txt`'s Discovered Products
section is a preview.

## Re-run behavior

When `Collections/[CompanyName]/` already exists:

| Artifact                        | Rule                                                                                                                                                                                                                               |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `brief.txt`                     | Overwrite.                                                                                                                                                                                                                         |
| `shopify-de.txt`                | Overwrite. Regenerate atomically alongside `brief.txt` and `shopify-en.txt`.                                                                                                                                                       |
| `shopify-en.txt`                | Overwrite. Regenerate atomically alongside `brief.txt` and `shopify-de.txt`.                                                                                                                                                       |
| Logo                            | Overwrite only if a new download succeeds. On failure keep existing and set `logo_status: kept_existing`.                                                                                                                          |
| `products.csv`                  | **Merge.** Read existing rows, run discovery, union on normalized `product_url`, add a `discovered_at` ISO date column (existing rows keep their original date, new rows get today's). Never silently delete rows the user pruned. |
| Markdown preview in `brief.txt` | Regenerate from the merged CSV.                                                                                                                                                                                                    |

Print a re-run summary block at the end:

```text
Re-run summary for Collections/[CompanyName]/:
  brief.txt:       overwritten
  shopify-de.txt:  overwritten
  shopify-en.txt:  overwritten
  logo:            refreshed | kept_existing | missing
  products.csv:    N existing rows kept, M new rows added, 0 removed
  → New rows: <name>, <name>, <name>
```

## Closing prompt (always print last)

```text
Manifest written to Collections/[CompanyName]/products.csv (N rows).
Review the CSV and delete any rows you don't want to research, then reply with:

  Run product-research for all rows in Collections/[CompanyName]/products.csv,
  3 in parallel, skip products whose brief.txt already exists.

To change concurrency, replace "3" with another number (e.g. 5 or 10).
```

## Validation

Before returning, verify:

- `Collections/[CompanyName]/brief.txt`, `shopify-de.txt`, and `shopify-en.txt` were all written in the same run.
- `Collections/[CompanyName]/products.csv` was created (header row present even if 0 data rows).
- Logo file was saved, OR `logo_status: missing` is set in `brief.txt` Research Summary AND the `=== image ===` banner in `shopify-de.txt` contains the literal value `MISSING — set collection image manually`.
- `brief.txt` contains Research Summary, Keyword Research, Collection Strategy, Structured data reminder, and Discovered Products — and contains no Shopify-pasteable values.
- `shopify-de.txt` contains the header block plus all 7 banners in the order defined in [OUTPUT-CONTRACT.md](OUTPUT-CONTRACT.md).
- `shopify-en.txt` contains the header block plus all 4 banners in the order defined in [OUTPUT-CONTRACT.md](OUTPUT-CONTRACT.md).
- Every banner uses the exact GraphQL path documented in the contract (`=== title ===`, `=== descriptionHtml ===`, `=== handle ===`, etc.).
- Every banner has at least one `# Admin UI:` comment line.
- `descriptionHtml` uses allowed HTML and no `<h1>` in both Shopify files.
- `seo.title` ≤ 70 characters in both Shopify files.
- `seo.description` ≤ 160 characters in both Shopify files.
- `handle` is lowercase, hyphenated, ASCII-only.
- German fields preserve real German characters (ä/ö/ü/ß); ASCII transliteration appears only in `handle` and file/folder names — including in the brief's German keyword research.
- Discovered Products section in `brief.txt` reports: total discovered, total excluded by category, total flagged (sets/variants), final manifest row count.
- On re-run, the re-run summary block is printed.
- The closing "next prompt" block is the last thing printed.

See [OUTPUT-CONTRACT.md](OUTPUT-CONTRACT.md) for the full file specs and per-banner rules.
