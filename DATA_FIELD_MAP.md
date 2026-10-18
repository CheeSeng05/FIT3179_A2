# Verified dataset field map for the 15-chart plan

Checked against actual local CSV headers on 7 October 2026. Friendly chart labels in the sketch are not literal CSV field names. All proposed charts have their source fields present locally. This verifies field availability, not completed cleaning, geographic accuracy or finished chart datasets.

## Files

G = data_research/bgg_2026/games_core_candidate.csv
GM = data_research/bgg_2026/b_game_mechanic.csv
M = data_research/bgg_2026/mechanic.csv
GP = data_research/bgg_2026/b_game_publisher.csv
P = data_research/bgg_2026/publisher.csv
W = data_research/publisher_geography_candidate.csv
C = data_research/country_rankings_2024/comparison_candidate.csv
MY/AU = malaysia.csv and australia.csv in data_research/country_rankings_2024
GLOBAL = global_2024-04-25.csv in that directory
A = data_research/sdj_candidate.csv, ksdj_candidate.csv, kindersdj_candidate.csv
MAP = class_content/3_choropleth_map/js/ne_110m_admin_0_countries.topojson
CENTRES = class_content/3_choropleth_map/data/countryInfo.csv

## Exact fields by chart

| # | Chart | Existing source fields | Values to calculate/prepare |
|---|---|---|---|
| 1 | Publication-year line | G: id_bgg, yearpublished, game_type | Distinct eligible game count by publication year |
| 2 | Mechanics bar | G: id_bgg, game_type, yearpublished; GM: id_bgg, id_mechanic; M: id_mechanic, mechanic | Distinct eligible games per mechanic; top-mechanic selection |
| 3 | Mechanics by decade heatmap | Same fields as #2 | publication_decade; eligible games with a mechanic / games with any recorded mechanic in each decade |
| 4 | Mechanics network | Same fields as #2 | Unique mechanic pairs per eligible game; pair co-occurrence counts; node/link tables |
| 5 | Complexity box plots | G: id_bgg, yearpublished, averageweight, numweights, game_type | Decade; valid complexity/vote filter; median, quartiles and whiskers |
| 6 | Complexity/time scatter | G: id_bgg, name_game, averageweight, playingtime, numweights, game_type, yearpublished | Valid field filter and reproducible point sample if necessary |
| 7 | Publisher treemap | G: id_bgg, game_type, yearpublished; GP: id_bgg, id_publisher; P: id_publisher, publisher | Distinct game-publisher credits per publisher; top publishers and Other |
| 8 | Headquarters dot map | GP/P: publisher IDs and names; G: eligible game IDs; W: bggPublisherId, publisher, publisherLabel, hqLabel, coordinate | Verified headquarters selection; parse Point(longitude latitude) into numeric coordinates; remove duplicate points/records under documented policy |
| 9 | Cooperative share choropleth | G/GP/P: game-publisher links; W: bggPublisherId, countryLabel; GM/M: mechanic links; MAP: country geometry | Validated country crosswalk; unique eligible games and Cooperative Game (2023) counts; proportion and sample threshold |
| 10 | Community proportional-symbol map | country_rankings_2024/countries.csv: country_code, country_name, num_users, total_ratings; CENTRES: country, latitude, longitude, name | Uppercase code join; numeric counts; circle area scale; missing counts stay missing. Prepared candidate: planning/map_revision/community_map_candidate.csv; 197 matched positive records, 2 unresolved, 17 missing user counts |
| 11 | Rank heatmap | C: bgg_id, name, global_rank_2024_04_25, malaysia_rank, australia_rank, malaysia_num_ratings, australia_num_ratings | Union of each source's top five, deduplicated; reshape three ranks into rows; missing rank stays unavailable |
| 12 | Top-20 mechanics comparison | MY/AU: bgg_id, rank; GLOBAL: ID, Rank; GM/M: mechanic links and names | Per-list top-20 selection, game-ID joins, unique mechanic games / eligible games with mechanics |
| 13 | Top-20 complexity dots | MY/AU: bgg_id, rank; GLOBAL: ID, Rank; G: id_bgg, name_game, averageweight, numweights | Per-list top-20 selection; join later complexity scores; consistent vote filter; overlap offsets for dots |
| 14 | Award mechanics comparison | A: bgg_id, jahrgang, winner, nominated, recommended, sonderpreis; G: id_bgg, yearpublished, game_type; GM/M: mechanic links | Derive award category from filename; verify main winners, exclude special awards; deduplicate games; calculate percentages for award/wider groups |
| 15 | Award game profiles | A: bgg_id, jahrgang, winner, sonderpreis; G: id_bgg, name_game, averageweight, playingtime, max_player, minage | Select eligible examples by documented rule; derive category from filename; separate scales for complexity, time, maximum players and age |

## Field meanings

- Complexity: G.averageweight, not a column named complexity. It is an average community complexity score, not the physical box weight.
- Game name: G.name_game.
- Release/publication year: G.yearpublished.
- Players: G.min_player and G.max_player.
- Playing time: G.playingtime. Available min/max estimates are G.minplaytime and G.maxplaytime; do not silently exchange them with playingtime.
- Minimum age: G.minage.
- Community rating: G.average; BGG adjusted rating: G.bayesaverage; global position in that later dataset: G.rank. Chart #11 deliberately uses the historical global_rank_2024_04_25 instead.
- Number of rating votes: G.usersrated; number of complexity votes: G.numweights. They are different measures.
- Country-file adjusted ratings: MY/AU.bayes_rating. These are the analyst's country-specific calculations, not the later global G.bayesaverage.
- Award year: A.jahrgang, not publication year. The award category is identified by the file, not an existing category column.

## Join keys

- G.id_bgg = GM.id_bgg; GM.id_mechanic = M.id_mechanic.
- G.id_bgg = GP.id_bgg; GP.id_publisher = P.id_publisher.
- P.id_publisher = W.bggPublisherId after consistent ID typing and entity checks. W.publisher is a Wikidata entity URL; it is not the same kind of value as P.publisher, a publisher name.
- G.id_bgg = A.bgg_id = MY/AU.bgg_id = C.bgg_id = GLOBAL.ID after consistent ID typing.
- W.countryLabel needs a checked crosswalk to the map/country-centre names or codes. Names are not guaranteed exact matches, and historical countries may need separate treatment.

## What is already present and what remains

All core source tables, country ranking files, award files, world country boundaries and representative country coordinates are already in this project. The class map file has 177 country geometries under object ne_110m_admin_0_countries. It is supporting map geometry, not board-game evidence. Use and credit its actual source when implementing the map; do not reuse class COVID values as game data.

The following are calculations, not missing datasets: counts, percentages, decades, graph edges, top-N selections, award-group labels, boxplot summaries and extracted longitude/latitude. Most graph-specific cleaned CSVs have not been generated yet. comparison_candidate.csv is already a joined candidate for the rank chart.

Publisher geography remains the principal quality check: the Wikidata query omits historical qualifiers and some headquarters coordinates represent cities or regions. Verify ambiguous records, reject unusable ones, and report missing coverage. Additional source checking may be needed to settle ambiguous entities/locations; no new primary dataset is currently required merely to supply the planned fields.

The sketch's drawn trends, bar lengths, map shading and point positions are illustrative placeholders. Available fields do not establish those pictured patterns. Actual findings and chart appearance must come from the cleaned data.

## Fields for linked interactions

No new external source is needed for the proposed interactions. Retain yearpublished in the prepared mechanic facts for the chart-1 brush; count distinct id_bgg within the selected years and recompute percentage denominators. Retain publication_decade in the publisher-country and headquarters linkage summaries for maps 8–9; verify and deduplicate country-game links before counting. Use a long-format country/decade table joined from data rows to geometry. Retain a common bgg_id across reshaped ranking rows and top-20 complexity rows for selection linking; averageweight is the same overall score for a game in every ranking group. Keep game IDs and names in the selected award profiles for hover highlighting. Derived names are prepared fields, not existing CSV headers.

Revision 8 October 2026: the former publisher game-count map is removed. Cooperative share is now chart 9. Chart 10 uses the already downloaded country user-count table with country coordinates and has no publication-year filter. See planning/map_revision/community_map_join_check.json for the tested join coverage.
