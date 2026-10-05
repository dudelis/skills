---
name: blog-write-shopify
description: >
  Prepares local German/English YuliSkin articles and writes confirmed Shopify drafts
  from topics, supplied articles, distributor materials, URLs, and images.
  Use when preparing local articles for confirmed Shopify creation or making
  explicitly confirmed changes to an existing draft.
---

# Blog Write Shopify

Prepare one Shopify article with German defaults and English translations for
one of two blog types: **Angebote & Neuheiten** (product news and promotions)
or **Kosmetik Insider** (tips, routines, and why a product is needed). The blog
type decides the intake questions and the body layout; address German readers
as "du". The collection below the article and products featured in its body
are separate selections.

## Quick start

Example creation request:

> Plan a Kosmetik Insider article about sunscreen for sensitive skin. I will
> provide product URLs, an existing collection for the section below it, and
> the banner image. Suggest the angle and additional products before writing.
> Save the completed article locally and ask for confirmation before writing
> to Shopify.

Example update request:

> Revise the introduction of my existing draft article. Show the proposed German
> and English changes and wait for my confirmation before updating Shopify.

## Required boundaries

- The user approves the editorial approach and final body product selections
  before the finished article is written. Additional products are suggestions
  until selected by the user.
- An Angebote & Neuheiten article features at least one body product. Every
  body product appears with its featured catalog image, linked to its product
  page, with ALT text.
- The section below the article uses one user-selected existing collection
  plus its heading, or the user's explicit "none". Never create/change
  collections or products to make an article work.
- The banner is supplied as a file or image URL. If a generation prompt is
  requested, first ask what exactly the user wants depicted, then write the
  prompt for their separate generator. Do not generate images or edit Canva.
- Wait for the supplied banner before creating the Shopify article. Once the
  article is ready, save all data locally and present it for review. Editorial
  approval authorizes preparation only. Obtain separate explicit confirmation
  before any Shopify image upload, article creation, metafield, or translation write.
- Every later update requires a concrete preview and explicit confirmation.
  Never edit published articles, their metafields, or their translations. Never
  unpublish them; wait for the user to return them to draft, then verify and
  obtain confirmation of the prepared changes.
- New articles remain unpublished with no scheduled publication. Recheck draft
  status before follow-on writes. Local files are not proof of live status or
  user consent.

## Create an article

1. Read [article-templates.md](references/article-templates.md). Ask first
   which blog type the article is for, then run that type's intake questions:
   topic, body products, promotion, associated collection and its heading, and
   banner. Skip what the user already supplied. The intake is complete when
   every question has an answer or an allowed "none".
2. Connect to Shopify, verify YuliSkin/locales, resolve the body products and
   their featured images, inspect two or three articles of the same blog type
   for tone, and discover the working template.
   Read [shopify-contract.md](references/shopify-contract.md) for field mapping.
3. Follow [editorial-workflow.md](references/editorial-workflow.md): propose
   reader problem, angle, keywords, outline, length, internal links, resource
   selections, and banner status. Wait for the user's approval.
4. Write equivalent, natural German and English HTML from the blog type's
   outline and building blocks, plus metadata, excerpts, and collection-section
   headings. Rewrite supplied material with an original
   structure and wording while preserving verified facts and product names.
   Save all completed content, metadata, and image assets locally first.
5. Check the approved inputs, supplied banner, HTML, URLs, and SEO lengths,
   and the blog type's "done when" criterion: a linked, ALT-tagged row per
   body product.
   Search for duplicate articles; resolve any likely match with the user.
   Show the local files and creation preview; wait for explicit confirmation
   to create this draft and upload the listed images to the selected Shopify blog.
6. Only after confirmation, upload new images once, create the German-default
   draft, set SEO/custom
   fields, and register English article and heading-metafield translations.
   Re-read and verify every required result before reporting completion.

## Update an existing draft

Read [draft-updates.md](references/draft-updates.md) before preparing any update.
Resolve one exact article, fetch live status, and stop if published. Prepare the
actual changes locally and show the target and field/content preview. Wait for
explicit confirmation, then recheck live draft status and concurrent changes
before every write. Preserve fields outside the approved proposal. Verify the
result and report any partial completion.

## Validation, tools, and outputs

- SEO titles: at most **70 characters**; descriptions: at most **160**, including
  spaces, in both languages. Count final strings programmatically.
- Generate descriptive lowercase ASCII handles with hyphens; preserve German
  characters in prose/metadata. Discover supported English handle translations.
- Use verified localized links and authentic product images. Inspect the live
  schema and validate each GraphQL operation before execution; paginate as needed.
- Keep the approved brief/source notes, `article-de.html`, `article-en.html`, and
  `shopify.json` together in the chosen directory or `BlogPosts/<article-slug>/`.
  Save banner/inline images in `assets/` and record pending uploads in the manifest.
  Save a banner prompt only when requested, and record IDs/upload results for
  recovery. Inspect uncertain writes before retrying; never create duplicates.
- Return the admin link, article ID, handle, draft status, language results,
  associated collection, and any failed fields or manual follow-up.
