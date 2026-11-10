# Shopify contract: reads, writes, mapping checklist

Discover fields from the live schema instead of guessing, and never guess an
ID or a handle. Record every returned ID in the brief's `## Shopify` section
as soon as it arrives, so an interrupted run can resume.

## Store facts

Observed on **2026-11-02**; recheck before relying on them:

- The homepage slideshow is the custom `ys-slideshow` section in the main theme
  (`yuliskin-de-shopify/main`, GitHub-connected). Each slide block reads its
  image, heading, description, and button label from a `slideshow` metaobject
  through dynamic sources. Theme writes to the main theme are blocked for the
  Shopify tools, which is why the user wires the block.
- `slideshow` metaobject fields: `heading` (single line, required),
  `subheading` (single line), `button_label` (single line), `image` (file
  reference), `button_link` (url). Translatable and publishable.
- Shop locales: `de` (primary), `en` (published).
- Every live slide block used heading size H1, text alignment center, content
  background on, and image overlay 20 %; the mapping checklist repeats these.

## Reads

| Need | Source | Use |
| --- | --- | --- |
| Store check | `shop { name primaryDomain { host } }` | Must be YuliSkin on `yuliskin.de`; stop otherwise |
| Target | Product, collection, or article by handle: title, status/published state, `onlineStoreUrl` or handle | Must be published. Link = `https://yuliskin.de/products|collections|blogs/<blog>/<handle>`, no `/en` |
| Fact sources | Product description and metafields, brand site, `Products/<Company>/<Product>/brief.txt` | Record each one under `## Sources` |
| Product photos | The product's featured media URL | Download to `product-photos/` only when the slide shows real products |
| Handle check | `metaobjectByHandle(handle: {type: "slideshow", handle: "<handle>"})` | `null` = free. Otherwise try `-2`, `-3`, … |

## Writes

Before the first write, recheck that the store is YuliSkin and the handle is
still free. If the handle was taken meanwhile, propose the next free suffix;
on a yes, update `handle` in the brief, rename the slide folder, and rerun
`prepare_image.py` so the file name matches. Show what each step will write
and wait for an explicit yes. Before retrying an uncertain write, read the
current state first, so nothing is created twice.

1. **Upload the image.** Call the file-upload tool; it opens a picker on the
   user's device. Tell the user to choose `<slide-folder>/<handle>.<ext>`
   and to say when the upload is done. Read the file ID from the widget update
   or the uploaded-files lookup. Then query the MediaImage until `fileStatus`
   is `READY` and the image is 1536×1024; `FAILED` stops the run.
2. **German alt text.** Once the file is `READY`, `fileUpdate(files: [{id, alt}])`
   with the German alt text. If Shopify stored the file under another name,
   set `filename` to `<handle>.<ext>` in the same call.
3. **Metaobject.** `metaobjectCreate` with `type: "slideshow"`, the handle,
   fields `heading`, `subheading`, `button_label` (German), `image` (the
   MediaImage GID), `button_link` (the link), and
   `capabilities: {publishable: {status: ACTIVE}}`. A draft would render blank
   in the theme, and an ACTIVE but unwired metaobject shows nowhere.
4. **English slide texts.** Fetch `translatableResource` for the new
   metaobject and register `en` for `heading`, `subheading`, and `button_label`
   with their returned digests via `translationsRegister`. `image` and
   `button_link` stay shared across languages; never register them.
5. **English alt text.** Fetch `translatableResource` for the MediaImage and
   register `en` for its `alt` key the same way.
6. **Read back.** Verify the metaobject's fields and ACTIVE status, its `en`
   translations, the MediaImage's German alt, `READY` status, and size, and
   its `en` alt translation. Compare each value with the brief. Any mismatch or
   missing value is reported as incomplete, never as success.

## Mapping checklist

Print this for the user with the slide's values filled in:

1. Online Store → Themes → Customize → Home page → slideshow section → **Add slide**.
2. Connect the dynamic sources to metaobject **Slideshow → `<handle>`**:
   - Image ← `image`
   - Heading ← `heading`
   - Description ← `subheading`
   - Button label ← `button_label`
   - Link ← `button_link`
3. Box position: **`<box_align>`**.
4. Match the other slides' settings (see [Store facts](#store-facts)): heading
   size H1, text alignment center, content background on, image overlay 20 %.
5. Drag the slide to its position, save, and check the storefront in German
   and English (desktop and mobile).
