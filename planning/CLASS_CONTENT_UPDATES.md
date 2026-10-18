> Historical record of the 7 October revision. The 8 October map change supersedes its maps 8–10 controls and publisher-count map: current publisher maps are 8–9; historical community map 10 opens section 4. See ../FINAL_GRAPH_LIST.md and map_revision/README.md.

# New class material review: 7 October 2026

Read every page of the three new PDFs and the updated Week 8 file:

- FIT3179 Week 10 Studio.pdf: 28 pages. Linked views, overview/detail brushing, coordinated selections, map controls and small multiples.
- Vega-Lite Code Example.pdf: 11 pages. Map lookups, long/wide data, selecting attributes and years, view composition.
- Vega-Lite FAQ.pdf: 8 pages. Raw data URLs, map joins, missing countries, geometry simplification, annotations, embedding and layout troubleshooting.
- FIT3179 Week 8 Studio - Geographic Vector Formats.pdf: 10 pages. GeoJSON, TopoJSON and shapefile structure. Figures checked alongside the extracted text.

These are teaching examples and troubleshooting notes. They do not introduce a new required number of charts, require every example interaction, or replace the Assignment 2 rubric. Existing class files were reviewed earlier; the new inventory contained no additional code/data examples beyond those previously examined.

## Changes to the planning reference

1. Chart 1: drag over publication years to update charts 2 and 3; add Reset. Keep chart 1 as a full-period overview. The selected range is visible. Recompute distinct-game counts and percentage denominators within that selection. State selected years and partial decades. Keep chart 3's selected mechanic set stable for comparison.
2. Maps 8–10: one shared Publication decade control and Reset maps. This filters the publication years of linked games. It does not reconstruct past headquarters or change historical local rankings. Chart 7 remains the full-period catalogue comparison.
3. Maps: equal-dot explanation for headquarters, a circle-area legend for credited game counts, and an explicit grey no/insufficient-data legend for the choropleth. An eligible country with a true zero cooperative share is a numeric value, not missing data. Recheck the sample threshold after filtering.
4. Charts 11 and 13: selecting a ranked game highlights its complexity dot wherever that game appears. Use the same BGG game ID and overall complexity value across all three lists. Provide Clear selection. These are not separate country-specific complexity scores.
5. Chart 15: label units clearly and highlight a game line on hover. Maximum players and minimum age are explicit; only complexity has the predefined 1–5 scale.
6. Retain the DV1 improvements: aligned two-column grid, serif main title, short copy, consistent ranking colours and selective annotations outside marks. Findings and annotation text must follow analysis; changing filters must not leave an inaccurate annotation visible.

## Implementation notes

- Build static charts first, then link them, following Week 10's suggested workflow. Keep interactions within small logical sections. A plain set of separately embedded JSON files does not automatically share selections; use a composed specification for a linked section or explicitly wire JavaScript events.
- Prepare small long-format data tables. A time-varying country table should have one row per country and publication period, joined from the CSV rows to map geometry, rather than overwriting several period rows with a one-row country lookup. Deduplicate game IDs before counts and proportions.
- Validate matching country keys and TopoJSON object names. Include every field needed later in a lookup. Missing map data needs a base-map layer.
- Keep geographic colour scales fixed across period selections. Keep circle area proportional to the counts and its legend consistent with the size scale. Counts, location coverage and map eligibility still need cleaning and validation.
- Fit each linked section and its legends within the laptop layout. Test the served page and public GitHub page; container width alone does not guarantee legends fit. Use readable raw/public data URLs and simplified geometry where useful.
- The materials' example datasets, placeholder URLs and library-version snippets are teaching examples, not board-game data or evidence that those versions are current. Do not copy them as final data sources.
- No extra small-multiple maps or duplicate overview charts are needed for this plan. Interaction does not change a basic idiom into an advanced one. Similar charts may count as one series under the rubric.

## Final design and remaining data work

Keep the five-section story and 15 chart instances. There are six basic and nine advanced instances, representing eight different advanced idioms. All three planned map idioms are retained. This is a final design plan, not a guaranteed rubric chart count or a completed analysis.

Final reference: hand-drawn-layout-class-v3.png. Built-in image generation was used; both prompts are saved in class-sketch-prompts.txt. Shapes, line positions and small/medium/large circles are illustrative. Real legends, axis domains, selected-game values and takeaway text must come from the processed data. The Brass: Birmingham ranking row is the previously verified example.

All required source fields are available locally. Publisher geography needs verification, map sample coverage must be calculated, award statuses need checking, and chart tables still need to be prepared. The country rankings remain historical April 2024 BGG-user rankings; mechanics and complexity come from the later 2026 dataset. Copy the reference onto paper for the assignment's hand-drawn sketch.
