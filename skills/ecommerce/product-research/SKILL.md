---
name: product-research
description: Researches one skincare or dermocosmetics product, compiles verified findings into a structured YuliSkin brief, and downloads 2 to 5 main product images with sequential file names. Use when the user provides a product name and company and wants facts, keyword direction, image assets, and ready-to-use bilingual content sections in the YuliSkin format.
---

# Product Research

## Quick Start

Use this skill to research one skincare or dermocosmetics product and generate a structured product research file for `yuliskin.de`.

Required input:

```text
Product name: [exact product name]
Company name: [brand/company]
URLs: [optional official, distributor, competitor, or YuliSkin URLs]
```

Final output file:

```text
Products/[CompanyName]/[ProductName]/brief.txt
```

Final image output files:

```text
Products/[CompanyName]/[ProductName]/[CompanyName]-[ProductName]-01.[ext]
Products/[CompanyName]/[ProductName]/[CompanyName]-[ProductName]-02.[ext]
Products/[CompanyName]/[ProductName]/[CompanyName]-[ProductName]-03.[ext]
Products/[CompanyName]/[ProductName]/[CompanyName]-[ProductName]-04.[ext]
Products/[CompanyName]/[ProductName]/[CompanyName]-[ProductName]-05.[ext]
```

Create the folder if needed. Sanitize the folder and file names only enough to make them valid paths; keep product and company names readable.

## Workflow

1. Confirm the product name and company name from the user input.
2. Use provided URLs first. Then use Google Search or web search for official, distributor, competitor, and YuliSkin sources.
3. Research the product before writing shop copy. Verify product type, texture, hero ingredients, usage, routine position, target concerns, skin types, product code/SKU, claims, images, and related products.
4. Separate verified facts from unknown facts. If a fact cannot be verified, mark it as unknown and do not use it in customer-facing content.
5. Perform keyword research in German and English before writing content.
6. Prepare a short Product Strategy explaining why the product exists, who it is for, which exact ingredients matter, and how it fits into the company routine.
7. Generate the required German and English product sections using the contract in [OUTPUT-CONTRACT.md](OUTPUT-CONTRACT.md).
8. Download the main product images from verified official sources first, then distributor sources, then competitor sources when needed.
9. Save 2 to 5 images when available in `Products/[CompanyName]/[ProductName]/` as `[CompanyName]-[ProductName]-01.[ext]`, `[CompanyName]-[ProductName]-02.[ext]`, and so on.
10. Write the final content to `Products/[CompanyName]/[ProductName]/brief.txt`.
11. Validate title/meta lengths, HTML structure, language separation, claim safety, allowed metadata values, and image outputs before finishing.

## Research Rules

- Prefer official brand/product pages, distributor pages, verified YuliSkin pages, and credible retailer pages.
- Use source facts for terminology, product-category logic, routine logic, ingredient language, positioning, and claim boundaries.
- Use source assets for image files. Prioritize official brand or product pages, then distributor pages, then competitor pages.
- Do not copy long source passages. Rewrite in original YuliSkin-appropriate language.
- Do not invent hero ingredients, full INCI, usage frequency, texture, claims, routine position, product code/SKU, Shopify handles, internal links, or related-product URLs.
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
- General Description must be HTML with `<h2>`, `<h3>`, `<p>`, `<ul>`,`<li>` and others. Do not use `<h1>`.
- Application, Effect, Ingredients, Related products, metadata fields, and Structured data reminder are plain text with labelled lines.
- Ingredients must be customer-facing and list exact active/key ingredients and benefits only. Do not output the full INCI unless it is verified and specifically useful.
- Image ALT Texts are English only for both language versions.
- SEO Title must be 70 characters or less.
- SEO Meta Description must be 160 characters or less.

## Validation

Before returning the final answer, check:

- The file was created at `Products/[CompanyName]/[ProductName]/brief.txt`.
- 2 to 5 product images were downloaded when available and saved as `[CompanyName]-[ProductName]-01.[ext]` through `[CompanyName]-[ProductName]-05.[ext]` in `Products/[CompanyName]/[ProductName]/`.
- Research Summary, Keyword Research, and Product Strategy appear before language sections.
- German and English sections are separated and no section mixes languages.
- HTML description has no `<h1>`.
- SEO titles are within 70 characters.
- SEO meta descriptions are within 160 characters.
- Related products follow routine or concern logic and do not include the same product.
- Skin Application Areas, Skin problems, and Skin types use only allowed values from [OUTPUT-CONTRACT.md](OUTPUT-CONTRACT.md).
- Unknown facts are excluded from customer-facing sections.

