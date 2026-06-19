# Product Research Output Contract

Use this contract when generating product-research output for `yuliskin.de`. The
deliverables are split into three text files plus image downloads. The research file
(`brief.txt`) is the thinking layer. The Shopify files (`shopify-de.txt`,
`shopify-en.txt`) are the copy-paste layer — every value in them must be derived
from the research file.

## File Outputs

```text
Products/[CompanyName]/[ProductName]/brief.txt
Products/[CompanyName]/[ProductName]/shopify-de.txt
Products/[CompanyName]/[ProductName]/shopify-en.txt
Products/[CompanyName]/[ProductName]/[CompanyName]-[ProductName]-01.[ext]
Products/[CompanyName]/[ProductName]/[CompanyName]-[ProductName]-02.[ext]
Products/[CompanyName]/[ProductName]/[CompanyName]-[ProductName]-03.[ext]
Products/[CompanyName]/[ProductName]/[CompanyName]-[ProductName]-04.[ext]
Products/[CompanyName]/[ProductName]/[CompanyName]-[ProductName]-05.[ext]
```

Image rules:

- Prioritize source order: official brand/product page, distributor page, then competitor page.
- Download 2 to 5 images when available.
- Use only images that clearly match the exact product.
- Prefer primary product packshots and key gallery images.
- Skip logos, banners, watermarked ads, and unrelated lifestyle images.
- Preserve source extension when possible (`.jpg`, `.jpeg`, `.png`, `.webp`).

Generate all three text files in a single run. If a re-run is requested, regenerate
all three atomically (do not leave stale Shopify files alongside a new brief).

## brief.txt — Research File

Plain text. Contains only the thinking layer plus the structured-data reminder. No
Shopify-pasteable values live here.

### brief.txt structure

```text
1. Research Summary
2. Keyword Research
3. Product Strategy
4. Structured data reminder
```

### Research Summary

Plain text. Include verified facts and unknown facts:

```text
Product type:
Texture:
Routine position:
Hero ingredients:
Verified claims:
Target concerns:
Skin feel / customer outcome:
Vendor:
Variant volume:
Product weight:
Country of origin:
HS code:
DHL customs description:
SKU:
Barcode / GTIN / UPC / ISBN:
Verified source URLs:
Verified YuliSkin URLs:
Unknown facts:
```

### Keyword Research

Plain text. Research how customers search for this exact product and similar products
in Google, marketplaces, retailer sites, brand sites, YuliSkin search/category logic,
and other search systems. Provide German and English keyword directions grouped by
intent:

```text
German keywords:
Brand + product:
Product type:
Skin concern:
Benefit:
Active ingredient / formulation:
Routine step:
Buyer intent:
Search intent summary:
Primary keyword direction:
Secondary keyword direction:
Long-tail opportunities:
Terms to avoid:

English keywords:
Brand + product:
Product type:
Skin concern:
Benefit:
Active ingredient / formulation:
Routine step:
Buyer intent:
Search intent summary:
Primary keyword direction:
Secondary keyword direction:
Long-tail opportunities:
Terms to avoid:
```

Do not keyword-stuff. Use keyword research to shape natural headings, description
HTML, meta title, meta description, image ALT options, related-product logic, and
Shopify field choices.

### Product Strategy

Plain text:

```text
Product Strategy
Product Type:
Target Customer:
Target Concerns:
Hero Ingredients:
Texture:
Routine Position:
Routine Logic:
Keyword Direction DE:
Keyword Direction EN:
Description Direction DE:
Description Direction EN:
Meta Direction DE:
Meta Direction EN:
Related Product Logic:
Claim Boundaries:
```

The description, effect, meta title, meta description, related products, and Shopify
field choices in both `shopify-de.txt` and `shopify-en.txt` must follow this strategy.

### Structured data reminder

Plain text. Mention useful Product and BreadcrumbList schema fields:

```text
Product schema:
Brand:
SKU / product code:
Description:
Images:
Offers:
Price / currency:
Availability:
Reviews / aggregateRating:
BreadcrumbList:
Canonical / hreflang:
Manual verification:
```

Use reviews or aggregateRating only if real review data exists.

## Shopify Files — Banner Format

Both `shopify-de.txt` and `shopify-en.txt` use the same banner format. One field per
block. Each block has three parts:

```text
=== <shopify-field-path> ===
# Admin UI: <visible label> | <validation/hint notes>
<value to paste into Shopify>
```

- Banner = Shopify Admin GraphQL field path. Future Shopify automation parses these.
- Comment line = human-readable Admin UI label plus validation hints (max chars,
  format, allowed values). Multiple comment lines are allowed; each must start with `#`.
- Value = the actual content to paste into Shopify Admin. May be multi-line.

Both files start with a header block that names the locale and reminds the user how
to use it. See section "shopify-de.txt — File Header" and "shopify-en.txt — File
Header" below for exact text.

### Standard system metafields

`metafields.shopify.<key>` are Shopify's built-in standard metafield definitions.
`metafields.shopify--discovery--product_recommendation.related_products` is Shopify's
standard "Related products" metafield (list of product references).

### Custom metafields (YuliSkin store)

| Banner path                                            | Definition type        |
| ------------------------------------------------------ | ---------------------- |
| `metafields.custom.application`                        | Multi-line text        |
| `metafields.custom.effect`                             | Multi-line text        |
| `metafields.custom.ingredients`                        | Multi-line text        |
| `metafields.custom.skin_application_areas`             | List of `body_area`    |
| `metafields.custom.skin_problem`                       | List of `skin_problem` |
| `metafields.custom.skin_type`                          | List of `skin_types`   |
| `variants[0].metafields.dhlapp.customsItemDescription` | Variant-level text     |

### Keyword reuse rule (applies to both locale files)

Keyword Research is the reason research runs first. The terms it produces must
show up in the customer-facing prose of every Shopify file — woven into natural
sentences, never bolted on as a list, label row, or visible tag block.

**Where keywords must appear naturally:**

- `=== descriptionHtml ===` (Main Description) — inside `<h2>` / `<h3>` headings
  and `<p>` body copy, plus inside the labelled `<li>` text where it reads
  naturally. Headings and section intros are the highest-value placements.
- `=== seo.description ===` (Meta Description) — weave the primary keyword and
  one secondary keyword into the sentence; do not stuff.
- `=== seo.title ===` (Meta Title) — the third "Catchy SEO phrase" segment
  carries the strongest keyword.
- `=== metafields.custom.application ===` — inside the labelled prose values
  (e.g. `Step 1:`, `Frequency:`), not as a separate keyword line.
- `=== metafields.custom.effect ===` — inside the labelled prose values
  (`Visible effect:`, `Best for:`), not as a separate keyword line.
- `=== metafields.custom.ingredients ===` — inside the customer-facing prose
  describing what each ingredient does.
- `=== media[].alt ===` — inside natural ALT sentences.

**Per-locale source of keywords:**

- `shopify-de.txt` reuses **Keyword Direction DE** (Primary keyword direction,
  Secondary keyword direction, Long-tail opportunities) from `brief.txt`.
- `shopify-en.txt` reuses **Keyword Direction EN** with the same logic.

**Hard rules:**

- Aim for the primary keyword to appear once in `descriptionHtml`, once in
  `seo.title`, and once in `seo.description`. Aim for two to four secondary or
  long-tail keywords across the rest of the description and the application,
  effect, and ingredients prose.
- Use `Terms to avoid` from Keyword Research as an exclusion list; never use
  those terms in any Shopify file.
- Do not output a visible "Keywords:", "Tags:", or comma-separated keyword line
  inside any banner value. Keywords are signal for prose only.
- Do not keyword-stuff. Each keyword must read as natural German or English in
  context; if a sentence sounds robotic, drop the keyword.
- Translation, not copy-paste: EN keywords are pulled from Keyword Direction EN,
  not transliterated from the DE keyword list.

## shopify-de.txt — German Locale (default)

### shopify-de.txt — File Header

The file starts with this exact header block:

```text
# Shopify product fields — German locale (default)
# Banner format: === <shopify-field-path> ===
# Comment lines start with #. Paste each value into the matching field in Shopify Admin.
# Banner paths use Shopify GraphQL field names so future automation can parse this file.
```

### shopify-de.txt — Banner Order

Generate the banners in this exact order:

```text
1.  === title ===
2.  === descriptionHtml ===
3.  === productType ===
4.  === vendor ===
5.  === variants[0].title ===
6.  === variants[0].sku ===
7.  === variants[0].barcode ===
8.  === variants[0].weight ===
9.  === metafields.shopify.country_of_origin ===
10. === metafields.shopify.harmonized_system_code ===
11. === variants[0].metafields.dhlapp.customsItemDescription ===
12. === metafields.shopify--discovery--product_recommendation.related_products ===
13. === metafields.custom.application ===
14. === metafields.custom.effect ===
15. === metafields.custom.ingredients ===
16. === metafields.custom.skin_application_areas ===
17. === metafields.custom.skin_problem ===
18. === metafields.custom.skin_type ===
19. === seo.title ===
20. === seo.description ===
21. === media[].alt ===
```

### shopify-de.txt — Per-Banner Specifications

#### `=== title ===`

```text
# Admin UI: Title
```

Use the product name as it should appear in Shopify.

#### `=== descriptionHtml ===`

```text
# Admin UI: Description | Paste in HTML/Source view, not Rich Text
```

HTML only. Allowed tags: `<h2>`, `<h3>`, `<p>`, `<ul>`, `<li>`, and verified
`<a href="">` links. Do not use `<h1>` (Shopify renders the product title as H1).

Must include: product name and company, product type, main skin concern or use case,
key benefits, exact verified hero ingredients, texture when verified, routine fit,
internal YuliSkin links only when URLs are verified.

Follow Product Strategy, Description Direction DE, Keyword Direction DE, and Claim
Boundaries. Do not write a generic category description.

#### `=== productType ===`

```text
# Admin UI: Product type | Single value
```

Choose exactly one product type. Prefer one of these existing Shopify values:

```text
Augenpflege, Brush, Cleanser, Concentrate, Creme, Gel, Geschenkset, Gesichtsgerät,
Haarpflege, Heimpflegeset, Körperpflege, Lippenpflege, Maske, Nachtcreme, Oil,
Online consultation, Other, Peeling, Produktset, Serum, Sonnenschutz, Spot Gel,
Tagescreme, Tonic
```

If no existing value fits, output one proposed new value and add a note in
`brief.txt` Research Summary that the Shopify product type must be created.

#### `=== vendor ===`

```text
# Admin UI: Vendor
```

Use the producer or brand/company name.

#### `=== variants[0].title ===`

```text
# Admin UI: Variant title (volume) | Normalized lowercase units (50 ml, 100 g, 1 l, 10 pcs)
```

Use `pcs` only when the product is genuinely sold by count. Preserve exact source
packaging wording in `brief.txt` Research Summary if it differs from the normalized
value.

#### `=== variants[0].sku ===`

```text
# Admin UI: SKU | Output "Unknown" if not verified
```

Verify SKU from official sources, distributors, competitor Shopify shops, provided
links, packaging images, or credible retailer data. Never infer.

#### `=== variants[0].barcode ===`

```text
# Admin UI: Barcode (ISBN, UPC, GTIN, ...) | Output "Unknown" if not verified
```

Same verification rules as SKU. Never infer barcode values.

#### `=== variants[0].weight ===`

```text
# Admin UI: Weight | In grams | Fallback: volume_ml + 50g if unverified
```

Rules:

- If exact product or shipping weight is verified, use the verified weight.
- If only volume is known, estimate as the numeric ml amount plus 50 g.
- If contents are already in g, estimate as contents weight plus 50 g.
- Do not include the DHL parcel box weight.
- Do not output calculation notes in the value; put uncertainty in `brief.txt`.

Examples: `30 ml → 80`, `50 ml → 100`, `150 ml → 200`, `500 ml → 550`, `100 g → 150`.

#### `=== metafields.shopify.country_of_origin ===`

```text
# Admin UI: Country/Region of origin | Standard system metafield | ISO 3166-1 alpha-2 country code
```

Use the brand's declared commercial country of origin. If it cannot be verified,
output `Unknown` and note the uncertainty in `brief.txt`.

Known brand mappings when source research supports them: `GIGI → IL`,
`Meder → CH`, `Dr. Medion → JP` (if confirmed).

#### `=== metafields.shopify.harmonized_system_code ===`

```text
# Admin UI: HS code | Standard system metafield
```

Rules:

- Default for skincare cosmetics: `33049900`.
- Haircare: `33059000`.
- Sunscreen / sun protection: `33049900` unless source says otherwise.
- Brushes, tools, devices: classify separately; do not force the cosmetics code.
- Gift sets: use the dominant item's HS code when clearly skincare-only; otherwise
  mark for manual review in `brief.txt`.

#### `=== variants[0].metafields.dhlapp.customsItemDescription ===`

```text
# Admin UI (Variant level): DHL customs item description | English only | Max 30 chars | Plain customs wording, not marketing copy
```

Examples: `Face cream`, `Face serum`, `Cleanser`, `Eye cream`, `Sunscreen`,
`Cosmetic set`, `Face brush`, `Skin care device`.

#### `=== metafields.shopify--discovery--product_recommendation.related_products ===`

```text
# Admin UI: Related products | Standard system metafield | List of products | One per line, YuliSkin product handle or full URL
```

Select complementary products from the same company on YuliSkin whenever possible.
Verify YuliSkin URLs before linking. If the product does not exist on YuliSkin yet,
write the plain product name on its own line (no URL).

Rules:

- Do not recommend the same product.
- Do not recommend products only because they share the company name.
- Use strict routine or concern logic.

Routine patterns:

```text
Cleanser / preparation → serum / treatment → concentrate / cream / maintenance
Preparation → treatment → hydration / soothing / brightening / maintenance
Mask / treatment → serum / cream / protection
```

#### `=== metafields.custom.application ===`

```text
# Admin UI: Application | Multi-line text | Labelled lines
```

Format:

```text
Schritt 1:
Schritt 2:
Schritt 3:
Häufigkeit:
Routine-Hinweis:
Vorsichtsmaßnahme:
```

Include amount, frequency, routine sequence, application area, whether to rinse, and
precautions when verified. Mark unknowns only in `brief.txt`, not here.

#### `=== metafields.custom.effect ===`

```text
# Admin UI: Effect | Multi-line text | Labelled lines | Compliant cosmetic language
```

Format:

```text
Sichtbarer Effekt:
Textur-Effekt:
Komfort-Effekt:
Geeignet für:
```

#### `=== metafields.custom.ingredients ===`

```text
# Admin UI: Ingredients | Multi-line text | Customer-facing key ingredients only (not full INCI)
```

Rules:

- Name exact ingredients when known.
- Do not use generic labels instead of exact names.
- Do not output the full INCI unless verified and requested.
- Do not include editorial notes such as "verify before publishing".
- Do not invent ingredient roles.

#### `=== metafields.custom.skin_application_areas ===`

```text
# Admin UI: Skin application areas | List of body_area | One per line
```

Allowed values only:

```text
Lippen
Haende
Hals
Gesicht
Augen
Dekollete
Koerper
```

#### `=== metafields.custom.skin_problem ===`

```text
# Admin UI: Skin problem | List of skin_problem | One per line
```

Allowed values only:

```text
Cellulite
Post-Treatment (nach Peelings, Laser, Needling)
Schwellungen
Schwangerschaft & Stillzeit
Roetungen & Rosazea
Pigmentierung / Pigmentflecken / Melasma
Schuppige Haut (Sebaroe)
Oelige Haut (erweiterte Poren)
Falten & feine Linien
empfindliche / atopische Haut
Ausgetrocknete Haut
Augenringe
Anti-Aging
Akne / unreine Haut (Pickel, Mitesser)
```

#### `=== metafields.custom.skin_type ===`

```text
# Admin UI: Skin type | List of skin_types | One per line
```

Allowed values only: `Mischhaut`, `Trocken`, `Oelig`, `Normal`.

#### `=== seo.title ===`

```text
# Admin UI: SEO title | Max 70 chars | Required format: {Company} | {Product Name} | Catchy SEO phrase
```

**Required format (mandatory, no exceptions):**

```text
{CompanyName} | {Product Name} | {Catchy SEO phrase}
```

All three segments are required and separated by `|` (space, pipe, space). The
catchy SEO phrase is a German benefit-, concern-, or product-type phrase pulled
from Product Strategy, Keyword Direction DE, and Meta Direction DE — never a
store slogan. Tune the phrase length so the full string stays ≤ 70 characters.

#### `=== seo.description ===`

```text
# Admin UI: SEO description | Max 160 chars
```

Include company, product name, product type, target concern, and one or two hero
ingredients when verified. End with a soft YuliSkin or shopping benefit. Follow
Product Strategy, Keyword Direction DE, Meta Direction DE, and Claim Boundaries.

#### `=== media[].alt ===`

```text
# Admin UI: Media → Alt text (set per uploaded image) | English ALT options for rotation
# Image files in this folder (upload these to Shopify):
#   [CompanyName]-[ProductName]-01.[ext]
#   [CompanyName]-[ProductName]-02.[ext]
#   ...
```

Provide 3 to 6 English ALT options, one per line under the comment block. Include
company, product name, product code when relevant, packaging, texture, or product
context. Do not mention people or make medical claims.

## shopify-en.txt — English Locale (translated)

### shopify-en.txt — File Header

The file starts with this exact header block:

```text
# Shopify product fields — English locale (translated)
# Banner format: === <shopify-field-path> ===
# Use these values in Shopify's Translate & Adapt app or any English-locale storefront.
# Fields not in this file (vendor, SKU, barcode, weight, HS code, country of origin,
# DHL customs description, related products, skin metafields) reuse the values from
# shopify-de.txt.
```

### shopify-en.txt — Banner Order

Generate the banners in this exact order:

```text
1. === title ===
2. === descriptionHtml ===
3. === productType ===
4. === variants[0].title ===
5. === metafields.custom.application ===
6. === metafields.custom.effect ===
7. === metafields.custom.ingredients ===
8. === seo.title ===
9. === seo.description ===
```

### shopify-en.txt — Per-Banner Specifications

#### `=== title ===`

```text
# Admin UI (EN locale): Title
```

Use the English product title when available; otherwise use the official product name.

#### `=== descriptionHtml ===`

```text
# Admin UI (EN locale): Description | Paste in HTML/Source view, not Rich Text
```

Same HTML rules as DE. Follow Product Strategy, Description Direction EN, Keyword
Direction EN, and Claim Boundaries. Do not write a generic category description.

#### `=== productType ===`

```text
# Admin UI: Product type | Same value as DE; only translate if Shopify requires a separate English value
```

#### `=== variants[0].title ===`

```text
# Admin UI (EN locale): Variant title (volume) | Same normalized value as DE
```

#### `=== metafields.custom.application ===`

```text
# Admin UI (EN locale): Application | Multi-line text | Labelled lines
```

Format:

```text
Step 1:
Step 2:
Step 3:
Frequency:
Routine note:
Precaution:
```

#### `=== metafields.custom.effect ===`

```text
# Admin UI (EN locale): Effect | Multi-line text | Labelled lines
```

Format:

```text
Visible effect:
Texture effect:
Comfort effect:
Best for:
```

#### `=== metafields.custom.ingredients ===`

```text
# Admin UI (EN locale): Ingredients | Multi-line text | Customer-facing key ingredients only (not full INCI)
```

#### `=== seo.title ===`

```text
# Admin UI (EN locale): SEO title | Max 70 chars | Required format: {Company} | {Product Name} | Catchy SEO phrase
```

**Required format (mandatory, no exceptions):**

```text
{CompanyName} | {Product Name} | {Catchy SEO phrase}
```

All three segments are required and separated by `|` (space, pipe, space). The
catchy SEO phrase is an English benefit-, concern-, or product-type phrase pulled
from Product Strategy, Keyword Direction EN, and Meta Direction EN — never a
store slogan. Tune the phrase length so the full string stays ≤ 70 characters.

#### `=== seo.description ===`

```text
# Admin UI (EN locale): SEO description | Max 160 chars
```

Follow Product Strategy, Keyword Direction EN, Meta Direction EN, and Claim Boundaries.

## Final Quality Checklist

- All three files (`brief.txt`, `shopify-de.txt`, `shopify-en.txt`) are written in the same run.
- 2 to 5 product images were downloaded when available and saved with sequential names (`-01` to `-05`).
- `brief.txt` contains Research Summary, Keyword Research, Product Strategy, and Structured data reminder — and nothing else.
- `shopify-de.txt` contains the header block and all 21 banners in the documented order.
- `shopify-en.txt` contains the header block and all 9 banners in the documented order.
- Every banner uses the exact GraphQL path documented above.
- Every banner has at least one `# Admin UI:` comment line.
- `descriptionHtml` uses allowed HTML and no `<h1>`.
- `productType` is exactly one value and either uses an allowed value or `brief.txt` notes that a new Shopify value must be created.
- `variants[0].title` uses normalized lowercase units.
- `variants[0].weight` follows verified source data or the `volume_ml + 50g` fallback.
- `metafields.shopify.country_of_origin` uses an ISO alpha-2 code or `Unknown`.
- `metafields.shopify.harmonized_system_code` follows the HS code rules.
- `variants[0].metafields.dhlapp.customsItemDescription` is English and ≤ 30 characters.
- `metafields.custom.skin_application_areas`, `skin_problem`, and `skin_type` use allowed values only, one per line.
- `seo.title` matches the required format `{CompanyName} | {Product Name} | {Catchy SEO phrase}` (three pipe-separated segments) and is ≤ 70 characters in both files.
- `seo.description` ≤ 160 characters in both files.
- Keyword reuse rule satisfied: the Primary keyword from Keyword Direction DE appears in `descriptionHtml`, `seo.title`, and `seo.description` of `shopify-de.txt`; the Primary keyword from Keyword Direction EN appears in the same three banners of `shopify-en.txt`. Two to four secondary or long-tail keywords per locale are woven into description, application, effect, or ingredients prose. No `Terms to avoid` are used. No banner contains a visible `Keywords:` / `Tags:` line.
- Unknown facts appear only in `brief.txt` Research Summary, never in the Shopify files.
- All Shopify-file values are derived from the strategy sections in `brief.txt`.
