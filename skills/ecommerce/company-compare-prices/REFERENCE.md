# Reference: Competitor Price Monitoring

Detailed file formats, schemas, and edge-case handling for [SKILL.md](SKILL.md). Read the relevant section before producing the corresponding output.

---

## Output structure

Use one root directory:

```text
price-monitoring/
```

Create **one folder per competitor website**, using the site's domain name as the folder name.

```text
price-monitoring/
├── competitor-a.de/
│   ├── price-comparison_competitor-a.de.csv
│   ├── run-log.csv                # optional, see § Run log
│   ├── raw/
│   ├── screenshots/
│   └── runs/
│
├── competitor-b.de/
│   ├── price-comparison_competitor-b.de.csv
│   ├── raw/
│   ├── screenshots/
│   └── runs/
│
└── competitor-c.de/
    ├── price-comparison_competitor-c.de.csv
    ├── raw/
    ├── screenshots/
    └── runs/
```

Sanitize domain names only when required by the operating system. Remove protocol, paths, query strings, and trailing slashes from the folder name.

For example, `https://www.example-shop.de/collections/gigi?sort=price` becomes `example-shop.de/`.

Do not create a combined multi-competitor CSV unless the user explicitly asks for one later. Do not include YuliSkin as an ordinary competitor.

---

## Run timestamp and filenames

Use the local runtime date, ISO format (`YYYY-MM-DD`, e.g. `2026-08-22`).

Every raw snapshot and screenshot filename must contain the date. If multiple executions occur on the same day, add a timestamp to avoid destroying earlier evidence: `YYYY-MM-DD_HHMMSS`. Never silently overwrite an earlier raw snapshot or screenshot.

---

## Website acquisition workflow

Process every competitor independently. A failure on one competitor must not prevent the others from being processed.

### Step 1: Inspect the supplied URL

Determine: canonical domain; whether it appears to be a Shopify storefront; whether the supplied page is a homepage, brand page, collection page, or product page; where the products for the requested brand are located.

Look for Shopify indicators such as Shopify-specific HTML or script variables, `/cdn/shop/`, Shopify theme assets, Shopify storefront metadata, or working Shopify JSON endpoints. Do not rely on a single indicator.

---

## Shopify mode

### Test product JSON

For a suspected Shopify store, test product JSON, beginning with an endpoint such as:

```text
/products.json?limit=250
```

Use an appropriate collection/brand endpoint as well when it gives a more accurate result, e.g. `/collections/all/products.json` or `/collections/<collection-handle>/products.json`. Use pagination when necessary.

A successful HTTP response alone is not sufficient. Verify that the returned JSON contains valid product records, contains products from the requested brand, appears sufficiently complete for the storefront, and exposes the pricing information needed for the comparison.

If the JSON endpoint works but omits relevant products, variants, sale pricing, or other information necessary for an accurate comparison, supplement it with page scraping or switch to scraping for the affected records.

### Brand filtering in Shopify data

Prefer Shopify `vendor` when it clearly corresponds to the selected brand. Also inspect title, tags, product type, collection membership, handles, and variant data. Do not include similarly named products from another brand.

### Shopify variants

Treat variants carefully. Capture, when available: product title, product handle, product URL, vendor, variant title, SKU, barcode/EAN, current price, compare-at/list price, availability.

If different variants have different identifiers or prices, keep them separate when they represent distinct sellable items. Do not collapse materially different SKUs into a single price.

---

## Non-Shopify / scraping mode

Use web scraping when the site is not Shopify, Shopify JSON is disabled/blocked/incomplete, pricing is rendered only in the storefront, or important sale information is not represented in product JSON.

Start with the user-provided URL. Find the selected brand's brand page, category/collection page, search results, or product pages. Follow pagination or lazy-loaded product grids when necessary.

For each relevant product, extract as much of the following as possible: GG / SKU; SKU or item number; barcode/EAN if visible; product name; brand; current selling price; original/list/crossed-out price; currency; discount percentage shown by the shop; availability; product URL; promotion text associated with the product; acquisition timestamp.

For non-Shopify stores, create a normalized JSON snapshot from the scraped data so the historical evidence uses the same general structure as Shopify stores.

---

## Price semantics

The primary competitor price is the **actual price a normal customer can purchase the product for at the time of the run**.

When available, capture both:

- `price` = effective/current selling price;
- `compare_at_price` or equivalent = original/list/crossed-out price.

```json
{
  "price": 79.00,
  "compare_at_price": 100.00
}
```

For comparison calculations, use `79.00`. Do not replace the actual selling price with the crossed-out/list price.

If a discount requires a coupon code, membership, minimum basket value, subscription, login, or another condition, record that condition explicitly. Do not treat a conditional discount as universally available without noting the condition.

---

## Raw JSON snapshots

Every competitor run must produce a raw or normalized JSON snapshot, stored in `<competitor-domain>/raw/`.

```text
price-monitoring/competitor-a.de/raw/2026-08-22_competitor-a.de.json
```

For repeat runs on the same date: `2026-08-22_183500_competitor-a.de.json`.

The JSON should include run metadata similar to:

```json
{
  "run_date": "2026-08-22",
  "run_timestamp": "2026-08-22T18:35:00+02:00",
  "brand": "GIGI",
  "domain": "competitor-a.de",
  "source_url": "https://competitor-a.de/...",
  "source_type": "shopify_products_json",
  "currency": "EUR",
  "products": []
}
```

Possible `source_type` values: `shopify_products_json`, `shopify_json_plus_scraping`, `web_scraping`.

Preserve useful source fields whenever possible instead of discarding them during normalization.

---

## Screenshots

Screenshots are evidence of how promotions are presented to customers. For each competitor and run, try to capture the pages that best demonstrate sale banners, seasonal campaigns (e.g. "Summer Sale", Mother's Day, Back to School), coupon codes, site-wide discount messages, crossed-out prices, visible product discounts, or repeated promotional messaging.

Prefer pages relevant to the selected brand. Good candidates, in order:

1. homepage when it contains a prominent promotion;
2. selected brand/collection page showing multiple products and their prices;
3. a representative product page when it clearly shows sale pricing or discount conditions.

Do not create excessive duplicate screenshots — capture the smallest useful set that adequately documents the promotion. Prefer a full-page screenshot when practical.

Store screenshots in `<competitor-domain>/screenshots/`:

```text
2026-08-22_home.png
2026-08-22_gigi-collection.png
2026-08-22_product_<sku>.png
```

For multiple same-day runs, add the timestamp. If screenshot capability is unavailable, record this limitation in the run summary and continue with price collection.

---

## Promotion evidence

Do not infer that a promotion is temporary merely because the website calls it a sale — record facts instead. Capture, where visible: promotion name; promotion text; discount percentage; coupon code; start/end dates if published; minimum-order requirements; membership requirements; affected brand/category; URL where the promotion is displayed; screenshot filename.

The historical data should make it possible to determine later whether one campaign was simply replaced by another while effective prices stayed discounted.

---

## Product matching

Reliable matching is critical. Priority order:

1. exact GG / distributor SKU;
2. exact competitor SKU when known to represent the same distributor item;
3. barcode / EAN;
4. normalized manufacturer identifier;
5. normalized product name + size/volume;
6. product-name matching only as a last resort.

Normalize identifiers before comparison: trim whitespace, normalize case where appropriate, remove irrelevant formatting, preserve leading zeroes in identifiers.

For cosmetics, size/volume is important — `50 ml` must not automatically match `100 ml`, a professional/cabin size must not be matched to a retail size, and bundles must not be matched to individual products.

If matching confidence is not sufficient, do not guess. Mark the row as unresolved and ask the user when manual clarification is necessary.

---

## CSV files

Maintain **one cumulative CSV file per competitor**:

```text
price-monitoring/competitor-a.de/price-comparison_competitor-a.de.csv
```

Use plain UTF-8, comma-separated, one header row, one row per SKU. Keep GG/SKU values as text (quote them, e.g. `"00123"`) so leading zeroes are never lost. Write prices as plain numbers with no currency symbol. Leave a cell blank for unavailable observations — never write `0` for a missing price. Do not merge cells (not applicable to CSV, but do not invent placeholder rows either).

### Mode A: Distributor recommended price baseline

```text
GG / SKU,Product Name,Recommended Price,2026-08-22 Price,2026-08-22 Δ %,2026-08-29 Price,2026-08-29 Δ %
```

The first three columns stay stable: `GG / SKU`, `Product Name`, `Recommended Price`. For every new monitoring date, append two columns: `<YYYY-MM-DD> Price` and `<YYYY-MM-DD> Δ %`. Do not remove or overwrite older date columns.

### Mode B: YuliSkin.de baseline

YuliSkin prices must be historical too:

```text
GG / SKU,Product Name,2026-08-22 YuliSkin Price,2026-08-22 Competitor Price,2026-08-22 Δ %,2026-08-29 YuliSkin Price,2026-08-29 Competitor Price,2026-08-29 Δ %
```

For every monitoring date, append three columns: `<YYYY-MM-DD> YuliSkin Price`, `<YYYY-MM-DD> Competitor Price`, `<YYYY-MM-DD> Δ %`. This is necessary because changing the current YuliSkin price must never change the meaning of an older historical percentage.

### Percentage calculation

```text
Δ % = (competitor_price - baseline_price) / baseline_price
```

Write the result as a plain number rounded to two decimals representing the percentage value, with no `%` sign (e.g. `-21.00` for -21%, `10.00` for +10%) so it stays machine-parseable.

- negative = competitor is cheaper than the baseline;
- zero = same price;
- positive = competitor is more expensive than the baseline.

If the baseline is zero or missing, leave the cell blank and record the problem in the run summary.

### CSV update behavior

The CSV file is cumulative. On each run:

1. read the existing CSV if it exists;
2. preserve all historical date columns and all existing rows;
3. append the new date column group(s) to the right;
4. add newly discovered products as new rows;
5. keep rows for products that have disappeared from the competitor site — never delete a historical observation just because a product is no longer available;
6. leave the current run's price columns blank for products not found this run;
7. rewrite the full file (header + all rows) — CSV has no in-place column insert, so read the whole table into memory, add the new columns, and write it back out complete.

If the same monitoring date already exists: do not create duplicate date-column groups by default; update that day's columns only when the run is clearly intended as a correction/re-run; keep the separate timestamped JSON and screenshot evidence either way. If overwriting the same day's observation could destroy meaningful information and intent is unclear, ask the user.

### Run log

An optional `run-log.csv` may be added per competitor folder, one row per run:

```text
Run Date,Timestamp,Brand,Baseline,Source Type,Products Found,Products Matched,Products Unmatched,Promotion Found,Raw JSON,Screenshot(s),Notes
```

Use it to record acquisition quality and anomalies. Do not put the entire raw JSON into this file.

---

## Run summary

Create a small JSON run summary in `<competitor-domain>/runs/`:

```text
2026-08-22_summary.json
```

Include: brand; competitor; supplied URL; actual pages used; Shopify detected (yes/no); acquisition method; baseline type; number of products found/matched/unmatched; promotions detected; screenshot filenames; raw JSON filename; CSV filename; warnings/errors.

---

## Recommended-price source handling

When the distributor recommended-price source is selected:

1. read the source;
2. detect the relevant brand;
3. identify GG/SKU;
4. identify product name;
5. identify recommended price;
6. normalize decimal and currency formats;
7. preserve identifier strings;
8. build the baseline catalog;
9. match competitor items to that catalog.

If the source contains prices for many brands, filter to the selected brand. If the source contains gross and net prices, several price lists, wholesale prices, or regional prices and the correct reference price cannot be inferred reliably, ask the user — do not guess which distributor price is "recommended".

---

## YuliSkin baseline handling

When YuliSkin.de is the baseline:

1. retrieve the same selected brand from YuliSkin.de;
2. use Shopify JSON when sufficiently complete, otherwise scrape;
3. capture current actual selling prices, preserving compare-at/list prices separately when present;
4. match YuliSkin items to competitor items primarily by SKU/GG/EAN;
5. record the YuliSkin price for the current run date;
6. calculate competitor deviation against that same-date YuliSkin price.

YuliSkin data may be stored in the competitor run snapshot or in a shared reference snapshot, but the CSV must preserve the exact YuliSkin baseline used for each date.

---

## Missing products

A missing product is meaningful. Differentiate between: product not sold by competitor; product temporarily out of stock; product page unavailable; product found but identifier could not be matched; scrape failed; price unavailable.

Do not convert all of these states to `0`. Use blank CSV prices for unavailable observations and record the reason in JSON/run logs.

---

## Currency

Do not compare values across different currencies without normalization. If all shops and the baseline are in the same currency, use that currency directly.

If currencies differ: ask the user whether conversion should be performed unless a conversion rule has already been provided; record the source currency; never silently compare `100 EUR` with `100 CHF` as though they were equivalent.
