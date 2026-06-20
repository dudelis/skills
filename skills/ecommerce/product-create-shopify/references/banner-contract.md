# Product Create Shopify Banner Contract

Use this reference when parsing `product-research` output for create-only Shopify
product creation.

## Input folder

```text
Products/[CompanyName]/[ProductName]/brief.txt
Products/[CompanyName]/[ProductName]/shopify-de.txt
Products/[CompanyName]/[ProductName]/shopify-en.txt
Products/[CompanyName]/[ProductName]/[CompanyName]-[ProductName]-01.[ext]
...
```

`brief.txt` is context only. Do not parse Shopify values from it. The Shopify source
of truth is the two banner files.

## Banner parsing

Each field block starts with:

```text
=== <shopify-field-path> ===
```

Comment lines start with `#`. The value is everything after comments until the next
banner. Preserve multiline values and HTML.

## German default banners

`shopify-de.txt` normally provides these banners in order:

```text
title
descriptionHtml
handle                          # optional; may be absent in older product folders
productType
vendor
variants[0].title
variants[0].sku
variants[0].barcode
variants[0].weight
metafields.shopify.country_of_origin
metafields.shopify.harmonized_system_code
variants[0].metafields.dhlapp.customsItemDescription
metafields.shopify--discovery--product_recommendation.related_products
metafields.custom.application
metafields.custom.effect
metafields.custom.ingredients
metafields.custom.skin_application_areas
metafields.custom.skin_problem
metafields.custom.skin_type
seo.title
seo.description
media[].alt
```

Map these to the default Shopify product, variant, media, SEO, and metafields. German
is the primary storefront language for YuliSkin.

Hard-required German values before creation:

```text
title
vendor
descriptionHtml
```

`handle` is preferred when present. If absent, generate it from
`Products/[CompanyName]/[ProductName]/`; if that shape is unclear, generate it from
`vendor` + `title`.

ASCII normalization is only for the URL handle and filesystem-safe names. Preserve
German umlauts, sharp s, accents, capitalization, and official brand/product spelling
in all descriptive fields. If `title` already starts with `vendor`, do not prepend
`vendor` again in SEO fields, descriptions, ALT text, or metafields.

## English translation banners

`shopify-en.txt` must provide these banners in order:

```text
title
descriptionHtml
productType
variants[0].title
metafields.custom.application
metafields.custom.effect
metafields.custom.ingredients
seo.title
seo.description
```

Apply these through Shopify translations/localized resources. Do not overwrite the
German default product fields with English values.

## Fields intentionally ignored in v1

Do not set these from this skill:

```text
metafields.shopify--discovery--product_recommendation.related_products
collections
tags
compare-at price
unit price
inventory quantity
inventory policy
tax settings
```

Related/recommended products are handled by a later update skill after enough products
exist in the catalog.

## Required handling notes

- `descriptionHtml` is HTML and must not be escaped into visible markup.
- Descriptive German fields must preserve real German characters; do not apply
  handle-style transliteration outside handles or file names.
- If the product title already contains the vendor/company name, no descriptive
  field should contain the duplicated phrase `vendor + title`.
- `variants[0].weight` is grams.
- `media[].alt` contains English ALT options, one per line. Use them in image order.
  If there are fewer ALT values than sequential images, generate simple non-repeated
  English fallback ALT text.
- `Unknown` values are allowed for SKU, barcode, and country of origin when research could
  not verify them. Prefer omitting those values in Shopify when the API supports omission.
- `variants[0].price` is the EUR general price shown on the product page. Set the variant
  **price** from it (normalize: strip currency symbols/spaces, comma is the decimal
  separator) and set **Cost per item** (`inventoryItem.unitCost`) to that price ÷ 2, rounded
  to 2 decimals. If `variants[0].price` is missing or `Unknown`, set neither price nor cost
  and report a manual follow-up. The price must be verified manually before the product is
  switched from `DRAFT` to `ACTIVE`.
- The product status must be `DRAFT` after creation.
- Product images are uploaded and attached to the product in a single operation; there is
  no separate pre-upload step. Uploading an image once unattached and then uploading a
  second copy to attach it is a bug. Attach exactly one copy per local source image.
- Product images are best-effort. Missing or failed images do not block draft creation.
- English translations are best-effort through `translatableResource` and
  `translationsRegister`. Never overwrite German defaults with English values.
