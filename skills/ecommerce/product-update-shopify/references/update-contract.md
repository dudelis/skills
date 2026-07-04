# Product Update Shopify Contract

This reference defines the update-only behavior for applying freshly generated
`product-research` output to existing Shopify products.

## Inputs

```text
Products/[CompanyName]/[ProductName]/brief.txt
Products/[CompanyName]/[ProductName]/shopify-de.txt
Products/[CompanyName]/[ProductName]/shopify-en.txt
Products/[CompanyName]/[ProductName]/[image-slug]-01.[ext]
...
```

The two Shopify files are the source of truth for Shopify values. `brief.txt` is context and
audit material only.

## Automation metadata

Both Shopify files may begin with automation metadata banners:

```text
=== shopify.product_id ===
gid://shopify/Product/123456789

=== shopify.product_url ===
https://yuliskin.de/products/example-handle

=== shopify.match_confidence ===
admin exact handle match
```

`shopify.product_id` is preferred for updates. `Unknown`, empty strings, and missing metadata
are treated as absent. `shopify.product_url` is useful for human review but is not sufficient
for mutation unless the Admin product ID can be resolved.

## Dry-run statuses

- `changed`: current Shopify value differs and will be updated after confirmation.
- `unchanged`: current Shopify value already matches the source file.
- `skipped empty`: banner is empty or `Unknown`; leave Shopify unchanged.
- `protected`: banner exists but this skill never writes that field.
- `fill-if-empty`: field is writeable only because Shopify currently has no value.
- `media upload`: append-only local image upload planned.
- `blocked`: product cannot be safely updated.

## Field behavior

### Always update when non-empty and changed

```text
descriptionHtml
metafields.custom.application
metafields.custom.effect
metafields.custom.ingredients
seo.title
seo.description
```

### Replace full list when non-empty and changed

```text
metafields.custom.skin_application_areas
metafields.custom.skin_problem
metafields.custom.skin_type
```

These are `list.metaobject_reference` fields. Fetch existing metaobject entries and map each
label to a GID. Never create metaobjects. If one label cannot be mapped, write the mapped
values only when the remaining list is still meaningful; report skipped labels.

### Fill only if Shopify is empty

```text
metafields.shopify.country_of_origin
metafields.shopify.harmonized_system_code
variants[0].metafields.dhlapp.customsItemDescription
```

Never overwrite existing Shopify values for these fields. Treat `Unknown` as empty.

### Protected

```text
title
handle
productType
vendor
variants[0].title
variants[0].price
variants[0].sku
variants[0].barcode
variants[0].weight
metafields.shopify--discovery--product_recommendation.related_products
```

Also never write product status, publishing, collections, tags, inventory, markets, sales
channels, tax settings, redirects, compare-at price, unit price, or cost per item.

## English translations

Use `translatableResource` to fetch keys, source values, and digests, then
`translationsRegister` for locale `en`. English values are never written to German/default
fields. If a translation key or digest is unavailable, skip that translation and report it.

## Product matching

Matching order:

1. `shopify.product_id` from the banner files.
2. Exact Admin lookup by handle.
3. Exact Admin search by vendor and title.
4. Public storefront search on `yuliskin.de` to discover a URL/handle, followed by Admin lookup.

If no confident Admin product is found, stop that product and ask the user for the Shopify
product ID. The update skill never creates products.

## Batch behavior

Process at most 5 folders. Prepare a dry run for every valid, matchable folder. Mark invalid
or unmatched folders as blocked. After confirmation, update non-blocked products one by one.
Skip product-specific failures and continue unless the failure appears systemic.
