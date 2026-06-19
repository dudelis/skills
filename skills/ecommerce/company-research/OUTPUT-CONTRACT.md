# Company Research Output Contract

Use this contract when generating company-research output for `yuliskin.de`. The
deliverables are split into a research file plus two Shopify-ready collection files
and a logo image. The research file (`brief.txt`) is the thinking layer. The Shopify
files (`shopify-de.txt`, `shopify-en.txt`) are the copy-paste layer — every value in
them must be derived from the research file.

## File Outputs

```text
Collections/[CompanyName]/brief.txt
Collections/[CompanyName]/shopify-de.txt
Collections/[CompanyName]/shopify-en.txt
Collections/[CompanyName]/products.csv
Collections/[CompanyName]/[CompanyName]-logo.[ext]   # optional, may be missing
```

`products.csv` schema:

```csv
product_name,product_url,discovered_at
```

`discovered_at` is the ISO date (`YYYY-MM-DD`) the row was first added. On a fresh
run all rows get today's date; on a re-run, existing rows keep their original date
and only new rows get today's date.

Generate `brief.txt`, `shopify-de.txt`, and `shopify-en.txt` in a single run. If a
re-run is requested, regenerate all three atomically (do not leave stale Shopify
files alongside a new brief).

## brief.txt — Research File

Plain text. Contains only the thinking layer plus the structured-data reminder and
the discovered-products manifest preview. No Shopify-pasteable values live here.

### brief.txt structure

```text
1. Research Summary
2. Keyword Research
3. Collection Strategy
4. Structured data reminder
5. Discovered Products
   - Discovery summary line (total found, excluded by category, flagged sets/variants, final count)
   - Markdown table preview of products.csv
   - Re-run summary block (only when folder already existed)
```

### Research Summary

Plain text. Include verified facts and unknown facts:

```text
Brand name:
Legal entity / parent company:
Founding year:
Country of origin / HQ:
Brand category:               # e.g. dermocosmetics, clean beauty, pharmacy skincare
Brand philosophy:             # paraphrased, not copy-pasted
Hero ingredient(s) / signature technology:
Target customer:
Target skin concerns:
Product range overview:       # categories the brand sells
Certifications:               # vegan, cruelty-free, dermatologist-tested, organic, made in EU, etc.
Distribution context in DE:   # pharmacy-only, online-only, salon brand, etc.
Logo status:                  # downloaded | kept_existing | missing
Verified source URLs:
Verified YuliSkin URLs:
Pages fetched (Pass 1):       # which brand-info pages returned 200
Pages missing (Pass 1):       # which 404'd
Unknown facts:
```

### Keyword Research

Plain text. Research how customers search for this brand and its products in Google,
marketplaces, retailer sites, brand sites, and YuliSkin search/category logic.
Provide German and English keyword directions grouped by intent:

```text
German keywords:
Brand name searches:
Brand + product category:
Brand + skin concern:
Brand + benefit:
Brand + ingredient:
Brand comparison ("[Brand] vs ..."):
Buyer intent:
Search intent summary:
Primary keyword direction:
Secondary keyword direction:
Long-tail opportunities:
Terms to avoid:

English keywords:
Brand name searches:
Brand + product category:
Brand + skin concern:
Brand + benefit:
Brand + ingredient:
Brand comparison ("[Brand] vs ..."):
Buyer intent:
Search intent summary:
Primary keyword direction:
Secondary keyword direction:
Long-tail opportunities:
Terms to avoid:
```

Do not keyword-stuff. Use keyword research to shape natural collection title,
description HTML, meta title, meta description, image ALT options, related-collection
logic, and Shopify field choices.

### Collection Strategy

Plain text:

```text
Collection Strategy
Why YuliSkin carries this brand:
Target Customer:
Target Concerns:
Hero Ingredients:
Routine Coverage:                # which routine steps the brand covers across its range
Keyword Direction DE:
Keyword Direction EN:
Description Direction DE:
Description Direction EN:
Meta Direction DE:
Meta Direction EN:
Related Collections Logic:       # by hero ingredient, concern, routine step, or price tier
Claim Boundaries:                # what can/cannot be promised
```

The description, meta title, meta description, related collections, and Shopify
field choices in both `shopify-de.txt` and `shopify-en.txt` must follow this strategy.

### Structured data reminder

A short reminder block listing the Shopify schema fields the merchant must populate
in Shopify Admin (title, description, image, handle, meta title, meta description)
plus a note to verify related-collection links resolve.

### Discovered Products

```text
Discovery: N product URLs found, M excluded (breakdown by category: blog, about, gift card, ...).
Manifest: N - M rows.
Heads-up: X rows look like sets/kits/bundles, Y rows look like size/shade variants — review before fan-out.

| product_name | product_url |
| --- | --- |
| ... | ... |
```

The Markdown table is a preview only. `products.csv` is the source of truth used by
the second prompt that fans out to `product-research`.

### Re-run summary (only when folder already existed)

```text
Re-run summary for Collections/[CompanyName]/:
  brief.txt:       overwritten
  shopify-de.txt:  overwritten
  shopify-en.txt:  overwritten
  logo:            refreshed | kept_existing | missing
  products.csv:    N existing rows kept, M new rows added, 0 removed
  → New rows: <name>, <name>, <name>
```

## Shopify Files — Banner Format

Both `shopify-de.txt` and `shopify-en.txt` use the same banner format. One field per
block. Each block has three parts:

```text
=== <shopify-field-path> ===
# Admin UI: <visible label> | <validation/hint notes>
<value to paste into Shopify>
```

- Banner = Shopify Admin GraphQL field path. Future Shopify automation parses these.
- Comment line = human-readable Admin UI label plus validation hints. Multiple
  comment lines are allowed; each must start with `#`.
- Value = the actual content to paste into Shopify Admin. May be multi-line.

Both files start with a header block that names the locale.

## shopify-de.txt — German Locale (default)

### shopify-de.txt — File Header

The file starts with this exact header block:

```text
# Shopify collection fields — German locale (default)
# Banner format: === <shopify-field-path> ===
# Comment lines start with #. Paste each value into the matching field in Shopify Admin.
# Banner paths use Shopify GraphQL field names so future automation can parse this file.
```

### shopify-de.txt — Banner Order

Generate the banners in this exact order:

```text
1. === title ===
2. === descriptionHtml ===
3. === handle ===
4. === image ===
5. === image.altText ===
6. === seo.title ===
7. === seo.description ===
8. === related_collections ===
```

### shopify-de.txt — Per-Banner Specifications

#### `=== title ===`

```text
# Admin UI: Title
```

Usually the brand name as customers know it (`BABOR`, `La Roche-Posay`,
`Dr. Hauschka`). Keep the brand's own typography conventions (uppercase, spacing).

#### `=== descriptionHtml ===`

```text
# Admin UI: Description | Paste in HTML/Source view, not Rich Text
```

HTML only. Allowed tags: `<h2>`, `<h3>`, `<p>`, `<ul>`, `<li>`, and verified
`<a href="">` links. Do not use `<h1>` (Shopify renders the collection title as H1).

Structure suggestion: one `<h2>` per major angle (brand origin / philosophy, hero
ingredients, who it's for, routine coverage), short `<p>` blocks, `<ul>` lists for
certifications or hero ingredients.

Tone: German uses formal `Sie`. Must be derived from verified facts in `brief.txt`
Research Summary and Collection Strategy.

#### `=== handle ===`

```text
# Admin UI: URL handle | Lowercase, hyphenated, ASCII-only
```

Strip diacritics, apostrophes, periods. Examples:

| Brand name       | Handle           |
| ---------------- | ---------------- |
| `BABOR`          | `babor`          |
| `Dr. Hauschka`   | `dr-hauschka`    |
| `La Roche-Posay` | `la-roche-posay` |
| `L'Oréal Paris`  | `loreal-paris`   |
| `MartiDerm`      | `martiderm`      |

#### `=== image ===`

```text
# Admin UI: Collection image | Upload from local file
```

Local path to the downloaded logo file relative to the workspace root:
`Collections/[CompanyName]/[CompanyName]-logo.[ext]`. If `logo_status: missing` in
`brief.txt`, output the literal value `MISSING — set collection image manually` and
keep the banner in place so the file structure stays consistent.

#### `=== image.altText ===`

```text
# Admin UI: Image alt text | English only
```

Provide 2 to 3 ALT options that include brand name + visible angle ("BABOR brand
logo on white background", "BABOR Doctor Babor skincare brand mark"). One per line.

#### `=== seo.title ===`

```text
# Admin UI: SEO title | Max 70 chars | Must contain the brand name
```

May contain one primary keyword from Keyword Research.

#### `=== seo.description ===`

```text
# Admin UI: SEO description | Max 160 chars | Customer-facing, claim-safe, verified facts only
```

Must reflect Meta Direction from the Collection Strategy.

#### `=== related_collections ===`

```text
# Admin UI: Related collections | Not a native collection field
# Configure via Shopify navigation menu, theme blocks, or a "Related collections"
# metafield if your theme supports one. Reference list below — verified YuliSkin
# URLs or plain collection names with no link.
```

Up to 5 entries, one per line. For each, prefer a verified YuliSkin collection URL.
If a URL cannot be verified on yuliskin.de, output the plain collection name without
a link. Pick related collections by hero ingredient, concern, routine step, or price
tier. Do not include the same collection. Do not invent URLs.

## shopify-en.txt — English Locale (translated)

### shopify-en.txt — File Header

The file starts with this exact header block:

```text
# Shopify collection fields — English locale (translated)
# Banner format: === <shopify-field-path> ===
# Use these values in Shopify's Translate & Adapt app or any English-locale storefront.
# Fields not in this file (handle, image, related collections) reuse the values from
# shopify-de.txt.
```

### shopify-en.txt — Banner Order

Generate the banners in this exact order:

```text
1. === title ===
2. === descriptionHtml ===
3. === seo.title ===
4. === seo.description ===
```

### shopify-en.txt — Per-Banner Specifications

#### `=== title ===`

```text
# Admin UI (EN locale): Title | Same as DE unless the brand uses a different English form
```

#### `=== descriptionHtml ===`

```text
# Admin UI (EN locale): Description | Paste in HTML/Source view, not Rich Text
```

Same HTML rules as DE. English uses polished, neutral ecommerce language. Must be
derived from verified facts and Collection Strategy.

#### `=== seo.title ===`

```text
# Admin UI (EN locale): SEO title | Max 70 chars | Must contain the brand name
```

#### `=== seo.description ===`

```text
# Admin UI (EN locale): SEO description | Max 160 chars | Customer-facing, claim-safe, verified facts only
```

## Writing Rules

- Store: YuliSkin.
- Store languages: German and English.
- German uses formal address with `Sie`.
- English uses polished, neutral ecommerce language.
- Use the strongest relevant keywords naturally; do not force every keyword into copy.
- Claims must remain cosmetic and evidence-aware. Avoid medical promises such as
  curing acne, healing rosacea, or treating disease.
- Customer-facing values (Shopify files) must use only verified facts. Unknown facts
  may appear in `brief.txt` Research Summary but must not appear in any Shopify-file
  value.

## Validation Checklist

Before returning, verify:

- `Collections/[CompanyName]/brief.txt`, `shopify-de.txt`, and `shopify-en.txt` were all written in the same run.
- `Collections/[CompanyName]/products.csv` exists with header row.
- Logo was saved, OR `logo_status: missing` is recorded in `brief.txt` Research Summary AND the `=== image ===` banner in `shopify-de.txt` contains the literal value `MISSING — set collection image manually`.
- `brief.txt` contains Research Summary, Keyword Research, Collection Strategy, Structured data reminder, and Discovered Products — and contains no Shopify-pasteable values.
- `shopify-de.txt` contains the header block plus all 8 banners in the documented order.
- `shopify-en.txt` contains the header block plus all 4 banners in the documented order.
- Every banner uses the exact GraphQL path documented above.
- Every banner has at least one `# Admin UI:` comment line.
- `descriptionHtml` uses allowed HTML and no `<h1>` in both Shopify files.
- `seo.title` ≤ 70 characters in both Shopify files.
- `seo.description` ≤ 160 characters in both Shopify files.
- `handle` is lowercase, hyphenated, ASCII-only.
- `related_collections` entries are either verified YuliSkin URLs or plain names with no link.
- Discovered Products summary line in `brief.txt` reports total found, excluded breakdown, flagged sets/variants count, and final manifest count.
- On a re-run, the re-run summary block is printed.
- The closing "next prompt" block is the last thing printed (per the skill).
- Unknown facts appear only in `brief.txt` Research Summary, never in the Shopify files.
