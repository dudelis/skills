# Shopify fields, resources, and verification

Read before field mapping or any Shopify write. Discover the connected tools,
live schema, locale support, and applicable theme instead of relying on fixed
API versions, dated store snapshots, or template names.

## Live discovery and native fields

Verify the connected store is YuliSkin. The workflow expects German defaults
and enabled English translations; report locale/configuration mismatches
instead of changing store configuration. Discover existing blogs and author
attribution, and use the selections approved in the editorial brief.

Use purpose-built catalog lookup and image-upload tools where available.
Discover types/fields before constructing each Admin GraphQL operation, validate
it, then execute. Include pagination and follow it for required results.
Do not guess input fields, metafield types, or translation keys.

| Deliverable | Mapping to verify in the live API |
| --- | --- |
| Destination blog | `blogId`, using the selected existing Blog GID |
| German article title | `title` |
| German HTML fragment | `body` in the Admin GraphQL input |
| German HTML excerpt | `summary` |
| German URL slug | `handle`, unique within the destination blog |
| Article template | `templateSuffix`, with verified collection binding |
| Author attribution | `author`, using appropriate existing attribution |
| Supplied banner | `image.url` and `image.altText`, using a hosted image URL |
| New draft state | `isPublished: false`, with no publication schedule |
| German SEO title | Article metafield `global.title_tag` |
| German SEO description | Article metafield `global.description_tag` |
| Collection below article | `custom.associated_collection`, `collection_reference` |
| Collection-section heading | `custom.linked_collection_web_part_title`, `single_line_text_field` |

Inspect the actual SEO storage on existing articles and verify the supported
write mechanism. Do not assume a native `seo` input object or copy a legacy
metafield type into a new field without validation. Preserve compatible existing
types. Use schema-validated native article operations and `metafieldsSet` for
the required SEO/custom values, then retrieve the results.

The collection reference holds one existing Collection GID, not a title or
handle. The approved body product list is planning data; do not invent an
article product-reference field. Never create definitions, locales, blogs,
products, collections, or shared templates to compensate for missing setup.

## Template and collection section

Inspect the applicable article template and section where access permits.
Verify that the collection setting reads:

```liquid
{{ article.metafields.custom.associated_collection.value }}
```

and its heading reads:

```liquid
{{ article.metafields.custom.linked_collection_web_part_title.value }}
```

A template name suggesting a collection is not proof of dynamic binding. A
fixed collection handle in its settings may show the same collection across
articles. Inspect any section overrides before selecting the working template.
If access is unavailable, ask for its relevant source or the user's identified
working template rather than guessing. Report missing binding as a prerequisite.

Products below the article follow the selected collection, its order, and theme
settings. They are not an independently selected body-product list. Do not
change collection membership/order or a shared template for one article.

### Advisory YuliSkin template notes

The inspection on **2026-09-13** found that
`templates/article.blog-post-with-collection.json` binds both its collection and
heading to the article's custom fields. Its featured-collection section was
configured to display up to 12 products.

The inspected `templates/article.blog-post-filtered-collec.json` binds the
heading dynamically but has `sonnenschutz` fixed as its collection setting.
That setting does not establish per-article product filtering. Check any
section overrides before deciding how it behaves.

Use these dated observations as discovery hints and recheck the live bindings
before selecting a template. Prefer the template verified to read the chosen
associated collection; preserve shared template settings.

## English translations

Write German source values first, then fetch `translatableResource` for the
article to obtain actual keys and digests. Register `en` values against that
same article using `translationsRegister`. Discover supported equivalents for
title, body, summary, SEO title/description, and handle; translation keys can
differ from native input names (`body_html` versus `body`, for example).
Do not overwrite German defaults or create a second article as a fallback.

Translate the collection-section heading separately: retrieve its metafield
GID, fetch its translatable content, and register English with the returned
key/digest. Verify the localized value through the supported translation query.
Check type/access eligibility instead of changing metafield configuration.
The associated collection GID is shared across languages.
[Shopify translation guide](https://shopify.dev/docs/apps/build/markets/manage-translated-content)

Localize body-image ALT text inside each HTML body. The shared banner has
German default ALT text; register English only if a supported key exists.
Missing locale support, keys, scopes, or heading translation are incomplete
results, not reasons to change configuration or silently claim bilingual success.
Keep intended English values locally for recovery.

## Banner and media handling

Inspect the supplied file/image URL. Determine dimensions from the target
blog's featured-image treatment, appropriate examples, and current Shopify
image guidance. Match its actual ratio and account for mobile display; optimize
file size without blurring imagery. Put these requirements in the generation
prompt when requested. The user generates/supplies the image separately.
[Shopify image guidelines](https://www.shopify.com/blog/image-sizes)

Before creation confirmation, save banner and inline assets locally with
the completed content/metadata, and record pending uploads in the manifest.
Use local asset paths for local previews where needed. Never upload an image
to Shopify merely to build the preview or prepare a CDN URL for confirmation.

Only after explicit creation confirmation, upload the supplied banner and new
external inline images once using the available Shopify upload tool. Prefer
the reviewed local asset copies; for a URL-based upload, verify it still matches
the reviewed image. Changed assets require renewed review and confirmation.
Verify the tool's inputs; never put a local path in an article URL field.
Record the hosted CDN URL/file ID and reuse them. Existing Shopify catalog
images do not need another upload.

## Creation checks and recovery

Before creation, verify the approved brief/selections, both HTML bodies,
metadata/heading values, supplied banner, existing associated collection,
author/blog, working template, URLs, and SEO lengths. Resolve likely duplicate
handles or title/topic matches with the user before writing.

Save the complete local bundle first, including HTML, all separate fields,
source notes, and banner/inline asset files with pending-upload mappings.
Present the files and exact creation preview and obtain separate explicit
confirmation before **any** Shopify mutation or image upload. Approval of
the editorial plan is not creation confirmation. If confirmation is missing,
keep the prepared bundle locally and wait without writing to Shopify.

After confirmation, upload new assets and replace their mapped local HTML
references with the returned CDN URLs. Validate the Shopify payload has no
local paths or unresolved placeholders before creating the article. Upload
URL substitution does not authorize changing reviewed wording, metadata,
products, or collection selections.

Create one German-default unpublished article without scheduling. Completing
its reviewed metadata, images, and English translations is covered by the
final creation confirmation. Before each follow-on field/translation write,
freshly verify it is still a draft. Stop on publication or unverifiable state; never
force it back to draft. Changes to the approved payload require update review.

Keep a manifest with operation, article ID once known, blog GID, author,
template suffix, default/localized handle, language-specific title/summary/SEO/
heading, associated collection GID, approved body resource GIDs, verified URLs,
banner source/hosted URL/file ID, and applied/failed fields. It is recovery data,
not evidence of live draft state or consent.

After writes, re-read and verify draft status, both bodies/titles/excerpts/SEO,
image, template, exact associated collection GID, and both section headings.
Count persisted SEO strings in each language: at most 70 title characters and
160 description characters, including spaces. Check HTML for concrete URLs,
hosted images, unresolved placeholders, local paths, and copied source scripts.

Inspect uncertain or timed-out writes before retrying. Once an article ID
exists, reuse it and complete only the same creation-confirmed payload; never
create another article to retry translation or metadata completion. Stop on concurrent
publication. Report partial results and failures honestly and retain the draft
and local intended values for recovery. Published articles cannot be repaired
by this skill until the user returns them to draft and reconfirms the update.
