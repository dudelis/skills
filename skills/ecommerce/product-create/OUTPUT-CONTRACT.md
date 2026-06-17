# Create Product Output Contract

Use this contract when generating `[CompanyName]/[ProductName].txt` for YuliSkin product creation.

## Required File Structure

```text
1. Research Summary
2. Keyword Research
3. Product Strategy

German
1. General Description (HTML)
2. Application
3. Effect
4. Ingredients
5. Image ALT Texts
6. SEO Title
7. SEO Meta Description
8. Related products
9. Skin Application Areas
10. Skin problems
11. Skin types
12. Structured data reminder

English
1. General Description (HTML)
2. Application
3. Effect
4. Ingredients
5. Image ALT Texts
6. SEO Title
7. SEO Meta Description
8. Related products
9. Skin Application Areas
10. Skin problems
11. Skin types
12. Structured data reminder
```

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
Product code / SKU:
Verified source URLs:
Verified YuliSkin URLs:
Unknown facts:
```

### Keyword Research

Plain text. Provide German and English keyword directions grouped by intent:

```text
German keywords:
Brand + product:
Product type:
Skin concern:
Benefit:
Active ingredient / formulation:
Routine step:
Buyer intent:

English keywords:
Brand + product:
Product type:
Skin concern:
Benefit:
Active ingredient / formulation:
Routine step:
Buyer intent:
```

Do not keyword-stuff. Use keyword research to shape natural headings, descriptions, SEO title, and meta description.

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
Related Product Logic:
Claim Boundaries:
```

The description, effect, SEO, and related products must follow this strategy.

## Language Sections

### 1. General Description (HTML)

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

### 2. Application

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

### 3. Effect

Plain text. Keep distinct from the description:

```text
Visible effect:
Texture effect:
Comfort effect:
Best for:
```

Use compliant cosmetic language.

### 4. Ingredients

Customer-facing plain text only. List exact active/key ingredients and their benefits.

Rules:

- Name exact ingredients when known.
- Do not use generic labels instead of exact names.
- Do not output the full INCI unless verified and requested.
- Do not include editorial notes such as "verify before publishing".
- Do not invent ingredient roles.

### 5. Image ALT Texts

English only. Provide multiple concise options.

Include company, product name, product code when relevant, packaging, texture, or product context. Do not mention people or make medical claims.

### 6. SEO Title

Maximum 70 characters.

Preferred pattern:

```text
[CompanyName] | [Product Name] | [Benefit or concern]
```

If the code is unknown, omit it. Use product type or concern, not store slogans.

### 7. SEO Meta Description

Maximum 160 characters.

Include company, product name, product type, target concern, and one or two hero ingredients when verified. End with a soft YuliSkin or shopping benefit.

### 8. Related products

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

### 9. Skin Application Areas

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

### 10. Skin problems

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

### 11. Skin types

Choose one or more only from this list:

```text
Mischhaut
Trocken
Oelig
Normal
```

### 12. Structured data reminder

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
- German section comes before English.
- Each language contains all 12 requested sections.
- General Description uses allowed HTML and no `<h1>`.
- Plain text sections use labelled lines.
- SEO title is 70 characters or less.
- SEO meta description is 160 characters or less.
- Related products use verified URLs or product names only.
- Skin Application Areas, Skin problems, and Skin types use allowed values only.
- Unknown facts are listed in Research Summary or Product Strategy and excluded from customer-facing copy.
- Claims are cosmetic, evidence-aware, and source-supported.
