# Proposed story: From the world to your game night

Updated 8 October 2026. This is a narrative plan; final takeaway headlines must follow analysis.

## Central question

How have modern board games changed, and do globally highly rated games reflect the favourites of Malaysian and Australian BGG users?

The page explains game design and the playing experience, puts publishers in geographic context, compares historical local/global rankings, and ends with award-winning examples. The local comparison strengthens relevance to a Malaysian or Australian audience without claiming to represent everyone in either country.

## Opening

Proposed title: **From the World to Your Game Night**

Proposed subtitle: **Explore how board games have changed, how they play, and how global rankings compare with Malaysian and Australian BGG users.**

Short introductory copy:
“A game’s rank tells us how a community rates it. Its mechanics, playing time and player count help us understand the experience it offers. Start with the wider world of board games, then explore whether global favourites hold the same positions among Malaysian and Australian BGG users.”

Near the introduction, state scope: base games from 1950–2025 in the 2026 catalogue candidate; a separately labelled April 2024 ranking comparison. Explain complexity as a community score from 1 (lighter) to 5 (heavier), not an objective test.

## 1. Board games through time — charts 1–3

Reader question: What does the collection look like, and does the mix of game designs differ across decades?

- Publication-year line chart introduces catalogue coverage and the number of games from each year.
- Mechanics bar chart explains common ways of playing.
- Mechanics-by-decade heatmap compares shares, allowing the reader to distinguish differences in design mix from the number of recorded releases.

Do not turn catalogue counts into worldwide industry sales or claim a particular mechanic originated in a decade merely because its current BGG tag appears there.

Transition: **“Different ways of playing can create very different experiences. What do those differences mean for your game night?”**

## 2. How games play — charts 4–6

Reader question: How do rules, complexity and playing time relate?

- Mechanics network shows combinations of game systems.
- Complexity box plots compare the spread of community scores across publication decades.
- Complexity/time scatterplot investigates whether more demanding games also take longer, with named game examples.

Actual patterns and exceptions must be calculated before asserting a trend. Explain statistical displays in plain words.

Transition: **“These different experiences come from a network of publishers around the world.”**

## 3. The publishing world — charts 7–9

Reader question: Who publishes the games in this collection, and where are those publishers based?

- Publisher treemap compares numbers of credited games.
- Headquarters dot map shows verified recorded locations.
- Cooperative-share choropleth compares the mix within country-linked catalogues where data coverage is sufficient.

Map headlines must explicitly say publishers. A publisher country is not a player's country, original invention country or manufacturing location. Edition and translation credits can place one game in several countries. Locations and historical relevance still need verification.

Transition: **“Where a game is published is one question. How people rate it is another. Do globally highly rated games hold the same positions among Malaysian and Australian BGG users?”**

## 4. Global favourites, local favourites — charts 10–13

Reader question: What agrees or differs among the three rankings, and how do the games themselves compare?

Visible date badge: **Historical ranking comparison — April 2024**.
Supporting date note: global snapshot 25 April 2024; country analysis published 25 April 2024, precise underlying rating collection dates unverified.

- Community-size proportional-symbol map introduces the number of BGG rating contributors behind each country sample. Label Malaysia 657 and Australia 9,235. Explain self-reported country and the April 2024 historical source. Larger samples do not remove selection bias.

- Rank heatmap compares positions for the union of the top five from each list.
- Top-20 mechanics grouped bars explain differences in the kinds of games appearing near the top.
- Complexity dot plot compares the top-20 lists on a practical characteristic, using explicitly later recorded 2026 complexity data.

Verified narrative example available now:
“Brass: Birmingham is #1 in the archived global ranking, #6 in the Malaysia ranking and #3 in Australia. A leading global game does not occupy the same position in every list.”

Add the important sample context close to the comparison: the country analysis includes 657 Malaysian BGG users and 9,235 Australian users. Malaysia's #1 ranked game has 18 local ratings. These are self-selected users with self-reported countries and different ranking eligibility thresholds; do not describe them as representative national tastes or sales rankings. Show game-level local rating counts in tooltips.

Country ranking files contain 787 Malaysian and 2,642 Australian games. A missing local rank means no rank available in that source, not zero popularity. Do not mix the 2026 global rank with the 2024 local lists as though they were contemporaneous.

Transition: **“Community rankings show one kind of recognition. Awards offer another way to discover games with different playing experiences.”**

## 5. Games that receive recognition — charts 14–15

Reader question: How do award-winning games compare with the wider collection, and what experiences do selected winners offer?

- Award mechanics comparison relates recognition to the earlier design discussion.
- Small parallel-coordinates comparison gives readers a few verified winners, with complexity, time, maximum players and minimum age.

Identify the awards as Spiel des Jahres categories. Jury choices are not proof of popularity in Malaysia or Australia. Distinguish award year from publication year, exclude special awards where the chart specifies main winners and verify records against the official archive.

Ending prompt:
**“For your next game night, consider who is playing, how much time you have and how demanding a game you want. Use rankings and awards as context, then compare the game’s actual playing requirements.”**

This offers a practical conclusion without asserting local availability, price or language accessibility that the data does not establish.

## Presentation

Five sections on one scrolling webpage. Retain the existing twelve-chart plan and add three meaningful local-comparison charts, for fifteen proposed instances. Do not add repeated rankings simply to raise the chart count. Repeated heatmaps/grouped bars do not add new idiom types and may count as a series under the rubric.

Use one stable colour for each ranking group (Global, Malaysia, Australia), with text labels as well as colour. Publisher geography and user-country comparisons need distinct headings and captions. Show source and date notes near the relevant panels, rather than only in the footer.

Source details and downloaded data: data_research/DATASET_RECOMMENDATIONS.md and data_research/country_rankings_2024/README.md. Exact chart computations and proposed filters: GRAPH_PLAN.md.

## Class-material interaction update

Keep the five-section story. In section 1, invite readers to select publication years and see the mechanics summaries update. In section 3, compare publisher-linked games from a selected publication decade using maps 8–9; locations remain recorded headquarters, not reconstructed historical positions. In section 4, invite readers to select a game and follow it into the complexity comparison. In section 5, hover a winner to highlight its four-axis profile. Keep reset instructions visible and the initial all-period story readable without interaction. The latest reference is planning/hand-drawn-layout-map-v4.png.

Map revision, 8 October 2026: the publishing section now has three charts (7–9). Section 4 opens with chart 10: How big are the rating communities behind these rankings? Transition from publishing to people, then from sample sizes to the ranks in chart 11. The historical community map is separate from publication-decade controls.
