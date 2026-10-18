"""Prepare small chart tables from the downloaded sources.

Run this once when the source data changes. The webpage itself only needs
HTML, CSS, JavaScript and the prepared CSV files in data/.
"""

import csv
import json
import math
import random
import re
import shutil
import textwrap
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data_research"
OUT = ROOT / "data"
OUT.mkdir(exist_ok=True)


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def number(value):
    try:
        result = float(value)
        return result if math.isfinite(result) else None
    except (ValueError, TypeError):
        return None


def save_csv(name, rows):
    assert rows, f"No data prepared for {name}"
    with (OUT / name).open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def decade(year):
    return "2020–2025" if year >= 2020 else f"{year // 10 * 10}s"


def quantile(values, fraction):
    position = (len(values) - 1) * fraction
    low = int(position)
    high = math.ceil(position)
    return values[low] + (values[high] - values[low]) * (position - low)


# 1. Keep base games and completed publication years.
games = {}
for row in read_csv(SOURCE / "bgg_2026/games_core_candidate.csv"):
    year = number(row["yearpublished"])
    if row["game_type"] == "boardgame" and year and 1950 <= year <= 2025:
        game_id = int(row["id_bgg"])
        games[game_id] = {
            "id": game_id, "name": row["name_game"], "year": int(year),
            "complexity": number(row["averageweight"]),
            "complexity_votes": number(row["numweights"]) or 0,
            "minutes": number(row["playingtime"]),
            "max_players": number(row["max_player"]),
            "min_age": number(row["minage"]),
        }

year_counts = Counter(game["year"] for game in games.values())
save_csv("publications.csv", [{"year": year, "games": year_counts[year]}
                              for year in range(1950, 2026)])

# 2–4. Mechanics are many-to-many: a game can have several mechanics.
mechanic_names = {int(row["id_mechanic"]): row["mechanic"]
                  for row in read_csv(SOURCE / "bgg_2026/mechanic.csv")}
game_mechanics = defaultdict(set)
for row in read_csv(SOURCE / "bgg_2026/b_game_mechanic.csv"):
    game_id, mechanic_id = int(row["id_bgg"]), int(row["id_mechanic"])
    if game_id in games and mechanic_id in mechanic_names:
        game_mechanics[game_id].add(mechanic_id)
mechanic_counts = Counter(mid for mids in game_mechanics.values() for mid in mids)
top_mechanics = [mid for mid, count in mechanic_counts.most_common(10)]
eligible_years = Counter(games[gid]["year"] for gid in game_mechanics)
mechanic_years = Counter((games[gid]["year"], mid)
                        for gid, mids in game_mechanics.items() for mid in mids)
save_csv("mechanics_years.csv", [
    {"year": year, "decade": decade(year), "mechanic": mechanic_names[mid],
     "order": order, "games": mechanic_years[year, mid],
     "eligible_games": eligible_years[year]}
    for order, mid in enumerate(top_mechanics)
    for year in range(1950, 2026)
])

# A fixed circular layout keeps this first network easy to read and reproduce.
network_ids = top_mechanics[:8]
short_names = {"Deck, Bag, and Pool Building": "Deck / bag building",
               "Variable Player Powers": "Player powers",
               "Cooperative Game": "Cooperative play"}
nodes = [{"id": index, "mechanic": mechanic_names[mid],
          "label": "\n".join(textwrap.wrap(short_names.get(mechanic_names[mid], mechanic_names[mid]), 10, break_long_words=False)),
          "games": mechanic_counts[mid], "angle": 2 * math.pi * index / 8}
         for index, mid in enumerate(network_ids)]
pairs = Counter(pair for mids in game_mechanics.values()
                for pair in combinations(sorted(set(network_ids) & mids), 2))
links = [{"source": network_ids.index(a), "target": network_ids.index(b),
          "shared_games": count,
          "source_name": mechanic_names[a], "target_name": mechanic_names[b]}
         for (a, b), count in pairs.most_common(12)]
save_csv("network_nodes.csv", nodes)
save_csv("network_links.csv", links)

# 5–6. A stated vote threshold limits very sparsely rated complexity scores.
complex_games = [game for game in games.values()
                 if game["complexity"] is not None
                 and 1 <= game["complexity"] <= 5
                 and game["complexity_votes"] >= 10]
by_decade = defaultdict(list)
for game in complex_games:
    by_decade[decade(game["year"])].append(game["complexity"])
boxes = []
for label, values in sorted(by_decade.items()):
    values.sort()
    q1, median, q3 = [quantile(values, fraction) for fraction in (.25, .5, .75)]
    inside = [value for value in values if q1 - 1.5 * (q3-q1) <= value <= q3 + 1.5 * (q3-q1)]
    boxes.append({"decade": label, "q1": q1, "median": median, "q3": q3,
                  "low": min(inside), "high": max(inside), "games": len(values)})
save_csv("complexity_decades.csv", boxes)
scatter_pool = [game for game in complex_games
                if game["minutes"] and 0 < game["minutes"] <= 360]
scatter = random.Random(3179).sample(sorted(scatter_pool, key=lambda g: g["id"]),
                                   min(1200, len(scatter_pool)))
save_csv("complexity_time.csv", scatter)

# 7. Count distinct publisher-game credits, not exclusive market shares.
publisher_names = {int(row["id_publisher"]): row["publisher"]
                   for row in read_csv(SOURCE / "bgg_2026/publisher.csv")}
publisher_games = defaultdict(set)
for row in read_csv(SOURCE / "bgg_2026/b_game_publisher.csv"):
    game_id, publisher_id = int(row["id_bgg"]), int(row["id_publisher"])
    if game_id in games and publisher_id in publisher_names:
        publisher_games[publisher_id].add(game_id)
ranked_publishers = sorted([pid for pid in publisher_games if not publisher_names[pid].startswith("(")],
                           key=lambda p: (-len(publisher_games[p]), p))
tree = [{"id": "root", "parent": "", "publisher": "All credits", "games": 0}]
tree += [{"id": str(pid), "parent": "root", "publisher": publisher_names[pid],
          "games": len(publisher_games[pid])} for pid in ranked_publishers[:12]]
save_csv("publishers.csv", tree)

# 8–9. Join known publishers to recorded geography, excluding ambiguous countries.
centres = read_csv(ROOT / "class_content/3_choropleth_map/data/countryInfo.csv")
country_codes = {row["name"]: row["country"] for row in centres}
country_codes.update({"United States": "US", "United Kingdom": "GB",
                      "Czechia": "CZ", "Czech Republic": "CZ", "South Korea": "KR",
                      "People's Republic of China": "CN", "China": "CN",
                      "Republic of China": "TW", "Taiwan": "TW", "Russia": "RU"})
world_path = ROOT / "class_content/3_choropleth_map/js/ne_110m_admin_0_countries.topojson"
world = json.loads(world_path.read_text(encoding="utf-8"))
admin_by_code = {geo["properties"]["ISO_A2"]: geo["properties"]["ADMIN"]
                 for geo in world["objects"]["ne_110m_admin_0_countries"]["geometries"]}
admin_by_code.update({"FR": "France", "NO": "Norway"})
shutil.copyfile(world_path, OUT / "world.topojson")
geography = defaultdict(list)
for row in read_csv(SOURCE / "publisher_geography_candidate.csv"):
    pid = number(row["bggPublisherId"])
    if pid is not None and int(pid) in publisher_games:
        geography[int(pid)].append(row)
periods = ["All"] + [f"{year}s" for year in range(1950, 2020, 10)] + ["2020–2025"]
country_game_sets = defaultdict(set)
hq_rows = []
ambiguous_countries = 0
for pid, locations in geography.items():
    countries = {row["countryLabel"] for row in locations if row["countryLabel"]}
    if len(countries) != 1:
        ambiguous_countries += 1
        continue
    country = next(iter(countries))
    code = country_codes.get(country)
    if code not in admin_by_code:
        continue
    admin = admin_by_code[code]
    points = {(row["hqLabel"], row["coordinate"]) for row in locations if row["coordinate"]}
    for game_id in publisher_games[pid]:
        country_game_sets[admin].add(game_id)
    # Do not choose an arbitrary point when the source has multiple HQ records.
    if len(points) == 1:
        place, coordinate = next(iter(points))
        match = re.fullmatch(r"Point\(([-\d.]+) ([-\d.]+)\)", coordinate)
        if match:
            lon, lat = map(float, match.groups())
            if -180 <= lon <= 180 and -90 <= lat <= 90:
                represented = {"All"} | {decade(games[gid]["year"]) for gid in publisher_games[pid]}
                for period in periods:
                    if period in represented:
                        hq_rows.append({"publisher_id": pid, "publisher": publisher_names[pid],
                                        "place": place, "country": country, "longitude": lon,
                                        "latitude": lat, "period": period})
save_csv("publisher_locations.csv", hq_rows)
country_shares = []
for admin, ids in sorted(country_game_sets.items()):
    for period in periods:
        eligible = {gid for gid in ids if game_mechanics.get(gid)
                    and (period == "All" or decade(games[gid]["year"]) == period)}
        cooperative = sum(2023 in game_mechanics[gid] for gid in eligible)
        country_shares.append({"country": admin, "period": period, "eligible_games": len(eligible),
                               "cooperative_games": cooperative,
                               "share": round(cooperative / len(eligible), 6) if len(eligible) >= 50 else ""})
save_csv("cooperative_countries.csv", country_shares)

# 10. Historical contributor counts are separate from publisher geography.
community = read_csv(ROOT / "planning/map_revision/community_map_candidate.csv")
save_csv("communities.csv", [{**row, "highlight": row["country_name"]
                              if row["country_code"] in ("MY", "AU") else "Other countries"}
                             for row in community])

# 11–13. Keep list membership in 2024, metadata in the later BGG dataset.
rank_dir = SOURCE / "country_rankings_2024"
comparison = {int(row["bgg_id"]): row for row in read_csv(rank_dir / "comparison_candidate.csv")}
list_ids = {}
local_votes = {}
for group, filename in [("Malaysia", "malaysia.csv"), ("Australia", "australia.csv")]:
    rows = sorted(read_csv(rank_dir / filename), key=lambda r: int(r["rank"]))[:20]
    list_ids[group] = [int(row["bgg_id"]) for row in rows]
    for row in rows:
        local_votes[group, int(row["bgg_id"])] = int(row["num_ratings"])
global_rows = sorted([row for row in read_csv(rank_dir / "global_2024-04-25.csv")
                      if number(row["Rank"]) and float(row["Rank"]) > 0],
                     key=lambda row: int(row["Rank"]))[:20]
list_ids["Global"] = [int(row["ID"]) for row in global_rows]
rank_ids = sorted(set(gid for ids in list_ids.values() for gid in ids[:5]),
                  key=lambda gid: (number(comparison[gid]["global_rank_2024_04_25"]) or 999999, gid))
rank_fields = {"Global": "global_rank_2024_04_25", "Malaysia": "malaysia_rank", "Australia": "australia_rank"}
rank_table = []
for order, gid in enumerate(rank_ids):
    for group, field in rank_fields.items():
        row = comparison[gid]
        rank = number(row[field])
        votes = row.get(group.lower() + "_num_ratings", "")
        rank_table.append({"id": gid, "name": row["name"], "group": group, "order": order,
                           "rank": int(rank) if rank else "", "rank_label": str(int(rank)) if rank else "—",
                           "local_ratings": votes})
save_csv("rank_comparison.csv", rank_table)
selected_mechanics = Counter(mid for ids in list_ids.values()
                             for gid in ids for mid in game_mechanics.get(gid, set()))
compare_ids = [mid for mid, count in selected_mechanics.most_common(6)]
top_bars = []
top_dots = []
for group in ("Global", "Malaysia", "Australia"):
    ids = list_ids[group]
    eligible = [gid for gid in ids if game_mechanics.get(gid)]
    for order, mid in enumerate(compare_ids):
        count = sum(mid in game_mechanics[gid] for gid in eligible)
        top_bars.append({"group": group, "mechanic": mechanic_names[mid], "order": order,
                         "games": count, "eligible_games": len(eligible), "share": count / len(eligible)})
    for index, gid in enumerate(ids):
        game = games.get(gid)
        if game and game["complexity"] and 1 <= game["complexity"] <= 5 and game["complexity_votes"] >= 10:
            top_dots.append({"id": gid, "name": game["name"], "group": group,
                             "complexity": game["complexity"], "complexity_votes": game["complexity_votes"],
                             "jitter": ((gid * 17) % 9 - 4) * 2, "list_rank": index + 1})
save_csv("top20_mechanics.csv", top_bars)
save_csv("top20_complexity.csv", top_dots)

# 14–15. Winner means winner=1, with no special award, through 2025.
awards = []
for category, filename in [("General", "sdj_candidate.csv"), ("Experienced", "ksdj_candidate.csv"),
                           ("Children", "kindersdj_candidate.csv")]:
    for row in read_csv(SOURCE / filename):
        gid = int(row["bgg_id"])
        if row["winner"] == "1" and not row["sonderpreis"] and int(row["jahrgang"]) <= 2025 and gid in games:
            awards.append({**games[gid], "category": category, "award_year": int(row["jahrgang"])})
wider = {gid for gid, game in games.items() if game["year"] >= 2011 and game_mechanics.get(gid)}
winners = {game["id"] for game in awards if game["year"] >= 2011 and game_mechanics.get(game["id"])}
award_ids = [mid for mid, count in Counter(mid for gid in wider for mid in game_mechanics[gid]).most_common(6)]
award_bars = []
for group, ids in [("All eligible games", wider), ("Award winners", winners)]:
    for order, mid in enumerate(award_ids):
        count = sum(mid in game_mechanics[gid] for gid in ids)
        award_bars.append({"group": group, "mechanic": mechanic_names[mid], "order": order,
                           "games": count, "eligible_games": len(ids), "share": count / len(ids)})
save_csv("award_mechanics.csv", award_bars)
profiles = []
for category in ("General", "Experienced", "Children"):
    eligible = [game for game in awards if game["category"] == category
                and all(game[field] is not None and game[field] > 0
                        for field in ("complexity", "minutes", "max_players", "min_age"))]
    profiles += sorted(eligible, key=lambda game: (-game["award_year"], game["id"]))[:2]
save_csv("award_profiles.csv", profiles)
save_csv("award_profiles_long.csv", [
    {"id": game["id"], "name": game["name"], "category": game["category"],
     "award_year": game["award_year"], "metric": metric, "value": game[metric], "order": index}
    for game in profiles for index, metric in enumerate(("complexity", "minutes", "max_players", "min_age"))
])

# Summaries also supply truthful annotations and the page's methodology notes.
peak_year = max(year_counts, key=year_counts.get)
cooperative_mid = 2023
summary = {
    "prepared_date": "2026-10-10", "core_games": len(games),
    "games_with_mechanics": len(game_mechanics), "complexity_games": len(complex_games),
    "scatter_pool": len(scatter_pool), "scatter_sample": len(scatter),
    "peak_year": peak_year, "peak_games": year_counts[peak_year],
    "top_mechanic": mechanic_names[top_mechanics[0]], "top_mechanic_games": mechanic_counts[top_mechanics[0]],
    "publishers": len(publisher_games), "mapped_country_games": len(set().union(*country_game_sets.values())),
    "mapped_publishers": len({row["publisher_id"] for row in hq_rows}),
    "country_count": len(country_game_sets), "ambiguous_publishers_excluded": ambiguous_countries,
    "cooperative_map_countries_all": sum(row["period"] == "All" and row["share"] != "" for row in country_shares),
    "country_records": len(community), "unmatched_community_records": 2, "missing_community_counts": 17,
    "award_winners": len(winners), "award_wider_games": len(wider),
    "award_profiles": profiles, "top20_samples": {group: sum(row["group"] == group for row in top_dots)
                                                  for group in list_ids},
    "network_strongest": links[0],
}
(OUT / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps({key: value for key, value in summary.items() if key != "award_profiles"}, indent=2))
print("Prepared chart data in", OUT)
