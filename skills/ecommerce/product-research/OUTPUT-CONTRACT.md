# Product Research Output Contract

Use this contract when generating `Products/[CompanyName]/[ProductName]/brief.txt` for YuliSkin product research output. The brief is research-first: Research Summary, Keyword Research, and Product Strategy are required foundation sections, and all Shopify-ready fields, descriptions, meta titles, meta descriptions, related products, and image ALT options must be derived from them. Keyword Research must document how customers search for the product, its category, concerns, benefits, ingredients, routine step, and buying intent.

## Image Download Output

In addition to `brief.txt`, download the main product images and store them in the same folder:

```text
Products/[CompanyName]/[ProductName]/[CompanyName]-[ProductName]-01.[ext]
Products/[CompanyName]/[ProductName]/[CompanyName]-[ProductName]-02.[ext]
Products/[CompanyName]/[ProductName]/[CompanyName]-[ProductName]-03.[ext]
Products/[CompanyName]/[ProductName]/[CompanyName]-[ProductName]-04.[ext]
Products/[CompanyName]/[ProductName]/[CompanyName]-[ProductName]-05.[ext]
```

Rules:

- Prioritize source order: official brand/product page, distributor page, then competitor page.
- Download 2 to 5 images when available.
- Use only images that clearly match the exact product.
- Prefer primary product packshots and key gallery images.
- Skip logos, banners, watermarked ads, and unrelated lifestyle images.
- Preserve source extension when possible (`.jpg`, `.jpeg`, `.png`, `.webp`).

## Required File Structure

```text
1. Research Summary
2. Keyword Research
3. Product Strategy

German
1. Title
2. Description HTML
3. Media / Images
4. Image ALT options
5. Product type
6. Vendor
7. Variant name / volume
8. SKU
9. Barcode / GTIN / UPC / ISBN
10. Product weight
11. Country of origin
12. HS code
13. DHL customs description
14. Related products
15. Application
16. Effect
17. Ingredients
18. Skin application area
19. Skin problem
20. Skin type
21. Meta title
22. Meta description

English
1. Title
2. Description HTML
3. Product type
4. Meta title
5. Meta description
6. Variant name / volume
7. Application
8. Effect
9. Ingredients

Supporting sections
1. Structured data reminder
```

The German section contains the full Shopify product setup fields. The English section contains translated Shopify-facing content fields only; use the German values for shared admin/import fields unless Shopify requires localized values.

Do not generate the German, English, or supporting sections until Research Summary, Keyword Research, and Product Strategy are complete. Unknown facts may appear in the foundation sections, but customer-facing copy and copyable Shopify fields must use only verified facts or allowed fallback rules from this contract.

## Strategy Sections

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

Plain text. Research how customers search for this exact product and similar products in Google, marketplaces, retailer sites, brand sites, YuliSkin search/category logic, and other search systems when available. Provide German and English keyword directions grouped by intent:

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

Do not keyword-stuff. Use keyword research to shape natural headings, description HTML, meta title, meta description, image ALT options, related-product logic, and Shopify field choices. Prefer the strongest relevant keywords and search-intent language; do not force every keyword into customer-facing copy.

### Product Strategy

Plain text. Summarize why the product exists, who it is for, which exact ingredients matter, and how it fits into a routine for the specific company.

Use this format:

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

The description, effect, meta title, meta description, related products, and Shopify field choices must follow this strategy.

## Shopify Field Rules

### Product type

Choose exactly one product type.

Prefer one of these existing Shopify values:

```text
Augenpflege
Brush
Cleanser
Concentrate
Creme
Gel
Geschenkset
Gesichtsgerät
Haarpflege
Heimpflegeset
Körperpflege
Lippenpflege
Maske
Nachtcreme
Oil
Online consultation
Other
Peeling
Produktset
Serum
Sonnenschutz
Spot Gel
Tagescreme
Tonic
```

If no existing value fits, output one proposed new value and add a note in Research Summary that the Shopify product type must be created. Do not output multiple product types.

### Vendor

Use the producer or brand/company name for the Shopify vendor field.

### Variant name / volume

Use normalized Shopify-friendly lowercase units:

```text
50 ml
100 g
1 l
1 kg
10 pcs
```

Use `pcs` only when the product is genuinely sold by count. Preserve exact source packaging wording in Research Summary if it differs from the normalized value.

### Product weight

Use a copyable final value only:

```text
100 g
550 g
```

Rules:

- If exact product or shipping weight is verified, use the verified weight.
- If only volume is known, estimate as the numeric ml amount plus 50 g.
- If contents are already in g, estimate as contents weight plus 50 g.
- Do not include the DHL parcel box weight.
- Do not output calculation notes in the copyable field; put uncertainty or assumptions in Research Summary.

Examples:

```text
30 ml -> 80 g
50 ml -> 100 g
150 ml -> 200 g
500 ml -> 550 g
100 g -> 150 g
```

### Country of origin

Use the brand's declared commercial country of origin. Do not over-investigate factory location unless a source clearly states it and it matters for customs. If the country of origin cannot be verified, output `Unknown` in the copyable field and note the uncertainty in Research Summary.

Known brand mappings may be used when source research supports them:

```text
GIGI -> Israel
Meder -> Switzerland
Dr. Medion -> Japan if confirmed or strongly established
```

### HS code

Use one HS code:

```text
33049900
```

Rules:

- Default for skincare cosmetics: `33049900`.
- Haircare: `33059000`.
- Sunscreen / sun protection: use `33049900` unless a source or customs rule suggests otherwise.
- Brushes, tools, and devices: classify separately and do not force the skincare cosmetics code.
- Gift sets and product sets: use the dominant item's HS code when clearly skincare-only; otherwise mark for manual review in Research Summary.

### DHL customs description

English only. Maximum 30 characters. Use plain customs-friendly wording, not marketing copy.

Examples:

```text
Face cream
Face serum
Cleanser
Eye cream
Sunscreen
Cosmetic set
Face brush
Skin care device
```

### SKU and barcode

Include SKU and Barcode / GTIN / UPC / ISBN when verified from official sources, distributors, competitor Shopify shops, provided links, packaging images, or credible retailer data. If unavailable, output `Unknown`. Never infer barcode values.

## German Shopify Fields

### 1. Title

Plain text. Use the product name as it should appear in Shopify.

### 2. Description HTML

Use HTML only. Allowed tags: `<h2>`, `<h3>`, `<p>`, `<ul>`, `<li>`, and verified `<a href="">` links. Do not use `<h1>`.

Must include:

- Product name and company.
- Product type.
- Main skin concern or use case.
- Key benefits.
- Exact verified hero ingredients.
- Texture when verified.
- Routine fit.
- Internal YuliSkin links only when URLs are verified.

The description must follow Product Strategy, Description Direction DE, Keyword Direction DE, and Claim Boundaries. Do not write a generic category description.

### 3. Media / Images

Plain text. List the downloaded image files in order.

```text
Image 1:
Image 2:
Image 3:
Image 4:
Image 5:
```

### 4. Image ALT options

English only. Provide multiple concise options.

Include company, product name, product code when relevant, packaging, texture, or product context. Do not mention people or make medical claims.

### 5. Product type

Use the Product type rules above. Output exactly one value.

### 6. Vendor

Use the Vendor rules above.

### 7. Variant name / volume

Use the Variant name / volume rules above.

### 8. SKU

Use the SKU and barcode rules above.

### 9. Barcode / GTIN / UPC / ISBN

Use the SKU and barcode rules above.

### 10. Product weight

Use the Product weight rules above.

### 11. Country of origin

Use the Country of origin rules above.

### 12. HS code

Use the HS code rules above.

### 13. DHL customs description

Use the DHL customs description rules above.

### 14. Related products

Plain text. Select complementary products from the same company on YuliSkin whenever possible. If the products do not exist on Yuliskin, write just names of the complimentary products from the same company.

Rules:

- Verify YuliSkin URLs before linking.
- Do not recommend the same product.
- Do not recommend products only because they share the company name.
- Use strict routine or concern logic.

Routine patterns:

```text
Cleanser / preparation -> serum / treatment -> concentrate / cream / maintenance
Preparation -> treatment -> hydration / soothing / brightening / maintenance
Mask / treatment -> serum / cream / protection
```

### 15. Application

Plain text with labelled lines:

```text
Step 1:
Step 2:
Step 3:
Frequency:
Routine note:
Precaution:
```

Include amount, frequency, routine sequence, application area, whether to rinse, and precautions when verified. Mark unknowns only in strategy, not in customer-facing copy.

### 16. Effect

Plain text. Keep distinct from the description:

```text
Visible effect:
Texture effect:
Comfort effect:
Best for:
```

Use compliant cosmetic language.

### 17. Ingredients

Customer-facing plain text only. List exact active/key ingredients and their benefits.

Rules:

- Name exact ingredients when known.
- Do not use generic labels instead of exact names.
- Do not output the full INCI unless verified and requested.
- Do not include editorial notes such as "verify before publishing".
- Do not invent ingredient roles.

### 18. Skin application area

Choose one or more only from this list:

```text
Lippen
Haende
Hals
Gesicht
Augen
Dekollete
Koerper
```

### 19. Skin problem

Choose one or more only from this list:

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

### 20. Skin type

Choose one or more only from this list:

```text
Mischhaut
Trocken
Oelig
Normal
```

### 21. Meta title

Maximum 70 characters.

Preferred pattern:

```text
[CompanyName] | [Product Name] | [Benefit or concern]
```

If the code is unknown, omit it. Use product type or concern, not store slogans.

The meta title must follow Product Strategy, Keyword Direction DE, and Meta Direction DE.

### 22. Meta description

Maximum 160 characters.

Include company, product name, product type, target concern, and one or two hero ingredients when verified. End with a soft YuliSkin or shopping benefit.

The meta description must follow Product Strategy, Keyword Direction DE, Meta Direction DE, and Claim Boundaries.

## English Shopify Fields

### 1. Title

Plain text. Use the English product title when available; otherwise use the official product name.

### 2. Description HTML

Use HTML only. Allowed tags: `<h2>`, `<h3>`, `<p>`, `<ul>`, `<li>`, and verified `<a href="">` links. Do not use `<h1>`.

The description must follow Product Strategy, Description Direction EN, Keyword Direction EN, and Claim Boundaries. Do not write a generic category description.

### 3. Product type

Use the same product type chosen for German. Do not translate dropdown values unless Shopify requires a separate English value.

### 4. Meta title

Maximum 70 characters.

The meta title must follow Product Strategy, Keyword Direction EN, and Meta Direction EN.

### 5. Meta description

Maximum 160 characters.

The meta description must follow Product Strategy, Keyword Direction EN, Meta Direction EN, and Claim Boundaries.

### 6. Variant name / volume

Use the same normalized value as German.

### 7. Application

Plain text with labelled lines:

```text
Step 1:
Step 2:
Step 3:
Frequency:
Routine note:
Precaution:
```

### 8. Effect

Plain text:

```text
Visible effect:
Texture effect:
Comfort effect:
Best for:
```

### 9. Ingredients

Customer-facing plain text only. List exact active/key ingredients and their benefits.

## Supporting Sections

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

## Final Quality Checklist

- Strategy sections come first.
- Research Summary, Keyword Research, and Product Strategy are complete before any language or Shopify fields.
- German section comes before English.
- German contains all 22 requested Shopify fields.
- English contains all 9 requested Shopify fields.
- Supporting sections contain Structured data reminder after the language sections.
- 2 to 5 product images were downloaded when available and saved with sequential names (`-01` to `-05`) in the product folder.
- Description HTML uses allowed HTML and no `<h1>`.
- Plain text sections use labelled lines.
- Meta title is 70 characters or less.
- Meta description is 160 characters or less.
- Product type is exactly one value and either uses an existing allowed value or clearly notes that a new Shopify value must be created.
- Variant name / volume uses normalized lowercase units.
- Product weight follows verified source data or the simple `amount + 50 g` fallback.
- Country of origin uses the brand's declared commercial origin or `Unknown` when it cannot be verified.
- HS code and DHL customs description are included.
- SKU and barcode are verified or marked `Unknown`.
- Related products use verified URLs or product names only.
- Skin application area, Skin problem, and Skin type use allowed values only.
- Unknown facts are listed in Research Summary or Product Strategy and excluded from customer-facing copy.
- Descriptions, meta titles, meta descriptions, related products, and Shopify field choices are derived from the foundation sections.
- Claims are cosmetic, evidence-aware, and source-supported.
