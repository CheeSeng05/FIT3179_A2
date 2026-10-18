# Board-game webpage: proposed graph plan

Updated: 8 October 2026. This is a proposed design, not a report of findings. Titles below ask questions; the data must establish the answers before we write takeaway headlines. See STORY_PLAN.md for the reader-facing story and transitions.

## Scope and sources

- Main source: BGG Data Full, listed update 22 September 2026; local core and relationship tables in data_research/bgg_2026.
- Geography: Wikidata country and headquarters records in data_research/publisher_geography_candidate.csv. ID links exist, but historical locations, multiple locations and coordinate precision need validation.
- Recognition: sdj_candidate.csv, ksdj_candidate.csv and kindersdj_candidate.csv; third-party award histories, to verify against the official Spiel des Jahres archive.
- Local/global rankings: country_rankings_2024/malaysia.csv and australia.csv from Markus Shepherd's April 2024 analysis, plus global_2024-04-25.csv from the beefsack archive. These are historical BGG ratings-based rankings, not 2026 national popularity or sales. Precise collection dates for the country ratings are not established.
- Proposed core population: base games (game_type=boardgame), with publication years 1950–2025. This is a deliberate focus on modern games. Exclude year 0 and unknown/invalid values; omit incomplete 2026 from historical comparisons. Every chart states its actual sample and missing-data exclusions.
- This is the BGG catalogue sample, not a census of worldwide publication, sales or player behaviour. Collection update dates do not establish a common observation date for all ratings.

## Section 1 — Board games through time

### 1. Publication-year line chart — basic
Question: How many games in this catalogue were published each year?
Data: yearpublished; count distinct id_bgg per year within the core population.
Encoding: year on x, number of games on y.
Purpose: introduce the scale and release-year pattern of the collection. Do not assert growth before calculation or label the values worldwide releases.

### 2. Mechanics ranked bar chart — basic
Question: Which ways of playing occur most often?
Data: game, b_game_mechanic and mechanic; count distinct core games per mechanic, show approximately the top 10.
Encoding: mechanic names on y, number of games on x.
Purpose: introduce common mechanics in plain language, with short explanations for unfamiliar terms. Multiple mechanics can belong to one game, so bars are not mutually exclusive.

### 3. Mechanics-by-decade heatmap — advanced
Question: Does the mix of mechanics differ between older and newer games?
Data: the same links plus publication decade; percentage of games with a mechanic among core games in that decade having at least one recorded mechanic. Show a small selected set using a declared rule, such as the eight most common overall.
Encoding: decade on x, mechanic on y, percentage by colour; tooltip includes numerator and denominator.
Purpose: distinguish changes in the mix from increases in total recorded games. Label 2020–2025 as a partial decade. Current catalogue labels applied to old games are not proof of when those labels were invented.

## Section 2 — How games play

### 4. Mechanic co-occurrence network — advanced
Question: Which mechanics appear together in the same games?
Data: unique unordered mechanic pairs for each core game with known mechanics. Limit to around 8–10 common mechanics and a small set of strongest links.
Encoding: nodes represent mechanics; edges represent shared games; thicker edges mean more shared games.
Purpose: show that a game can combine systems such as dice rolling and hand management. This is co-occurrence, not causation, similarity of player experience or a geographic map.

### 5. Complexity-by-decade box plot — advanced
Question: How does the spread of complexity differ by publication decade?
Data: yearpublished, averageweight and numweights. Complexity must be 1–5. Proposed reliability filter: at least 10 complexity votes, with sensitivity checked before finalising. Show the resulting sample size per decade.
Encoding: decade on x, complexity on y; box and centre line show the distribution.
Purpose: compare variation, rather than using an average alone. Explain: the centre line is the middle score; the box contains the middle half of scores. The scores are present-day recorded opinions about games from each decade, not historical opinions measured in that decade.

### 6. Complexity versus playing-time scatterplot — basic
Question: Do games with higher complexity scores also tend to take longer?
Data: averageweight, playingtime, numweights; valid recorded duration and complexity. Apply the same declared complexity-vote filter. Display a small reproducible sample of points or otherwise control overplotting; do not ship tens of thousands of marks needlessly.
Encoding: playing time on x, complexity on y; tooltip gives game name and values.
Purpose: investigate an association and reveal exceptions. Source cleaning removes playingtime above 360 minutes, so the graph cannot represent the full range of lengthy games. Association does not establish cause.

## Section 3 — The publishing world

### 7. Publisher catalogue treemap — advanced
Question: Which publishers are credited on the largest numbers of games in this collection?
Data: core game IDs linked via b_game_publisher to publisher. Count each game-publisher pair once; display top publishers and an Other group.
Encoding: rectangle area represents the number of credited games for that publisher.
Purpose: compare credited catalogue sizes across companies. Several companies can be credited for editions/translations of one game; area shares are shares of publisher-game credits, not mutually exclusive shares of unique games, original publication or market sales.

### 8. Publisher-headquarters dot map — advanced; map idiom 1
Question: Where are the verified recorded headquarters of publishers linked to this collection?
Data: publishers linked to core games, joined by BGG publisher IDs to Wikidata headquarters coordinates; verify location type and historical relevance.
Encoding: equal-sized dots; one per verified publisher headquarters record. Show multiple records only with a stated policy. Explain overlapping locations in tooltips.
Purpose: show the spatial distribution of recorded publishers. Do not claim precise office locations where coordinates describe a city, or plot a state/region centroid as a specific headquarters. Use a suitable world projection, such as Equal Earth.

### 9. Cooperative-game share choropleth — advanced; map idiom 2
Question: How does the share of cooperative games differ between publisher countries?
Data: core game-publisher links joined to validated Wikidata country records and mechanic links. Identify Cooperative Game mechanic ID 2023. Divide distinct cooperative-tagged games by distinct games with any recorded mechanic in each country. Proposed minimum: 50 eligible games; check coverage after filtering.
Encoding: country fill represents percentage. Insufficient-data countries have a separate grey legend. Tooltip includes eligible game count and numerator. Use Equal Earth and a fixed percentage scale across publication-period selections.
Purpose: compare design mix in publisher-linked catalogues. This is not resident gaming preference, invention location or sales. Several countries may receive credits for the same game. Validate countries and historic publisher relevance.

## Section 4 — Global favourites, local favourites

### 10. BGG rating contributors by country — proportional-symbol map; advanced; map idiom 3
Question: How large are the country samples behind this historical BGG analysis?
Data: data_research/country_rankings_2024/countries.csv; country_code, country_name, num_users, total_ratings. Match uppercased codes to representative country coordinates from the class countryInfo.csv. The tested candidate is planning/map_revision/community_map_candidate.csv. 197 of 199 positive-user records currently match coordinates; two unresolved codes and 17 missing user counts are logged separately. Missing counts are not zero.
Encoding: circle AREA proportional to num_users on a world map; numeric size legend; label Malaysia (657) and Australia (9,235) directly. Other countries use neutral circles; Malaysia orange and Australia blue. Tooltip adds total_ratings, country name and the historical source date. Use a fixed area scale with zero baseline; handle very large circles by drawing large first and allowing hover rather than distorting counts.
Purpose: establish the size and geographic distribution of the BGG rating-contributor sample before comparing ranks. This directly explains why the Malaysia and Australia lists have different amounts of evidence. It is not a count of all board-game players, all BGG members, sales or objectively verified residents. Self-reported countries may be inaccurate. Label analysis published April 2024; precise underlying extraction date remains unknown. The map is static historical data and must not respond to the publisher publication-decade filter.
Verified examples: Malaysia 657 contributors / 33,256 ratings; Australia 9,235 contributors / 468,659 ratings. Contributor count is not the vote count of each individual ranked game; those counts remain in chart 11 tooltips. Do not claim larger samples eliminate selection bias or automatically make a rank reliable.

### 11. Global/Malaysia/Australia rank heatmap — advanced
Question: Are globally highly rated games also highly ranked by Malaysian and Australian BGG users?
Data: comparison_candidate.csv. Select the union of the top five games from each historical ranking, deduplicate by game ID, and show their positions in all three lists. Selection can yield up to 15 games. Keep rank 1 visually prominent; neutral cells mean no rank available, never zero or dislike. Explain different list lengths and eligibility thresholds.
Encoding: one row per game; Global, Malaysia and Australia columns; print rank inside each cell and use colour only as a supporting cue. Display local rating counts in tooltips.
Purpose: demonstrate agreements and differences in the ranking order. Verified example: Brass: Birmingham is global #1, Malaysia #6 and Australia #3 in these files. Label the panel Historical comparison: published April 2024; global snapshot 25 April 2024. Country calculation and global BGG ranking are not identical algorithms or guaranteed synchronized observations. Country refers to users' self-reported country, not publisher country.

### 12. Top-20 mechanics comparison — grouped bar chart; basic
Question: Do the highest-ranked games in the three lists use different mixes of mechanics?
Data: take the first 20 ranked games in each historical list, joined by BGG IDs to the 2026 main mechanic links. For each list, count unique games using each mechanic and divide by eligible top-20 games with recorded mechanics. Select approximately six mechanics using a declared rule, such as the most common in the union, rather than selectively choosing those with biggest gaps.
Encoding: three bars per mechanic, one for each list; percentages on the quantitative axis.
Purpose: connect the local ranking comparison to the earlier explanation of game design. Explain that a game can have multiple mechanics and can appear in more than one list. This describes the top-ranked lists, not a nationwide preference for a mechanic. Labels must distinguish historical list membership from later recorded mechanic metadata.

### 13. Complexity of the three top-20 lists — dot plot; basic
Question: Are the highly ranked games in each list similarly demanding?
Data: the same top-20 selections joined by game ID to recorded averageweight and numweights in the 2026 main data. All 20 games in each list currently match the main table and have valid complexity scores. Apply any declared complexity-vote threshold consistently and report resulting sample sizes.
Encoding: complexity 1–5 on x, ranking group on y; one dot per game, with deterministic vertical offsets to avoid overlap. Highlight the same game across groups on hover and label a few recognisable examples. Explain that the score is community-reported complexity, not an objective difficulty assessment.
Purpose: link ranking differences to a practical game-night question. The 60 dots represent three sets of 20, with overlapping games; they are not 60 distinct games or individual local users' complexity ratings. State: games in 2024 rankings, using complexity scores recorded in the 2026 dataset. Do not claim these are 2024 complexity measurements or that all Malaysians/Australians favour a particular difficulty.

## Section 5 — Games that receive recognition

### 14. Award-winner mechanics comparison — grouped bar chart; basic
Question: Which mechanics occur more often among award winners than in the broader collection?
Data: award CSVs joined by bgg_id to game and mechanic links. Define the comparison using base games published 2011–2025 with recorded mechanics; use verified main-category winners from those publication years, excluding special awards. Count each game once in each comparison group. Keep winning, nominated and recommended status separate. Award year differs from publication year.
Encoding: approximately six mechanics on y; two bars per mechanic, one for the award-winning subset and one for the broader BGG population; bars show percentages, not raw counts.
Purpose: compare the kinds of games receiving recognition with the defined wider sample. The broader population contains the winners; label it as all eligible BGG games, not non-winners. No claim that the award causes particular mechanics to succeed.

### 15. Award-winning game profiles — parallel-coordinates chart; advanced
Question: How can award-winning games offer different playing experiences?
Data: verified main-category winners linked to game data; select the two most recent eligible winners per category through 2025 with complete values for complexity, playingtime, max_player and minage, using a published selection rule.
Encoding: four labelled axes (complexity, minutes, maximum players and minimum age), each with its own scale; each line is one game. Label lines directly and support hover highlighting. Do not imply the axes use the same units.
Purpose: let readers compare a small number of recognisable examples; one winner can suit a short family session while another demands more time. The actual contrast must follow the calculated values. These examples do not establish the typical game in each category.

## Rubric and implementation

15 proposed chart instances. The original eight advanced types remain: heatmap, network, box plot, treemap, dot map, proportional-symbol map, choropleth and parallel coordinates. The extra rank heatmap repeats an existing advanced type; it is not a ninth advanced idiom. Basic types are line, bar, scatterplot, grouped bar and dot plot. The three maps have distinct geographic questions and encodings. Similar grouped bars or heatmaps may be assessed as a series and count as one chart. Therefore do not equate 15 instances with 15 guaranteed rubric-counted charts, or adding charts with a guaranteed grade. Effective design and the final count require review.

Use Vega-Lite for charts it supports naturally. Use Vega for the network and parallel coordinates if needed; both libraries are allowed. Chart complexity is not a reason to introduce another unapproved chart library.

Present this as one scrolling page with five clear sections. Give each graph one sentence explaining what to read and, after analysing the data, one supported takeaway. Use simple explanations of mechanics and complexity. Add interaction only where useful: publication-period controls, mechanic selection, map tooltips and highlighting individual game profiles. Keep the historical ranking section visually labelled and distinguish the countries of users from the countries of publishers.

DV1 feedback revision, 7 October 2026: use one consistent two-column grid with shared margins and gutter; full-width charts 1, 6, 9, 10 and 11, with the remaining charts in equal-width pairs: 2/3, 4/5, 7/8, 12/13 and 14/15. Use a serif main title, short paragraph lines and selective annotations that do not obscure marks. Reserve ranking colours consistently: Global purple, Malaysia orange, Australia blue. See planning/DV1_FEEDBACK_ACTIONS.md for explicit marker comments versus our design choices and planning/hand-drawn-layout-map-v4.png for the revised illustrative sketch.

Do not finalise findings, map coverage or definitive takeaway headlines before cleaning, checking geography and calculating summaries. Keep final browser downloads below a few megabytes using chart-specific summaries.

## New class-material revision

The latest plan still has 15 chart instances; the 8 October map revision below changes charts 9–10. Dragging across years in chart 1 filters mechanics charts 2–3; the overview line remains visible. Publisher maps 8–9 share a publication-decade control, with reset and explicit equal-dot and no/insufficient-data legends. Historical community map 10 has its own circle-area legend. Selecting a game in chart 11 highlights that same game in chart 13, using one consistent BGG complexity value across lists. Chart 15 supports line highlighting and explicitly labels maximum players and minimum age. See planning/CLASS_CONTENT_UPDATES.md for data preparation, implementation and validation details, and FINAL_GRAPH_LIST.md for the simple final list.

## Map revision, 8 October 2026

The former publisher-country game-count map is removed because it repeated the publisher geography story. The former cooperative-share map moves from 10 to 9 and stays in section 3. New chart 10 maps BGG rating contributors by country and opens section 4. The three geographic questions now concern publisher locations, cooperative design shares, and the size of historical rating communities. No new external dataset is required.
