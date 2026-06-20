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
  [image-slug]-01.[ext]
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
   - ASCII transliteration is handle-only. Do not transliterate descriptive fields.
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
   - first variant **price** from `variants[0].price` (the general price shown on the
     product page). Normalize the value before writing: strip currency symbols and spaces
     and treat a comma as the decimal separator (`€24,90` → `24.90`). Write the price exactly
     as researched (no rounding of the price itself).
   - first variant **Cost per item** (`inventoryItem.unitCost`, written via the
     `inventoryItem.cost` input) = the normalized price ÷ 2, rounded to 2 decimals
     (half-up). Only set cost when a real numeric price exists.
   - if `variants[0].price` is absent, empty, or `Unknown`, set neither price nor cost;
     leave Shopify defaults and report it as a manual follow-up. Never estimate a price.
   - do not set compare-at price, unit price, inventory quantity, inventory policy, tax
     settings, collections, or tags.
   - country of origin and HS code when accepted.
   - DHL customs item description variant metafield when accepted.
   - custom metafields after mapping display labels to existing stored values/options when needed.
   - SEO title and description.
   - English ALT text on attached media (see step 9 for the single upload-and-attach flow).
9. Attach sequential local product images to the created product in a single operation:
   - Use the Shopify app's purpose-built image upload tool that ingests the local file and
     attaches it to the product in one call, passing the created product ID.
   - Do NOT perform a separate pre-upload to obtain a hosted URL. One image = one call =
     one upload that lands attached. Never upload an image to Files first and then attach a
     second copy.
   - Attach only after the product exists, so the product ID is available.
   - Use only product-folder images ending in `-01`, `-02`, etc. with `.jpg`, `.jpeg`, `.png`, or `.webp`.
   - Use English ALT lines from `media[].alt` in order.
   - If there are fewer ALT lines than images, generate simple non-repeated English fallback ALT text from vendor, title, and image number.
   - Missing images or failed uploads do not block product creation.
10. Use Shopify Admin GraphQL for product creation fields that are not covered by
    higher-level Shopify tools. Before every query or mutation, inspect the live schema and
    validate the GraphQL operation with the Shopify app validation tool. Do not guess
    mutation names, input field names, metafield types, or translation keys.

- For images, only fall back to raw Admin GraphQL `stagedUploadsCreate` →
  `productCreateMedia` if the purpose-built upload-and-attach tool is unavailable. Even
  then, perform exactly one staged upload per image and attach that same resource —
  never a pre-upload plus a separate re-ingest.

11. Best-effort apply English values from `shopify-en.txt` through Shopify's translation
    API, not by overwriting German default values:

- Use `translatableResource` to fetch keys, source values, and digests.
- Use `translationsRegister` for locale `en`.
- Query nested translatable resources when translating variants or metafields requires it.
- If locale support, keys, digests, or translation writes fail, keep the draft product and report the failed fields.

12. Re-read the created product from Shopify and verify:
    - Product exists and status is `DRAFT`.
    - German default title/vendor/product type/SEO/metafields are present.
    - When a price was set: the created variant's **price** equals the normalized
      `variants[0].price` and its **Cost per item** (`inventoryItem.unitCost`) equals the
      price ÷ 2 (2 decimals). Report any mismatch as a warning.
    - Images were attached: query the product node's media and confirm the count of
      attached `MediaImage` nodes equals the number of local source images (3 local files
      → exactly 3 attached, no more). Report any mismatch as a warning. Shopify renames
      uploaded media filenames/CDN URLs (often with a GUID-like suffix); this is expected
      and is never treated as a duplicate signal. Do not verify by filename.
    - English translations were registered or clearly reported as skipped with a reason.
13. Return a concise report: product ID, handle, draft status, uploaded image count,
    fields written (including the price set and the computed cost per item), translations
    applied, skipped fields, validation warnings, and manual follow-ups. Always include the
    follow-up: verify the price before switching the product from `DRAFT` to `ACTIVE`.

## Guardrails

- Never publish a product. If a tool or mutation attempts `ACTIVE`, stop and correct it to
  `DRAFT`.
- This skill is create-only. If a duplicate product exists, stop and report it. Use a
  future update skill for updates.
- Never invent missing commercial data. If price, inventory, SKU, barcode, HS code, or
  country of origin is absent or `Unknown`, leave it empty/unknown when Shopify permits
  and report the manual follow-up. When `variants[0].price` is missing or `Unknown`, set
  neither the general price nor the Cost per item.
- Set the general price from `variants[0].price` and the Cost per item
  (`inventoryItem.unitCost`) to half of it. Do not set compare-at price, unit price,
  inventory quantity, inventory policy, tax settings, collections, or tags. Leave those
  Shopify defaults.
- Do not set related/recommended products in v1. Ignore
  `metafields.shopify--discovery--product_recommendation.related_products`; a later skill
  can update related products after the catalog exists.
- Do not enable locales, publish locales, create metafield definitions, create product
  types, or change store configuration. Report missing configuration as a manual follow-up.
- Never put unknown facts into customer-facing fields.
- Preserve German umlauts, sharp s, accents, and official casing in descriptive
  fields. Only URL handles and filesystem-safe names may be ASCII-normalized.
- If a product title already includes the vendor or company name, do not write the
  vendor again immediately before the title in SEO, description, ALT text, or any
  other descriptive field.
- Attach images using the purpose-built upload tool that ingests the local file and
  attaches it to the product in a single operation. Do not perform a separate pre-upload to
  obtain a hosted URL, and never paste a local filesystem path into a GraphQL media URL
  field. Uploading an image once and then uploading a second copy to attach it is a bug.
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
