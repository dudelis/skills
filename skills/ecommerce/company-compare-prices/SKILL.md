---
name: company-compare-prices
description: Monitors one product brand across competitor websites, capturing historical prices and promotions into one cumulative CSV file per competitor, with dated JSON snapshots and screenshots as evidence. Prefers Shopify products.json when available, falling back to web scraping otherwise; supports comparison against distributor recommended prices or YuliSkin.de prices. Use when the user wants to track competitor pricing for a brand over time, benchmark prices against a distributor price list or YuliSkin.de, or build historical evidence of competitor promotions and discounting.
---

# Competitor Price Monitoring

## Purpose

Monitor the prices of **one brand at a time** across one or more competitor websites.

The skill must:

- ask which brand to monitor, which competitor website links to use, and the comparison baseline;
- determine whether each competitor is a Shopify store and prefer Shopify product JSON, falling back to scraping;
- save a dated raw JSON snapshot and dated promotion screenshots for every competitor on every run;
- maintain **one cumulative CSV file per competitor**, preserving historical price data instead of overwriting previous runs;
- compare competitor prices against either distributor recommended prices or YuliSkin.de prices.

The goal is objective historical evidence of how a competitor prices a selected brand over time.

Full file/directory formats, JSON schemas, matching rules, and CSV column layouts are in [REFERENCE.md](REFERENCE.md) — read it before producing any output file.

---

## Required interaction flow

Gather these inputs before collecting any prices.

### 1. Brand

Ask: **"Which brand do you want to monitor?"** Process only **one brand per run** — do not mix brands unless the user explicitly changes this.

### 2. Competitor links

Ask: **"Which competitor website links should I monitor for this brand?"** Accept one or more URLs — homepage, brand page, collection page, or direct shop URL. Use the given URL as a starting point but navigate elsewhere on the same domain to find all of the brand's products.

### 3. Comparison baseline

Ask the user to pick one:

- **Distributor recommended price** — ask where to get it from (CSV/XLSX/JSON/local file/URL). Try to auto-detect the SKU, product name, and recommended-price columns; ask the user only if they can't be determined reliably. See REFERENCE.md § Recommended-price source handling.
- **YuliSkin.de price** — retrieve the same brand's current YuliSkin prices using the same Shopify-JSON-first, scrape-fallback approach, and store that reference price per run date (never overwrite an older one). See REFERENCE.md § YuliSkin baseline handling.

### 4. Ask only when it materially affects correctness

E.g. several possible price columns, unreliable identifier matching, ambiguous regional storefronts, or a site choice that changes which price customers actually see. Do not ask when the answer is reliably derivable from the data.

---

## Workflow overview

Process every competitor independently — a failure on one must not block the others.

1. **Inspect the supplied URL**: canonical domain, Shopify indicators, page type, where the brand's products live. See REFERENCE.md § Website acquisition workflow.
2. **Acquire product data**: prefer Shopify `products.json` (test it, verify it's complete and has pricing); fall back to scraping when it's missing, blocked, incomplete, or the site isn't Shopify. See REFERENCE.md § Shopify mode and § Non-Shopify / scraping mode.
3. **Capture price semantics**: use the actual effective selling price for comparison, keep compare-at/list price separate, and record any condition a discount requires (coupon, membership, minimum basket, login). See REFERENCE.md § Price semantics.
4. **Save a raw JSON snapshot** per competitor per run in `<competitor-domain>/raw/`, dated, never overwritten. See REFERENCE.md § Raw JSON snapshots.
5. **Capture screenshots** of the smallest useful set of pages that document visible promotions. See REFERENCE.md § Screenshots and § Promotion evidence.
6. **Match products** to the baseline catalog using the identifier priority chain (SKU/GG → EAN → normalized name+size); do not guess low-confidence matches. See REFERENCE.md § Product matching.
7. **Update the competitor's cumulative CSV file**, appending a new date-column group and preserving all history and disappeared products. See REFERENCE.md § CSV files.
8. **Write a run summary** JSON in `<competitor-domain>/runs/`. See REFERENCE.md § Run summary.

---

## Quality checks before completion

Before considering a run complete, verify:

- the requested brand and every requested competitor were processed, each in its own folder;
- Shopify detection was actually tested, with scraping fallback used where required;
- raw JSON and dated screenshots exist for every successfully processed competitor;
- the correct baseline mode was used and CSV history was preserved (new date columns appended, nothing overwritten);
- percentage calculations are correct and no SKU leading zeroes were lost;
- no obvious size/variant mismatches were introduced;
- unresolved product matches were reported rather than guessed.

---

## Completion response

Summarize: brand monitored, baseline used, competitors processed, products found/matched, notable price deviations, promotions observed, files created or updated, and any unresolved matches or collection failures. Keep it concise and link to generated files when the runtime supports file links.

---

## Important rules

1. Process only one brand per run.
2. Never combine competitors into one historical comparison CSV.
3. Never overwrite historical raw evidence (JSON snapshots, screenshots).
4. Prefer Shopify JSON, but do not trust it blindly — verify it's complete.
5. Fall back to web scraping when necessary.
6. Compare against the actual effective selling price, not the crossed-out/list price.
7. Preserve original/list/compare-at prices separately when available.
8. Preserve historical baseline values — a YuliSkin price change must never alter an older historical percentage.
9. Do not invent product matches; mark unresolved matches and ask when necessary.
10. Ask the user when ambiguity materially affects correctness.
11. Keep evidence objective: price, promotion text, condition, URL, date, and screenshot.
12. Do not describe a promotion as temporary or permanent unless the collected historical evidence supports that conclusion.
