# Critique: Visitor Spending in Australia

Reviewed 15 October 2026 against the supplied critique requirements, class materials, screenshots, live page and public chart/data files.

[Visualisation](https://marcusmonash.github.io/FIT3179_DV2_33590486/)

The critique requirements specify at least four substantial bullet points ordered from most to least important, and a two-minute oral critique. This document is a preparation draft for the user; no feedback has been posted to the peer or Moodle.

## Priority feedback, ordered by importance

- **1. Separate spending and length of stay instead of connecting them on one axis.** In “How Long People Stay Vs Their Spendings”, dollars and days share a logarithmic y-axis called “Value”. For example, Education connects $8,900 with 45 days. These are different units, so the downward line has no meaningful interpretation as a change. A logarithmic transformation cannot make the units comparable. Use a scatterplot with average stay in days on x and average spending in AUD on y, with a labelled point for each visit purpose. With only four purposes, describe the comparison without claiming robust correlation or causation. Alternatively, use two aligned charts with separate, clearly labelled units. Class principles: expressiveness, meaningful data abstraction and suitable idiom selection. [Chart specification](https://github.com/marcusmonash/FIT3179_DV2_33590486/blob/main/idioms/idiom1.json), [data](https://github.com/marcusmonash/FIT3179_DV2_33590486/blob/main/data/idiom1.csv).

- **2. Correct the “big cities” map's geographical claim.** “Tourist Spending In Big Cities” sums `Spend (AUD m)` grouped by `State`, latitude and longitude. The CSV repeats capital-city coordinates for each state's categories. The resulting Sydney circle therefore represents a sum of New South Wales categories, not verified Sydney expenditure. This can mislead readers about where the spending actually occurred. Obtain genuine city-level expenditure or relabel the chart as state-level spending in the included categories, with symbols positioned and explained accordingly. Also state its coverage: it sums selected categories rather than the same totals used in the neighbouring state map. Class principle: an encoding must express the actual meaning and geographical scope of its data. [Map specification](https://github.com/marcusmonash/FIT3179_DV2_33590486/blob/main/idioms/map3.json), [data](https://github.com/marcusmonash/FIT3179_DV2_33590486/blob/main/data/chart2.csv).

- **3. Use an appropriate measure and projection for the state choropleth.** “Total Tourist Spending By State” directly maps raw expenditure totals to fill colour. Larger tourism markets can have higher totals simply because they receive more visitors, so this does not distinguish visitor volume from spending intensity. The course's choropleth guidance recommends standardised values. For a spending-intensity story, use a justified measure such as expenditure per visitor or per visitor-night. If the goal is total expenditure, retain the totals in proportional symbols or sorted bars. For an Australia-wide choropleth, also replace the current equirectangular projection with a suitable equal-area projection. Class principles: choropleth standardisation and map projection choice. [Map specification](https://github.com/marcusmonash/FIT3179_DV2_33590486/blob/main/idioms/map2.json). This is not a request to divide every spending measure by population or land area regardless of the question.

- **4. Remove the radial chart's exaggerated area differences.** “What Tourists Spend their Money On” maps the same spending value to both slice angle and radius. Large categories therefore get both wider and longer slices, so their visible area is not proportional to their share of expenditure. Small categories, especially taxis/rideshare, become very difficult to see. Use sorted horizontal bars for accurate comparison, or a conventional doughnut with a constant outer radius and clear percentage labels. Class principles: effective magnitude channels and faithful part-to-whole representation. [Chart specification](https://github.com/marcusmonash/FIT3179_DV2_33590486/blob/main/idioms/idiom3.json).

- **5. Add source, date and scope information.** The published page has no visible data-source links, reference period, author/date or explanation of coverage. Readers cannot verify whether charts use comparable periods, whether the national/category totals cover the same spending, or how the averages were calculated. Add a concise introduction defining the reference period, visitor populations and currency, plus specific dataset links and an authorship/date footer. Missing provenance is a verifiability problem; it does not establish that the data is fabricated. Class principles: audience context, metadata and reliable data.

- **6. Turn the chart collection into an explanatory story.** The page has headings but no narrative paragraphs, takeaway annotations or explanations of important patterns. Readers must derive every conclusion and work out why each chart follows the previous one. Use a short opening question, evidence-based takeaway headings, selective annotations and transitions connecting visitor origins, spending locations and spending categories. Explain “VFR” as visiting friends and relatives. Class principles: goal-oriented storytelling and guiding attention.

- **7. Align the transport title with the measured variable.** “The Transport Tourists Use” plots expenditure, not users, trips or mode share. A costly mode can generate high expenditure even when fewer people use it, so spending cannot establish the most-used transport. Rename it “Tourist spending by transport category”, or use passenger/trip counts for a usage comparison. Sort by spending if ranking the categories is the purpose. Class principle: match the data and idiom to the question.

- **8. Make labels readable without requiring hover.** The domestic/international chart truncates categories such as “Food alcohol and other beverage prod...” and “Recreational cultural and gambling se...”. Small legend text and rotated labels add further reading effort. Widen the label area, wrap category names, shorten them consistently and increase label/legend sizes. The full category identity should be readable in the default view. Class principles: typographic legibility and reducing unnecessary lookup.

- **9. Fix chart overflow and use the column grid consistently.** The city map fixes its plot width at 600 pixels inside a half-width column, with the legend needing further space. In the observed narrower browser view, the canvas extends beyond the visible viewport and requires horizontal scrolling. The final stacked chart also occupies only the left half of its row while its labels are truncated. Account for the entire chart including axes and legends, stack columns at a suitable breakpoint, and give the final comparison more width. Use space for narrative if it supports the story. Class principles: sight-lines, balance, purposeful white space and responsive presentation. The inspection did not establish a precise laptop breakpoint; do not quote an unverified 1280-pixel failure.

- **10. Improve contrast and identification in the transport chart.** Its small pastel markers, particularly mint and peach, have weak visual contrast against white and require repeated matching to a separate legend. Use darker markers or contrasting outlines and direct labels where useful. Preserve distinguishable categories without making colour the only identification cue. Class principles: foreground/background contrast and accessible colour design. The heatmap's Viridis palette is appropriate for quantitative data and should not be criticised as an unordered rainbow palette.

## Approximately two-minute speaking version

The highest-priority improvements are about how the charts represent the data.

First, the stay-versus-spending chart connects dollars and days on the same axis. These units cannot be compared as a change, so the downward lines are misleading. I would use a scatterplot with days on one axis and spending in AUD on the other.

Second, the big-cities map actually groups spending by state and places those sums at capital-city coordinates. This makes state expenditure look like city expenditure. It needs genuine city data or an accurate state-level title and explanation.

Third, the state choropleth uses absolute spending. That mixes tourism volume with spending intensity. A rate such as spending per visitor would suit the choropleth; total spending would be clearer with proportional symbols or sorted bars. The choropleth should also use a suitable equal-area projection.

Fourth, the radial spending chart changes both slice angle and radius, exaggerating area differences. Sorted bars or a constant-radius doughnut would communicate the shares more faithfully.

For presentation, the category labels need more space because several are truncated, and the small pastel transport markers need stronger contrast. The city map also overflows its column in a narrower view.

Finally, add the data period, source links and short takeaway annotations. These would make the charts easier to verify and give the page a clear story.

Practise aloud and adjust to the user's actual speaking pace. The written list contains more detail than should be read in the oral presentation.

## Class references

PDF page references count from each file's cover page. The broader [course checklist](../CRITIQUE_CHECKLIST.md) records the complete review.

| Feedback | Course material |
| --- | --- |
| 1, 2, 4, 7 | Marks and Channels, PDF pp. 3-8; Introduction What/Why/How, pp. 6-14; Visualisation of Table Datasets, pp. 9-20 |
| 3 | Choropleth Maps, pp. 2-4; Map Projections, pp. 3-8 |
| 5, 6 | Storytelling with Data, pp. 2-6; DV2 assignment brief, pp. 2-6 |
| 8 | Typography, pp. 5-7, 11-12 |
| 9 | Layout, pp. 3-6; Vega-Lite FAQ, p. 5 Q10 |
| 10 | Colour, pp. 5-11 |

The critique requirements are at `C:/Users/User/Downloads/FIT2179 DV2 Critique Requirements.pdf`. Public source snapshots for the key findings are saved in the adjacent `source` directory. No claim is made that the draft has fabricated data, lacks hover tooltips, or must reproduce every studio example.
