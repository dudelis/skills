# Shopify Email contract

Shopify Email is also shown as "Shopify Messaging" in the admin. This file
covers what the platform allows, what the skill may read from Shopify, and how
the user pastes the result.

## Platform facts

- **No public API.** No Admin API creates, reads, or updates Shopify Email
  campaigns or drafts. The skill never tries to; the user pastes the result.
- **Custom Liquid section.**
  - Raw HTML + Liquid, at most **50 KB** per section. The validator fails above
    50 KB and warns above 45 KB; if it warns, strip indentation and blank lines.
  - JavaScript does not run in email clients.
  - CSS background images are unreliable. Use inline styles and `<img>`.
- **Liquid that works in campaigns:**
  - `customer.first_name` (and other customer fields)
  - `shop.name`, `shop.url`
  - `all_products['handle']` with `.title`, `.url`, `.price`, and `| image_url: width: N`
  - `{{ 'now' | date: '%Y' }}`
  - There is no documented `collections['handle']` lookup and no discount object.
    Never rely on them.
- **Native sections the user may combine with the block:**
  - Header (logo)
  - Countdown (generates a live GIF from an end date)
  - Product and Collection (prices handled by Shopify)
  - Discount (shows an existing discount)
  - Footer (address and unsubscribe; cannot be removed)
- **Email client limits:** Gmail does not show SVG, and some Outlook versions do
  not show WebP. Use only PNG, JPG, or GIF.

## Section order the user builds

```
[Native Header – logo]
[Custom Liquid – email.liquid  |  email-part-1.liquid]
[Native Countdown – only when split]
[Custom Liquid – email-part-2.liquid]
[Native Product/Collection – only when prices are wanted]
[Native Footer – address + unsubscribe]
```

## Shopify reads

Verify that the connected store is YuliSkin before resolving anything else.
Discover fields from the live schema instead of guessing. Never guess an ID or a handle.

| Need | Source | Use |
| --- | --- | --- |
| Product tile | Product by handle/search: title, vendor, `onlineStoreUrl`/handle, featured image URL + altText, status | Write image, brand, title, and link into the HTML. Skip non-active products and tell the user. |
| Collection tile / logo | Collection: title, handle, image URL | Logo grid and collection tiles. A missing image gets reported, never replaced by a guess. |
| Article | Article by URL/handle: title, summary, image, handle, blog handle, published state | Blog-Teaser and article cards. Warn if unpublished. |
| Discount | Code discount by code: status, value, minimum requirement, end date, product/collection scope | Compare with the email text and terms. Stop on a mismatch. |
| Fact sources | Product description/metafields, brand site, `Products/<Company>/<Product>/brief.txt` | Record each source in `brief.md`. |

Image URLs:
- Use Shopify CDN URLs with a width parameter: twice the display width, e.g. `&width=400`
  for a 200 px tile.
- If the source is WebP or SVG, try `&format=png` (or `&format=jpg`) on the CDN URL
  and confirm that it loads. If it does not, ask the user for a PNG/JPG.

Prices are not written into the HTML by default. If the user wants prices, add a
native Product section. `all_products[...].price` (see [blocks.md](blocks.md#live-price-advanced))
is only allowed after a test send has confirmed the price format.

## The only write: banner upload

1. Show the local banner file, the target filename (`email-<slug>-banner.jpg`),
   and the alt text.
2. Upload only after the user explicitly says yes, using the file-upload tool,
   once. Before any retry, inspect the uncertain result to avoid duplicates.
3. Record the file ID and CDN URL in `brief.md`.

A supplied public HTTPS image URL needs no upload.

## Links

- Absolute `https://yuliskin.de/...` links, and no UTM parameters unless the user asks.
- Shopify Email tracks clicks itself.
- Discount links: `https://yuliskin.de/discount/<CODE>?redirect=%2Fcollections%2F<handle>`.
  - The code must be active. URL-encode the redirect path, and the code too if
    it has special characters.
  - One code per link.
- German links never contain `/en`. English full links do (see [copy-rules.md](copy-rules.md#english-adaptation)).

## Hand-over notes for the user

- The section order above, and which file goes into which Custom Liquid section.
- The countdown end date and time, plus its colours from [brand-themes.md](brand-themes.md#shopify-editor-settings).
- The email background colour, when the theme is not Standard.
- Subject and preview text, ready to paste.
- Send a test to yourself (Gmail and Outlook if possible) before scheduling.
