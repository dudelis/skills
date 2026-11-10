# Slide image: prompt, composition, processing, alt text

Every slide image is **1536×1024 (3:2)**, PNG, JPG, or WebP. The heading,
description, and button are rendered by the theme on top of the image, so the
image itself carries the scene only.

## Composition

The text box sits opposite the main object. The Box position goes into the
brief's `box_align` and the mapping checklist:

| Main object | Free space in the image | Box position |
| --- | --- | --- |
| left | right half | `middle-right` |
| right | left half | `middle-left` |
| center | lower third | `bottom-center` |

## Prompt

Write the prompt in English (both ChatGPT and Gemini follow English best),
filled from the intake answers:

```
Create a wide homepage banner image, exactly 1536 × 1024 px (3:2 landscape),
photographic, soft natural light. Scene: <what the user described>.
Main subject: <object> placed on the <left/right/center> of the frame.
Keep calm, uncluttered negative space on the <opposite side / lower third>
for a text overlay. Mood: calm, premium skincare studio. Palette: warm cream,
soft white, natural beige, with <accent from the product packaging>.
No text, no letters, no logos, no watermarks, no prices.
High-end skincare aesthetic, realistic textures, no plastic look.
```

- **Real products on the slide:** generated packaging comes out inaccurate.
  Download the product's featured image(s) from Shopify into
  `product-photos/` and add to the prompt: "Use the attached product photos
  as the exact products; keep their shape, colours, and printed labels
  unchanged." Tell the user to attach those files in the generator. Printed
  product names on real packaging are fine.
- In ChatGPT, choose the landscape 1536×1024 size; in Gemini, choose a
  landscape 3:2 aspect ratio. The script crops whatever comes back.

## Processing

`scripts/prepare_image.py` takes the one image dropped into the slide folder
(or `--image <path>`), crops to 3:2 from the center, resizes to 1536×1024, and
saves it as `<handle>.<ext>` in the source's format. That filename becomes the
CDN URL, so the user uploads this file, not the original. Its tests run from
`scripts/` with `python -m unittest test_prepare_image`.

When a center crop cuts the main object, ask the user to regenerate or crop by
hand and pass the result with `--image`.

## Alt text

Write alt text after looking at the processed image, describing what it
actually shows:

- German and English, ≤ 125 characters each, real umlauts in German.
- Pattern: what is visible + the slide's subject, e.g.
  "Re[Sens] Bakuchiol Neuro Eye Cream und Barrier & Biome Hand Cream – neu bei YuliSkin".
- Name products and brands as they appear on the packaging; describe people
  by role ("Kosmetikerin"), not by appearance.
