# Email types, intake, and recipes

Every email has one **main type**, which supplies the intake questions and the
default block order (recipe). Blocks from other types can be added as add-ons,
for example a discount module inside a Shop-Info email.

## Fixed intake (every email)

Ask these first. Skip any that the user has already answered.

1. **Main type and add-ons.** One of the five types below, plus any extra
   blocks from [blocks.md](blocks.md).
2. **Occasion and goal.** What happens, and what the reader should do.
3. **Send date.** Used for the folder name and for checking deadlines.
4. **Theme.** "Standard YuliSkin or a theme?" See [brand-themes.md](brand-themes.md).
5. **Language.** "German only, or also English?" Default: German only.
6. **Banner.** A finished banner (file or URL), or a ChatGPT/Gemini prompt (the default).
7. **Greeting.** A personal greeting with the customer's first name? Default: off.

## Kampagne / Rabatt

Use for a discount code, a sale, or a seasonal promotion.

**Type questions:**
- The discount code. The user creates it; the skill never does.
- What is promoted: products, collections, brands, or the whole shop.
- Deadline, minimum order value, and exclusions.
- Countdown: yes or no, and its position (after the intro, or before the discount code box).
- Landing page for the button.

**Recipe:**
1. Banner
2. Heading + intro
3. Countdown split (optional)
4. Product grid, logo grid, or collection tiles
5. Discount code box
6. Button
7. Deadline line
8. Divider
9. Signature
10. Terms

**Variant ideas:**
- Urgency first: countdown straight after the intro.
- Story first: occasion and why, then the products.
- Product first: the grid directly under the banner, the code box after it.

**Done when:** every button and tile uses the verified `/discount/CODE?redirect=…`
link, and the terms match the live discount.

## Neuheiten

Use for new products or a new brand in the shop.

**Type questions:**
- Which products or which brand.
- What is special about them, from verified facts only.
- An optional launch offer.
- The button target.

**Recipe:**
1. Banner
2. Heading + intro
3. Product grid, or brand panel (logo + 2–3 sentences)
4. Ingredient spotlight (optional)
5. Button
6. Article card (optional)
7. Divider
8. Signature

**Done when:** each new product appears with a linked image tile and alt text.

## Kosmetik Insider

Use for an educational email: an ingredient, a routine, a skin concern, or why
and how a product works.

**Type questions:**
- The topic and the one key message.
- The fact sources: product page, brand site, or a shopify-product-research brief.
- The products to link.
- A related blog article.

**Recipe:**
1. Banner
2. Heading + hook (one reader problem)
3. Explanation (2–4 short paragraphs)
4. Ingredient spotlight
5. Application info box
6. Product grid (products that contain the ingredient or fit the routine)
7. Article card (optional, "Mehr dazu im Blog")
8. Button
9. Divider
10. Signature

Long explanation paragraphs may use `text-align:left`. Headings stay centred.

**Done when:** every claim is traceable to a source recorded in `brief.md`.

## Blog-Teaser

Use to promote one published blog article.

**Type questions:**
- The article URL or handle. Read it live; fall back to `BlogPosts/<slug>/` for wording.
- Which products from the article to show, if any.

**Recipe:**
1. Banner (offer the article image)
2. Heading
3. Teaser (2–3 sentences, without giving the whole article away)
4. Button "Zum Artikel"
5. Product grid (optional)
6. Divider
7. Signature

**Done when:** the article is published (warn if it is not), and the button
links to the live article URL.

## Shop-Info

Use for a holiday break, shipping changes, opening hours, or a service notice.

**Type questions:**
- What changes.
- Exact dates.
- Impact on orders and shipping.
- An optional thank-you gesture (discount add-on).

**Recipe:**
1. Banner
2. Heading + explanation
3. Highlight paragraph (dates in bold)
4. Info box (shipping or service details)
5. Discount add-on (optional)
6. Divider
7. Signature
8. Terms (only with a discount)

**Done when:** every date appears consistently in the text, the info box, and the terms.

## Proposing variants

Present each variant like this:

```
Variante A – Dringlichkeit zuerst
Banner → H2 + Intro → [Countdown] → 4 Produkte → Code-Box → Button → Frist → Signatur → Bedingungen
Pitch: Der Timer direkt unter der Einleitung erzeugt Tempo; Produkte als Beweis.
```

Then list 3 subject lines and 3 preview texts (see [copy-rules.md](copy-rules.md)).
Variants may differ in block order, the choice of grid (products, logos, or
collections), and tone. They never differ in facts.
