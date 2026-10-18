# Final board-game graph plan

Five sections, 15 planned charts. B = basic; A = advanced. These are questions to investigate, not calculated findings.

| # | Graph | Level | Dataset | Use |
|---|---|---|---|---|
| 1 | Publication-year line | B | BGG | Show games in the catalogue by publication year. |
| 2 | Mechanics bar chart | B | BGG | Introduce common ways of playing. |
| 3 | Mechanics-by-decade heatmap | A | BGG | Compare the share using each mechanic across decades. |
| 4 | Mechanics network | A | BGG | Show mechanics that appear together. |
| 5 | Complexity-by-decade box plot | A | BGG | Compare the spread of complexity scores. |
| 6 | Complexity/time scatterplot | B | BGG | Explore whether more complex games take longer. |
| 7 | Publisher treemap | A | BGG | Compare credited publisher catalogue sizes. |
| 8 | Headquarters dot map | A | BGG + Geography | Show recorded publisher headquarters. |
| 9 | Cooperative-share choropleth | A | BGG + Geography | Compare cooperative-game percentages in country-linked catalogues. |
| 10 | BGG community proportional-symbol map | A | Community + country coordinates | Show the size of the historical rating-contributor samples. |
| 11 | Global/Malaysia/Australia rank heatmap | A | Rankings | Compare historical positions of selected top games. |
| 12 | Top-20 mechanics grouped bars | B | Rankings + BGG | Compare mechanics used in the three top-20 lists. |
| 13 | Top-20 complexity dot plot | B | Rankings + BGG | Compare complexity of games in those lists. |
| 14 | Winners/collection mechanics grouped bars | B | Awards + BGG | Compare winners' mechanics with the wider sample. |
| 15 | Winner profiles: parallel coordinates | A | Awards + BGG | Compare complexity, time, maximum players and minimum age. |

Dataset key (all local):

- **BGG:** data_research/bgg_2026/games_core_candidate.csv; mechanic.csv + b_game_mechanic.csv for mechanics; publisher.csv + b_game_publisher.csv for publishers. Kaggle BGG Data Full, listed update September 2026. Core story: base games published 1950–2025.
- **Geography:** data_research/publisher_geography_candidate.csv (Wikidata), plus class_content/3_choropleth_map/js/ne_110m_admin_0_countries.topojson (world boundaries) and data/countryInfo.csv in the same class example (representative country marker locations). Geography and country matching need verification.
- **Rankings:** data_research/country_rankings_2024/malaysia.csv, australia.csv, global_2024-04-25.csv and comparison_candidate.csv. Historical April 2024 BGG ratings-based lists, not current national popularity or sales.
- **Community:** data_research/country_rankings_2024/countries.csv; num_users sets circle area, total_ratings appears in tooltips. Coordinates come from class_content/3_choropleth_map/data/countryInfo.csv. A checked candidate and unresolved-code report are in planning/map_revision. These are users who contributed ratings to the April 2024 analysis, not all national players or BGG members.
- **Awards:** data_research/sdj_candidate.csv, ksdj_candidate.csv and kindersdj_candidate.csv. Spiel des Jahres award-history files; filter actual main-category winners and verify against the official archive. Chart 14 uses the defined 2011–2025 publication-year sample; chart 15 selects eligible winners through 2025.

Story order: through time (1–3) → playing experience (4–6) → publishers (7–9) → rating communities and global/local rankings (10–13) → award-winning examples (14–15).

Interactions: select years in 1 to update 2–3; shared publication-decade selection for maps 8–9; select a game in 11 to highlight its dots in 13; hover a line in 15. Clear/reset controls are visible. Rankings membership is from 2024; joined mechanics and complexity are recorded in the 2026 source.

Nine advanced instances use eight different advanced types because the two heatmaps repeat a type. Similar displays can be counted as a series; 15 instances do not guarantee 15 rubric-counted charts. Source fields are present, but cleaned chart data and validated findings remain to be produced.

Latest drawing: planning/hand-drawn-layout-map-v4.png. This is an AI-generated reference to redraw by hand, not the hand-drawn submission itself.

Revision 8 October 2026: remove the publisher-country game-count map, renumber the cooperative-share map to 9, and use country rating contributors for new chart 10. Graph count and the three distinct map idioms remain unchanged. Chart 10 has its own historical scope and is not connected to the publication-decade filter.
