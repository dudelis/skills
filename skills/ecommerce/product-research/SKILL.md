---
name: product-research
description: Researches one skincare or dermocosmetics product, builds a verified strategic foundation for YuliSkin product copy, compiles Shopify-ready fields, and downloads 2 to 5 main product images with sequential file names. Use when the user provides a product name and company and wants facts, keyword direction, image assets, Shopify product data, and ready-to-use bilingual content sections in the YuliSkin format.
---

# Product Research

## Quick Start

Use this skill to research one skincare or dermocosmetics product and generate a structured product research file for `yuliskin.de`. The research and strategy sections are the foundation for all generated descriptions, metadata, related products, and Shopify-ready fields.

Required input:

```text
Product name: [exact product name]
Company name: [brand/company]
URLs: [optional official, distributor, competitor, or YuliSkin URLs]
```

Final output files:

```text
Products/[CompanyName]/[ProductName]/brief.txt        # research + strategy + structured data reminder
Products/[CompanyName]/[ProductName]/shopify-de.txt   # German Shopify fields, banner-formatted for copy-paste
Products/[CompanyName]/[ProductName]/shopify-en.txt   # English Shopify fields, banner-formatted for copy-paste
Products/[CompanyName]/[ProductName]/[image-slug]-01.[ext]
Products/[CompanyName]/[ProductName]/[image-slug]-02.[ext]
Products/[CompanyName]/[ProductName]/[image-slug]-03.[ext]
Products/[CompanyName]/[ProductName]/[image-slug]-04.[ext]
Products/[CompanyName]/[ProductName]/[image-slug]-05.[ext]
```

`[image-slug]` is the exact `handle` value defined in [OUTPUT-CONTRACT.md](OUTPUT-CONTRACT.md)
(`{company-slug}-{product-slug}`: lowercase, ASCII-only, diacritics transliterated
`ö → o` / `ß → ss`, punctuation and descriptive/volume/edition/packaging words dropped,
brand de-duplicated). Example: company `Plamine` + product
`Plamine Core Care MINAMOTO – Mineralische Unterstützung für Energie und Vitalität`
→ `plamine-core-care-minamoto-01.jpg`.

The Shopify files use Shopify Admin GraphQL field paths as banners (e.g.
`=== descriptionHtml ===`, `=== metafields.custom.application ===`) so future Shopify
automation can parse them. Always write all three text files in the same run.

Create the folder if needed. Keep the folder names readable (real product and company
names, German characters allowed). Image file names use the ASCII `[image-slug]` form
above — never German letters or the full descriptive product name.

## Workflow

1. Confirm the product name and company name from the user input.
2. Use provided URLs first. Then use Google Search or web search for official, distributor, competitor, and YuliSkin sources.
3. Determine the **product nature** first: **topical** (cream, serum, tonic, mask, oil, peeling…), **ingestible** (supplement, beauty drink, powder), or **tool/device** (roller, brush, gadget). Product nature drives the product type, HS code, DHL customs description, and which skin metafields apply. Never force a skin-taxonomy tag onto a product whose nature does not support it. Then research the product before writing shop copy or filling Shopify fields. Verify product identity, product type, vendor, variant volume, product weight, country of origin, HS code, DHL customs description, texture, hero ingredients, usage, routine position, target concerns, skin types, SKU, barcode/GTIN/UPC/ISBN, claims, images, and related products.
4. Separate verified facts from unknown facts. If a fact cannot be verified, mark it as unknown and do not use it in customer-facing content.
5. Research how customers search for this product and similar products in Google, marketplaces, retailer sites, and other search systems when available. Identify German and English keyword clusters, search intent, product-category language, concern language, benefit language, ingredient language, and buyer-intent terms before writing content.
6. Prepare a short Product Strategy explaining why the product exists, who it is for, which exact ingredients matter, how it fits into the company routine, which complementary products make sense, and how the description, meta title, meta description, and other Shopify fields should be angled.
7. Write `brief.txt` with Research Summary, Keyword Research, Product Strategy, and the Structured data reminder, following [OUTPUT-CONTRACT.md](OUTPUT-CONTRACT.md).
8. Download the main product images from verified official sources first, then distributor sources, then competitor sources when needed.
9. Save 2 to 5 images when available in `Products/[CompanyName]/[ProductName]/` as `[image-slug]-01.[ext]`, `[image-slug]-02.[ext]`, and so on, where `[image-slug]` equals the `handle` value (lowercase, ASCII-only, brand de-duplicated).
10. Generate `shopify-de.txt` and `shopify-en.txt` using the banner format and per-banner specifications in [OUTPUT-CONTRACT.md](OUTPUT-CONTRACT.md). Every value must be derived from the verified Research Summary, Keyword Research, and Product Strategy in `brief.txt`.
11. Validate title/meta lengths, HTML structure, language separation, claim safety, allowed metadata values, banner paths, and image outputs before finishing.

On re-run for an existing product folder, regenerate all three text files atomically. Do not leave stale `shopify-de.txt` / `shopify-en.txt` alongside a freshly regenerated `brief.txt`.

## Research Rules

- Prefer official brand/product pages, distributor pages, verified YuliSkin pages, and credible retailer pages.
- Use source facts for terminology, product-category logic, routine logic, ingredient language, positioning, and claim boundaries.
- Treat Research Summary, Keyword Research, and Product Strategy as required working material, not optional notes. Complete them before generating Shopify fields or customer-facing copy.
- Keyword Research must capture how the product is likely searched for, including exact product-name searches, category searches, skin-concern searches, benefit searches, ingredient searches, routine-step searches, and buying-intent searches.
- Use the strongest relevant keywords naturally in headings, description HTML, meta title, meta description, ALT options, related-product logic, and field choices. Do not force every keyword into the copy.
- Customer-facing sections must be derived from verified facts and the Product Strategy, not from generic product-category assumptions.
- Use source assets for image files. Prioritize official brand or product pages, then distributor pages, then competitor pages.
- Do not copy long source passages. Rewrite in original YuliSkin-appropriate language.
- Do not invent hero ingredients, full INCI, usage frequency, texture, claims, routine position, SKU, barcode/GTIN/UPC/ISBN, internal links, or related-product URLs. The Shopify product handle is constructed deterministically as `{company-slug}-{product-slug}` per the contract — not researched.
- Use official, distributor, competitor, and provided Shopify shop sources to verify SKU and barcode data. If SKU or barcode cannot be obtained, mark it as unknown.
- Product type must be exactly one value. Prefer an existing allowed Shopify product type; if no allowed value fits, propose one new product type and mark that the Shopify value must be created. For ingestible products (supplements, beauty drinks, powders) use the product type `Nahrungsergänzung`.
- Cross-check every hero ingredient against the brand's own positioning. Never state an ingredient the official source does not support, and never let a generic assumption (e.g. "fruit/papaya enzymes" on a product the brand markets as probiotic and explicitly _not_ fruit-acid based) override the verified facts. Omitting a real ingredient is also an error: list the verified hero ingredients the brand actually names.
- Normalize variant volume as Shopify-friendly lowercase units such as `50 ml`, `100 g`, `1 l`, or `10 pcs`.
- If exact product weight is not verified, estimate it as the numeric ml or g amount plus 50 g. Do not include DHL parcel box weight.
- Country of origin means the brand's declared commercial origin, not necessarily the literal factory location. If it cannot be verified, output `Unknown` and note the uncertainty in Research Summary.
- Use the default skincare cosmetics HS code unless the product is clearly haircare, a tool, a device, or a mixed set requiring review.
- DHL customs description must be English, plain, non-marketing, and 30 characters or less.
- Use only verified YuliSkin URLs for internal links and related products. If a URL cannot be verified, use the product name without a link.
- Download only real product images for the exact product. Prefer front packshot and key gallery images, avoid logos, banners, and unrelated lifestyle images.
- Keep the source extension where possible (`.jpg`, `.jpeg`, `.png`, `.webp`).
- Claims must remain cosmetic and evidence-aware. Avoid medical promises such as curing acne, healing rosacea, or treating disease.

## Writing Rules

- Store: YuliSkin.
- Store languages: German and English.
- German first, then English.
- German uses formal address with `Sie`.
- English uses polished, neutral ecommerce language.
- Preserve German umlauts, sharp s, accents, and brand/product casing in all
  descriptive and customer-facing fields. Transliterate to ASCII only for URL
  handles and filesystem-safe file names.
- If the product name already contains the company or brand name, do not prepend
  the company again in titles, SEO fields, descriptions, ALT text, or any other
  descriptive copy. For example, write `Plamine Clear Lotion`, never
  `Plamine Plamine Clear Lotion`.
- Description HTML must use `<h2>`, `<h3>`, `<p>`, `<ul>`, `<li>`, and verified `<a href="">` links only. Do not use `<h1>`.
- Application, Effect, Ingredients, Related products, metadata fields, and Structured data reminder are plain text with labelled lines.
- Ingredients must be customer-facing and list exact active/key ingredients and benefits only. Do not output the full INCI unless it is verified and specifically useful.
- Image ALT Texts are English only for both language versions.
- Meta title must be 70 characters or less.
- Meta description must be 160 characters or less.

## Brand Voice

YuliSkin is a **curated boutique**: a small, hands-on studio that hand-picks and
personally tests every brand it sells. The voice is a knowledgeable, warm expert who
guides the customer — not a clinical data sheet and not a hype-driven discounter.

- Write warm, precise, and confident. Every sentence must carry a verified fact, a
  benefit, or the curation angle — never empty filler.
- Express the curated/tested credibility tastefully. In the on-page description,
  include one short, sincere note on **why the product earned a place in the YuliSkin
  range** (real-world use in the studio). Write it like a boutique owner's genuine
  remark, never a repeated slogan.
- The curation/testing angle is a **real-world studio test only**. Never imply or
  state clinical, dermatological, or laboratory testing unless the manufacturer
  states it on a verified source.
- In the meta description the curation is **implied through tone only** — do not write
  a literal "handverlesen und getestet" tag.

## Description Anatomy

`descriptionHtml` is the always-visible top zone. The collapsible metafields below it
(`application`, `effect`, `ingredients`) and the structured tag lists (`skin_problem`,
`skin_type`, `skin_application_areas`) are SEO-indexed and own the mechanical detail —
so the description must **not** duplicate them. Build `descriptionHtml` as four blocks:

1. **Hook + concept** — one opening `<h2>` (the product name) + a `<p>` that leads with
   the concept/benefit and who it is for, naming the verified hero ingredients in plain
   language. Carries the primary keyword.
2. **Curation note** — a short `<p>` on why YuliSkin selected the product (per Brand
   Voice). Tasteful, never a slogan, never a clinical claim.
3. **Concern \u2192 mechanism \u2192 benefit** — an `<h3>` + `<ul>` where each `<li>` takes one
   _verified_ target concern and explains _how_ a hero ingredient or property works on
   it, ending in a claim-safe benefit. Only narrate concerns verified for this product.
4. **F\u00fcr wen geeignet** — an `<h3>` + `<ul>` with persona/concern guidance; include a
   "weniger geeignet, wenn \u2026" line when honestly applicable.

Target depth: ~110\u2013180 words DE (EN similar). For thin-data products, merge blocks
rather than padding with filler or inventing facts. The collapsible `effect` field's
`Geeignet f\u00fcr:` line stays a short skin-type/suitability note so it does not echo
block 4.

## Claim-Safety Lexicon

Applies to all customer-facing copy in both locales. This both lifts richness and
protects against EU Cosmetics Regulation 1223/2009 and German UWG/HWG risk.

Approved DE framing: `unterst\u00fctzt`, `pflegt`, `spendet Feuchtigkeit`, `sorgt f\u00fcr ein
geschmeidiges/gepflegtes Hautgef\u00fchl`, `kann das Hautbild ausgeglichener wirken lassen`,
`f\u00fcr einen sp\u00fcrbar \u2026 Teint`, `umsorgt`, `verw\u00f6hnt`, `erg\u00e4nzt die Routine`.

Banned DE (hard exclusion): `heilt`, `behandelt`, `bek\u00e4mpft`, `wirkt gegen [Krankheit]`,
`beseitigt`, `garantiert`, `100 %`, `sofort dauerhaft`, `Wundermittel`, `beste/r/s`,
`Nr. 1`, `klinisch bewiesen` (unless verified), and any disease-cure outcome
(`Akne heilen`, `Rosazea behandeln`).

`klinisch getestet` / `dermatologisch getestet` may be used **only** when the
manufacturer states it on a verified source; otherwise it is banned.

Anti-filler: never use empty phrases such as `ein wahrer Allrounder`, `darf in keiner
Routine fehlen`, `das gewisse Etwas`.

EN mirrors the same logic: approved `supports`, `nourishes`, `helps the skin feel \u2026`;
banned `cures`, `treats`, `eliminates`, `guaranteed`, `clinically proven` (without
verified proof).

## Customer-Voice Purity

Every customer-facing field (`descriptionHtml`, `application`, `effect`, `ingredients`,
`seo.title`, `seo.description`, `media[].alt`) is shopper copy only. Research, sourcing,
and analyst language stays in `brief.txt` and must never appear in a Shopify value:

- No sourcing references — `laut offizieller … Seite`, `laut Herstellerseite`,
  `according to the … page`, `Quelle:`, or any citation of where a fact came from.
- No marketing-analyst framing — `positioniert`, `antioxidativ positionierter
Wirkstoff`, `positioned as`, `marketed as`, `hero ingredient`, `USP`, `Keyword`.
- No meta/process language — `verifiziert`, `unverified`, `Fallback`, `geschätzt`,
  `estimated`, `placeholder`.

State the benefit directly: write `Ein hochwirksames Antioxidans, das die Haut vor
oxidativem Stress schützt.` not `Ein antioxidativ positionierter Wirkstoff`; write
`Kann ergänzend zum CLIONE Fit Gerät verwendet werden.` not `Kann laut offizieller
Plamine EU Seite mit CLIONE Fit verwendet werden.`

## Non-Topical Products

When the product nature is **not** a topical cosmetic:

- **Ingestible** (supplement, beauty drink, powder): use `productType: Nahrungserg\u00e4nzung`;
  frame benefits as honest inside-out / "von innen" support; leave
  `skin_application_areas`, `skin_problem`, and `skin_type` **empty** rather than
  force-mapping a skin tag; use food-supplement HS code and DHL description.
- **Tool / device** (roller, brush, gadget): omit skin-chemistry fields; copy focuses
  on use and material; `variants[0].title` may be `Default Title`.
- An empty structured field is always better than a misleading one — it keeps the
  store's faceted filters honest.

## Validation

Before returning the final answer, check:

- All three files were written in the same run: `brief.txt`, `shopify-de.txt`, `shopify-en.txt` under `Products/[CompanyName]/[ProductName]/`.
- 2 to 5 product images were downloaded when available and saved as `[image-slug]-01.[ext]` through `[image-slug]-05.[ext]`, where `[image-slug]` is the lowercase ASCII `handle` slug (no German letters, no descriptive tail).
- `brief.txt` contains Research Summary, Keyword Research, Product Strategy, and Structured data reminder — and contains no Shopify-pasteable values.
- `shopify-de.txt` contains the header block plus all 23 banners in the order defined in [OUTPUT-CONTRACT.md](OUTPUT-CONTRACT.md).
- `shopify-en.txt` contains the header block plus all 9 banners in the order defined in [OUTPUT-CONTRACT.md](OUTPUT-CONTRACT.md).
- `handle` in `shopify-de.txt` follows the format `{company-slug}-{product-slug}` (lowercase, hyphenated, ASCII-only).
- Every product has at least one variant: the six `variants[0].*` banners (`title`, `price`, `sku`, `barcode`, `weight`, `metafields.dhlapp.customsItemDescription`) are all present in `shopify-de.txt` (use `Unknown` for unverified values — never skip the banner). Additional real variants are listed in `brief.txt` Research Summary.- Every banner uses the exact GraphQL path documented in the contract (`=== title ===`, `=== descriptionHtml ===`, `=== metafields.custom.application ===`, etc.).
- Every banner has at least one `# Admin UI:` comment line.
- `descriptionHtml` uses allowed HTML and no `<h1>`.
- Descriptive German fields preserve real German characters; ASCII
  transliteration is used only for `handle` and file names.
- If the product name already starts with the company/brand name, no field repeats
  the company immediately before the product name. Run this check before writing
  every field.
- `seo.title` uses the three-segment format `{Company} | {Product} | {Catchy phrase}`. If the product name already starts with the company name, the company is stripped **from the product segment only** so the brand appears once, leading (`Plamine | Core Care IKI-IKI | …`). The product name itself and the `<h2>` keep their full natural form; the company is never prepended to a product name that lacks it. The catchy phrase is a real benefit/concern phrase, never a bare keyword (✗ `… | Core Care Supplement`), and the full string is ≤ 70 characters (aim 55–70) in both Shopify files.
- `descriptionHtml` follows the four-block anatomy (hook+concept, curation note, concern→mechanism→benefit list, Für wen geeignet) and does not duplicate the `application`, `effect`, or `ingredients` collapsibles.
- The curation note is present, tasteful, and implies real-world studio testing only — no clinical/dermatological claim unless the manufacturer states it.
- The `effect` field's `Geeignet für:` line is a short skin-type/suitability note only — never a routine/persona sentence that duplicates description block 4 ("Für wen geeignet").
- No customer-facing field leaks research, sourcing, or analyst language (no `laut offizieller … Seite` / `according to the … page` / `Quelle:`, no `positioniert` / `positioned as` / `marketed as`, no `Fallback` / `geschätzt` / `unverified`); benefits are stated directly.
- No banned lexicon term appears in any customer-facing field; no empty filler phrases; approved claim-safe framing is used.
- For non-topical products: `productType` is `Nahrungsergänzung` (ingestible) or appropriate; `skin_application_areas`, `skin_problem`, and `skin_type` are left empty rather than force-mapped.
- Every hero ingredient is supported by the brand's own positioning; no invented or brand-contradicting ingredient; no verified hero ingredient omitted.
- `seo.description` ≤ 160 characters in both Shopify files.
- Keyword reuse rule satisfied per [OUTPUT-CONTRACT.md](OUTPUT-CONTRACT.md): the Primary keyword from the locale's Keyword Direction is woven naturally into `descriptionHtml`, `seo.title`, and `seo.description`; two to four secondary or long-tail keywords per locale are woven into description, application, effect, or ingredients prose; no `Terms to avoid` are used; no banner contains a visible `Keywords:` / `Tags:` line.
- `variants[0].metafields.dhlapp.customsItemDescription` is English and ≤ 30 characters.
- `metafields.custom.skin_application_areas`, `skin_problem`, and `skin_type` use only allowed values from [OUTPUT-CONTRACT.md](OUTPUT-CONTRACT.md), one per line.
- `metafields.shopify--discovery--product_recommendation.related_products` follows routine or concern logic and does not include the same product.
- Unknown facts appear only in `brief.txt` Research Summary, never in the Shopify files.
