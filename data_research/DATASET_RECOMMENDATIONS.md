# Dataset recommendations — inspected 6 October 2026

## Preferred combination

1. BGG Data Full: https://www.kaggle.com/datasets/sylvainballerini/bgg-data-full
2. Wikidata publisher geography: https://www.wikidata.org/wiki/Wikidata:WikiProject_Board_Games
3. Award history: https://github.com/recommend-games/spiel-des-jahres/tree/main/src/spiel_des_jahres/data
   Primary verification source: https://www.spiel-des-jahres.de/spiele/

These add game characteristics, geography and award recognition respectively. They are research candidates; final figures require cleaning and validation. Additional sources are welcome when they answer an additional useful question.

## BGG Data Full — preferred main candidate

Kaggle lists an update on 22 September 2026. This is a dataset update date, not a verified common observation date for every row. The author's README describes incremental additions and less frequent full refreshes; dynamic values can therefore have different ages.

Actual game.csv inspection: 181,218 rows and 181,218 unique BGG IDs. Includes 141,336 base games and 39,882 expansions. No duplicate game IDs found. The supplied mechanics table has 200 mechanics; 455,498 game-mechanic links reference valid game and mechanic IDs. The publisher table contains 30,116 entities and 272,897 game-publisher links.

Fields include publication year, min/max players, min/max playing time, averageweight (complexity), ratings, vote counts, ownership, ranking and game type. Mechanics, categories and publishers are connected through ID-based bridge tables. These are source tables, not extra independent sources.

Local copy: bgg_2026/games_core_candidate.csv removes descriptions and image URLs from the original CSV but preserves all rows and the remaining fields without cleaning. The supporting tables and original README are in the same directory. Full original game.csv is retained outside the project in the task's visualization research directory. These files are too large to serve directly on the final webpage: derive small chart-specific summaries later.

Limitations:
- 104,907 records lack complexity. 62,666 base-game records have complexity in the 1–5 range, before further filtering.
- 12,131 records use publication year 0; 955 records have years after 2026, potentially announced games. Do not treat these as completed historical releases.
- The author's cleaning rules null playingtime over 360 minutes, minplaytime over 240 minutes, maxplaytime over 360 minutes and minage over 20, among other changes. Some genuine lengthy games may be affected. Avoid claiming to cover the full duration extremes.
- Separate expansions from base games; identify which population each chart describes. Mechanics evolve as catalogue labels as well as game designs; current labels applied to old games do not prove that those labels existed at publication.
- Dataset metadata declares CC BY-NC-SA 4.0; original BGG data remains attributed to BGG and its contributors.

## Publisher geography — independent geographic source

Existing publisher_geography_candidate.csv contains Wikidata country and headquarters properties queried on 6 October 2026. See README.md for the exact query. Comparing its BGG publisher IDs with the new publisher table gives 598 entities with countries and 507 with headquarters coordinates. Through publisher links, these cover 45,248 game records and 40,347 game records respectively, including expansions. These are preliminary unfiltered matches, not a validated final geographic sample.

Current query does not include historical qualifiers or distinguish headquarters city/region coordinates from office coordinates. Multiple countries/headquarters can yield multiple records. Verify matched entities and time relevance before maps. Count unique games within each country and explain games can appear in multiple countries. Publisher credits may include translation/edition publishers; do not label these as game invention or manufacturing locations.

Useful views: proportional-symbol map of games credited to publishers by country; choropleth of a clearly defined mechanic percentage or median complexity with adequate sample sizes; dot map of verified headquarters locations. Geographic gaps must remain visible.

## Award history — adds a new story

Downloaded sdj_candidate.csv (528 records, 1979–2026), ksdj_candidate.csv (101 records, 2011–2026) and kindersdj_candidate.csv (279 records, 1989–2026). All 908 records match game IDs in the new main table. These include winners, nominations, recommendations and special awards, not 908 winners. Older children's records include predecessor/special-award history; do not assume the modern category existed throughout that range. Award year (jahrgang) differs from publication year.

The CSVs are third-party curated data from Recommend.Games. Verify selected records against the official Spiel des Jahres archive. The three 2026 main winning records correspond to JinxO / DITO!, Rebirth and Mooki Island / Die Insel der Mookies; the English/German title differences are why ID joins are preferable. Do not treat the project's predicted rankings as actual award results. Repository software is MIT-licensed; that alone does not establish a separate license for every underlying source record.

Useful charts: complexity distribution by award category; award-winner timeline; mechanic shares among award recipients compared with a clearly defined BGG comparison group. Restrict to matched records with the required fields and distinguish winner/nominated/recommended/special status.

## Other inspected sources

- https://www.kaggle.com/datasets/fotopoulosvasileios/board-games-info-from-boardgamegeek-com — actual dated-directory CSV has 25,200 rows and 24,767 distinct titles, complexity/player/time/year fields, but no game IDs or mechanics. Uploaded 29 August 2025; directory says 15 August 2025 while description still cites December 2023. Date ambiguity and title-only joins make it less useful than the new main dataset. Retained as fotopoulos_info_candidate.csv.
- https://www.kaggle.com/datasets/chik0di/board-games-dataset-complete-features — earlier 2,000-row candidate. Superseded because of smaller ranked sample and duplicates.
- https://github.com/julianss/bgg-data-explorer — live API metadata reports 30,199 games and 28 February 2026 snapshot, but its repository explicitly omits the database and requires an API token to build one. Not a ready downloadable dataset.
- https://www.kaggle.com/datasets/thedevastator/board-game-ratings-by-country — potentially useful reviewer-country data, but file listing includes May 2019 material and country provenance/coverage would need validation. Metadata inspected only; not downloaded or recommended for final maps yet.

## Practical next step

Update, 7 October 2026: downloadable Malaysia/Australia ratings-based rankings from a 2024 analysis and a 25 April 2024 global archive were found and inspected. See [country_rankings_2024/README.md](country_rankings_2024/README.md) for provenance, samples, caveats and a prepared comparison. These provide a historical local/global comparison; they are not national sales figures or 2026 country rankings.

Use the newer BGG candidate for the core story, join Wikidata for geographic context, and add awards only if the page benefits from discussing recognition. Clean once, document dates and missingness, then create small precomputed CSVs for the final Vega-Lite charts. Do not combine historical snapshots as though all values were measured on the same date.
