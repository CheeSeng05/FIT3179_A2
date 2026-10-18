"""Write the readable JSON chart specifications used by vegaEmbed.

This is an optional authoring helper. You can edit each saved JSON directly.
No Python or build tool is needed to view the finished page.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "js/charts"
OUT.mkdir(parents=True, exist_ok=True)
SUMMARY = json.loads((ROOT / "data/summary.json").read_text(encoding="utf-8"))
LITE = "https://vega.github.io/schema/vega-lite/v5.json"
VEGA = "https://vega.github.io/schema/vega/v5.json"
GREY = "#59636c"
INK = "#27313a"
CATALOGUE = "#167d73"
COMPLEXITY = "#965071"
# ColorBrewer BuGn: light values are low, dark values are high.
CATALOGUE_SHADES = ["#edf8fb", "#b2e2e2", "#66c2a4", "#2ca25f", "#006d2c"]
GROUPS = ["Global", "Malaysia", "Australia"]
GROUP_COLOURS = ["#7651a8", "#b65c0a", "#2674ae"]
CONFIG = {
    "font": "Arial", "background": "transparent",
    "view": {"stroke": None},
    "axis": {"labelFontSize": 14, "titleFontSize": 14, "titleFontWeight": "normal",
             "labelColor": INK, "titleColor": INK, "gridColor": "#e9ecef",
             "domain": False, "tickColor": "#d8dde0", "titlePadding": 12, "labelPadding": 7},
    "legend": {"labelFontSize": 14, "titleFontSize": 14, "titleFontWeight": "normal",
               "labelColor": INK, "titleColor": INK,
               "orient": "bottom", "padding": 12, "labelLimit": 240},
    "text": {"fontSize": 14},
}


def csv_data(name, numeric=()):
    return {"url": f"data/{name}", "format": {"type": "csv", "parse": {field: "number" for field in numeric}}}


def field(name, kind="quantitative", **options):
    return {"field": name, "type": kind, **options}


def lite(name, data, height=280):
    return {"$schema": LITE, "description": name, "width": "container", "height": height,
            "autosize": {"type": "fit", "contains": "padding"}, "data": data, "config": CONFIG}


def save(name, spec):
    (OUT / name).write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")


def tip(name, title, kind="quantitative", format=None):
    result = field(name, kind, title=title)
    if format:
        result["format"] = format
    return result


# 01: one full-period overview, with a brush that controls 02 and 03.
spec = lite("Games in this catalogue by publication year", csv_data("publications.csv", ("year", "games")), 250)
spec["params"] = [{"name": "year_brush", "select": {"type": "interval", "encodings": ["x"],
                                                         "clear": "dblclick", "zoom": False}}]
spec["encoding"] = {"x": field("year", title="Publication year", scale={"domain": [1950, 2025]}, axis={"format": "d", "grid": False}),
                      "y": field("games", title="Games in the catalogue"),
                      "tooltip": [tip("year", "Publication year", format="d"), tip("games", "Games", format=",")]}
spec["layer"] = [{"mark": {"type": "line", "color": CATALOGUE, "strokeWidth": 2}},
                   {"transform": [{"filter": f"datum.year == {SUMMARY['peak_year']}"}],
                    "mark": {"type": "point", "filled": True, "color": "#27313a", "size": 60}},
                   {"transform": [{"filter": f"datum.year == {SUMMARY['peak_year']}"}],
                    "mark": {"type": "text", "align": "right", "dx": -9, "dy": -12, "fontWeight": "bold"},
                    "encoding": {"text": {"value": f"{SUMMARY['peak_year']}: {SUMMARY['peak_games']:,} games"}}}]
spec["layer"][0]["params"] = spec.pop("params")
save("01_publications.vg.json", spec)

# 02–03: pre-counted annual rows still allow correct selected-year totals.
mechanic_data = csv_data("mechanics_years.csv", ("year", "games", "eligible_games", "order"))
range_params = [{"name": "start_year", "value": 1950}, {"name": "end_year", "value": 2025}]
range_filter = {"filter": "datum.year >= start_year && datum.year <= end_year"}
spec = lite("Ten most recorded mechanics", mechanic_data, 350)
spec["params"] = range_params
spec["transform"] = [range_filter, {"aggregate": [{"op": "sum", "field": "games", "as": "games"}], "groupby": ["mechanic"]}]
spec["mark"] = {"type": "bar", "color": CATALOGUE, "cornerRadiusEnd": 2}
spec["encoding"] = {"x": field("games", title="Games", axis={"grid": True}),
                      "y": field("mechanic", "nominal", title=None, sort="-x", axis={"labelLimit": 180}),
                      "tooltip": [tip("mechanic", "Mechanic", "nominal"), tip("games", "Games", format=",")]}
save("02_mechanics.vg.json", spec)
spec = lite("Mechanic shares by publication decade", mechanic_data, 350)
spec["params"] = range_params
spec["transform"] = [range_filter, {"filter": "datum.order < 8"},
                       {"aggregate": [{"op": "sum", "field": "games", "as": "games"},
                                      {"op": "sum", "field": "eligible_games", "as": "eligible_games"}],
                        "groupby": ["mechanic", "decade", "order"]},
                       {"calculate": "datum.eligible_games > 0 ? datum.games / datum.eligible_games : null", "as": "share"}]
spec["mark"] = {"type": "rect", "stroke": "white", "strokeWidth": 2}
spec["encoding"] = {"x": field("decade", "ordinal", title="Publication decade", axis={"labelAngle": -35}),
                      "y": field("mechanic", "nominal", title=None, sort={"field": "order"}, axis={"labelLimit": 155}),
                      "color": field("share", title="Percentage of eligible games",
                                     scale={"range": CATALOGUE_SHADES, "domain": [0, 1], "interpolate": "lab"},
                                     legend={"title": "Mechanic percentage", "format": ".0%", "gradientLength": 160, "values": [0, .5, 1]}),
                      "tooltip": [tip("mechanic", "Mechanic", "nominal"), tip("decade", "Publication decade", "ordinal"),
                                  tip("share", "Percentage", format=".1%"), tip("games", "Games", format=","),
                                  tip("eligible_games", "Games with mechanics", format=",")]}
save("03_mechanics_decades.vg.json", spec)

# 04: Vega is used for the idioms without a built-in Vega-Lite chart type.
spec = {"$schema": VEGA, "description": "Mechanics used together; strongest twelve links among eight common mechanics",
        "width": 700, "height": 340, "padding": 5, "autosize": "none", "background": "transparent",
        "signals": [{"name": "radius_x", "update": "width * (width < 500 ? 0.25 : 0.34)"},
                    {"name": "radius_y", "update": "height * 0.28"}],
        "data": [
            {"name": "nodes", **csv_data("network_nodes.csv", ("id", "games", "angle")),
             "transform": [{"type": "formula", "expr": "width/2 + radius_x*cos(datum.angle)", "as": "x"},
                           {"type": "formula", "expr": "height/2 + radius_y*sin(datum.angle)", "as": "y"}]},
            {"name": "links", **csv_data("network_links.csv", ("source", "target", "shared_games")),
             "transform": [{"type": "lookup", "from": "nodes", "key": "id", "fields": ["source"], "values": ["x", "y"], "as": ["x1", "y1"]},
                           {"type": "lookup", "from": "nodes", "key": "id", "fields": ["target"], "values": ["x", "y"], "as": ["x2", "y2"]}]}
        ], "scales": [{"name": "link_width", "type": "linear", "domain": {"data": "links", "field": "shared_games"},
                        "range": [1, 7], "zero": True}],
        "marks": [
            {"type": "rule", "from": {"data": "links"}, "encode": {"update": {
                "x": {"field": "x1"}, "y": {"field": "y1"}, "x2": {"field": "x2"}, "y2": {"field": "y2"},
                "stroke": {"value": CATALOGUE}, "strokeOpacity": {"value": .55}, "strokeWidth": {"scale": "link_width", "field": "shared_games"},
                "tooltip": {"signal": "{'Mechanic 1': datum.source_name, 'Mechanic 2': datum.target_name, 'Shared games': datum.shared_games}"}}}},
            {"type": "symbol", "from": {"data": "nodes"}, "encode": {"update": {
                "x": {"field": "x"}, "y": {"field": "y"}, "size": {"value": 160}, "fill": {"value": CATALOGUE}, "stroke": {"value": "white"},
                "tooltip": {"signal": "{'Mechanic':datum.mechanic, 'Games':datum.games}"}}, "hover": {"fill": {"value": "#222b34"}}}},
            {"type": "text", "from": {"data": "nodes"}, "encode": {"update": {
                "x": {"signal": "width/2 + (radius_x+22)*cos(datum.angle)"},
                "y": {"signal": "height/2 + (radius_y+22)*sin(datum.angle) - (sin(datum.angle) < -0.9 ? 12 : 0)"},
                "text": {"signal": "split(datum.label, '\\n')"},
                "align": {"signal": "cos(datum.angle) > 0.4 ? 'left' : cos(datum.angle) < -0.4 ? 'right' : 'center'"}, "baseline": {"value": "middle"},
                "font": {"value": "Arial"}, "fontSize": {"value": 14}, "fill": {"value": INK}}}}
        ]}
save("04_mechanics_network.vg.json", spec)

# 05: explicit quartile/whisker layers display full-data box plots without shipping every score.
spec = lite("Distribution of recorded complexity by publication decade",
            csv_data("complexity_decades.csv", ("q1", "median", "q3", "low", "high", "games")), 320)
spec["encoding"] = {"x": field("decade", "ordinal", title="Publication decade", axis={"labelAngle": -35}),
                      "tooltip": [tip("decade", "Decade", "ordinal"), tip("median", "Median", format=".2f"),
                                  tip("q1", "Lower quartile", format=".2f"), tip("q3", "Upper quartile", format=".2f"),
                                  tip("games", "Games (at least 10 complexity votes)", format=",")]}
spec["layer"] = [
    {"mark": {"type": "rule", "color": COMPLEXITY}, "encoding": {"y": field("low", title="Complexity (1 light, 5 heavy)", scale={"domain": [1, 5]}), "y2": {"field": "high"}}},
    {"mark": {"type": "bar", "size": 28, "color": "#ead6e0", "stroke": COMPLEXITY}, "encoding": {"y": field("q1"), "y2": {"field": "q3"}}},
    {"mark": {"type": "tick", "color": "#67314d", "size": 28, "thickness": 2}, "encoding": {"y": field("median")}},
    {"mark": {"type": "tick", "color": COMPLEXITY, "size": 14}, "encoding": {"y": field("low")}},
    {"mark": {"type": "tick", "color": COMPLEXITY, "size": 14}, "encoding": {"y": field("high")}}]
save("05_complexity_decades.vg.json", spec)

# 06: a reproducible sample keeps the first version responsive.
spec = lite("Complexity and recorded playing time", csv_data("complexity_time.csv", ("id", "complexity", "complexity_votes", "minutes", "year", "max_players")), 320)
spec["mark"] = {"type": "circle", "color": COMPLEXITY, "opacity": .45, "size": 27}
spec["encoding"] = {"x": field("minutes", title="Recorded playing time (minutes)", scale={"domain": [0, 360]}, axis={"grid": False}),
                      "y": field("complexity", title="Complexity (1 light, 5 heavy)", scale={"domain": [1, 5]}),
                      "tooltip": [tip("name", "Game", "nominal"), tip("year", "Publication year", format="d"),
                                  tip("minutes", "Minutes"), tip("complexity", "Complexity", format=".2f"), tip("complexity_votes", "Complexity votes", format=",")]}
save("06_complexity_time.vg.json", spec)

# 07: twelve named publishers; placeholder entries are excluded.
spec = {"$schema": VEGA, "description": "Twelve largest named publisher catalogues by game credits",
        "width": 700, "height": 400, "padding": 2, "autosize": "none", "background": "transparent",
        "data": [{"name": "tree", **csv_data("publishers.csv", ("games",)), "transform": [
            {"type": "formula", "expr": "datum.parent == '' ? null : datum.parent", "as": "parent"},
            {"type": "stratify", "key": "id", "parentKey": "parent"},
            {"type": "treemap", "field": "games", "sort": {"field": "value", "order": "descending"},
             "method": {"signal": "width < 500 ? 'binary' : 'squarify'"},
             "size": [{"signal": "width"}, {"signal": "height"}], "padding": 2}]},
                 {"name": "leaves", "source": "tree", "transform": [{"type": "filter", "expr": "!datum.children"}]}],
        "marks": [{"type": "rect", "from": {"data": "leaves"}, "encode": {"update": {
            "x": {"field": "x0"}, "x2": {"field": "x1"}, "y": {"field": "y0"}, "y2": {"field": "y1"},
            "fill": {"value": "#c4e6df"}, "stroke": {"value": "white"},
            "tooltip": {"signal": "{'Publisher':datum.publisher,'Credited games':datum.games}"}}, "hover": {"fill": {"value": "#99cfc3"}}}},
                  {"type": "text", "from": {"data": "leaves"}, "encode": {"update": {
            "x": {"signal": "(datum.x0+datum.x1)/2"},
            "y": {"signal": "(datum.y0+datum.y1)/2 - (length(split(datum.publisher, ' '))-1)*10"},
            "text": {"signal": "split(datum.publisher, ' ')"}, "align": {"value": "center"}, "baseline": {"value": "middle"},
            "lineHeight": {"value": 20}, "font": {"value": "Arial"},
            "fontSize": {"signal": "width < 500 ? 14 : 16"}, "fill": {"value": INK}}}}]}
save("07_publishers.vg.json", spec)

world = {"url": "data/world.topojson", "format": {"type": "topojson", "feature": "ne_110m_admin_0_countries"}}
base_map = {"data": world, "mark": {"type": "geoshape", "fill": "#e6e9ec", "stroke": "white", "strokeWidth": .6}}
period = [{"name": "publication_period", "value": "All"}]

# 08: the place coordinate can represent a city or region, not an exact office.
spec = lite("Recorded publisher headquarters places", csv_data("publisher_locations.csv", ("longitude", "latitude", "publisher_id")), 620)
spec["projection"] = {"type": "equalEarth"}
spec["params"] = period
spec["layer"] = [base_map, {"transform": [{"filter": "datum.period == publication_period"}],
                            "mark": {"type": "circle", "size": 40, "color": CATALOGUE, "opacity": .7, "stroke": "white", "strokeWidth": .5},
                            "encoding": {"longitude": field("longitude"), "latitude": field("latitude"),
                                         "tooltip": [tip("publisher", "Publisher", "nominal"), tip("place", "Recorded headquarters place", "nominal"), tip("country", "Publisher country", "nominal")]}}]
save("08_headquarters.vg.json", spec)

# 09: a proportion, with a minimum sample and a grey no-data base layer.
spec = lite("Cooperative game share in publisher-linked catalogues", csv_data("cooperative_countries.csv", ("share", "eligible_games", "cooperative_games")), 680)
spec["projection"] = {"type": "equalEarth"}
spec["params"] = period
spec["layer"] = [base_map, {"transform": [{"filter": "datum.period == publication_period"},
                                         {"filter": "datum.eligible_games >= 50 && isValid(datum.share)"},
                                         {"lookup": "country", "from": {"data": world, "key": "properties.ADMIN"}, "as": "geo"},
                                         {"filter": "isValid(datum.geo)"}],
                            "mark": {"type": "geoshape", "stroke": "white", "strokeWidth": .6},
                            "encoding": {"shape": field("geo", "geojson"),
                                         "color": field("share", title="Cooperative-game percentage", scale={"domain": [0, .4], "range": CATALOGUE_SHADES, "interpolate": "lab"}, legend={"title": "Cooperative games (%)", "format": ".0%", "values": [0, .1, .2, .3, .4]}),
                                         "tooltip": [tip("country", "Publisher country", "nominal"), tip("share", "Cooperative-game percentage", format=".1%"),
                                                     tip("cooperative_games", "Cooperative games", format=","), tip("eligible_games", "Eligible games", format=",")]}}]
save("09_cooperative_map.vg.json", spec)

# 10: circle area, not radius, is proportional to the contributor count.
spec = lite("Rating contributors in the historical country analysis", csv_data("communities.csv", ("num_users", "total_ratings", "longitude", "latitude")), 700)
spec["projection"] = {"type": "equalEarth"}
position = {"longitude": field("longitude"), "latitude": field("latitude")}
spec["layer"] = [base_map,
    {"transform": [{"filter": "datum.highlight == 'Other countries'"}], "mark": {"type": "circle", "color": "#8c969f", "opacity": .5, "stroke": "white", "strokeWidth": .8},
     "encoding": {**position, "size": field("num_users", title="Rating contributors", scale={"type": "linear", "domain": [0, 131718], "range": [0, 5000]}, legend={"values": [1000, 10000, 100000], "format": ",.0f"}),
                  "tooltip": [tip("country_name", "Self-reported country", "nominal"), tip("num_users", "Contributors", format=","), tip("total_ratings", "Ratings", format=",")]}},
    {"transform": [{"filter": "datum.highlight != 'Other countries'"}], "mark": {"type": "circle", "opacity": .8, "stroke": "white", "strokeWidth": 1},
     "encoding": {**position, "size": field("num_users", title="Rating contributors", scale={"type": "linear", "domain": [0, 131718], "range": [0, 5000]}, legend={"values": [1000, 10000, 100000], "format": ",.0f"}),
                  "color": field("highlight", "nominal", scale={"domain": ["Malaysia", "Australia"], "range": GROUP_COLOURS[1:]}, legend=None),
                  "tooltip": [tip("country_name", "Self-reported country", "nominal"), tip("num_users", "Contributors", format=","), tip("total_ratings", "Ratings", format=",")]}},
    {"transform": [{"filter": "datum.highlight != 'Other countries'"}, {"calculate": "datum.country_name + ': ' + format(datum.num_users, ',')", "as": "label"}],
     "mark": {"type": "text", "align": "right",
              "dx": {"expr": "datum.highlight == 'Australia' ? -12 : -8"},
              "dy": {"expr": "datum.highlight == 'Australia' ? 24 : -15"},
              "fontSize": 14, "fontWeight": "bold", "color": INK}, "encoding": {**position, "text": field("label", "nominal")}}]
save("10_community_map.vg.json", spec)

# 11: every cell states the rank; shading is only a secondary guide.
spec = lite("Selected games in three historical ranking lists", csv_data("rank_comparison.csv", ("id", "rank", "order", "local_ratings")), 400)
spec["params"] = [{"name": "selected_game", "value": 0}]
spec["encoding"] = {"x": field("group", "nominal", sort=GROUPS, title=None,
                                 axis={"orient": "top", "labelAngle": 0,
                                       "labelExpr": "width < 220 ? (datum.label == 'Malaysia' ? 'MY' : datum.label == 'Australia' ? 'AU' : datum.label) : datum.label"}),
                      "y": field("name", "nominal", sort={"field": "order"}, title=None,
                                 axis={"labelLimit": {"expr": "width < 220 ? 160 : 280"}}),
                      "tooltip": [tip("name", "Game", "nominal"), tip("group", "Ranking list", "nominal"), tip("rank_label", "Rank", "nominal"), tip("local_ratings", "Local ratings", format=",")]}
spec["layer"] = [{"mark": {"type": "rect", "strokeWidth": 2}, "encoding": {
    "color": {"condition": {"test": "isValid(datum.rank) && datum.rank > 0", "field": "rank", "type": "quantitative", "scale": {"scheme": "greys", "domain": [1, 30], "reverse": True, "clamp": True}, "legend": None}, "value": "#e6e9ec"},
    "stroke": {"condition": {"test": "datum.id == selected_game", "value": "#27313a"}, "value": "white"}}},
    {"mark": {"type": "text", "fontSize": 14}, "encoding": {"text": field("rank_label", "nominal"),
    "color": {"condition": {"test": "isValid(datum.rank) && datum.rank <= 8", "value": "white"}, "value": "#27313a"}}}]
save("11_rank_comparison.vg.json", spec)


def grouped_bars(name, source, groups, colours):
    spec = lite(name, csv_data(source, ("share", "games", "eligible_games", "order")), 320)
    spec["mark"] = {"type": "bar", "cornerRadiusEnd": 1}
    spec["encoding"] = {"x": field("share", title="Percentage of eligible games", axis={"format": ".0%"}, scale={"domain": [0, 1]}),
                          "y": field("mechanic", "nominal", sort={"field": "order", "op": "min"}, title=None, axis={"labelLimit": 150}),
                          "yOffset": field("group", "nominal", sort=groups),
                          "color": field("group", "nominal", title=None, scale={"domain": groups, "range": colours},
                                         legend={"direction": "vertical", "columns": 1, "symbolSize": 70, "rowPadding": 5}),
                          "tooltip": [tip("mechanic", "Mechanic", "nominal"), tip("group", "Group", "nominal"), tip("share", "Percentage", format=".1%"), tip("games", "Games"), tip("eligible_games", "Eligible games")]}
    return spec


spec = grouped_bars("Mechanics in the historical top-20 lists", "top20_mechanics.csv", GROUPS, GROUP_COLOURS)
# The two country-comparison plots share a labelled HTML colour key above them.
spec["encoding"]["color"]["legend"] = None
save("12_top20_mechanics.vg.json", spec)

# 13: small deterministic offsets reveal otherwise overlapping dots.
spec = lite("Complexity of games in the historical top-20 lists", csv_data("top20_complexity.csv", ("id", "complexity", "jitter", "list_rank", "complexity_votes")), 320)
spec["params"] = [{"name": "selected_game", "value": 0}]
spec["mark"] = {"type": "circle", "size": 60, "strokeWidth": 2}
spec["encoding"] = {"x": field("complexity", title="Complexity (1 light, 5 heavy)", scale={"domain": [1, 5]}, axis={"tickCount": 5}),
                      "y": field("group", "nominal", sort=GROUPS, title=None),
                      "yOffset": field("jitter", scale=None),
                      "color": field("group", "nominal", scale={"domain": GROUPS, "range": GROUP_COLOURS}, legend=None),
                      "opacity": {"condition": {"test": "selected_game == 0 || datum.id == selected_game", "value": 1}, "value": .2},
                      "stroke": {"condition": {"test": "datum.id == selected_game", "value": "#27313a"}, "value": "white"},
                      "tooltip": [tip("name", "Game", "nominal"), tip("group", "2024 ranking list", "nominal"), tip("list_rank", "Rank"), tip("complexity", "Recorded complexity", format=".2f"), tip("complexity_votes", "Complexity votes", format=",")]}
save("13_top20_complexity.vg.json", spec)

spec = grouped_bars("Award winners and the broader publication-year sample", "award_mechanics.csv", ["Award winners", "All eligible games"], ["#333e48", CATALOGUE])
# Two labels explain the cooperative comparison without labelling every bar.
spec["layer"] = [{"mark": spec.pop("mark")},
    {"transform": [{"filter": "datum.mechanic == 'Cooperative Game'"}],
     "mark": {"type": "text", "align": "left", "dx": 6, "fontSize": 14, "fontWeight": "bold"},
     "encoding": {"text": {"field": "share", "type": "quantitative", "format": ".1%"}, "color": {"value": "#27313a"}}}]
save("14_award_mechanics.vg.json", spec)

# 15: four axes have different units. Six profiles, with hover/dropdown emphasis.
metrics = ["complexity", "minutes", "max_players", "min_age"]
titles = ["Complexity", "Minutes", ["Maximum", "players"], ["Minimum", "age"]]
spec = {"$schema": VEGA, "description": "The 2024 and 2025 award-winning game profiles; separate scales for each axis",
        "width": 360, "height": 260, "padding": {"left": 35, "right": 15, "top": 45, "bottom": 20}, "autosize": "none", "background": "transparent",
        "signals": [{"name": "selected_profile", "value": 0},
                    {"name": "hover_profile", "value": 0, "on": [{"events": "@profile_line:mouseover", "update": "datum.id"}, {"events": "@profile_line:mouseout", "update": "0"}]}],
        "data": [{"name": "profiles", **csv_data("award_profiles_long.csv", ("id", "value", "order", "award_year"))}],
        "scales": [{"name": "dimension", "type": "point", "domain": metrics, "range": "width", "padding": .05}],
        "axes": [], "marks": []}
for metric, title in zip(metrics, titles):
    values = [game[metric] for game in SUMMARY["award_profiles"]]
    domain = [1, 5] if metric == "complexity" else [0, max(values)]
    spec["scales"].append({"name": metric, "type": "linear", "domain": domain, "range": "height", "zero": False, "nice": False})
    spec["axes"].append({"orient": "left", "scale": metric, "offset": {"scale": "dimension", "value": metric, "mult": -1},
                          "title": None, "grid": False, "tickCount": 4, "labelFont": "Arial", "labelFontSize": 14, "labelColor": INK, "domainColor": "#bdc5cc", "tickColor": "#bdc5cc"})
    spec["marks"].append({"type": "text", "encode": {"update": {"x": {"scale": "dimension", "value": metric}, "y": {"value": -23},
                                                    "text": {"value": title}, "font": {"value": "Arial"}, "fontSize": {"value": 14},
                                                    "align": {"value": "right" if metric == "min_age" else "left" if metric == "complexity" else "center"}, "fill": {"value": "#27313a"}}}})
spec["marks"].append({"type": "group", "from": {"facet": {"name": "series", "data": "profiles", "groupby": ["id", "name"]}},
    "marks": [{"type": "line", "name": "profile_line", "from": {"data": "series"}, "sort": {"field": "datum.order"},
               "encode": {"update": {"x": {"scale": "dimension", "field": "metric"}, "y": {"signal": "scale(datum.metric, datum.value)"},
                "stroke": {"value": "#3d4852"}, "strokeWidth": {"signal": "datum.id == selected_profile || datum.id == hover_profile ? 3 : 1.5"},
                "strokeOpacity": {"signal": "selected_profile == 0 && hover_profile == 0 || datum.id == selected_profile || datum.id == hover_profile ? 0.8 : 0.12"},
                "tooltip": {"signal": "{'Game':datum.name,'Award year':datum.award_year,'Category':datum.category}"}}}}]})
save("15_award_profiles.vg.json", spec)
print("Wrote 15 readable chart JSON files to", OUT)
