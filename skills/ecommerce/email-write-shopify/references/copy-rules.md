# Copy rules: voice, subject, preview text, banner, alt text, English

## Voice

- German, informal "du", warm and expert. Speak as Julia, a cosmetician.
- No pressure tactics beyond a real deadline.
- No exclamation-mark chains. Use emojis sparingly: at most one in a heading.
- Keep real ä/ö/ü/ß in all copy. Only slugs and filenames are ASCII.
- Write percentages and prices as "12 %" and "50 €", with a space.
- Use dates such as "23.10.2026" or "23. Oktober 2026", consistently within one email.
- Short paragraphs: 2–4 lines on mobile. Bold only the facts the reader must
  not miss (dates, value, minimum order).

## Subject and preview text

- **Variant step:** offer 3 subject lines and 3 preview texts. The chosen pair goes into `brief.md`.
- **Subject:** at most 50 characters (counted in code), at most one emoji, no clickbait.
  It names the benefit or the occasion.
- **Preview text:** 40–90 characters. It adds to the subject (deadline, code value,
  teaser) and never repeats it.
- **English emails:** get their own adapted pair with the same limits.

## Brief front matter

`brief.md` starts with this YAML front matter; `build_preview.py` and
`validate_email.py` read it. Leave out keys that do not apply.

```yaml
---
subject: "12 % fürs Warten – nur bis 23.10."
preheader: "Wir machen kurz Pause. Dein Dankeschön: Code AUTUMN-2026 ab 50 €."
subject_en: ""
preheader_en: ""
discount_code: "AUTUMN-2026"
countdown_end: "2026-10-23 23:59"
theme: "standard"
---
```

The body below it contains:
- Intake answers
- The chosen variant
- Key copy points
- Resolved resources (handles and URLs)
- Fact sources
- The custom theme table, if any
- Upload results (banner file ID and CDN URL)

## Banner prompt (ChatGPT / Gemini)

First ask what the banner should show: subject, products or mood, season, and
people or no people. Then save `banner-prompt.md` using this pattern:

```
Create a wide email banner image, 1120 × 600 px (approx. 16:9), photographic,
soft natural light. Scene: <what the user described>. Mood: <calm, premium,
skincare studio>. Colour palette: <theme colours by name, e.g. warm cream,
terracotta, soft white>. Composition: main subject on the <left/right>, calm
negative space on the other side. No text, no letters, no logos, no watermarks.
High-end skincare aesthetic, realistic skin texture, no plastic look.
```

- Write the prompt in English: both tools follow English prompts best.
- Never ask for real brand packaging to be generated, because generated
  packaging is inaccurate. Use real product photos in the product grid instead.
- The headline is HTML text in the email, not part of the image.

## Alt text

- Every `<img>` gets alt text in the email's language, at most about 125 characters.
- **Banner:** describe the image plus the occasion, e.g. "Herbstliche Pflegeprodukte
  auf Leinen – YuliSkin Urlaubsaktion".
- **Products:** brand + product name.
- **Logos:** the brand name.
- **Article images:** the article topic.

## English adaptation

- Write English only after the German version is approved.
- Adapt it naturally rather than translating word for word. Keep the facts, codes,
  dates, and structure identical.
- **Full yuliskin.de links** get the `/en` prefix:
  - Products and collections: `https://yuliskin.de/en/products/<handle>`
  - Discount links: `https://yuliskin.de/en/discount/CODE?redirect=%2Fen%2Fcollections%2F<handle>`
  - Verify the English handle if a translated handle exists.
- **Labels:** "YOUR DISCOUNT CODE", "Shop now →", "Read more →".
- **Signature:** "Warm regards" + Julia Fukszon + YuliSkin Kosmetik Studio.
- **Date format:** use "23 October 2026".
