# Basic webpage implementation

Prepared 10 October 2026. This document describes the implemented draft, not hidden marking requirements or a guarantee of marks.

## Class code structure

Reviewed the class HTML/CSS/JavaScript examples, particularly the week 7 basic Vega-Lite example, week 9 multiple-chart and interactive-scatter examples, and the symbol/choropleth map examples. The page retains their central approach: chart containers in HTML, separate CSS, small JavaScript calls to `vegaEmbed`, and readable chart JSON files. Simple native controls connect the views. CSS grid replaces the example's external Pure.css grid; no application framework is required.

The browser loads only the prepared `data/` tables, the 15 specifications and three local libraries. It does not download the large source datasets. The preparation scripts are optional authoring tools, not prerequisites for viewing the assignment.

## Design notes read and applied

All pages of the following five attached notes were read. Relevant design examples were also inspected visually.

| Notes | Pages | Application in this draft |
| --- | --- | --- |
| `C:/Users/User/Downloads/FIT3179 -S2-2026 - Course Notes 7 Storytelling with Data.pdf` | 6 | Five question-led sections, an overview before comparisons, short explanations and transitions, findings supported by prepared data |
| `C:/Users/User/Downloads/FIT2179 Course Notes 6 Data-ink Ratio and Chartjunk.pdf` | 4 | Plain background, light useful gridlines, no ornamental chart frames or shadows, selective labels and hover details |
| `C:/Users/User/Downloads/FIT2179 Course Notes 8 Colour.pdf` | 11 | Consistent Global purple / Malaysia orange / Australia blue; other values use neutral marks or sequential grey; text and legends accompany colour |
| `C:/Users/User/Downloads/FIT2179 Course Notes 9 Layout.pdf` | 6 | Repeated equal-width columns, common margins and gutters, full-width overview/comparison charts, a clear top-to-bottom reading order |
| `C:/Users/User/Downloads/FIT2179 Course Notes 11 Typography.pdf` | 13 | Georgia main title; legible sans-serif body/chart labels; left-aligned short paragraphs; contrasting text and explicit units |

The notes inform design choices. The assignment brief remains the source of assignment requirements.

## Assignment 1 feedback applied

The feedback is `C:/Users/User/Downloads/DV1Feedback.pdf` (all 3 pages reviewed). The submitted work is `C:/Users/User/Downloads/LaiCheeSeng_Studio1_DV1.pdf` (16 pages, previously reviewed with its screenshots). Detailed distinctions between explicit feedback and our observations are in `DV1_FEEDBACK_ACTIONS.md`.

- The main title uses a serif font, as explicitly requested.
- Repeated columns and common gutters reduce changing sight lines. Charts have no narrow side-note columns.
- Short explanations and selective, verified findings support the story. Captions sit outside plotting areas.
- The page avoids labelling every point. The small ranking matrix retains numbers because precise ranks are its purpose.
- Population colours keep the same meanings across maps, bars and dots. Other charts use neutrals with explicit legends.
- The word **percentage** is used in axes and explanations. No `pct` abbreviation is used.
- The very dense waffle from Assignment 1 is not reused. Chart sizes and labels were checked in the browser.
- Author, source, dates and AI assistance remain in the footer.

## The implemented 15 charts

| No. | Chart | Question | Data |
| --- | --- | --- | --- |
| 01 | Line | How many games are recorded for each publication year? | BGG catalogue |
| 02 | Horizontal bars | Which common mechanics occur in the selected years? | BGG mechanic links |
| 03 | Heatmap | How does the percentage using each selected mechanic differ across decades? | BGG mechanic links |
| 04 | Network | Which of eight common mechanics often occur together? | BGG mechanic pairs |
| 05 | Box plots | How does recorded complexity vary by publication decade? | BGG complexity scores |
| 06 | Scatterplot | How do recorded playing time and complexity relate? | BGG metadata; reproducible sample |
| 07 | Treemap | Which twelve named publishers have the largest recorded catalogues? | BGG publisher credits |
| 08 | Equal-dot map | Where are recorded publisher headquarters places? | BGG publisher links + Wikidata candidates |
| 09 | Choropleth | What percentage of eligible publisher-linked games use cooperative play? | BGG mechanic/publisher links + Wikidata countries |
| 10 | Proportional-symbol map | How large are the country rating communities in the historical analysis? | Recommend.Games / Analysis Paralysis country summary |
| 11 | Rank heatmap | How do selected games rank in the three historical lists? | Global historical archive + Malaysia/Australia lists |
| 12 | Grouped bars | Which mechanics occur in each historical top-20 list? | Historical list membership + later BGG mechanics |
| 13 | Dot plot | How complex are the games in each historical top-20 list? | Historical list membership + later BGG scores |
| 14 | Grouped bars | How do winner mechanics compare with the broader eligible collection? | Award histories + BGG mechanic links |
| 15 | Parallel coordinates | How do six winners differ in complexity, minutes, player limits and minimum age? | Award histories + BGG metadata |

Twelve specifications use Vega-Lite. Charts 04, 07 and 15 use Vega. All three maps use Equal Earth; they represent different quantities and map idioms. Repeated idiom instances should not be presented as extra unique idiom types when discussing the rubric.

## Conservative changes from the sketch

- The network uses a fixed circular arrangement of eight mechanics and the twelve strongest pair links. Position has no analytical meaning; link thickness conveys shared-game counts.
- The treemap shows twelve named publishers. Non-company placeholder entries are excluded; an enormous heterogeneous “Other” block is not added. This is a selected-catalogue comparison, not market share.
- Publisher countries with conflicting candidate records are excluded. Headquarters also require a single unambiguous recorded place/coordinate. These checks reduce ambiguity but do not establish a complete, independently verified current office directory.
- Maps 09 and 10 occupy full-width rows. This preserves legibility and keeps the story order 01–15.
- Award profiles show the 2024/2025 winners, which were checked against the official award pages. The historical winner comparison is filtered from the downloaded history and has not been individually checked against every official award year.

## Data interpretation and counts

- Main catalogue: 120,563 base games published 1950–2025. Publication year is not a sales measure. 2020–2025 is a partial decade. Old-game scores reflect recorded community opinions, not opinions collected in the publication decade.
- Complexity: at least ten votes and scores in the 1–5 range. The scatterplot samples 1,200 games deterministically from 13,739 games with valid positive playing time. The source's cleaning removes durations above 360 minutes.
- Geography: 387 all-year mapped publisher places, 33 countries in the country-linked sample, and 22 countries meeting the cooperative map's 50-game denominator threshold across all years. One game can have credits in several countries. Geography does not represent invention, manufacturing, player preferences or sales.
- Community map: 197 matched records. Seventeen missing contributor counts are not treated as zero; two positive-count records have no coordinate match. Circles encode area proportional to contributor counts, not radius.
- Rankings: historical April 2024 country analysis and global snapshot dated 25 April 2024. Different calculations, thresholds and observation times affect comparability. Self-reported BGG countries do not establish nationwide popularity. Charts 12/13 use later 2026 mechanics/complexity metadata.
- Awards: 44 ordinary-category winners with publication years 2011–2025 and recorded mechanics, compared with 63,563 eligible games from those same publication years. The broad group includes the winners. Special awards and nominations are excluded. Chart 15 has six complete profiles with different units and a separate scale on each axis.

## Verification

The page was checked in headless Microsoft Edge with all 15 charts rendered and no browser errors or warnings. Actual pointer brushing updates charts 02/03; year reset, map period/reset, rank-cell and rank-number selection, linked dot highlighting/reset, and award dropdown selection were exercised.

Layouts were checked at 1366, 1024 and 390 pixels wide with no horizontal page overflow. Screenshots were reviewed for clipped labels and legends. Small-screen improvements include stacked legends, inward map labels, multiline network labels and axis headings. Final screenshots and `browser-errors.json` are in this folder. These checks verify the local draft, not a deployed GitHub Pages site.

The assignment's written template, student's own paper sketch and public deployment remain separate deliverables. No site was published by this implementation task.

## Colour and copy revision — 15 October 2026

The requested revision adds restrained colour while preserving meanings. Catalogue counts, publisher locations and mechanic percentages use a teal family. Complexity box plots and the complexity/time scatterplot use rose. Global, Malaysia and Australia retain purple, orange and blue. Award winners use charcoal; the wider catalogue comparison uses catalogue teal. Colour is supported by labels, axes, legends and quantities rather than being the only means of interpretation.

The percentage heatmap and choropleth use ColorBrewer's five-colour BuGn sequence with Lab interpolation. Low percentages are light; high percentages are dark. Map 09 uses a fixed 0–40% domain across publication periods: the maximum eligible value in the prepared data is 30.0532%. Its legend and caption state the domain. Chart 03 retains 0–100%. The two legends make their different ranges explicit. Missing map data remain neutral grey.

Chart 14 adds just two on-chart labels to the cooperative-play bars, calculated from their data: 18/44 winners (40.9%) and 6,808/63,563 broader eligible games (10.7%). These annotations sit beside the bar ends, not over the bars. The line chart keeps its existing data-supported peak annotation. No invented trend annotations were added.

Written paragraphs and source notes use explicit line breaks with at most nine words between breaks. Shorter sentences replace the long source descriptions. Dynamic map coverage and winner explanations use the same approach. Paragraph widths are capped at 50ch as a further reading aid; narrower screens may wrap lines sooner. The serif Georgia title remains, while the conclusion, short explanations, axes, legends and annotations use sans-serif fonts. Chart axis labels are slightly larger. Small all-uppercase section captions were changed to mixed case. On narrow screens, long rank-chart game names truncate sooner so the three country headings keep sufficient space; full names remain in tooltips.

The revision retains the plain class-style files and all existing chart interactions. The downloaded source datasets and prepared data values were not changed.

On phones, ranking-table column labels use MY and AU, with their full meanings stated directly beneath the chart. Desktop headings keep the full names. This prevents enlarged sans-serif labels from overlapping.

## Tutor layout feedback — 19 October 2026

This revision supersedes the earlier paired-chart layout described above. All 15 charts and their data remain. The 12 non-map charts now read vertically, each with a wider figure and a short context column on its right. The three maps occupy full-width rows. Below 800 pixels, context notes move beneath their charts.

Map heights now follow their container widths, with extra space for legends. This enlarges the actual Equal Earth geometry rather than leaving a small world inside a large container. At the checked 1366-pixel viewport, each map container was 1,196 pixels wide and the world drawing was 1,184 pixels wide, approximately 99% of the available width.

Publisher names wrap at word boundaries without ellipses or hidden labels. The treemap has a larger plotting area and uses squarify on larger screens, with binary layout below a 500-pixel plotting width. Both layouts preserve the same publisher counts and proportional areas. All twelve labels, including Pegasus Spiele and Ravensburger AG, were checked against their actual tile bounds at desktop, laptop and phone widths.

Visible notes now provide short interaction instructions, qualifications or explanations of unfamiliar encodings. Redundant readings of axes, generic transitions and repeated findings were removed. Detailed sampling rules, date qualifications and data limitations remain in an expandable methods section in the footer. Default side notes contain no more than 22 words in total, with explanation lines capped at nine words. This avoids using many short lines simply to fill the sidebar.

Normal explanatory text uses 18-pixel sans-serif type in the same dark ink colour. Controls are 17 pixels, metadata is 16 pixels, and chart axes and legends are 14 pixels. These size differences retain hierarchy without using lighter shades for secondary body copy. The Georgia serif main title and existing meaningful palette are retained. Chart legend titles were shortened so they remain fully visible.

The network spreads across its larger plotting area; node positions remain a layout choice, while link width encodes shared-game counts. Map circle scales remain proportional to contributor counts. Year brushing/reset, shared publication filtering/reset, game highlighting/reset and profile selection were rechecked. No changes were pushed to GitHub as part of this local layout revision.

## Mixed layout and class code format — 19 October 2026

The student's subsequent request supersedes the all-vertical arrangement. Charts 02/03 now compare mechanic totals with mechanic shares over time. Charts 05/06 pair complexity distributions with complexity versus duration. Charts 12/13 compare mechanics and complexity within the same three historical top-20 lists. Each pair has equal-width figures and brief notes underneath. Charts 12/13 share a labelled colour key immediately above them; the duplicate chart 12 legend has been removed. Both figures are 320 pixels high, and chart 13 has fewer x-axis ticks.

Other charts retain wider rows with short notes beside them. All three maps still span the page. The treemap retains the area and label wrapping needed for every publisher name. Pairs stack at viewport widths of 1,200 pixels or less; notes move below all charts at 800 pixels or less. At the checked 1,366-pixel desktop viewport, each paired chart is 584 pixels wide, each map is 1,196 pixels wide, and the actual world geometry is 1,184 pixels wide.

The code was compared directly with `class_content/Studio Codes (week 7)/Part A - Intro to javascript/events.js` and `class_content/studio codes (week 9)/5_multiple_charts_html/index.html` plus its stylesheet. The page retains separate HTML content, CSS presentation, an external JavaScript file and readable chart JSON files. The loader now uses `var`, ordinary functions and the demonstrated `vegaEmbed(...).then(function (result) { ... }).catch(...)` pattern. A shared function avoids repeating the same embed block fifteen times. Download links are ordinary HTML rather than being generated by JavaScript.

The class demo provides `result.view` and links to its API. Our Vega view signals, linked selections, resize calls and browser fetches are extensions, not verbatim class examples; comments in the JavaScript identify them. The responsive CSS is custom CSS, rather than the Pure.css grid used in the Week 9 example. No new framework or dependency was added. Matching the basic file structure does not establish a marking guarantee or mean that every chart-specific line appears in class materials. `CLASS_CODE_GUIDE.md` records this distinction for interview preparation.

The final local version rendered all fifteen charts with no browser errors or warnings. Year brushing/reset, shared map filtering/reset, game-cell and number selection, linked dot highlighting/reset, profile selection, full publisher labels and full-width map geometry passed browser checks. Desktop pairs align at their top edges. At 1,024 and 390 pixels the page has no horizontal overflow, and all twelve publisher labels remain inside their tiles. Sources, data values and qualifications are unchanged. No commit or deployment was performed.
