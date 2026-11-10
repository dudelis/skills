# Confirmed updates to existing drafts

Use this mode for every change after initial creation, including edits to
German/English bodies, SEO, section headings, banner, or associated collection.
Final creation confirmation may cover completion of its reviewed fields on
the new article;
subsequent content revisions always follow this workflow.

## Resolve and inspect first

Resolve exactly one article from an ID, admin/storefront URL, or unambiguous
lookup. If the user returns to a previous run, use its saved article ID but fetch
the live article. A local manifest or the article's unpublished-looking URL is
not evidence that it is currently a draft.

If `isPublished` is true, stop. Explain that the user must manually return that
article to draft. Do not write its body, metafields, translations, image, or
publication settings; do not create a substitute article. When the user says
it is now a draft, re-fetch it, prepare the changes, and obtain explicit
confirmation. Earlier confirmation does not authorize changes after this
publication-state interruption.

Capture a local before-snapshot of its German/default fields, English
translations, affected metafields, images, associated collection, and available
version indicators such as `updatedAt`. Reuse existing values for fields the
user has not asked to change. A small correction does not require repeating the
entire original planning interview; a new angle or product selection needs an
updated editorial plan and approval.

## Make the proposal reviewable

Save the actual revised German and English content, changed metadata, and
asset references locally before asking for confirmation. Show a concise
diff or before/after preview identifying the article and every field that will
change. Give enough revised text to review substantial edits. Include relevant
SEO character counts and any changes to products, collection, heading, banner,
or links.

Maintain the bilingual article's factual consistency. Ordinarily revise both
languages for a substantive content change. If the user explicitly requests a
single-language correction, keep the other language unless the correction
creates a factual conflict; raise that conflict in the preview.

Preserve the existing banner, associated collection, author, blog, handle,
template suffix, and tags unless their change was requested and appears in the
preview. New body product suggestions still require the user's selection. A
new associated collection must be an existing collection selected by the user.

Ask for explicit confirmation of the prepared update. "Please update this
article" alone is not confirmation of an unseen proposal. Confirmation applies
to the exact target and prepared changes; do not silently extend the update
after approval. Keep the pending proposal available until the user responds.

## Apply only while it is a draft

After confirmation, re-fetch the target immediately before writing. If the
current affected values or version differ from the before-snapshot, refresh the
preview and obtain confirmation again. If published or state cannot be verified,
stop without making any article-related write.

For **every** subsequent native-field, metafield, or translation write, perform
a fresh draft-state check immediately before that operation. Do not set
`isPublished: false` in update payloads as a way to force a published article
back to draft. Never change `publishDate`, schedule publication, or publish.
If a scheduled publication is discovered, ask the user to remove that schedule
before proceeding with the draft update.

Use schema discovery and validation before each GraphQL operation. Write only
the approved changed fields, reusing the saved article ID. Update German source
values before obtaining fresh translation keys/digests and registering approved
English values. Translate the section-heading metafield as its own resource.
Uploading a new banner is part of the confirmed change; reuse the existing
Shopify image when unchanged.

These checks are not an atomic Shopify lock: article, metafield, and translation
writes are separate requests. Keep the interval between a state check and write
short, stop if publication or concurrent changes are detected, and do not claim
the API prevents every concurrent publication race. Never undo publication or
restore an old snapshot automatically to recover from an interruption.

## Verify and record

Re-read the target and verify the approved fields, English translations and
source digests, associated collection/heading when changed, SEO limits, and
draft status. Confirm fields outside the approved delta were preserved.

Record the update, target ID, approved changes, resulting fields, and failures
beside the HTML and manifest. If a write times out, inspect the current values
before retrying. Do not create another article. A retry may complete only the
same confirmed payload, with a fresh draft check; an altered proposal or
concurrent edit needs another confirmation.

Report partial success explicitly. If the article is found published during
recovery, stop all remaining writes and tell the user what completed before the
interruption. Wait for manual return to draft and renewed confirmation before
continuing.
