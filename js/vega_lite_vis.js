/* Class examples: Week 7 events.js and Week 9 multiple-charts index.html.
 * HTML holds content; CSS handles layout; each JSON describes one chart.
 * This file uses vegaEmbed(...).then(function (result) { ... }).catch(...).
 * The class demo exposes result.view. Its signal/data/size calls below are
 * our extensions for linked charts and resizing, not copied demo code.
 */
var charts = [
  { id: "01", file: "01_publications" },
  { id: "02", file: "02_mechanics" },
  { id: "03", file: "03_mechanics_decades" },
  { id: "04", file: "04_mechanics_network" },
  { id: "05", file: "05_complexity_decades" },
  { id: "06", file: "06_complexity_time" },
  { id: "07", file: "07_publishers" },
  { id: "08", file: "08_headquarters" },
  { id: "09", file: "09_cooperative_map" },
  { id: "10", file: "10_community_map" },
  { id: "11", file: "11_rank_comparison" },
  { id: "12", file: "12_top20_mechanics" },
  { id: "13", file: "13_top20_complexity" },
  { id: "14", file: "14_award_mechanics" },
  { id: "15", file: "15_award_profiles" }
];
var views = {};
var loadedCharts = 0;

// Keep live explanations short, just like the written HTML captions.
function setExplanation(id, lines) {
  var element = document.getElementById(id);
  element.replaceChildren();
  lines.forEach(function (line, index) {
    if (index) element.appendChild(document.createElement("br"));
    element.appendChild(document.createTextNode(line));
  });
}

// Keep the actual world drawing large, not just its surrounding container.
function fitChart(id) {
  if (!views[id]) return;
  var containerWidth = document.getElementById("vis" + id).clientWidth;
  if (["08", "09", "10"].includes(id)) {
    var legendSpace = { "08": 0, "09": 0, "10": 100 }[id];
    return views[id].height(Math.round(containerWidth * 0.45) + legendSpace).runAsync();
  }
  if (["04", "07", "15"].includes(id)) {
    var padding = id === "15" ? 74 : 12;
    views[id].width(Math.max(200, containerWidth - padding));
    if (id === "07") views[id].height(containerWidth < 500 ? 780 : 520);
    return views[id].runAsync();
  }
}

// One reusable version of the studio's vegaEmbed call, used for all 15 JSONs.
function loadChart(chart) {
  var target = "#vis" + chart.id;
  var spec = "js/charts/" + chart.file + ".vg.json";
  document.querySelector(target).setAttribute("aria-busy", "true");
  return vegaEmbed(target, spec, { actions: false, renderer: "svg" }).then(function (result) {
    views[chart.id] = result.view;
    return fitChart(chart.id);
  }).then(function () {
    loadedCharts++;
  }).catch(function (error) {
    delete views[chart.id];
    console.error("Chart " + chart.id, error);
    var message = document.createElement("p");
    message.className = "chart-error";
    message.setAttribute("role", "status");
    message.textContent = "Chart unavailable. Refresh to retry.";
    document.querySelector(target).replaceChildren(message);
  }).then(function () {
    document.querySelector(target).setAttribute("aria-busy", "false");
  });
}

function selectYears(selection) {
  var bounds = selection && selection.year;
  var start = bounds ? Math.ceil(bounds[0]) : 1950;
  var end = bounds ? Math.floor(bounds[1]) : 2025;
  // A very narrow brush still chooses one whole publication year.
  if (bounds && end < start) start = end = Math.round((bounds[0] + bounds[1]) / 2);
  document.getElementById("year-selection").textContent = "Showing " + start + " to " + end;
  for (var id of ["02", "03"]) {
    if (views[id]) views[id].signal("start_year", start).signal("end_year", end).runAsync();
  }
}

function selectGame(id, name) {
  for (var chart of ["11", "13"]) {
    if (views[chart]) views[chart].signal("selected_game", id).runAsync();
  }
  document.getElementById("game-selection").textContent = id ? name : "No game selected";
  document.getElementById("game-selection-13").textContent = id ? "Selected: " + name : "No game selected";
}

function selectMapPeriod() {
  var period = document.getElementById("map-period").value;
  for (var id of ["08", "09"]) {
    if (views[id]) views[id].signal("publication_period", period).runAsync();
  }
}

var profiles = [];

function selectProfile() {
  var id = Number(document.getElementById("profile-game").value);
  if (views["15"]) views["15"].signal("selected_profile", id).runAsync();
  var game = profiles.find(function (profile) { return profile.id === id; });
  setExplanation("profile-details", game ? [
    game.name + " (" + game.award_year + ").",
    "Complexity: " + game.complexity.toFixed(2) + ". Playing time: " + game.minutes + " minutes.",
    "Maximum players: " + game.max_players + ". Recommended age: " + game.min_age + "+."
  ] : ["All six winners are shown."]);
}

// Native button/select events follow Week 7. The view calls pass their
// values to the parameters already declared in the chart JSON files.
function connectControls() {
  document.getElementById("reset-years").disabled = !views["01"];
  document.getElementById("clear-game").disabled = !views["11"];
  document.getElementById("map-period").disabled = !views["08"] && !views["09"];
  document.getElementById("reset-maps").disabled = !views["08"] && !views["09"];
  if (views["01"]) {
    views["01"].addSignalListener("year_brush", function (name, value) { selectYears(value); });
  }
  document.getElementById("reset-years").addEventListener("click", function () {
    // Clear the visual interval too, so resizing cannot restore old bounds.
    if (views["01"]) views["01"].signal("year_brush_x", []).data("year_brush_store", []).runAsync();
    selectYears(null);
  });
  if (views["11"]) {
    views["11"].addEventListener("click", function (event, item) {
      if (item && item.datum && item.datum.id) selectGame(item.datum.id, item.datum.name);
    });
  }
  document.getElementById("clear-game").addEventListener("click", function () { selectGame(0, ""); });

  var profileMenu = document.getElementById("profile-game");
  profileMenu.disabled = !views["15"] || !profiles.length;
  profileMenu.addEventListener("change", selectProfile);
  if (views["15"] && profiles.length) selectProfile();

  document.getElementById("map-period").addEventListener("change", selectMapPeriod);
  document.getElementById("reset-maps").addEventListener("click", function () {
    document.getElementById("map-period").value = "All";
    selectMapPeriod();
  });

}

// Read supporting captions from the same prepared data used by the charts.
// fetch is ordinary browser JavaScript; it is an addition to the class demo.
function startPage() {
  // Independent requests keep a missing caption from blocking the charts.
  // Promise.all extends the studio's existing then/catch embed pattern.
  var profileRequest = fetch("data/summary.json").then(function (response) {
    if (!response.ok) throw new Error("Winner details: HTTP " + response.status);
    return response.json();
  }).then(function (summary) {
    if (!Array.isArray(summary.award_profiles)) throw new Error("Winner profiles missing");
    profiles = summary.award_profiles;
  }).catch(function (error) {
    console.error("Winner details", error);
    document.getElementById("profile-details").textContent = "Winner details unavailable. Hover profiles for names.";
  });
  // Each embed handles its own error, so working views retain controls.
  var chartRequests = charts.map(loadChart);
  Promise.all(chartRequests.concat([profileRequest])).then(function () {
    connectControls();
    selectMapPeriod();
    document.body.dataset.ready = "true";
  });
}

var resizeTimer;
window.addEventListener("resize", function () {
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(function () { ["04", "07", "08", "09", "10", "15"].forEach(fitChart); }, 150);
});
// Wait for the chosen fonts before Vega measures chart labels.
document.fonts.ready.then(startPage);
