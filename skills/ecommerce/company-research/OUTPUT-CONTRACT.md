# Company Research Output Contract

Use this contract when generating `Collections/[CompanyName]/brief.txt` for YuliSkin
collection-page research output. The brief is research-first: Research Summary, Keyword
Research, and Collection Strategy are required foundation sections, and all Shopify-ready
collection fields, descriptions, meta titles, meta descriptions, and related collections
must be derived from them.

## File Outputs

```text
Collections/[CompanyName]/brief.txt
Collections/[CompanyName]/products.csv
Collections/[CompanyName]/[CompanyName]-logo.[ext]   # optional, may be missing
```

`products.csv` schema:

```csv
product_name,product_url,discovered_at
```

`discovered_at` is the ISO date (`YYYY-MM-DD`) the row was first added. On a fresh run
all rows get today's date; on a re-run, existing rows keep their original date and only
new rows get today's date.

## Required brief.txt Structure

```text
1. Research Summary
2. Keyword Research
3. Collection Strategy

German
1. Title
2. Description HTML
3. Collection image (path to local logo file)
4. Image ALT options
5. Collection handle (lowercase-hyphenated)
6. Related collections
7. Meta title
8. Meta description

English
1. Title
2. Description HTML
3. Meta title
4. Meta description

Supporting sections
1. Structured data reminder
2. Discovered Products
   - Discovery summary line (total found, excluded by category, flagged sets/variants, final count)
   - Markdown table preview of products.csv
   - Re-run summary block (only when folder already existed)
```

The German section contains the full Shopify collection setup fields. The English
section contains translated Shopify-facing content fields only.

Do not generate the German, English, or supporting sections until Research Summary,
Keyword Research, and Collection Strategy are complete.

## Strategy Sections

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
marketplaces, retailer sites, brand sites, and YuliSkin search/category logic. Provide
German and English keyword directions grouped by intent:

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

Plain text. Summarize why YuliSkin carries this brand, who it's for, which ingredients
matter, and how the collection page should be angled.

Use this format:

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

The description, meta title, meta description, related collections, and Shopify field
choices must follow this strategy.

## Shopify Field Rules

### Title

The collection title shown at the top of the Shopify collection page. Usually the
brand name as customers know it (`BABOR`, `La Roche-Posay`, `Dr. Hauschka`). Keep
the brand's own typography conventions (uppercase, spacing).

### Description HTML

- Allowed tags: `<h2>`, `<h3>`, `<p>`, `<ul>`, `<li>`, `<a href="">` (verified URLs only).
- Forbidden: `<h1>` (Shopify renders the collection title as the H1).
- Structure suggestion: one `<h2>` per major angle (brand origin / philosophy, hero
  ingredients, who it's for, routine coverage), short `<p>` blocks, `<ul>` lists for
  certifications or hero ingredients.
- Tone: German uses formal `Sie`. English uses polished, neutral ecommerce language.
- Must be derived from verified facts in Research Summary and the Collection Strategy.

### Collection image

Local path to the downloaded logo file:
`Collections/[CompanyName]/[CompanyName]-logo.[ext]`. If `logo_status: missing`, leave
this field blank and add a note: `Set collection image manually.`

### Image ALT options

English only, regardless of language section. Provide 2–3 ALT options that include
brand name + visible angle ("BABOR brand logo on white background", "BABOR Doctor
Babor skincare brand mark"). Same convention as `product-research`.

### Collection handle

Lowercase, hyphenated, ASCII-only. Strip diacritics, apostrophes, periods. Examples:

| Brand name       | Handle           |
| ---------------- | ---------------- |
| `BABOR`          | `babor`          |
| `Dr. Hauschka`   | `dr-hauschka`    |
| `La Roche-Posay` | `la-roche-posay` |
| `L'Oréal Paris`  | `loreal-paris`   |
| `MartiDerm`      | `martiderm`      |

### Related collections

Up to 5 entries. For each, prefer a verified YuliSkin collection URL. If a URL cannot
be verified on yuliskin.de, output the plain collection name without a link. Pick
related collections by hero ingredient, concern, routine step, or price tier.
Do not include the same collection. Do not invent URLs.

### Meta title

- Max 70 characters.
- Must contain the brand name.
- May contain one primary keyword from Keyword Research.

### Meta description

- Max 160 characters.
- Must reflect Meta Direction from the Collection Strategy.
- Must be customer-facing, claim-safe, and use verified facts only.

## Writing Rules

- Store: YuliSkin.
- Store languages: German and English.
- German first, then English.
- German uses formal address with `Sie`.
- English uses polished, neutral ecommerce language.
- Use the strongest relevant keywords naturally; do not force every keyword into copy.
- Claims must remain cosmetic and evidence-aware. Avoid medical promises such as
  curing acne, healing rosacea, or treating disease.
- Customer-facing sections must use only verified facts. Unknown facts may appear
  in Research Summary but must not appear in Description HTML, meta fields, or
  related-collection rationale.

## Supporting Sections

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
  brief.txt:    overwritten
  logo:         refreshed | kept_existing | missing
  products.csv: N existing rows kept, M new rows added, 0 removed
  → New rows: <name>, <name>, <name>
```

## Validation Checklist

Before returning the final answer, check:

- The file was created at `Collections/[CompanyName]/brief.txt`.
- `Collections/[CompanyName]/products.csv` exists with header row.
- Logo was saved, OR `logo_status: missing` is recorded in Research Summary.
- Research Summary, Keyword Research, and Collection Strategy appear before the German block.
- German and English sections are separated; no section mixes languages.
- Description HTML has no `<h1>`.
- Meta titles ≤ 70 characters in both languages.
- Meta descriptions ≤ 160 characters in both languages.
- Related collections are either verified YuliSkin URLs or plain names with no link.
- Discovered Products summary line reports total found, excluded breakdown, flagged
  sets/variants count, and final manifest count.
- On a re-run, the re-run summary block is printed.
- The closing "next prompt" block is the last thing printed.
- Unknown facts are excluded from customer-facing sections.
