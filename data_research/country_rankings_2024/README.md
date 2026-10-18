# Malaysia, Australia and global ranking candidates

Downloaded and inspected 7 October 2026.

## Sources and dates

Country analysis by Markus Shepherd / Recommend.Games, published 25 April 2024:
https://analysisparalysis.games/posts/world-of-board-games/

Direct files:
- https://analysisparalysis.games/posts/world-of-board-games/rankings/my.csv
- https://analysisparalysis.games/posts/world-of-board-games/rankings/au.csv
- https://analysisparalysis.games/posts/world-of-board-games/countries.csv

Published calculation code inspected:
https://gitlab.com/recommend.games/blog/-/blob/master/experiments/rankings_by_country/Rankings%20per%20country.py

Historical global BGG ranking, 25 April 2024, archived by beefsack:
https://github.com/beefsack/bgg-ranking-historicals/blob/master/2024-04-25.csv

Publication of the country analysis in April 2024 is verified. The precise observation/extraction date of its underlying ratings is not established by these CSVs or inspected calculation code. The global snapshot is explicitly dated 25 April 2024. These are close-period historical comparison candidates, not proof that all three populations were measured at the exact same instant. Do not present this comparison as 2026 rankings.

## What was verified

- malaysia.csv: 787 records. Columns: country_code, rank, bgg_id, name, year, avg_rating, bayes_rating, num_ratings.
- australia.csv: 2,642 records, with the same columns.
- countries.csv: 216 country/statistics records, including 657 Malaysian BGG users with 33,256 ratings and 9,235 Australian users with 468,659 ratings.
- User country is self-reported in BGG profiles, not independently verified residency or nationality.
- These are ratings-based rankings computed by the analyst, not official BGG country leaderboards or national sales/popularity rankings.
- The code joins user-country information to individual BGG ratings. It adds dummy ratings of 5.5, with the dummy count equal to all country ratings / 10,000. Games must have at least min(3 * dummy count, 30) ratings, and a country needs at least 10,000 total ratings. Malaysia therefore has a minimum of 10 actual ratings per included game; Australia has 30. Different evidence thresholds and sample sizes affect comparisons.
- For Malaysia, the highest-ranked War of the Ring: Second Edition has 18 ratings; Australia’s highest-ranked Pandemic Legacy: Season 1 has 1,063 ratings. Show vote counts and explain uncertainty; do not treat ranks as nationally representative preferences.

## Prepared comparison

comparison_candidate.csv joins by BGG game ID. It has 2,663 unique games appearing in at least one country ranking; 2,611 are found in the historical global file. Missing ranks remain blank, not zero or last place. Missing country rank can mean insufficient ratings, rather than that residents dislike or do not play a game.

The comparison has global rank, Malaysia rank, Australia rank, local vote counts, local average ratings and local adjusted ratings. It is a research join, not a final filtered chart dataset. The unmodified source files are preserved alongside it.

Verified examples:
| Game | Global 25 April 2024 | Malaysia country file | Australia country file |
|---|---:|---:|---:|
| Brass: Birmingham | 1 | 6 | 3 |
| Pandemic Legacy: Season 1 | 2 | 4 | 1 |
| Gloomhaven | 3 | 14 | 2 |
| Ark Nova | 4 | 25 | 8 |
| Twilight Imperium: Fourth Edition | 5 | 19 | 4 |

## Useful chart ideas

1. Rank-comparison slope/bump chart: Global → Malaysia → Australia for a clearly selected small group of games. These are populations, not chronological time points. Use rank 1 at the top, exact labels and vote counts in tooltips. Its advanced/basic rubric classification should be checked; do not automatically count it as advanced merely because rank is on the axis.
2. Rank heatmap: the union of the top five games from each list, with three columns and neutral cells for unavailable ranks. Declare the selection rule and keep the display small.
3. Local-versus-global mechanics comparison: join country top-N game IDs to main BGG mechanic links, compare mechanic percentages among each chosen top-N set. Mechanics from the 2026 catalogue applied to 2024 ranked games are current recorded metadata, not necessarily their 2024 labels.

Do not replace the existing 2026 main dataset with these files. Use 2026 for broader catalogue analysis and an explicitly historical 2024 panel for local/global ranks. Alternatively, refreshing country rankings requires fresh individual rating and user-country data plus a documented calculation; the existing 2026 game table alone cannot calculate country ranks.

## Other source considered

https://rascasse.com/explore/my/top/subtype/board-game offers estimated search-audience rankings dated 18 August 2026. This measures search interest, not ratings or sales; entries include loosely categorised activities, and an equally verified Australian list was not obtained. It was not chosen for a like-for-like ratings comparison.

Attribute BGG for the original ratings, Markus Shepherd / Recommend.Games for the country calculations, and beefsack for the global archive. Check underlying source use and attribution before public publication. Do not reuse the author's chart graphics; build original Vega/Vega-Lite charts from the data.
