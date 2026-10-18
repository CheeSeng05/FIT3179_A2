# 

# Board Games Dataset

# 

## Overview

# 

This dataset gathers detailed information about board games from BoardGameGeek (BGG), the largest community-driven database dedicated to board games.


It is structured according to a star schema, with:


\- a central fact table `game`, containing the main characteristics of each game (year of publication, number of players, playing time, average rating, complexity, etc.)


\- satellite tables (`category`, `mechanic`, `family`, `designer`, `artist`, `publisher`) that provide complementary information and are linked to the `game` table via bridge tables


This dataset makes it possible to explore and analyze board games from different angles: popularity, complexity, game mechanics, designers, publishers, evolution over time, etc.

It can be used for statistical analyses, data visualizations, or even for training board game recommendation models.


## Tables

## `game` — fact table

|Column|Type|Description|
|-|-|-|
|id\_bgg|int|BGG primary key|
|name\_game|string|Game name|
|yearpublished|int|Year of publication|
|min\_players|int|Minimum number of players|
|max\_players|int|Maximum number of players|
|playing\_time|int|Playing time (minutes)|
|min\_age|int|Recommended minimum age|
|average\_rating|float|Average user rating|
|rank|int|BGG overall ranking|
|weight|float|Average complexity (weight)|
|description|string|Game description|

\---

## Satellite tables

Reference tables linked to `game` via bridge tables.

\---

### `category`

Reference table listing the categories associated with the games.

|Column|Type|Description|
|-|-|-|
|id\_category|int|Unique identifier of the category|
|category|string|Category name (general genre/theme)|

*Examples:* Strategy, Card Game, Wargame, Party Game

\---

### `mechanic`

Reference table listing the game mechanics used.

|Column|Type|Description|
|-|-|-|
|id\_mechanic|int|Unique identifier of the mechanic|
|mechanic|string|Mechanic name (rules/systems)|

*Examples:* Dice Rolling, Worker Placement, Deck Building

\---

### `family`

Reference table listing the game families (thematic groupings and licenses).

|Column|Type|Description|
|-|-|-|
|id\_family|int|Unique identifier of the family|
|family|string|Family name|

*Examples:* Catan, Animals: Cats, Components: Miniatures

\---

### `designer`

Reference table listing the creators and designers of the games.

|Column|Type|Description|
|-|-|-|
|id\_designer|int|Unique identifier of the designer|
|designer|string|Designer name|

*Examples:* Uwe Rosenberg, Reiner Knizia, Vital Lacerda

\---

### `artist`

Reference table listing the illustrators and graphic artists of the games.

|Column|Type|Description|
|-|-|-|
|id\_artist|int|Unique identifier of the artist|
|artist|string|Artist name|

*Examples:* Fiona Hsieh, Vincent Dutrait, Ilya Baranovsky

\---

### `publisher`

Reference table listing the publishers that released the games.

|Column|Type|Description|
|-|-|-|
|id\_publisher|int|Unique identifier of the publisher|
|publisher|string|Publisher name|

*Examples:* Asmodee, Days of Wonder, Fantasy Flight Games



## Bridge tables

The satellite tables (`category`, `mechanic`, `family`, `designer`, `artist`, `publisher`) are linked to the `game` table by a many-to-many relationship: a game can have multiple mechanics, categories, etc., and conversely a mechanic can appear in multiple games.

To represent this kind of relationship, bridge tables (or link tables) are used, named according to the format `b\_game\_[entity]` (e.g., `b\_game\_mechanic`, `b\_game\_category`...).

Each bridge table simply contains two columns:

| Column | Type | Description |

|---|---|---|

| `id\_bgg` | int | Foreign key to `game` |

| `id\_[entity]` | int | Foreign key to the corresponding satellite table |



## Data cleaning

The cleaning was performed with PySpark on the `game` table:

\- \*\*Duplicates\*\*: removal of strictly identical rows (`dropDuplicates`)

\- \*\*rank\*\*: converted to integer, then the value `0` replaced by `NULL` (no ranking available)

\- \*\*min\_player\*\*: values greater than 100 replaced by `NULL` (outliers)

\- \*\*max\_player\*\*: the value `0` replaced by `NULL`

\- \*\*average\*\*: the value `0` replaced by `NULL` (no average rating)

\- \*\*averageweight\*\*: the value `0` replaced by `NULL` (complexity not provided)

\- \*\*bayesaverage\*\*: the value `0` replaced by `NULL`

\- \*\*minage\*\*: the value `0` replaced by `NULL`, values greater than 20 years considered as outliers and replaced by `NULL`

\- \*\*minplaytime\*\*: value `0` or greater than 240 minutes replaced by `NULL`

\- \*\*maxplaytime\*\*: value `0` or greater than 360 minutes replaced by `NULL`

\- \*\*playingtime\*\*: value `0` or greater than 360 minutes replaced by `NULL`

All these rules aim to eliminate values set to `0` (absence of data coded by default by BGG) as well as unrealistic extreme values, by replacing them with `NULL` rather than deleting the affected rows.

## Data update

The pipeline allows regular data updates without requiring a full reset:

\- \*\*Incremental update (every 3 months)\*\*: retrieval of new games published on BGG since the last extraction, by identifying the missing identifiers between the last game present in the database and the latest game available on the site. This update does not refresh the dynamic values of already existing games (ranking, average ratings, etc.).

\- \*\*Full update (once a year)\*\*: re-extraction of all games already present in the database, in order to refresh data that may evolve over time (ranking, average ratings, number of votes, etc.).

\## Author

\*\*Sylvain Ballerini\*\* — Data Engineer, passionate about board games since 2015 and about data since 2020.

I make this dataset available in the hope that it can serve other board game and data enthusiasts to explore, analyze, or build projects around the BoardGameGeek universe.