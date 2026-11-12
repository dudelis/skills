---
name: shopify-slideshow-create
description: >
  Prepares one German/English YuliSkin homepage slide locally in `ys-slides/`:
  copy plus generated desktop and mobile images, no Shopify writes. Use when
  the user wants a new homepage slide, or continues a slide awaiting its images.
---

# Slideshow Create Shopify

Prepare one homepage slide (heading, short description, button, desktop image,
mobile image, alt text) in a local slide folder. The user uploads the images,
creates the `slideshow` metaobject, and wires the theme block by hand.

## Quick start

> Create a slide for the new GIGI PDRN serum, text middle-left, message:
> intensive Feuchtigkeit und Glow.

> continue

## Required boundaries

- Shopify is read-only for the whole run: reads check the user's context, the
  target, the link, and the handle.
- Every file goes into the slide folder `ys-slides/<YYYY-MM-DD>-<handle>/`
  (creation date, lowercase ASCII handle). `ys-slides/` sits at the project
  root; create it when it is missing.
- Claims come only from the live product/collection/article, the brand site,
  or `Products/<Company>/<Product>/brief.txt`. Ask when a claim cannot be verified.
- The user approves German and English copy together before the prompts are written.

## Run

1. **Intake.** Ask what is still missing, in one message:
   1. Subject type: product, collection, blog article, promotion, or general.
   2. Target (handle or URL). It becomes the link and the fact source.
      Promotion and general slides still need a link target: a collection,
      page, or `/collections/all`.
   3. What the slide should show (scene, products, mood).
   4. Where the text sits on the desktop image: one of the 9 Box positions
      (top/middle/bottom × left/center/right). The main object goes opposite,
      per [image.md](references/image.md#desktop-composition).
   5. Key message, or the exact German wording.
   6. Optional: campaign end date.

   Intake is complete when every question has an answer or an allowed "none".
2. **Resolve.** Follow [shopify-reads.md](references/shopify-reads.md).
   Resolve is complete when the store is verified, the target is published,
   the handle is free (`-2`, `-3`, … if taken), and every fact source is listed.
3. **Copy.** Follow [slide-copy.md](references/slide-copy.md). Keep exact
   wording (check limits and claims) or propose 2–3 German options; write the
   English version. Wait for joint DE+EN approval.
4. **Prompts.** Create the slide folder, then write `prompts.md` with the
   desktop and the mobile prompt per [image.md](references/image.md#prompts),
   and `brief.md` (format below) with `status: "awaiting-images"`. The prompts
   need no approval; they are the record of what was generated.
5. **Generate.** With an image-generation tool, generate both images per
   [image.md](references/image.md#generation); Generate is complete when
   `generated.<ext>` and `generated-mobile.<ext>` are in the slide folder. Without one, tell
   the user that no image tool is available, give the path to `prompts.md`,
   and explain the hand-off: generate both images elsewhere, drop them into
   the slide folder (the mobile one with a file name ending in `-mobile`), and
   run `/shopify-slideshow-create continue`. The run ends here.
6. **Process.** From this skill folder run:

   ```bash
   python scripts/prepare_image.py <slide-folder>
   ```

   It writes `<handle>.<ext>` at 1536×1024 and `<handle>-mobile.<ext>` at
   1536×864. On a non-zero exit, relay its message and ask for the missing
   image. Show every `WARNING` line; on an upscaling or shape warning, ask
   whether to continue or regenerate.
7. **Alt text.** Look at both processed images and write one German and
   English alt text pair per [image.md](references/image.md#alt-text). Save it
   to the brief and set `status: "ready"`.
8. **Report.** In chat: both image paths, then heading, description, and button
   label in German and in English, then the German and English alt text.

`continue` picks the newest `ys-slides/*/brief.md` with
`status: "awaiting-images"` (ask which when several qualify), reads the whole
brief, and resumes at step 6.

## Brief format

`ys-slides/<YYYY-MM-DD>-<handle>/brief.md`:

```markdown
---
handle: "gigi-pdrn-serum-lumine"
status: "awaiting-images"   # awaiting-images | ready
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

## Alt text
DE: …
EN: …

## Sources
<fact sources used for the copy>
```

Product photos downloaded as generator references go in a `product-photos/`
subfolder, so the slide folder itself holds only the slide images, the brief,
and `prompts.md`.
