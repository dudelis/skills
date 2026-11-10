# Blog types, intake questions, and body templates

Read at the start of every creation, before asking the user anything. The blog
type decides the intake questions, the body structure, and the template suffix.
The markup below is the single layout source; existing articles show tone and
topics only, because their HTML varies by age.

## The two blog types

| | Angebote & Neuheiten | Kosmetik Insider |
| --- | --- | --- |
| Blog handle | `news` | `cosmetics-insider` |
| Purpose | Announce new products, sets, and promotions | Explain a tip, routine, or why a kind of product is needed |
| Body products | Required: one or more | Optional: products that illustrate or prove a point |
| Typical length | 200–400 words | 450–700 words |
| Leads with | The product news | The reader's question |

Resolve each blog's GID from its handle in the live store.

## Intake questions

Ask in this order, one group per message, skipping anything the user already
supplied. The intake is complete when every row has an answer, including an
explicit "none" where that is allowed.

| # | Question | Angebote & Neuheiten | Kosmetik Insider |
| --- | --- | --- | --- |
| 1 | Which blog type? | — | — |
| 2 | Topic and source material | The news: launch, set, promotion, dates | The tip, routine, or reader question |
| 3 | Body products | Which product(s) to place in the text; at least one | Whether any products should illustrate the point; "none" allowed |
| 4 | Promotion details | Discount code, end date, and target collection, or "none" | — |
| 5 | Associated collection below the article | Which existing collection, or "none" | Which existing collection, or "none" |
| 6 | Collection-section heading | Asked whenever question 5 names a collection | Same |
| 7 | Banner | Supplied file/URL, or a generation prompt for the user's own generator | Same |

For question 6, propose a German and an English heading for the user to accept
or reword. A collection without a heading renders the product grid untitled, so
the heading is required whenever a collection is set.

Resolve every named product to its Shopify catalog entry and confirm ambiguous
matches before planning. For Kosmetik Insider, suggest fitting catalog products
with a reason each when the user is unsure; they stay suggestions until chosen.

## Product images, links, and ALT text

Each body product appears as a product row using its **featured (first) catalog
image**, taken from the live product's existing Shopify CDN URL. Both the image
and the button link to that product's page, so a click on the image opens the
product.

- Write internal links as relative paths, identical in both bodies:
  `/products/<handle>`, `/collections/<handle>`, `/discount/CODE?redirect=…`.
  The storefront adds the `/en` prefix itself when the shop is switched to
  English, so a relative path in the English body carries no locale prefix.
- Only a full URL in the English body carries the locale:
  `https://yuliskin.de/en/products/<handle>`. Use a full URL only where a
  relative path cannot work.
- ALT text is the image's stored catalog `altText`. When that is empty, use
  `<Brand> <Product name>` exactly as in the product title. The English body
  uses the English translation of the same value.
- Illustration images (non-product) get a short description of what is shown,
  written in the body's language.
- Every `<img>` carries a non-empty `alt`; the `alt` belongs on the `<img>`.

## Shared wrapper and CSS

Every body is one HTML fragment wrapped in `<div class="ys-post">`, starting
with this style block whenever it contains rows or buttons. Headings start at
`<h2>`; the theme renders the article title as `<h1>`.

```html
<div class="ys-post">
<style>
  .ys-post .product-container { display: flex; flex-wrap: wrap; margin-bottom: 20px; }
  .ys-post .product-container img { max-width: 100%; height: auto; border-radius: 8px; }
  .ys-post .product { display: flex; align-items: center; width: 100%; margin-bottom: 40px; }
  .ys-post .product:nth-child(2n) { flex-direction: row-reverse; }
  .ys-post .product-image { flex: 1; }
  .ys-post .product-description { flex: 1; padding: 0 20px; display: flex; flex-direction: column; justify-content: center; }
  .ys-post .product-title { font-weight: bold; margin-bottom: 12px; }
  .ys-post .btn-learn-more, .ys-post .btn-discount {
    margin-top: 15px; padding: 10px 20px; background-color: #b4005f; color: #fff !important;
    border: none; border-radius: 4px; font-weight: 600; text-decoration: none; text-align: center;
    align-self: center; width: fit-content; transition: background-color 0.3s ease;
  }
  .ys-post .btn-learn-more:hover, .ys-post .btn-discount:hover { background-color: #920048; }
  @media (max-width: 768px) {
    .ys-post .product, .ys-post .product:nth-child(2n) { flex-direction: column; text-align: center; }
    .ys-post .product-description { padding: 10px 0; order: 2; }
    .ys-post .product-image { order: 1; }
    .ys-post .btn-learn-more, .ys-post .btn-discount { margin: 20px auto 0 auto; }
  }
</style>
<!-- body -->
</div>
```

## Building blocks

**Product row** — one per body product, all rows inside a single
`product-container` so they alternate sides:

```html
<div class="product-container">
  <div class="product">
    <div class="product-description">
      <h4 class="product-title">Brand Product – kurzer Nutzen</h4>
      <p>Ein bis drei Sätze: was es ist und für wen.</p>
      <ul>
        <li>Optional: bis zu drei verifizierte Vorteile</li>
      </ul>
      <a href="/products/handle" class="btn-learn-more">Mehr erfahren</a>
    </div>
    <div class="product-image">
      <a href="/products/handle"><img src="https://cdn.shopify.com/…" alt="Brand Product"></a>
    </div>
  </div>
</div>
```

Button labels: `Mehr erfahren` / `Learn more` for products, `Zur Kollektion` /
`View collection` for a collection row.

**Illustration row** — the same row with an explanatory image, the text placed
directly in `product-description`, and no title, link, or button. Use it in
Kosmetik Insider to break up long explanations when the user supplies images.

**Discount button** — only for a promotion confirmed in question 4:

```html
<p style="text-align:center"><a href="/discount/CODE?redirect=%2Fcollections%2Fhandle" class="btn-discount">15% Rabatt mit Code CODE</a></p>
```

**Closing links** — a short list linking each body product and the related
collection, under a heading such as `Jetzt bei YuliSkin entdecken`.

**Disclaimer** — close product-led articles with:

```html
<p><strong>Hinweis:</strong> Kosmetische Produkte zur äußerlichen Anwendung. Die beschriebenen Eigenschaften beziehen sich auf kosmetische Pflegeeffekte und stellen keine medizinischen Aussagen dar.</p>
```

English: `Disclaimer: Cosmetic products for external use only. The described
benefits relate to cosmetic appearance and skincare support, not medical claims.`

## Angebote & Neuheiten outline

1. `<h2>` news headline, then one intro paragraph naming every body product.
2. Promotion paragraph and discount button, when a promotion applies.
3. One product row per body product.
4. Optional short sections such as `Für wen geeignet?` and `Anwendung`.
5. Closing links.
6. Disclaimer.

Done when every body product from the intake has exactly one row with its
featured image, a working product link on image and button, and an ALT text.

## Kosmetik Insider outline

1. Opening paragraph that states the reader's question; no heading above it.
2. `<h2>` sections that explain the why and the how, with lists where they help
   and illustration rows where images were supplied.
3. With body products: an `<h2>` section such as `Empfohlene Produkte` holding
   one product row per product, each description tying the product to the point
   it illustrates. With "none": leave this section out entirely.
4. `<h2>` Fazit, ending with a link to the associated or most relevant
   collection when one exists.
5. Disclaimer, when the article has product rows.

Done when every selected product has a row that names the point it supports,
and every product mentioned by name in the text links to its product page.

## Template suffix

- Associated collection set: `blog-post-with-collection`.
- No associated collection: the default `article` template.

Recheck the binding described in [shopify-contract.md](shopify-contract.md)
before relying on the suffix.
