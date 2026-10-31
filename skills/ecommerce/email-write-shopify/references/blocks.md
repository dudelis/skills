# Block library

These blocks come from the YuliSkin October 2026 holiday email.

**Placeholders**
- Lowercase `[[token]]` values are theme colours. See [brand-themes.md](brand-themes.md).
- Uppercase `[[SLOT]]` values are content to fill in.
- Nothing in `[[...]]` may remain in the final file.

**Formatting**
- Keep all styles inline.
- Keep one attribute group per line, so files stay readable and under 50 KB.
- Text is centred by default.

## Contents

[Shell](#shell) · [Banner](#banner) · [Greeting](#greeting) · [Heading and text](#heading-and-text) ·
[Spacer](#spacer) · [Panel](#panel) · [Logo grid](#logo-grid) · [Product grid](#product-grid) ·
[Collection tiles](#collection-tiles) · [Article card](#article-card) ·
[Ingredient spotlight](#ingredient-spotlight) · [Info box](#info-box) ·
[Discount code box](#discount-code-box) · [Button](#button) · [Deadline line](#deadline-line) ·
[Divider](#divider) · [Signature](#signature) · [Terms](#terms) · [Countdown split](#countdown-split) ·
[Live price (advanced)](#live-price-advanced)

## Shell

The outer frame and white card. All content blocks go inside `CONTENT`.

```html
<!-- YULISKIN · [[CAMPAIGN NAME]] · Shopify Email Custom Liquid -->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="[[page_bg]]"
  style="width:100%;background-color:[[page_bg]];border-collapse:collapse;font-family:Arial,Helvetica,sans-serif;">
  <tr>
    <td align="center" style="padding:20px 12px 30px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="[[card_bg]]"
        style="width:100%;max-width:560px;background-color:[[card_bg]];border-collapse:collapse;">
        <!-- BANNER -->
        <tr>
          <td align="center" style="padding:34px 22px;font-family:Arial,Helvetica,sans-serif;color:[[heading]];text-align:center;">
            <!-- CONTENT -->
          </td>
        </tr>
      </table>
      <!-- TERMS -->
    </td>
  </tr>
</table>
```

## Banner

A row placed at `<!-- BANNER -->`. Drop the `<a>` if the banner has no link.

```html
<tr>
  <td align="center" style="padding:0;">
    <a href="[[BANNER LINK]]" target="_blank" style="display:block;text-decoration:none;">
      <img src="[[BANNER URL]]" alt="[[BANNER ALT]]" width="560"
        style="display:block;width:100%;max-width:560px;height:auto;border:0;">
    </a>
  </td>
</tr>
```

## Greeting

Optional, and off by default. `default` also covers an empty first name.

```html
<p style="margin:0 0 14px;color:[[body]];font-size:16px;line-height:1.6;">
  Hallo {{ customer.first_name | default: "du" }},
</p>
```

## Heading and text

```html
<h2 style="margin:0 0 22px;color:[[heading]];font-size:26px;font-weight:600;line-height:1.3;">[[HEADLINE]]</h2>

<h3 style="margin:34px 0 14px;color:[[heading]];font-size:22px;font-weight:600;line-height:1.35;">[[SECTION HEADING]]</h3>

<p style="margin:0 0 18px;color:[[body]];font-size:16px;line-height:1.7;">[[PARAGRAPH]]</p>

<p style="margin:0 0 30px;color:[[soft]];font-size:14px;line-height:1.6;">[[SMALL NOTE]]</p>
```

Inline highlights inside a paragraph:

```html
<strong style="color:[[heading]];">[[KEY FACT]]</strong>
<strong style="color:[[accent]];">[[EMOTIONAL HOOK]]</strong>
```

## Spacer

Use a spacer for vertical space between tables. Do not put margins on tables,
because Outlook ignores them.

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="width:100%;border-collapse:collapse;">
  <tr><td height="24" style="height:24px;font-size:1px;line-height:1px;">&nbsp;</td></tr>
</table>
```

## Panel

A tinted section that wraps grids, article cards, and the spotlight.

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="[[panel_bg]]"
  style="width:100%;background-color:[[panel_bg]];border-collapse:collapse;">
  <tr>
    <td align="center" style="padding:28px 14px 26px;">
      <h3 style="margin:0 0 12px;color:[[heading]];font-size:21px;font-weight:600;line-height:1.3;">[[PANEL HEADING]]</h3>
      <p style="margin:0 0 24px;color:[[muted]];font-size:15px;line-height:1.6;">[[PANEL INTRO]]</p>
      <!-- PANEL CONTENT -->
      <!-- optional footnote: -->
      <p style="margin:22px 0 0;color:[[soft]];font-size:13px;line-height:1.6;">[[FOOTNOTE]]</p>
    </td>
  </tr>
</table>
```

## Grid container (logos, products, collections)

The container goes at `<!-- PANEL CONTENT -->`. It holds two tiles per row.
With an odd number of items, the last cell becomes an "Alle ansehen →" tile
that links to the matching collection or `/collections/all`.

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="6" border="0" bgcolor="[[panel_bg]]"
  style="width:100%;table-layout:fixed;border-collapse:separate;border-spacing:6px;background-color:[[panel_bg]];">
  <tr>
    <!-- TILE --><!-- TILE -->
  </tr>
</table>
```

### Logo grid

Logo tile. The logo comes from the collection image. Use a logo width of
95–165 px, set to balance how heavy each logo looks.

```html
<td width="50%" height="115" align="center" valign="middle" bgcolor="[[tile_bg]]"
  style="width:50%;height:115px;padding:14px 8px;background-color:[[tile_bg]];text-align:center;vertical-align:middle;">
  <a href="[[COLLECTION OR DISCOUNT LINK]]" target="_blank" style="display:inline-block;text-decoration:none;">
    <img src="[[LOGO URL]]" alt="[[BRAND NAME]]" width="[[LOGO WIDTH]]"
      style="display:block;width:[[LOGO WIDTH]]px;max-width:100%;height:auto;margin:0 auto;border:0;">
  </a>
</td>
```

### Product grid

Product tile. Use the featured image at `&width=400`. Prices are left out by default.

```html
<td width="50%" align="center" valign="top" bgcolor="[[tile_bg]]"
  style="width:50%;padding:14px 10px 16px;background-color:[[tile_bg]];text-align:center;vertical-align:top;">
  <a href="[[PRODUCT OR DISCOUNT LINK]]" target="_blank" style="display:block;text-decoration:none;">
    <img src="[[PRODUCT IMAGE URL]]" alt="[[BRAND]] [[PRODUCT TITLE]]" width="200"
      style="display:block;width:200px;max-width:100%;height:auto;margin:0 auto 10px;border:0;">
    <span style="display:block;color:[[soft]];font-size:11px;letter-spacing:1px;line-height:1.4;text-transform:uppercase;">[[BRAND]]</span>
    <span style="display:block;margin:4px 0 8px;color:[[heading]];font-size:14px;font-weight:600;line-height:1.4;">[[PRODUCT TITLE]]</span>
    <span style="display:block;color:[[accent]];font-size:13px;font-weight:700;line-height:1.4;">Ansehen &rarr;</span>
  </a>
</td>
```

### Collection tiles

Collection tile. Same structure as a product tile. Use the collection image,
put the collection title in place of brand + product, and label the link
`Entdecken &rarr;`.

## Article card

Goes at `<!-- PANEL CONTENT -->`, or inside its own panel with the heading
"Mehr dazu im Blog". Use 1–3 cards, each in its own row.

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="[[tile_bg]]"
  style="width:100%;background-color:[[tile_bg]];border-collapse:collapse;">
  <tr>
    <td style="padding:0;">
      <a href="[[ARTICLE URL]]" target="_blank" style="display:block;text-decoration:none;">
        <img src="[[ARTICLE IMAGE URL]]" alt="[[ARTICLE TOPIC]]" width="500"
          style="display:block;width:100%;max-width:500px;height:auto;border:0;">
      </a>
    </td>
  </tr>
  <tr>
    <td align="left" style="padding:16px 18px 20px;text-align:left;">
      <p style="margin:0 0 8px;color:[[heading]];font-size:17px;font-weight:600;line-height:1.4;">[[ARTICLE TITLE]]</p>
      <p style="margin:0 0 12px;color:[[muted]];font-size:14px;line-height:1.65;">[[ONE OR TWO LINE TEASER]]</p>
      <a href="[[ARTICLE URL]]" target="_blank" style="color:[[accent]];font-size:14px;font-weight:700;text-decoration:none;">Weiterlesen &rarr;</a>
    </td>
  </tr>
</table>
```

## Ingredient spotlight

Goes inside a panel. One row per ingredient or key fact. Use at most 4 rows,
and leave out the border on the last one.

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="[[tile_bg]]"
  style="width:100%;background-color:[[tile_bg]];border-collapse:collapse;">
  <tr>
    <td align="left" style="padding:14px 18px;border-bottom:1px solid [[divider]];text-align:left;">
      <p style="margin:0 0 4px;color:[[accent]];font-size:15px;font-weight:700;line-height:1.4;">[[INGREDIENT]]</p>
      <p style="margin:0;color:[[muted]];font-size:14px;line-height:1.65;">[[WHAT IT DOES AND WHY IT MATTERS]]</p>
    </td>
  </tr>
</table>
```

## Info box

Use for shipping notes, how to apply a product, or service notes.

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="[[panel_bg]]"
  style="width:100%;background-color:[[panel_bg]];border-collapse:collapse;">
  <tr>
    <td align="center" style="padding:22px 18px;">
      <p style="margin:0 0 10px;color:[[accent]];font-size:16px;font-weight:700;line-height:1.4;">[[EMOJI]] [[INFO TITLE]]</p>
      <p style="margin:0;color:[[muted]];font-size:14px;line-height:1.7;">[[INFO TEXT, <br><br> between paragraphs]]</p>
    </td>
  </tr>
</table>
```

## Discount code box

Put an h3 and an intro paragraph before it, and a "how to redeem" note after it:
"Gib den Code beim Checkout ein oder klicke auf den Button, um ihn direkt zu aktivieren."

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="[[code_bg]]"
  style="width:100%;background-color:[[code_bg]];border-collapse:collapse;">
  <tr>
    <td align="center" style="padding:24px 15px;">
      <p style="margin:0 0 9px;color:[[code_label]];font-size:12px;font-weight:600;letter-spacing:2px;line-height:1.4;">DEIN RABATTCODE</p>
      <p style="margin:0;color:[[code_text]];font-size:27px;font-weight:700;letter-spacing:1px;line-height:1.3;">[[CODE]]</p>
    </td>
  </tr>
</table>
```

## Button

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"
  style="width:100%;max-width:380px;margin:0 auto;border-collapse:collapse;">
  <tr>
    <td align="center" bgcolor="[[button_bg]]" style="background-color:[[button_bg]];border-radius:7px;text-align:center;">
      <a href="[[BUTTON LINK]]" target="_blank"
        style="display:block;padding:19px 16px;color:[[button_text]];font-family:Arial,Helvetica,sans-serif;font-size:17px;font-weight:700;line-height:1.35;text-decoration:none;">
        [[BUTTON LABEL]] &rarr;
      </a>
    </td>
  </tr>
</table>
```

## Deadline line

The written deadline. It always appears with a discount, even when a native
countdown is present.

```html
<p style="margin:22px 0 27px;color:[[accent]];font-size:14px;font-weight:600;line-height:1.6;">
  Nur bis [[DD.MM.YYYY]] &nbsp;&bull;&nbsp; Ab [[MIN]] € Bestellwert
</p>
```

## Divider

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="width:100%;margin-top:28px;border-collapse:collapse;">
  <tr><td style="height:1px;background-color:[[divider]];font-size:1px;line-height:1px;">&nbsp;</td></tr>
</table>
```

## Signature

The thank-you line changes per email. The sign-off is fixed. Shop address and
unsubscribe links come from the native footer and never go in the block.

```html
<p style="margin:27px 0 11px;color:[[body]];font-size:16px;line-height:1.6;">[[THANK-YOU LINE]]</p>
<p style="margin:0;color:[[body]];font-size:15px;line-height:1.65;">
  Liebe Grüße<br>
  <strong>Julia Fukszon</strong><br>
  YuliSkin Kosmetik Studio
</p>
```

## Terms

Placed at `<!-- TERMS -->`, outside the white card. Include terms only with a
discount, and build them from the live discount: end date and time, value,
minimum order, scope, and exclusions.

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:540px;border-collapse:collapse;">
  <tr>
    <td align="center" style="padding:20px 10px 0;text-align:center;font-family:Arial,Helvetica,sans-serif;color:[[fine]];font-size:11px;line-height:1.65;">
      Gültig bis einschließlich [[DD.MM.YYYY]], [[HH:MM]] Uhr. [[VALUE]] auf [[SCOPE]] ab [[MIN]] € Bestellwert. [[EXCLUSIONS]]
    </td>
  </tr>
</table>
```

## Countdown split

When the native Countdown sits mid-email, write two self-contained files, each
with its own complete shell:

- `email-part-1.liquid`:
  - Shell with outer padding `20px 12px 0` and content padding `34px 22px 28px`.
  - Contains the banner and the blocks before the timer.
- `email-part-2.liquid`:
  - Shell with outer padding `0 12px 30px` and content padding `28px 22px 34px`.
  - Contains the blocks after the timer, the signature, and the terms.

If the timer goes directly below the banner or at the very end, no split is
needed. Place the native Countdown before or after the single block.

## Live price (advanced)

Use only after the user has confirmed the price format in a test send. Uncertain
points: `price` may be in cents, and the `money` filter may not be available in
Shopify Email.

```liquid
{%- assign p = all_products['[[HANDLE]]'] -%}
<span style="display:block;color:[[heading]];font-size:14px;font-weight:700;">{{ p.price | money }}</span>
```
