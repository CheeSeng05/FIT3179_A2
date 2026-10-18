# Candidate data for planning (inspected 6 October 2026)

These are raw research candidates, not cleaned final visualisation data.

## Updated recommendation after broader search

Prefer **BGG Data Full + Wikidata publisher geography + Spiel des Jahres award history**. The initial 2,000-game dataset below is now a backup, not the preferred main source. See [DATASET_RECOMMENDATIONS.md](DATASET_RECOMMENDATIONS.md) for inspected coverage and limitations.

## Board-game data
Source: https://www.kaggle.com/datasets/chik0di/board-games-dataset-complete-features
Original filename: boardgame-geek-dataset_organized.csv
Kaggle update: 15 September 2025. This is an upload/update date, not a verified observation date.
Published collection notebook: https://github.com/chik0di/bottom_pot-archives/blob/main/BoardGameGeek/bgg.ipynb
2,000 rows; 1,991 distinct game URLs; rank_overall ranges 1–2,000. Publication years include 0 and run through 2025. This is a ranked sample, not a census of all board games. Core fields include mechanics, complexity, publication year, player limits, playing times, publishers and designers.
Clean duplicate games, invalid/unknown years and numeric values. Check scrape accuracy against original game pages before final selection. Multiple mechanics and publishers are separated by semicolons. Publishers may represent different editions or translations; do not interpret every credited publisher as the original publisher or country of game invention.

## Publisher geography
Source: https://www.wikidata.org/wiki/Wikidata:WikiProject_Board_Games
Query service: https://query.wikidata.org/
Downloaded 6 October 2026 using the query below. Includes all entities with a BGG publisher ID, not only publishers in the game CSV. Multiple countries/headquarters may produce multiple rows. No claim that every coordinate is a precise office location: some headquarters refer to cities or regions, and historical qualifiers are not included in this simple query.
Preliminary case-insensitive exact name matching: 168 unique publisher entities matched, 139 had countries, 109 had headquarters coordinates. These matches require manual/identifier verification; final coverage is not established.

```sparql
SELECT ?publisher ?publisherLabel ?bggPublisherId ?countryLabel ?hqLabel ?coordinate
WHERE {
  ?publisher wdt:P6160 ?bggPublisherId.
  OPTIONAL { ?publisher wdt:P17 ?country. }
  OPTIONAL {
    ?publisher wdt:P159 ?hq.
    OPTIONAL { ?hq wdt:P625 ?coordinate. }
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
```

Verify licenses and attribution on both sources before final publishing. Preserve a record of missing locations; never assign unverified countries. These two sources can potentially support the assignment's two-source requirement; two BGG mirrors alone would not constitute independent sources.
