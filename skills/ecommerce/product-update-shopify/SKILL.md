---
name: product-update-shopify
description: Updates existing Shopify products from freshly generated YuliSkin product-research files, with dry-run diffing, guarded bilingual content updates, and append-only media handling. Use when the user wants to update existing Shopify product descriptions, SEO, descriptive metafields, skin taxonomy, translations, or missing image ALT text from Products/[Company]/[Product]/shopify-de.txt and shopify-en.txt.
---

# Product Update Shopify

## Quick start

Use this skill after `product-research` has regenerated a product folder:

```text
Products/[CompanyName]/[ProductName]/
  brief.txt
  shopify-de.txt
  shopify-en.txt
  [image-slug]-01.[ext]
  ...
```

Default to a dry run. In batch mode, accept at most 5 product folders per run.
Batch updates always require confirmation after the dry-run report.

## Required workflow

1. Resolve one to five product folders. If a path is ambiguous, ask for the exact folder.
2. Validate each folder with `python scripts/validate_product_update_folder.py <product-folder>`.
   In batch mode, mark invalid folders as blocked and continue preparing the others.
3. Parse `shopify-de.txt` and `shopify-en.txt` by exact `=== <field> ===` banners.
   Ignore comment lines beginning with `#`; preserve multiline values exactly.
4. Identify the Shopify product:
   - Prefer `shopify.product_id` when it contains a real Product GID or numeric ID.
   - Otherwise search Shopify Admin/plugin by handle, exact vendor, and exact title.
   - If needed, search the public `yuliskin.de` storefront for a likely product URL/handle,
     then use that handle for Admin lookup.
   - If no confident product is found, stop that product and ask the user for the Shopify product ID.
5. Fetch the current Shopify product, including title, handle, vendor, product type, SEO,
   target metafields, media ALT text, media count, translations, and the three fill-if-empty
   logistics fields.
6. Build a dry-run diff. Report `changed`, `unchanged`, `skipped empty`, `protected`,
   `fill-if-empty`, `media upload`, and `blocked` fields.
7. Only after explicit confirmation, write changed values. In batch mode, update one product
   at a time; skip blocked products and continue unless the error indicates a systemic Shopify/API problem.
8. Re-read each updated product and verify the intended fields changed while protected fields
   did not change.
9. Write or append `shopify-update-log.txt` in each updated product folder with product ID,
   run date, fields updated, skipped fields, uploaded image count, warnings, and manual follow-ups.

## Update surface

German/default fields to update when non-empty and changed:

- `descriptionHtml`
- `metafields.custom.application`
- `metafields.custom.effect`
- `metafields.custom.ingredients`
- `metafields.custom.skin_application_areas`
- `metafields.custom.skin_problem`
- `metafields.custom.skin_type`
- `seo.title`
- `seo.description`

Apply English values from `shopify-en.txt` through Shopify translations only. Never overwrite
German/default fields with English values.

For the three skin taxonomy metafields, non-empty banners replace the complete Shopify list
after mapping labels to existing metaobject GIDs. Empty or `Unknown` banners are skipped and
do not clear Shopify.

## Media rules

- Never delete, replace, or reorder existing media.
- Fill existing image ALT text only when the current Shopify ALT is empty.
- Upload new local images append-only by count: if Shopify has 3 images and the folder has
  5 sequential local images, upload only local images 4 and 5.
- Add ALT text to newly uploaded images from `media[].alt` in order; use simple fallback ALT
  text only when needed.

## Protected fields

Never update title, handle/URL, vendor, product type, price, cost, SKU, barcode, variant
title, variant weight, inventory, product status, publishing, collections, tags, markets,
sales channels, tax settings, or related/recommended products.

Only these logistics fields may be filled when Shopify is currently empty and the banner has
a real non-empty value: `metafields.shopify.country_of_origin`,
`metafields.shopify.harmonized_system_code`, and
`variants[0].metafields.dhlapp.customsItemDescription`. Treat `Unknown` as empty.

Do not create Shopify configuration: no metafield definitions, metaobjects, locales, product
types, redirects, collections, or tags.

See [references/update-contract.md](references/update-contract.md) for detailed field rules.
