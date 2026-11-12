# Slide images: composition, prompts, generation, processing, alt text

Every slide has two images, PNG, JPG, or WebP, of the same scene and products:

| Image | Size | Text |
| --- | --- | --- |
| Desktop `<handle>.<ext>` | 1536×1024 (3:2) | Theme renders heading, description, and button on top, at the Box position |
| Mobile `<handle>-mobile.<ext>` | 1536×864 (16:9), the wide mobile slideshow frame | Theme renders them below the image |

Both images carry the scene only.

## Desktop composition

The text position from intake is the Box position (`box_align` in the brief).
The main object (bottles, device, person) fills the part of the frame away
from the text:

| Box position | Main object | Space for text |
| --- | --- | --- |
| `top-left`, `middle-left`, `bottom-left` | fills the right part | calm, uncluttered left part |
| `top-right`, `middle-right`, `bottom-right` | fills the left part | calm, uncluttered right part |
| `top-center`, `middle-center`, `bottom-center` | fills the whole frame; the image is a background | none reserved |

## Mobile composition

- Same products and visual style as the desktop image.
- Products centered, with every product and bag fully visible.
- Products fill the image, with small margins around the edges.
- No space reserved for text.

## Prompts

Write both prompts in English (image generators follow English best) into
`prompts.md`, filled from the intake answers.

Desktop:

```
Create a wide homepage banner image, exactly 1536 × 1024 px (3:2 landscape),
photographic, soft natural light. Scene: <what the user described>.
Main subject: <object>, <placement from the desktop composition table>.
<Left/right column: Keep the <left/right> part calm and uncluttered for a
text overlay. Center column: Let the scene fill the whole frame.>
Mood: calm, premium skincare studio. Palette: warm cream, soft white,
natural beige, with <accent from the product packaging>.
No text, no letters, no logos, no watermarks, no prices.
High-end skincare aesthetic, realistic textures, no plastic look.
```

Mobile, generated from the desktop image:

```
Turn the attached desktop banner into a separate mobile banner, ideally
1536 × 864 px (16:9 landscape), matching the wide mobile slideshow frame.
Keep the same products and visual style.
Center the products and keep every product and bag fully visible. Let the
products fill the image, with small margins around the edges. Reserve no
space for text. No text, no letters, no logos, no watermarks, no prices.
```

- **Real products on the slide:** generated packaging comes out inaccurate.
  Download the product's featured image(s) from Shopify into
  `product-photos/` and add to both prompts: "Use the attached product photos
  as the exact products; keep their shape, colours, and printed labels
  unchanged." Printed product names on real packaging are fine.
- In ChatGPT, choose the landscape size; in Gemini, choose the closest
  landscape aspect ratio. The script crops whatever comes back. When a tool
  offers only 3:2 for the mobile image, add to the mobile prompt: "Keep every
  product inside the central 16:9 band; the top and bottom 8 % are cropped."

## Generation

Generate the desktop image first, attaching the product photos. Then generate
the mobile image from the mobile prompt with the desktop image and the product
photos attached. A tool that returns both sizes from one request may take both
prompts at once. Save the results in the slide folder as `generated.<ext>`
and `generated-mobile.<ext>`.

## Processing

`scripts/prepare_image.py` reads the slide folder: the image whose file name
ends in `-mobile` is the mobile source, the one other image is the desktop
source (`--image` and `--mobile-image` take explicit paths instead). It
center-crops and resizes each to its exact size and saves `<handle>.<ext>`
and `<handle>-mobile.<ext>` in the source's format. It warns when a source
is upscaled or its shape is more than 20 % off its target (a portrait or
square source), since a center crop then cuts visible content; a 3:2 mobile
source stays below that limit. Its tests run from `scripts/` with
`python -m unittest test_prepare_image`.

When a center crop cuts the main object, regenerate, or crop by hand and pass
the result with `--image` / `--mobile-image`.

## Alt text

Write one alt text pair after looking at both processed images; it serves
both files:

- German and English, ≤ 125 characters each, real umlauts in German.
- Pattern: what is visible + the slide's subject, e.g.
  "Re[Sens] Bakuchiol Neuro Eye Cream und Barrier & Biome Hand Cream – neu bei YuliSkin".
- Name products and brands as they appear on the packaging; describe people
  by role ("Kosmetikerin"), not by appearance.
