---
name: shopify-slideshow-create
description: >
  Creates one new German/English YuliSkin homepage slide and publishes it as a
  Shopify `slideshow` metaobject. Use when the user wants a new homepage
  slide, or continues a slide awaiting its image.
---

# Slideshow Create Shopify

Prepare one homepage slide (image, heading, short description, button) and
publish it as a **new** `slideshow` metaobject with German defaults and English
translations. The user wires it into the `ys-slideshow` section in the theme
editor. A run has two sessions: session 1 ends with an image prompt; the user
generates the image elsewhere and comes back with "continue".

## Quick start

> Create a slide for the new GIGI PDRN serum, product on the right, message:
> intensive Feuchtigkeit und Glow.

> continue

## Required boundaries

- Read-only in Shopify until the publish step; there, confirm each write
  separately (upload, alt text, metaobject, each translation set).
- Always create a new metaobject. Existing metaobjects, theme files, products,
  and discounts stay untouched; automatic block creation is out of scope.
- Claims come only from the live product/collection/article, the brand site,
  or `Products/<Company>/<Product>/brief.txt`. Ask when a claim cannot be verified.
- The user approves German and English copy together before the image prompt is written.

## Session 1: brief and image prompt

1. **Intake.** Ask what is still missing, in one message:
   1. Subject type: product, collection, blog article, promotion, or general.
   2. Target (handle or URL). Resolve it read-only in Shopify and confirm it is
      published; it becomes the link and the fact source. Promotion and general
      slides still need a link target: a collection, page, or `/collections/all`.
   3. What the slide should show (scene, products, mood).
   4. Where the main object (bottles, device, person) sits: left, center, or right.
   5. Key message, or the exact German wording.
   6. Optional: campaign end date.

   Intake is complete when every question has an answer or an allowed "none".
2. **Resolve.** Follow [shopify-contract.md](references/shopify-contract.md#reads).
   Resolve is complete when the store is verified, the target is published,
   the handle is free (`-2`, `-3`, … if taken), and every fact source is listed.
3. **Copy.** Follow [slide-copy.md](references/slide-copy.md). Keep exact
   wording (check limits and claims) or propose 2–3 German options; write the
   English version. Wait for joint DE+EN approval.
4. **Image prompt.** Follow [image.md](references/image.md#prompt): write the
   prompt and derive the Box position from the object position.
5. **Save and pause.** Write `Slides/<YYYY-MM-DD>-<handle>/brief.md` (format
   below) with `status: "awaiting-image"`. Show the prompt and tell the user to
   drop the generated image into that folder and run
   `/shopify-slideshow-create continue`.

## Session 2: continue and publish

1. **Find the brief.** Pick the newest `Slides/*/brief.md` with
   `status: "awaiting-image"` or `"ready-to-publish"`; if several qualify, ask
   which. Read the whole brief before acting.
2. **Prepare the image.** From this skill folder run:

   ```bash
   python scripts/prepare_image.py <slide-folder> [--image <path>]
   ```

   It writes `<handle>.<ext>` at exactly 1536×1024. On a non-zero exit, relay
   its message and ask for the image. Show every `WARNING` line; on an
   upscaling warning, ask whether to continue or regenerate larger.
3. **Alt text.** Look at the processed image and write German and English alt
   text per [image.md](references/image.md#alt-text). Save it to the brief and
   set `status: "ready-to-publish"`.
4. **Publish.** Follow [shopify-contract.md](references/shopify-contract.md#writes)
   step by step, recording every ID in the brief as it is returned.
5. **Hand over.** Print the [mapping checklist](references/shopify-contract.md#mapping-checklist)
   with this slide's Box position, set `status: "published"`, and list any
   step that did not complete.

## Brief format

`Slides/<YYYY-MM-DD>-<handle>/brief.md` (creation date, lowercase ASCII handle):

```markdown
---
handle: "gigi-pdrn-serum-lumine"
status: "awaiting-image"   # awaiting-image | ready-to-publish | published
link: "https://yuliskin.de/products/gigi-pdrn-pure-serum-lumine"
box_align: "middle-left"
---

## Intake
<answers, resolved target title/type/status>

## Copy
| Field | DE | EN |
| --- | --- | --- |
| heading | … | … |
| subheading | … | … |
| button_label | … | … |

## Image prompt
<the prompt>

## Alt text
DE: …
EN: …

## Sources
<fact sources used for the copy>

## Shopify
<file ID, CDN URL, metaobject ID, translation results, as they are returned>
```

Product photos downloaded as generator references go in a `product-photos/`
subfolder, so the slide folder itself holds only the one slide image.
