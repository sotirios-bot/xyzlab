# XYZ Lab — Claude Code Project Notes

## Benchmark Excel File Format

When generating benchmark Excel files (e.g. from `/home/user/xyzlab/benchmarks/*-data.js`), use the following format:

### Structure
- One tab per country (61 countries, alphabetical)
- 38 industries per tab
- Tabs named by country (max 31 chars)

### Layout per sheet
- **Row 1**: `{Channel} Benchmarks — {Country}  ({CurrencyCode})` — bold, brand color, size 13
- **Row 2**: `{Channel Name}  ·  Cross-industry averages  ·  All monetary values in local currency` — italic, grey, size 9
- **Row 3**: blank spacer (height 6)
- **Row 4**: header row — white text on brand-color fill, bold Calibri 11, height 32, wrap text, **frozen**
- **Rows 5+**: data rows, height 18, alternating white / light-brand-color fill, Calibri 10

### Styling rules
- **No gridlines** (`ws.sheet_view.showGridLines = False`)
- Font: Calibri throughout
- Alternating row fill: blend brand hex with white at 92% white
- No cell borders
- Freeze panes at A5

### Color scales (conditional formatting)
- Metrics where high = good (CTR, Conv. Rate, ROAS, Open Rate, Click Rate, Traffic, Organic CTR, Profit Margin): red→yellow→green
- Metrics where high = bad (CPA, Bounce Rate, Unsubscribe Rate, Cart Abandonment, Keyword Difficulty, Domain Authority, Backlinks needed): green→yellow→red

### Brand colors per channel
| Channel | Hex |
|---|---|
| LinkedIn Ads | `0A66C2` |
| Meta Ads | `1877F2` |
| Google Ads | `4285F4` |
| TikTok Ads | `010101` |
| Reddit Ads | `FF4500` |
| SEO | `188038` |
| Email Marketing | `0072C6` |
| Shopify | `5C8E2A` |

### File naming
Clean names with no date/month: e.g. `LinkedIn Ads Benchmarks.xlsx`, `Meta Ads Benchmarks.xlsx`

### Subtitle line (row 2)
Use the channel name itself — e.g. `LinkedIn Ads`, `Meta Ads`, `TikTok Ads`, `Reddit Ads` — not a sub-description like "In-Feed Video & TopView" or "Promoted Posts".

### Number formats
- CTR / Conv. Rate / Open Rate / Click Rate / Unsubscribe / Bounce / Cart Abandonment / Profit Margin: `0.00` (percentage values stored as plain numbers, e.g. 1.23 displayed as 1.23%)
- Money (CPC, CPM, CPE, CPA): `#,##0.00`
- CPV: `0.000`
- ROAS: `0.00`
- Traffic / Backlinks: `#,##0`
- KD / DA scores: `0`

### Column widths per channel
- Industry column: 36
- Percentage columns: 9–18 depending on label length
- Money columns: 12
- ROAS: 10
