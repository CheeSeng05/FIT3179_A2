# FIT3179 peer critique reference

Prepared 15 October 2026 for the user's forthcoming critique. The peer's work has not yet been supplied. Everything below is a check to apply, not a finding about that work.

## Review completed

Read the extracted text of all 27 PDFs in `class_content` (342 PDF pages), including the two Munzner chapters, the studios, FAQ and code examples. Inspected selected visual examples for channel rankings, misleading charts, colour, layout, typography, map types, flow routing, relief shading and coordinated views. Read the supplied HTML, CSS, JavaScript and chart specifications. Checked the example CSV schemas and TopoJSON structures; the raw data rows and geometry coordinates are teaching assets, not additional design guidelines. Also read the six-page DV2 brief and rubric. Extractions, an inventory and visual review sheets are in `planning/critique_review`.

## How to turn observations into strong critique

Produce a minimum of four distinct, defensible improvements once the work arrives. Include more when they are substantive. Prioritise misleading encodings and obstacles to understanding before minor polish. Do not split one underlying issue into several points just to reach four.

For each point, use:

1. **Specific observation and location:** identify the actual chart, section, label, colour mapping or interaction.
2. **Relevant class principle:** name the concept and, where helpful, the source and PDF page.
3. **Why it is a problem:** explain the reader's likely misinterpretation, failed comparison, unnecessary effort or loss of context.
4. **Concrete improvement:** recommend a change that fits the existing data, audience and communication goal.

Example of the format, not a finding: "The middle segments of the stacked chart have different baselines. This makes the intended comparison of that category across years difficult because readers must judge two moving boundaries. Use aligned small multiples or separate lines for those category trends."

Distinguish direct observations from hypotheses that require data or code. A screenshot cannot establish whether a tooltip or reset works, whether a join is correct, or whether the source dataset is current. Say what is visible and what would need testing. Do not label a visualisation factually wrong without sufficient evidence.

## Checks for chart choice and encoding

| Check when the work arrives | Why an observed failure matters | Improvement to consider | Class basis |
| --- | --- | --- | --- |
| Can the audience identify the purpose, items, variables and intended comparison? | A chart can be technically valid yet fail to answer a useful question. | State the question; select the relevant data and encoding for that task. | S01 pp. 6-14; S02 pp. 2-3 |
| Are categorical, ordinal and quantitative variables treated appropriately? | A colour gradient can imply a magnitude order among nominal categories; arithmetic on rank can imply meaningful distances that do not exist. | Use hue/shape for identity, ordered channels for magnitude, and preserve genuine order. | S03 pp. 7-8; S04 pp. 3-8 |
| Is the most important comparison encoded with an effective channel? | Close values are hard to compare using area, angles or colour alone. | Prefer aligned position or length for precise comparison; retain other channels when they serve a useful secondary purpose. | S04 pp. 7-9; S02 pp. 3-9 |
| Do magnitude bars begin at zero? | Truncation exaggerates proportional differences because bar length represents quantity. | Restore zero, or use a clearly labelled dot/difference chart for close values. | S02 pp. 4-5 |
| Do chart scales support honest comparisons? | Different scales can make equal-looking changes represent very different quantities. An unexplained log scale can be misread as additive change. | Share scales where direct comparison is intended; explain necessary differences and log semantics. | S02 pp. 9-11; S22 pp. 4-6; S19 pp. 21-27 |
| Are lines/areas used across genuinely ordered positions? | Connecting unordered categories implies continuity. Equal spacing for irregular dates can distort timing. | Use bars/dots for nominal groups; preserve temporal spacing and show observation timing where useful. | S02 pp. 9-15 |
| Are stacks useful for the intended task? | Interior segments lack aligned baselines, making precise category comparisons hard. Normalised stacks also hide absolute totals. | Use separate lines, grouped bars or small multiples when component comparison matters; show totals if needed. | S02 pp. 5-8, 12-15 |
| Do slices/segments actually form one whole? | Overlapping categories, adding a total as a component, or mixing denominators creates false composition. | Use mutually exclusive components with a clear denominator, or another comparison idiom. | S02 pp. 8, 15-17 |
| Is a pie being asked to show precise differences or many categories? | Similar angles/areas are difficult to rank; tiny slices create label clutter. | Use sorted bars/dots, selective highlighting or a meaningful Others group. | S02 pp. 15-17 |
| Are bubbles sized by area, with a usable size legend? | Scaling radius linearly squares the apparent area relationship and exaggerates differences. | Make area proportional to the quantity; provide representative legend values and units. | S02 pp. 19-20; S12 pp. 2-5 |
| Does overplotting conceal density, outliers or categories? | Hidden points or lines can make a sparse-looking pattern misleading. | Use smaller/translucent marks, filtering, aggregation, binning or suitable small multiples. | S02 pp. 10, 18-20; S12 pp. 4-5 |
| Are smoothing, endpoint summaries or averages hiding structure? | Invented curvature, omitted intermediate variation or aggregate-only displays can change the apparent story. | Show observations or fuller trajectories when they matter; use smoothing only with suitable continuity and context. | S01 pp. 4-5; S02 pp. 9, 12 |
| Is depth/perspective justified by the actual task? | Decorative 3D adds occlusion and perspective distortion that impair magnitude comparison. | Use 2D for abstract magnitude comparison; reserve 3D for a defensible spatial/shape task. | S05 pp. 1-14; S07 pp. 2-3 |

## Checks for presentation, colour and story

| Check when the work arrives | Why an observed failure matters | Improvement to consider | Class basis |
| --- | --- | --- | --- |
| Are colour meanings stable across charts? | Reusing a colour for different categories makes readers carry the wrong meaning between views. | Maintain a stable category palette and explicit mappings. | S08 pp. 5, 8; S19 pp. 15-16 |
| Does the palette fit categorical, sequential or diverging data? | Rainbow hue alone has no intuitive magnitude order; a diverging palette without a meaningful centre implies a false split. | Use distinguishable categorical hues, a luminance-led sequential scale, or a diverging scheme around a justified midpoint. | S04 pp. 3-8; S08 pp. 5-10; S17 p. 7 |
| Is colour distinguishable and contrasted against the background? | Similar hues, low contrast or red-green dependence can prevent some viewers from identifying groups or reading text. | Use accessible colour choices and additional labels, shapes, patterns or line styles where needed. | S08 pp. 6-11; S05 p. 24 |
| Is there a clear visual hierarchy and viewing path? | Equal emphasis everywhere leaves the reader unsure where to begin or what matters. | Differentiate title, section headings, charts, annotations and metadata; foreground the intended evidence. | S07 p. 4; S09 pp. 2-4; S10 pp. 10-12 |
| Are related elements aligned and grouped? | Misaligned edges and ambiguous spacing make captions, controls and charts harder to associate. | Use a consistent column grid, sight-lines and purposeful proximity/white space. | S09 pp. 3-6 |
| Does the whole chart, including legends and labels, fit the viewport? | Clipping or horizontal scrolling hides information and breaks comparison. | Adjust composition, chart dimensions, spacing and legends; test the actual page. | S26 p. 5 Q10; S28 p. 3 |
| Is text comfortably legible and readable? | Tiny labels, weak contrast, excessive line length, tight leading and centred paragraphs increase reading effort. | Use appropriate sizes and weights, adequate contrast and leading, shorter lines and left alignment for paragraphs. | S10 pp. 4-7 |
| Does type styling create meaning consistently? | Arbitrary font/weight changes compete for attention and can imply importance unrelated to the data. | Use a coherent type system with deliberate hierarchy and topic-appropriate display type. | S10 pp. 4-5, 8-12 |
| Is decoration competing with the data? | Heavy borders, excessive grids or unrelated illustrations divert attention from the message. | Remove or soften elements that do not support interpretation, while retaining useful guides and engaging context. | S06 pp. 2-3; S07 pp. 3-4 |
| Do headings and annotations explain a meaningful takeaway? | A sequence of topic labels and charts can leave the audience to perform the entire analysis. | Add concise, evidence-based headlines and annotations for important comparisons, outliers or turning points. | S07 pp. 2-6; S02 pp. 11, 15; S22 pp. 30-32 |
| Are claims supported by the displayed evidence? | Correlation alone does not establish causation; a selected window can omit contrary context. | Use accurate association language, explain the chosen scope and include relevant context. | S02 pp. 10, 18-19; S01 pp. 4-5 |
| Are labels, units, definitions, periods and sources clear? | Readers cannot judge what the values mean, whether periods align, or where the evidence comes from. | Use human-readable axis/legend titles, units, defined terms, dates and specific source links. | S20 pp. 6-8; S22 pp. 7-12; S28 pp. 3-6 |
| Does the narrative suit a general Australian/Malaysian audience? | Unexplained specialist terms or statistics make key information inaccessible. | Introduce necessary terminology and use concise explanations tied to the charts. | S28 pp. 2-3 |

## Checks for maps and interaction

| Check when the work arrives | Why an observed failure matters | Improvement to consider | Class basis |
| --- | --- | --- | --- |
| Is geography useful for the question? | A map can consume space while making rank/value comparison harder than a list or chart. | Retain maps for spatial patterns; supplement or replace with a ranking when that is the task. | S01 pp. 6-14; S05 p. 15 |
| Are choropleth values standardised appropriately? | Raw totals may mainly reflect population or area, confounding the intended comparison. | Use a relevant per-capita rate, density, percentage or another justified denominator; consider proportional symbols for totals. | S11 pp. 2-3; S21 pp. 27-29 |
| Does the projection preserve the property relevant to the task? | Strong area distortion visually exaggerates some regions, particularly in world choropleths/density maps. | Use a suitable equal-area projection for area comparison and broad density patterns; choose regional projections appropriately. | S13 pp. 3-8; S11 p. 4; S14 p. 2 |
| Is missing data distinguished from zero and from the ocean? | White/unfilled areas can disappear or be interpreted as genuine low values. | Keep a neutral base layer and explicitly explain missing values; check failed joins before labelling data unavailable. | S26 pp. 2-3; S19 pp. 20-22 |
| Are mapped classes and legends meaningful? | Poor thresholds or changing domains can hide variation or make identical colours mean different values across maps. | Use justified thresholds, readable labels and stable scales when comparing periods. | S11 p. 4; S19 pp. 21-27; S21 pp. 23-29 |
| Is the geographical granularity appropriate? | Very coarse regions hide local variation; excessively fine boundaries obscure larger patterns. | Match aggregation and detail to the question and available screen space. | S11 p. 5 |
| Do dots communicate quantity and placement honestly? | An unstated dot value or synthetic placement can be mistaken for exact individual locations; dense dots can merge into blobs. | State what one dot means and how locations are assigned; adjust size/value or choose another idiom. | S14 pp. 2-3 |
| Are proportional symbols large enough to compare but not hiding geography? | Oversized marks overlap and obscure smaller values; tiny marks prevent useful size comparison. | Adjust size range, draw order, outlines/transparency and detail interactions. | S12 pp. 2-5 |
| Are flows traceable, and is their meaning clear? | Overlaps, tangential crossings and paths through unrelated nodes create ambiguous connections. OD arcs can be mistaken for actual routes. | Improve routing and separation, explain line width/direction and distinguish OD connections from tracked paths. | S16 pp. 2-6 |
| Can readers recognise cartogram regions and interpret area? | Distorted outlines or displaced circles can prevent place identification, while irregular areas are hard to compare precisely. | Add clear labels/reference geography or a complementary quantitative chart. | S15 pp. 2-3 |
| Are scalar-field encodings interpretable? | Excessively dense contours obscure information; variable contour intervals mislead; bottom-lit relief can invert perceived landforms. | Use constant, readable contour intervals and index labels; suitable colour gradients and top-left illumination; combine idioms when useful. | S17 pp. 3-12 |
| Does interaction help a real user task? | Decorative controls add work and can conceal the main message behind trial and error. | Provide a useful initial view and only controls that reveal meaningful comparisons/details. | S05 pp. 19-24; S18 pp. 3, 7-13; S28 p. 3 |
| Are selection state, control scope and clearing actions understandable? | Readers can mistake filtered subsets for the full dataset or become stuck in a selection. | Label controls and affected views, show selection feedback and provide clear/reset behaviour where needed. | S18 pp. 9-11, 16-17; S22 pp. 15-28 |
| Can comparisons be made without remembering previous views? | Repeated slider changes require limited working memory and invite missed changes. | Consider aligned small multiples, an overview, traces or side-by-side comparison. | S05 pp. 15-18; S19 pp. 23-28 |
| Do linked views and annotations actually update together? | A changing subset with stale text or an unrelated highlight can contradict the visible evidence. | Coordinate selections across relevant views and derive annotations from the displayed subset. | S19 pp. 9-17; S25 pp. 2-4 |
| Do tooltips reveal useful details without carrying the entire story? | Hovering every point is slow; raw field names and excessive precision make detail hard to interpret. | Keep the overview and key takeaways visible; show concise names, units and formatted values on demand. | S05 pp. 22-24; S22 pp. 11-12; S10 p. 12 |
| Is the published result responsive and reliable? | Slow loads, blank views or silent actions interrupt understanding. | Reduce unnecessary geometry/data, verify public data paths and joins, and provide timely visual feedback. | S05 pp. 21-24; S21 pp. 5-11; S26 pp. 2-6; S28 p. 1 |

## Important qualifications

- A non-zero line-chart or scatterplot axis is not automatically wrong. Judge the task, scale labels, chosen range and resulting interpretation. Length-encoded magnitude bars require a zero baseline.
- Pie charts are not automatically wrong. They suit a single whole with few, distinguishable components; they are weak for close-value precision and multiple-total comparison.
- White space is useful for grouping and balance. Do not equate all empty space with poor data-ink ratio or attempt to maximise density at the expense of readability.
- Not every decorative element is harmful. The class notes explicitly discuss interpretability, engagement and memorability as reasons to retain some non-data elements.
- Luminance-led palettes can vary hue too. Viridis is not the same as an unordered rainbow palette. Dark backgrounds can justify reversing the usual light-low/dark-high convention.
- Symmetry is favoured by the DV2 rubric, but the layout notes also accept deliberate, balanced asymmetry. Separate an assignment-specific expectation from a universal design claim.
- More interaction, more complexity and more charts are not automatically improvements. Presentation and meaningful communication are central to this assignment.
- Normalisation should fit the question, not be applied indiscriminately to every quantity. Equal-area bins do not need area normalisation, but may still need per-capita rates. Median price is already an intensive measure and is not equivalent to a raw event count.
- Do not penalise a peer for failing to reproduce every studio example. The examples teach options, not an obligation to include every interaction or chart.
- Some technical notes contain historical versions, simplified claims and example inconsistencies. Use them to understand the lesson; do not treat their version-specific capability statements, placeholder URLs or sample labels as guaranteed current API truth.

## DV2 brief cross-check, if the peer work is DV2

S28 specifies: a minimum of ten charts; at least three different map idioms; similar chart series/small multiples count as one chart; all map idioms count as advanced. The rubric values effective and meaningful advanced idioms, not complexity alone. It also requires a single publicly accessible scrolling page, no horizontal scrolling on a small laptop, meaningful storytelling and appropriate interaction, reliable real-world data combining two sources, sources/author/date metadata, and terminology understandable to the intended general audience.

The HD idiom rubric specifies at least eight advanced idioms across more than ten charts. Do not infer compliance from the number of chart panels alone. Only assess code/library compliance, data recency, sources, sketch adherence or chart counts when the supplied work gives enough evidence. No separate peer-critique brief has been supplied yet; the user's requested minimum is four improvement points.

## Source key (PDF page numbers, counting cover pages)

All paths below point to the original local teaching materials.

| ID | Source |
| --- | --- |
| S01 | [Introduction: What, Why, How](../class_content/Course%20notes%201%20Data%20Visualisation%20What%20Why%20How.pdf) |
| S02 | [Visualisation of Table Datasets](../class_content/Course%20notes%204%20Visualisation%20of%20Table%20Datasets.pdf) |
| S03 | [Data Types](../class_content/FIT2179%20Course%20Notes%202%20Data%20Types.pdf) |
| S04 | [Marks and Channels](../class_content/FIT2179%20Course%20Notes%203%20Marks%20and%20Channels.pdf) |
| S05 | [Munzner Chapter 6: Rules of Thumb](../class_content/Munzner%20-%20Chapter%206%20-%20Rules%20of%20Thumb.pdf) |
| S06 | [Data-ink Ratio and Chartjunk](../class_content/FIT2179%20Course%20Notes%206%20Data-ink%20Ratio%20and%20Chartjunk.pdf) |
| S07 | [Storytelling with Data](../class_content/FIT3179%20-S2-2026%20-%20Course%20Notes%207%20Storytelling%20with%20Data.pdf) |
| S08 | [Colour](../class_content/FIT2179%20Course%20Notes%208%20Colour.pdf) |
| S09 | [Layout](../class_content/FIT2179%20Course%20Notes%209%20Layout.pdf) |
| S10 | [Typography](../class_content/FIT2179%20Course%20Notes%2011%20Typography.pdf) |
| S11 | [Choropleth Maps](../class_content/FIT2179%20Course%20Notes%20Choropleth.pdf) |
| S12 | [Proportional Symbol Maps](../class_content/FIT2179%20Course%20Notes%20Proportional%20Symbol%20Maps.pdf) |
| S13 | [Map Projections](../class_content/FIT2179%20Course%20Notes%2014%20Map%20Projections.pdf) |
| S14 | [Dot Maps](../class_content/FIT2179%20Course%20Notes%20Dot%20Maps.pdf) |
| S15 | [Cartograms](../class_content/FIT2179%20Course%20Notes%2016f%20Cartograms.pdf) |
| S16 | [Flow Maps](../class_content/FIT2179%20Course%20Notes%20Flow%20Maps.pdf) |
| S17 | [Scalar Fields](../class_content/FIT2179%20Course%20Notes%2017%20Scalar%20Fields.pdf) |
| S18 | [Munzner Chapter 11: Manipulate View](../class_content/Munzner%20Textbook%20Chapter%2011%20-%20Manipulate%20View.pdf) |
| S19 | [Week 10 Studio](../class_content/FIT3179%20Week%2010%20Studio.pdf) |
| S20 | [Week 7: Introduction to Vega-Lite](../class_content/FIT3179%20-%20Week%207%20%28Part%20B%29%20-%20Introduction%20to%20Vega-lite.pdf) |
| S21 | [Week 8: Create Maps with Vega-Lite](../class_content/FIT3179%20Week%208%20Studio%20%E2%80%93%20Create%20Maps%20with%20Vega-Lite.pdf) |
| S22 | [Week 9 Studio](../class_content/FIT3179%20Week%209%20Studio.pdf) |
| S23 | [Week 8: Geographic Vector Formats](../class_content/FIT3179%20Week%208%20Studio%20-%20Geographic%20Vector%20Formats.pdf) |
| S24 | [Introduction to JavaScript](../class_content/Part%20A%20-%20Introduction%20to%20JavaScript.pdf) |
| S25 | [Vega-Lite Code Example](../class_content/Vega-Lite%20Code%20Example.pdf) |
| S26 | [Vega-Lite FAQ](../class_content/Vega-Lite%20FAQ.pdf) |
| S27 | [Bin Maps](../class_content/FIT2179%20Course%20Notes%20Bin%20Maps.pdf) |
| S28 | [DV2 Assignment Brief and Rubric](../FIT3179%20Data%20Visualisation%202_v1.2.pdf) |

S23 and S24 supply implementation context (spatial formats, data types and event handling). S27 pp. 2-3 supplies the bin-map standardisation qualification. The code examples illustrate embedding, sorted bars, map layers, missing data, label layers, tooltips, selections, responsive layouts and multiple independent charts. They are supporting examples rather than independent marking rules.
