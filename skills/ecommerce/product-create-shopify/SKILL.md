---
name: product-create-shopify
description: Creates one new draft Shopify product from a YuliSkin product-research output folder, including German default fields, best-effort English translations, metafields, variant data, SEO fields, handle, and product images. Use when the user wants to create a Shopify product from `Products/[CompanyName]/[ProductName]/shopify-de.txt` and `shopify-en.txt`; this skill is create-only, performs a duplicate safety check, and never updates or publishes existing products.
---

# Product Create Shopify

## Quick start

Use this skill after `product-research` has produced a complete folder:

```text
Products/[CompanyName]/[ProductName]/
  brief.txt
  shopify-de.txt
  shopify-en.txt
  [CompanyName]-[ProductName]-01.[ext]
  ...
```

Create exactly one Shopify product per run. German is the default product content.
English values are translations/localized counterparts. Always create the Shopify
product in `DRAFT` status. If an existing product is found, stop and report it; do
not update it.

## Required workflow

1. Resolve the product folder from the user-provided path. The normal shape is
   `Products/[CompanyName]/[ProductName]/`. If the path does not resolve to exactly
   one existing folder, stop and ask for the exact folder path.
2. Read `shopify-de.txt`, `shopify-en.txt`, and the local image list.
3. Validate the product-research files before using Shopify:
   - Run `python scripts/validate_product_folder.py <product-folder>` from this skill folder when available.
   - If the script reports hard errors, stop before touching Shopify.
   - If the script reports warnings only, continue and include them in the final report.
   - If the script is unavailable, manually verify the minimum required fields in [references/banner-contract.md](references/banner-contract.md).
4. Parse banner files by exact `=== <shopify-field-path> ===` headers. Ignore comment
   lines beginning with `#`; preserve multiline values exactly.
5. Derive the product handle:
   - Use a `handle` banner if present.
   - Otherwise parse company and product from `Products/[CompanyName]/[ProductName]/`.
   - If the path shape is unclear, use `vendor` and `title` from `shopify-de.txt`.
   - Normalize to lowercase ASCII with hyphens, for example `plamine-clear-lotion`.
6. Search Shopify for a likely duplicate before creating:
   - Always search exact `vendor` + exact `title`.
   - Also search exact SKU or barcode when those values exist and are not `Unknown`.
   - If any likely duplicate is found, stop and report it. Do not update, merge, or overwrite.
   - If no duplicate is found, continue.
7. Create the minimum German/default product as `DRAFT`:
   - `title`
   - `vendor`
   - `descriptionHtml`
   - `handle`
   - status `DRAFT`
8. Best-effort apply the remaining German/default fields:
   - `productType` only if Shopify accepts the existing value; do not create product types.
   - first variant title, SKU, barcode, and weight when accepted.
   - country of origin and HS code when accepted.
   - DHL customs item description variant metafield when accepted.
   - custom metafields after mapping display labels to existing stored values/options when needed.
   - SEO title and description.
   - uploaded media and English ALT text.
9. Upload sequential local product images with the Shopify app's image upload tool:
   - Use only product-folder images ending in `-01`, `-02`, etc. with `.jpg`, `.jpeg`, `.png`, or `.webp`.
   - Use English ALT lines from `media[].alt` in order.
   - If there are fewer ALT lines than images, generate simple non-repeated English fallback ALT text from vendor, title, and image number.
   - Missing images or failed uploads do not block product creation.
10. Use Shopify Admin GraphQL for product creation fields that are not covered by
   higher-level Shopify tools. Before every query or mutation, inspect the live schema and
   validate the GraphQL operation with the Shopify app validation tool. Do not guess
   mutation names, input field names, metafield types, or translation keys.
11. Best-effort apply English values from `shopify-en.txt` through Shopify's translation
   API, not by overwriting German default values:
   - Use `translatableResource` to fetch keys, source values, and digests.
   - Use `translationsRegister` for locale `en`.
   - Query nested translatable resources when translating variants or metafields requires it.
   - If locale support, keys, digests, or translation writes fail, keep the draft product and report the failed fields.
12. Re-read the created product from Shopify and verify:
    - Product exists and status is `DRAFT`.
    - German default title/vendor/product type/SEO/metafields are present.
    - Images were attached.
    - English translations were registered or clearly reported as skipped with a reason.
13. Return a concise report: product ID, handle, draft status, uploaded image count,
    fields written, translations applied, skipped fields, validation warnings, and manual follow-ups.

## Guardrails

- Never publish a product. If a tool or mutation attempts `ACTIVE`, stop and correct it to
  `DRAFT`.
- This skill is create-only. If a duplicate product exists, stop and report it. Use a
  future update skill for updates.
- Never invent missing commercial data. If price, inventory, SKU, barcode, HS code, or
  country of origin is absent or `Unknown`, leave it empty/unknown when Shopify permits
  and report the manual follow-up.
- Do not set price, compare-at price, inventory quantity, inventory policy, tax settings,
  collections, or tags. Leave Shopify defaults.
- Do not set related/recommended products in v1. Ignore
  `metafields.shopify--discovery--product_recommendation.related_products`; a later skill
  can update related products after the catalog exists.
- Do not enable locales, publish locales, create metafield definitions, create product
  types, or change store configuration. Report missing configuration as a manual follow-up.
- Never put unknown facts into customer-facing fields.
- Do not use a local file path as a Shopify media URL. Upload images first and use the
  returned Shopify-hosted URL.
- Do not create batch products from `products.csv` in v1. Process one researched product
  folder at a time. External orchestration may call this skill repeatedly for multiple folders.
- Do not translate German defaults by hand during creation if `shopify-en.txt` exists;
  use its values as the source of truth for English.
- Do not silently overwrite an existing Shopify product.

## Shopify tool use

If Shopify app tools are not already available, search for the Shopify plugin/app tools
first. Use purpose-built Shopify tools for product lookup and image upload when available.
Use raw Admin GraphQL only after schema discovery and validation.

For Admin GraphQL patterns, use the Shopify Admin skill/documentation for the current API
version. Product creation, metafields, media, SEO, variants, and translations can change
between Shopify versions, so the executing agent must validate against the live schema.

## Field contract

Read [references/banner-contract.md](references/banner-contract.md) when implementing or
debugging parsing/mapping. It lists the required banners and how `shopify-de.txt` maps to
the default product while `shopify-en.txt` maps to English translations.
