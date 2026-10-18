# Map revision: 8 October 2026

The old publisher-country game-count symbol map overlaps with the headquarters dot map. Remove it. Keep publisher headquarters as chart 8, move cooperative share to chart 9, and introduce historical BGG rating-community size as chart 10 at the beginning of the local/global section. Fifteen charts and three distinct map idioms remain.

| Chart | Question | Geography | Measure |
|---|---|---|---|
| 8: Dot map | Where are the recorded publisher headquarters? | Headquarters locations | One equal dot per verified publisher record |
| 9: Choropleth | How does cooperative design share differ across publisher-linked catalogues? | Publisher country | Percentage of eligible games with Cooperative Game mechanic |
| 10: Proportional symbols | How big are the country samples behind the historical rankings? | Self-reported user country | Number of rating contributors; circle area proportional to num_users |

New chart 10 uses an existing download: data_research/country_rankings_2024/countries.csv. The analyst's source explanation is https://analysisparalysis.games/posts/world-of-board-games/ (published 25 April 2024). It describes ratings by users who selected a country, not all BGG members or all board-game players. The exact extraction date is not established. User location is self-reported. Do not claim national popularity, current membership or national player counts.

Verified local values: Malaysia 657 users and 33,256 ratings; Australia 9,235 users and 468,659 ratings. Show those country labels directly and explain that per-game votes differ from total contributor counts. Larger country samples do not automatically make every individual game's rank reliable or remove selection bias.

community_map_candidate.csv joins uppercased country codes to the class countryInfo.csv representative coordinates. It preserves the unmodified source in data_research. Source has 216 rows: 199 positive num_users values and 17 blank counts. Coordinate join currently maps 197 positive records, including Malaysia and Australia. BQ (blank country name) and SS (South Sudan), each with one contributor, require representative coordinates before a fully covered map. Blanks are missing, not zero. Details are in community_map_join_check.json. This is a tested data candidate, not the finished chart.

Use Equal Earth, a numeric circle-area legend and neutral world context; highlight Malaysia orange and Australia blue. Large counts can overlap: draw large circles first, position local labels carefully and use hover details. Do not use a logarithmic area scale while claiming proportional area. Render missing/unmatched locations without inventing zero values. Source dates and scope stay visible.

Publication-decade controls apply only to publisher maps 8–9. Chart 10 is static historical country-sample data. Place charts 7/8 side by side, chart 9 full width at the end of section 3, chart 10 full width at the start of section 4, followed by rank chart 11 and paired charts 12/13. Other sections remain unchanged.

The previous v3 drawing is superseded by planning/hand-drawn-layout-map-v4.png. This change replaces a repeated publishing-count question with a people-and-evidence question, rather than inventing flow data or merely changing the old map's appearance.
