# Board Game — FIT3179 Assignment 2

A basic scrolling webpage with 15 charts in five story sections. Prepared 10 October 2026.

## Open the page

1. Open this whole folder in VS Code.
2. Right-click `index.html` and choose **Open with Live Server**.
3. Keep the server running while you view or edit the page.

Use Live Server rather than opening the HTML directly from the file browser: the charts fetch their CSV and JSON files through HTTP. The three Vega libraries are already included locally. You do not need Tableau, an installed Vega application, Python, Node.js or a build command to view the page.

## Which file should I edit?

| File or folder | Purpose |
| --- | --- |
| `index.html` | Page headings, explanations, chart containers and sources |
| `css/styles.css` | Fonts, colours, spacing and the two-column layout |
| `js/vega_lite_vis.js` | Loads the charts with `vegaEmbed` and connects controls |
| `js/charts/` | One readable `.vg.json` specification per chart |
| `data/` | Small prepared CSV tables used by the charts |
| `data_research/` | Downloaded source datasets; kept separate from the webpage |
| `planning/IMPLEMENTATION_NOTES.md` | Design decisions, source limits and verification |

This follows the class pattern of HTML + CSS + JavaScript + separate chart JSON files. The layout uses a small CSS grid. Twelve charts use Vega-Lite; the network, treemap and parallel coordinates use Vega. There is no application framework.

Colour/copy update, 15 October 2026: catalogue charts use teal, complexity plots use rose, and the ranking populations keep their original colours. Sequential percentages use the ColorBrewer BuGn palette. Explanation lines contain at most nine words, including the live map and winner descriptions. The main title is serif; short explanations and chart labels are sans-serif. The palette constants are near the top of `scripts/create_charts.py`.

## Try the controls

- Drag across chart 01 to filter the years in charts 02 and 03. Use **Reset years** to restore all years.
- Choose a publication decade above section 03 to update maps 08 and 09. The treemap always covers all years.
- Click a cell or number in chart 11 to highlight the same game in chart 13. Use **Clear selection** to show all games.
- Select a winner above chart 15 to emphasise its line and show its recorded values.
- Hover over chart marks for details. Expand the footer for sources, CSV files and chart specifications.

## Optional preparation scripts

The page already has its prepared data and specifications. These scripts are only for rebuilding them during development:

```text
python scripts/prepare_data.py
python scripts/create_charts.py
```

`prepare_data.py` reads the local downloaded files and writes `data/`. It does not scrape websites or edit the original datasets. `create_charts.py` writes all 15 JSON specifications. **If you edit a JSON file directly, rerunning that script will overwrite your edit.** If source data changes, review the fixed counts, findings and dates in `index.html` after rebuilding.

## Scope of this first version

The country comparison uses historical April 2024 lists. Its mechanics and complexity metadata come from the later 2026 catalogue. The publisher maps use an incomplete, filtered Wikidata geography sample. These qualifications are explained on the page.

The code is a local draft ready for refinement. GitHub Pages deployment, the written assignment template and the student's own hand-drawn submission are separate tasks.
