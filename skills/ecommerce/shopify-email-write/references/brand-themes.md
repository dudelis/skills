# Brand themes

The blocks in [blocks.md](blocks.md) use role tokens written as `[[token]]`.
Replace every token with the hex value from the chosen theme. No `[[...]]` may
remain in the final file; the validator checks this.

Fixed for every theme:
- Font: `Arial,Helvetica,sans-serif`
- Card max width: 560px
- Button radius: 7px

## Token values

| Token | Role | Standard | Black Friday |
| --- | --- | --- | --- |
| `page_bg` | Outer background and the area behind the terms | `#FAF5F2` | `#000000` |
| `card_bg` | Main white card | `#FFFFFF` | `#FFFFFF` |
| `panel_bg` | Tinted sections (grids, info box, article card) | `#FAF5F2` | `#F2F2F2` |
| `tile_bg` | Grid tiles inside a panel | `#FFFFFF` | `#FFFFFF` |
| `code_bg` | Discount code box | `#F7EDE5` | `#000000` |
| `code_label` | "DEIN RABATTCODE" label | `#7B6357` | `#BFBFBF` |
| `code_text` | The code itself | `#955D3F` | `#FFFFFF` |
| `heading` | h2/h3 and bold text | `#292724` | `#000000` |
| `body` | Main paragraphs | `#4A4541` | `#1F1F1F` |
| `muted` | Section paragraphs | `#5B524C` | `#3D3D3D` |
| `soft` | Small notes, brand labels | `#75685F` | `#5C5C5C` |
| `fine` | Terms text on `page_bg` | `#81746D` | `#A6A6A6` |
| `accent` | Highlights, deadline line, links | `#955D3F` | `#C8102E` |
| `button_bg` | Button background | `#AD6745` | `#000000` |
| `button_text` | Button label | `#FFFFFF` | `#FFFFFF` |
| `divider` | Divider line, spotlight row borders | `#EADFD8` | `#D9D9D9` |

Black Friday keeps the same structure: black frame, white card, black buttons,
and one red accent for highlights.

## Custom themes

When the user names colours or a mood (for example Christmas or summer):
1. Propose a complete value for every token in a table like the one above.
2. Check contrast. Text tokens on their background need at least 4.5:1
   (`fine` on `page_bg` too).
3. Wait for approval.

Record the approved table in `brief.md`. When the same custom theme has been
used twice, offer to add it here as a named preset.

## Shopify editor settings

Tell the user to set these in the Shopify editor so the native sections match the theme:
- **Email background colour:** `page_bg`
- **Native Countdown:** background `card_bg`, digits `accent`, labels `soft`
