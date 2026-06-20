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
Products/[CompanyName]/[ProductName]/[image-slug]-01.[ext]
Products/[CompanyName]/[ProductName]/[image-slug]-02.[ext]
Products/[CompanyName]/[ProductName]/[image-slug]-03.[ext]
Products/[CompanyName]/[ProductName]/[image-slug]-04.[ext]
Products/[CompanyName]/[ProductName]/[image-slug]-05.[ext]
```

`[image-slug]` is the exact `handle` value (`{company-slug}-{product-slug}`): lowercase,
ASCII-only, diacritics transliterated, descriptive/volume/edition/packaging words dropped,
brand de-duplicated. The parent **folder** names stay readable (real names, German
characters allowed); only the image **file** names are slugified. Example: company
`Plamine` + product `Plamine Core Care MINAMOTO – Mineralische Unterstützung …`
→ `plamine-core-care-minamoto-01.jpg`.

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

### Character preservation and repeated brand names

Preserve real German characters in every descriptive or customer-facing field:
German umlauts, sharp s, accents, capitalization, and official brand/product
spelling must stay as written. ASCII transliteration such as `ae`, `oe`, `ue`,
or `ss` is allowed only where the contract explicitly requires ASCII, especially
URL handles and filesystem-safe image names. Do not use transliterated German in
titles, descriptions, SEO fields, application/effect/ingredient prose, or ALT text.

If the product name already begins with the company or brand name, treat that full
product name as the display name. Do not prepend the company again in any
descriptive field. For example, write `Plamine Clear Lotion`, not
`Plamine Plamine Clear Lotion`.

### Customer-voice purity

Customer-facing fields (`descriptionHtml`, `metafields.custom.application`,
`metafields.custom.effect`, `metafields.custom.ingredients`, `seo.title`,
`seo.description`, `media[].alt`) must read as warm shopper-facing copy only.
Research, sourcing, and analyst language belongs in `brief.txt`, never in a Shopify
value.

**Never let these leak into a customer-facing field:**

- Sourcing references — `laut offizieller … Seite`, `laut Herstellerseite`,
  `according to the official … page`, `per the brand site`, `the EU page says`,
  `Quelle:`, or any citation of where a fact came from.
- Marketing-analyst framing — `positioniert`, `antioxidativ positionierter Wirkstoff`,
  `positioned as`, `marketed as`, `brand positioning`, `hero ingredient`,
  `Keyword`, `USP`.
- Meta/process language — `verifiziert`, `unverified`, `Fallback`, `geschätzt`,
  `estimated`, `placeholder`.

State the benefit directly instead. Write `Ein hochwirksames Antioxidans, das die
Haut vor oxidativem Stress schützt.`, not `Ein antioxidativ positionierter Wirkstoff`.
Write `Kann ergänzend zum CLIONE Fit Gerät verwendet werden.`, not `Kann laut
offizieller Plamine EU Seite mit CLIONE Fit verwendet werden.`

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
- **Buyer-intent terms are banned from description prose:** Never use `kaufen`,
  `bestellen`, `online kaufen`, `günstig kaufen`, `kaufen bei`, `buy`, `order`,
  `shop online`, or equivalent buyer-intent phrases inside `descriptionHtml`,
  `metafields.custom.application`, `metafields.custom.effect`, or
  `metafields.custom.ingredients`. These terms belong only in `seo.title` and
  `seo.description`, and only inside a natural phrase — never as the entire
  catchy segment.
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
3.  === handle ===
4.  === productType ===
5.  === vendor ===
6.  === variants[0].title ===
7.  === variants[0].price ===
8.  === variants[0].sku ===
9.  === variants[0].barcode ===
10. === variants[0].weight ===
11. === metafields.shopify.country_of_origin ===
12. === metafields.shopify.harmonized_system_code ===
13. === variants[0].metafields.dhlapp.customsItemDescription ===
14. === metafields.shopify--discovery--product_recommendation.related_products ===
15. === metafields.custom.application ===
16. === metafields.custom.effect ===
17. === metafields.custom.ingredients ===
18. === metafields.custom.skin_application_areas ===
19. === metafields.custom.skin_problem ===
20. === metafields.custom.skin_type ===
21. === seo.title ===
22. === seo.description ===
23. === media[].alt ===
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

`descriptionHtml` is the **always-visible top zone** and must not duplicate the
collapsible metafields below it (`application`, `effect`, `ingredients`) or the
structured tag lists (`skin_problem`, `skin_type`, `skin_application_areas`). Those are
SEO-indexed and own the mechanical detail; the description owns persuasion, trust,
concept, and self-qualification. Build it as **four blocks**:

1. **Hook + concept** — opening `<h2>` (the product name) + a `<p>` that leads with the
   concept/benefit and who it is for, naming the verified hero ingredients in plain
   language. Carries the primary keyword.
2. **Curation note** — a short `<p>` explaining why YuliSkin selected the product:
   a sincere, boutique-owner remark referencing real-world use in the studio. Never a
   repeated slogan; never implies clinical/dermatological testing unless the
   manufacturer states it.
3. **Concern → mechanism → benefit** — an `<h3>` + `<ul>` where each `<li>` takes one
   _verified_ target concern and explains _how_ a hero ingredient or property works on
   it, ending in a claim-safe benefit. Only narrate concerns verified for this product;
   never invent a mechanism for a broad taxonomy mapping.
4. **Für wen geeignet** — an `<h3>` + `<ul>` with persona/concern guidance; include a
   "weniger geeignet, wenn …" line when honestly applicable.

Target depth: ~110–180 words DE (EN similar). For thin-data products (e.g. supplements),
merge blocks rather than padding with filler or inventing facts.

**Opening `<h2>` heading rule:** When the product name already starts with the brand
name, the opening `<h2>` must use the product name alone — do not append
"von [Brand]". Add "von [Brand]" only when the product name does not already contain
the brand name.

- ✓ `<h2>Plamine Clear Lotion</h2>` (product name already contains brand)
- ✓ `<h2>Clear Lotion von Plamine</h2>` (product name does not contain brand)
- ✗ `<h2>Plamine Clear Lotion von Plamine</h2>` (brand repeated)

Apply the Claim-Safety Lexicon (see "Voice & Claim-Safety Lexicon" below). Follow
Product Strategy, Description Direction DE, Keyword Direction DE, and Claim Boundaries.
Do not write a generic category description.

#### `=== handle ===`

```text
# Admin UI: URL handle | Lowercase, hyphenated, ASCII-only | Format: {company-slug}-{product-slug}
```

Format is **`{company-slug}-{product-slug}`** — the brand always comes first, then
the product name, unless the product slug already starts with the brand slug. This
keeps product URLs grouped per brand on `yuliskin.de` and guarantees uniqueness
across products from different brands that share a name.

Rules for slugifying each segment:

- Lowercase, ASCII-only, hyphen-separated.
- Strip diacritics (`é → e`, `ö → o`, `ß → ss`), apostrophes, periods, commas,
  registered/trademark marks, and punctuation.
- Drop volume suffixes, edition tags, and packaging words (`50ml`, `limited edition`,
  `refill`, `set`, `kit`) unless they are essential to identify the product.
- If the product slug already starts with the company slug, do not duplicate it.
- Collapse repeated hyphens; never start or end with a hyphen.

This same slug is reused verbatim as the `[image-slug]` for downloaded image file names
(`[image-slug]-01.[ext]`, `-02`, …). Image files therefore never contain German letters
or the full descriptive product name.

Examples:

| Company          | Product                  | Handle                           |
| ---------------- | ------------------------ | -------------------------------- |
| `Plamine`        | `Hybrid Oil`             | `plamine-hybrid-oil`             |
| `Dr. Hauschka`   | `Rosen Tagescreme 30 ml` | `dr-hauschka-rosen-tagescreme`   |
| `BABOR`          | `HSR Lifting Cream`      | `babor-hsr-lifting-cream`        |
| `La Roche-Posay` | `Effaclar Duo+ M`        | `la-roche-posay-effaclar-duo-m`  |
| `L'Oréal Paris`  | `Revitalift Filler`      | `loreal-paris-revitalift-filler` |

#### `=== productType ===`

```text
# Admin UI: Product type | Single value
```

Choose exactly one product type. Prefer one of these existing Shopify values:

```text
Augenpflege, Brush, Cleanser, Concentrate, Creme, Gel, Geschenkset, Gesichtsgerät,
Haarpflege, Heimpflegeset, Körperpflege, Lippenpflege, Maske, Nachtcreme,
Nahrungsergänzung, Oil, Online consultation, Other, Peeling, Produktset, Serum,
Sonnenschutz, Spot Gel, Tagescreme, Tonic
```

Use `Nahrungsergänzung` for any ingestible product (supplement, beauty drink, powder).
If no existing value fits, output one proposed new value and add a note in
`brief.txt` Research Summary that the Shopify product type must be created.

#### `=== vendor ===`

```text
# Admin UI: Vendor
```

Use the producer or brand/company name.

### Variants — every product must have at least one variant

Shopify products are required to have at least one variant. The product itself
holds the title and description; the variant holds the price, SKU, barcode, and
weight. The `variants[0].*` banners below describe that **mandatory first variant**
and must always be present in `shopify-de.txt`, even when the product is sold in a
single SKU and has no real product options.

When the product has no real options:

- Use Shopify's implicit `Default Title` variant. Output the volume-only label in
  `=== variants[0].title ===` (e.g. `50 ml`); when no volume applies (a tool, a
  device), output `Default Title`.
- Always output `=== variants[0].sku ===`, `=== variants[0].barcode ===`,
  `=== variants[0].weight ===`, and `=== variants[0].metafields.dhlapp.customsItemDescription ===`.
  Use the value `Unknown` when the SKU or barcode is not verified — never skip the
  banner.

When the product has multiple real variants (sizes, shades, scents):

- The `[0]` banners describe the **primary variant only** — the largest size or
  the canonical variant offered as the default in the brand's shop.
- Note the additional variants in `brief.txt` Research Summary so they can be
  added manually in Shopify Admin or via a follow-up automation.
- Never silently drop variants without recording them in the brief.

#### `=== variants[0].title ===`

```text
# Admin UI: Variant title (volume) | Normalized lowercase units (50 ml, 100 g, 1 l, 10 pcs)
```

**Always output the actual volume or count** (`150 ml`, `30 g`, `60 pcs`, etc.).
`Default Title` is only valid when the product has absolutely no measurable quantity —
a physical tool or electronic device (e.g. a facial roller, a massager). For any
skincare, cosmetic, or topical product, always use the volume or weight unit even if
there is only one variant.

Use `pcs` only when the product is genuinely sold by count. Preserve exact source
packaging wording in `brief.txt` Research Summary if it differs from the normalized
value.

#### `=== variants[0].price ===`

```text
# Admin UI: Price | In EUR | Research from official brand site or distributor/retailer — in that priority order | Output "Unknown" if unverified
```

Research the retail price in EUR. Prefer the official brand site, then a distributor
or retailer. Do not use YuliSkin as a price source. Do not estimate or infer a price.
If no verified price is found, output `Unknown`.

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

Keep `Geeignet für:` a short skin-type / suitability note (e.g. "Alle Hauttypen;
empfindliche Haut"). The persona/concern guidance prose lives in description block 4
("Für wen geeignet"), so this line must not duplicate it. It must name skin types or
states only — never a routine/persona sentence.

```text
✓ Geeignet für: Trockene und normale Haut.
✗ Geeignet für: Gesichtspflege-Routinen, die ein antioxidatives Serum mit Feuchtigkeit
  und Fulleren verbinden möchten.   # persona prose — belongs in description block 4
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

**Non-topical rule:** for ingestible products (supplements, beauty drinks, powders)
and tools/devices, leave this field, `skin_problem`, and `skin_type` **empty**. Never
force a skin tag onto a product whose nature does not support it — an empty structured
field keeps the store's faceted filters honest.

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

**Required format (always three segments):**

```text
{Company} | {Product} | {Catchy phrase}
```

All three segments are separated by `|` (space, pipe, space). The company always
leads. If `{Product}` already begins with `{Company}`, strip the company **from the
product segment only** so the brand appears exactly once, in the lead:

- Company `Plamine`, product `Plamine Core Care IKI-IKI` → `Plamine | Core Care IKI-IKI | {Catchy phrase}`
- Company `Plamine`, product `Hybrid Oil` → `Plamine | Hybrid Oil | {Catchy phrase}`

This stripping is `seo.title`-only. Never strip or add the company in the `title`
field or the description `<h2>` — those keep the full natural product name. Never
prepend the company to a product name that does not already contain it.

The catchy phrase is a German benefit-, concern-, or product-type phrase
pulled from Product Strategy, Keyword Direction DE, and Meta Direction DE — never
a store slogan. Aim for 55–70 characters total so the SERP budget is used.

**Catchy phrase rules (applies to both locales):**

- Must read like a real ad headline fragment — a human-written phrase, not a
  bare keyword, a keyword + verb, or the product type alone.
- Forbidden patterns: `[keyword] kaufen`, `[keyword] online`, `[keyword] bestellen`,
  `[keyword] kaufen bei`, `[keyword] günstig kaufen`.
- The primary keyword must appear _inside_ a natural phrase, not stand alone as
  the entire segment.
- ✓ `Sanftes Enzympeeling für empfindliche Haut` — ✗ `Core Care Supplement` (bare keyword) — ✗ `Clear Lotion kaufen`

#### `=== seo.description ===`

```text
# Admin UI: SEO description | Max 160 chars
```

Include company, product name, product type, target concern, and one or two hero
ingredients when verified, but never duplicate the company if the product name
already contains it. Lead with the product substance; the curated-boutique
credibility is conveyed through a confident, expert tone — do **not** append a literal
trust tag such as "handverlesen und getestet". Weave the primary keyword and one
secondary keyword naturally. Follow Product Strategy, Keyword Direction DE, Meta
Direction DE, the Claim-Safety Lexicon, and Claim Boundaries.

#### `=== media[].alt ===`

```text
# Admin UI: Media → Alt text (set per uploaded image) | English ALT options for rotation
# Image files in this folder (upload these to Shopify):
#   [image-slug]-01.[ext]
#   [image-slug]-02.[ext]
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

Same HTML rules as DE, including the opening `<h2>` heading rule: when the product
name already starts with the brand name, use the product name alone in the opening
`<h2>` — do not append "by [Brand]". Follow Product Strategy, Description Direction
EN, Keyword Direction EN, and Claim Boundaries. Do not write a generic category
description.

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

**Required format (always three segments):**

```text
{Company} | {Product} | {Catchy phrase}
```

The company always leads. If `{Product}` already begins with `{Company}`, strip the
company **from the product segment only** so the brand appears once, leading. This
stripping is `seo.title`-only; the `title` field and `<h2>` keep the full product name,
and the company is never prepended to a product name that lacks it.

The catchy phrase is an English benefit-, concern-, or product-type phrase
pulled from Product Strategy, Keyword Direction EN, and Meta Direction EN — never
a store slogan. Aim for 55–70 characters total.

Apply the same catchy phrase rules as DE: the phrase must read like a real ad
headline fragment, never a bare keyword or the product type alone; buyer-intent terms
(`buy`, `order`, `shop`, `cheap`) are forbidden as the entire segment; the primary
keyword must appear inside a natural phrase, not stand alone.

#### `=== seo.description ===`

```text
# Admin UI (EN locale): SEO description | Max 160 chars
```

Lead with the product substance; convey curated-boutique credibility through a
confident, expert tone — do **not** append a literal trust tag. Follow Product
Strategy, Keyword Direction EN, Meta Direction EN, the Claim-Safety Lexicon, and
Claim Boundaries.

## Final Quality Checklist

- All three files (`brief.txt`, `shopify-de.txt`, `shopify-en.txt`) are written in the same run.
- 2 to 5 product images were downloaded when available and saved with sequential names (`[image-slug]-01` to `[image-slug]-05`), where `[image-slug]` is the lowercase ASCII `handle` slug — no German letters, no descriptive tail.
- `brief.txt` contains Research Summary, Keyword Research, Product Strategy, and Structured data reminder — and nothing else.
- `shopify-de.txt` contains the header block and all 23 banners in the documented order.
- `shopify-en.txt` contains the header block and all 9 banners in the documented order.
- Every banner uses the exact GraphQL path documented above.
- Every banner has at least one `# Admin UI:` comment line.
- `descriptionHtml` uses allowed HTML and no `<h1>`.
- `handle` follows the format `{company-slug}-{product-slug}`, is lowercase, hyphenated, ASCII-only, and starts with the brand slug.
- Descriptive German fields preserve real German characters; ASCII transliteration is used only for `handle` and file/image names.
- **Active brand deduplication check:** Before writing each field, check whether the product name starts with the brand name. If it does, use the product name alone as the subject in that field — never prepend the brand again. This applies to `title`, `descriptionHtml`, `seo.title`, `seo.description`, `media[].alt`, and all `metafields.custom.*` prose.
- Every product has at least one variant: `=== variants[0].title ===`, `=== variants[0].price ===`, `=== variants[0].sku ===`, `=== variants[0].barcode ===`, `=== variants[0].weight ===`, and `=== variants[0].metafields.dhlapp.customsItemDescription ===` are all present in `shopify-de.txt` (use `Unknown` for unverified values — never skip a banner). Additional real variants are listed in `brief.txt` Research Summary.
- `productType` is exactly one value and either uses an allowed value or `brief.txt` notes that a new Shopify value must be created.
- `variants[0].title` is the actual volume or weight unit (e.g. `150 ml`, `30 g`) for any skincare or cosmetic product; `Default Title` is only valid for physical tools or devices with no measurable quantity.
- `variants[0].price` is present in `shopify-de.txt` with a verified EUR value or `Unknown`.
- `variants[0].weight` follows verified source data or the `volume_ml + 50g` fallback.
- `metafields.shopify.country_of_origin` uses an ISO alpha-2 code or `Unknown`.
- `metafields.shopify.harmonized_system_code` follows the HS code rules.
- `variants[0].metafields.dhlapp.customsItemDescription` is English and ≤ 30 characters.
- `metafields.custom.skin_application_areas`, `skin_problem`, and `skin_type` use allowed values only, one per line.
- `seo.title` uses the three-segment format `{Company} | {Product} | {Catchy phrase}`; when the product name starts with the company name, the company is stripped from the product segment only (brand once, leading); the catchy phrase is a real benefit/concern phrase, never a bare keyword; ≤ 70 chars (aim 55–70) in both files.
- `descriptionHtml` follows the four-block anatomy and does not duplicate the `application`, `effect`, or `ingredients` collapsibles; it includes a tasteful curation note.
- `metafields.custom.effect`'s `Geeignet für:` line is a short skin-type / suitability note only — never a routine/persona sentence that duplicates description block 4 ("Für wen geeignet").
- No customer-facing field leaks research, sourcing, or analyst language (no `laut offizieller … Seite` / `according to the … page` / `Quelle:`, no `positioniert` / `positioned as` / `marketed as`, no `Fallback` / `geschätzt` / `unverified`); benefits are stated directly.
- No banned Claim-Safety Lexicon term and no empty filler phrase appears in any customer-facing field.
- Every hero ingredient is supported by the brand's own positioning; no invented or brand-contradicting ingredient, and no verified hero ingredient omitted.
- Non-topical products use `Nahrungsergänzung` (ingestible) and leave `skin_application_areas`, `skin_problem`, and `skin_type` empty rather than force-mapping.
- `seo.description` ≤ 160 characters in both files.
- Keyword reuse rule satisfied: the Primary keyword from Keyword Direction DE appears in `descriptionHtml`, `seo.title`, and `seo.description` of `shopify-de.txt`; the Primary keyword from Keyword Direction EN appears in the same three banners of `shopify-en.txt`. Two to four secondary or long-tail keywords per locale are woven into description, application, effect, or ingredients prose. No `Terms to avoid` are used. No banner contains a visible `Keywords:` / `Tags:` line.
- Unknown facts appear only in `brief.txt` Research Summary, never in the Shopify files.
- All Shopify-file values are derived from the strategy sections in `brief.txt`.

## Voice & Claim-Safety Lexicon

YuliSkin is a **curated boutique** — a hands-on studio that hand-picks and personally
tests every brand it sells. Write as a warm, knowledgeable expert who guides the
customer; never a clinical data sheet, never a hype discounter. Every sentence carries
a verified fact, a benefit, or the curation angle — never empty filler.

The curation/testing credibility is **real-world studio use only**. Express it
tastefully in the on-page description (one sincere "why we selected it" note); imply it
through tone in the meta fields. Never imply clinical, dermatological, or laboratory
testing unless the manufacturer states it on a verified source.

|                  | German                                                                                                                                                                                                     | English                                                                                             |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Approved framing | `unterstützt`, `pflegt`, `spendet Feuchtigkeit`, `sorgt für ein geschmeidiges/gepflegtes Hautgefühl`, `kann das Hautbild ausgeglichener wirken lassen`, `für einen spürbar … Teint`, `umsorgt`, `verwöhnt` | `supports`, `nourishes`, `helps the skin feel …`, `leaves skin looking …`, `cares for`              |
| Banned (hard)    | `heilt`, `behandelt`, `bekämpft`, `wirkt gegen [Krankheit]`, `beseitigt`, `garantiert`, `100 %`, `sofort dauerhaft`, `Wundermittel`, `beste/r/s`, `Nr. 1`, `klinisch bewiesen` (unless verified)           | `cures`, `treats`, `eliminates`, `guaranteed`, `clinically proven` (without proof), `best`, `No. 1` |
| Anti-filler      | `ein wahrer Allrounder`, `darf in keiner Routine fehlen`, `das gewisse Etwas`                                                                                                                              | `a true all-rounder`, `a must-have`, `that special something`                                       |

`klinisch getestet` / `dermatologisch getestet` (and EN equivalents) may be used **only**
when the manufacturer states it on a verified source.

## Gold-Standard Examples

These are the quality bar for `descriptionHtml` and the SEO fields. Match the depth,
voice, claim-safety, and content-ownership shown here.

### Example A — Topical (MEDER Enzy-Peel, real verified facts)

Verified hero actives: probiotic enzymes, micronized opal particles, shea butter;
microbiome-friendly. (Note: the brand markets it explicitly as _not_ fruit-acid based —
do **not** claim "papaya/fruit enzymes".)

**`descriptionHtml` (DE):**

```html
<h2>Enzy-Peel (2EZ)</h2>
<p>
  Das Enzy-Peel ist eine mikrobiomfreundliche Peeling-Maske mit doppelter
  Wirkung: Probiotische Enzyme und fein vermahlene Opal-Partikel lösen
  abgestorbene Hautschüppchen, ohne die Haut zu strapazieren. So wirkt der Teint
  glatter, frischer und ebenmäßiger.
</p>
<p>
  Wir haben das Enzy-Peel in unser Sortiment aufgenommen, weil es selbst
  empfindliche Haut sanft exfoliert – ein Punkt, der uns in der Arbeit in
  unserem Kosmetikstudio besonders wichtig ist. Ein Peeling, das wir guten
  Gewissens für die regelmäßige Pflege empfehlen.
</p>
<h3>Was das Enzy-Peel für Ihre Haut tut</h3>
<ul>
  <li>
    Stumpfer, müder Teint: Probiotische Enzyme lösen gezielt abgestorbene
    Hautzellen für ein sichtbar frischeres Hautbild.
  </li>
  <li>
    Unebene Hautstruktur: Mikrofeine Opal-Partikel verfeinern die Oberfläche für
    ein spürbar glatteres Hautgefühl.
  </li>
  <li>
    Trockenheit beim Peeling: Sheabutter spendet Feuchtigkeit und umsorgt die
    Haut während der Exfoliation.
  </li>
  <li>
    Pflege danach: Die geklärte Haut kann nachfolgende Seren und Cremes besser
    aufnehmen.
  </li>
</ul>
<h3>Für wen geeignet</h3>
<ul>
  <li>
    Für alle Hauttypen, die einen fahlen oder unebenen Teint sanft auffrischen
    möchten.
  </li>
  <li>
    Auch für empfindliche Haut – die Formel ist mikrobiomfreundlich und
    besonders schonend.
  </li>
  <li>
    Weniger geeignet bei akut gereizter oder geschädigter Hautbarriere – hier
    zuerst beruhigen.
  </li>
</ul>
```

- `seo.title`: `MEDER | Enzy-Peel | Sanftes Enzympeeling für empfindliche Haut`
- `seo.description`: `Enzy-Peel von MEDER: mikrobiomfreundliche Peeling-Maske mit probiotischen Enzymen für ein glatteres, frischeres Hautbild – auch bei empfindlicher Haut.`

**EN excerpt (same shape):**

```html
<h2>Enzy-Peel (2EZ)</h2>
<p>
  Enzy-Peel is a microbiome-friendly, dual-action exfoliating mask: probiotic
  enzymes and finely milled opal particles lift away dead skin cells without
  stressing the skin, leaving the complexion smoother, fresher and more even.
</p>
<p>
  We added Enzy-Peel to our range because it exfoliates even sensitive skin
  gently — something that matters to us in our studio work. A peel we are happy
  to recommend for regular care.
</p>
```

### Example B — Non-topical (Plamine Core Care IKI-IKI, ingestible)

`productType: Nahrungsergänzung`; `skin_application_areas`, `skin_problem`, and
`skin_type` left **empty**; inside-out framing; no skin-treatment claims.

**`descriptionHtml` (DE):**

```html
<h2>Plamine Core Care IKI-IKI</h2>
<p>
  Plamine Core Care IKI-IKI ist eine Nahrungsergänzung aus der japanischen
  Core-Care-Routine von Plamine. Der Pulver-Stick verbindet Enzyme aus Gemüse,
  Obst und Getreide mit fermentiertem Lactobacillus-Extrakt aus Sojabohnen und
  präbiotischen Bestandteilen für eine Pflege von innen.
</p>
<p>
  Wir führen IKI-IKI, weil es Plamines Inside-out-Konzept auf einfache Weise in
  den Alltag bringt – ein Produkt, das gut zu den Routinen passt, die wir in
  unserem Studio begleiten.
</p>
<h3>Was IKI-IKI ergänzt</h3>
<ul>
  <li>
    Darm-Haut-Balance von innen: fermentierte Soja-Bestandteile und Präbiotika
    unterstützen eine mikrobiotenfreundliche Routine.
  </li>
  <li>
    Tägliche Einfachheit: Portionssticks machen die Einnahme planbar – 1 Stick
    täglich mit Wasser.
  </li>
</ul>
<h3>Für wen geeignet</h3>
<ul>
  <li>
    Für alle, die Plamines japanische Inside-out-Routine bewusst auch von innen
    begleiten möchten.
  </li>
  <li>
    Hinweis: enthält Sojabohnen und Milchbestandteile; kein Ersatz für eine
    ausgewogene Ernährung.
  </li>
</ul>
```

- `seo.title`: `Plamine | Core Care IKI-IKI | Nahrungsergänzung für Darm-Haut-Balance`
- `seo.description`: `Plamine Core Care IKI-IKI: Nahrungsergänzung für die Darm-Haut-Balance, mit Enzymen & fermentiertem Soja für eine japanische Pflege von innen.`
