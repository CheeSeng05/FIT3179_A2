/* The class pattern: a chart JSON path, then vegaEmbed('#vis', path).
 * The small helpers below add error messages, resizing and linked controls.
 * Vega handles all chart rendering; there is no application framework.
 */
const charts = [
  { id: "01", file: "01_publications", data: "publications" },
  { id: "02", file: "02_mechanics", data: "mechanics_years" },
  { id: "03", file: "03_mechanics_decades", data: "mechanics_years" },
  { id: "04", file: "04_mechanics_network", data: "network_links" },
  { id: "05", file: "05_complexity_decades", data: "complexity_decades" },
  { id: "06", file: "06_complexity_time", data: "complexity_time" },
  { id: "07", file: "07_publishers", data: "publishers" },
  { id: "08", file: "08_headquarters", data: "publisher_locations" },
  { id: "09", file: "09_cooperative_map", data: "cooperative_countries" },
  { id: "10", file: "10_community_map", data: "communities" },
  { id: "11", file: "11_rank_comparison", data: "rank_comparison" },
  { id: "12", file: "12_top20_mechanics", data: "top20_mechanics" },
  { id: "13", file: "13_top20_complexity", data: "top20_complexity" },
  { id: "14", file: "14_award_mechanics", data: "award_mechanics" },
  { id: "15", file: "15_award_profiles", data: "award_profiles_long" }
];
const views = {};

// Keep live explanations short, just like the written HTML captions.
function setExplanation(id, lines) {
  const element = document.getElementById(id);
  element.replaceChildren();
  lines.forEach(function (line, index) {
    if (index) element.appendChild(document.createElement("br"));
    element.appendChild(document.createTextNode(line));
  });
}

// Vega charts 04, 07 and 15 use an explicit plotting width.
function fitVegaChart(id) {
  if (!["04", "07", "15"].includes(id) || !views[id]) return;
  const containerWidth = document.getElementById("vis" + id).clientWidth;
  const padding = id === "15" ? 54 : 12;
  views[id].width(Math.max(200, containerWidth - padding)).runAsync();
}

async function loadChart(chart) {
  const target = "#vis" + chart.id;
  try {
    const result = await vegaEmbed(target, "js/charts/" + chart.file + ".vg.json", {
      actions: false, renderer: "svg"
    });
    views[chart.id] = result.view;
    fitVegaChart(chart.id);
  } catch (error) {
    console.error("Chart " + chart.id, error);
    const message = document.createElement("p");
    message.className = "chart-error";
    message.textContent = "Chart unavailable. Open with VS Code Live Server.";
    document.querySelector(target).replaceChildren(message);
  }
}

function selectYears(selection) {
  const bounds = selection && selection.year;
  let start = bounds ? Math.ceil(bounds[0]) : 1950;
  let end = bounds ? Math.floor(bounds[1]) : 2025;
  // A very narrow brush still chooses one whole publication year.
  if (bounds && end < start) start = end = Math.round((bounds[0] + bounds[1]) / 2);
  document.getElementById("year-selection").textContent = "Showing " + start + " to " + end;
  for (const id of ["02", "03"]) {
    if (views[id]) views[id].signal("start_year", start).signal("end_year", end).runAsync();
  }
}

function selectGame(id, name) {
  for (const chart of ["11", "13"]) {
    if (views[chart]) views[chart].signal("selected_game", id).runAsync();
  }
  document.getElementById("game-selection").textContent = id ? name : "No game selected";
}

function selectMapPeriod() {
  const period = document.getElementById("map-period").value;
  for (const id of ["08", "09"]) {
    if (views[id]) views[id].signal("publication_period", period).runAsync();
  }
  const eligible = cooperativeRows.filter(row => row.period === period && row.eligible_games >= 50);
  setExplanation("cooperative-coverage", [
    eligible.length + " countries meet the 50-game threshold.",
    period === "All" ? "Publication years: 1950 to 2025." : "Publication period: " + period + "."
  ]);
}

let cooperativeRows = [];
let profiles = [];

async function startPage() {
  // Independent charts load together, like the multiple-charts studio example.
  await Promise.all(charts.map(loadChart));

  if (views["01"]) {
    views["01"].addSignalListener("year_brush", function (name, value) { selectYears(value); });
  }
  document.getElementById("reset-years").addEventListener("click", function () {
    if (views["01"]) views["01"].data("year_brush_store", []).runAsync();
    selectYears(null);
  });
  if (views["11"]) {
    views["11"].addEventListener("click", function (event, item) {
      if (item && item.datum && item.datum.id) selectGame(item.datum.id, item.datum.name);
    });
  }
  document.getElementById("clear-game").addEventListener("click", function () { selectGame(0, ""); });

  const summary = await fetch("data/summary.json").then(response => response.json());
  profiles = summary.award_profiles;
  const profileMenu = document.getElementById("profile-game");
  profiles.forEach(function (game) {
    const option = document.createElement("option");
    option.value = game.id;
    option.textContent = game.name + " (" + game.award_year + ")";
    profileMenu.appendChild(option);
  });
  profileMenu.addEventListener("change", function () {
    const id = Number(profileMenu.value);
    if (views["15"]) views["15"].signal("selected_profile", id).runAsync();
    const game = profiles.find(game => game.id === id);
    setExplanation("profile-details", game ? [
      game.name + " (" + game.award_year + ").",
      "Complexity: " + game.complexity.toFixed(2) + ". Playing time: " + game.minutes + " minutes.",
      "Maximum players: " + game.max_players + ". Minimum age: " + game.min_age + "."
    ] : ["Choose a game or hover over its line.", "Each axis uses its own units and scale."]);
  });

  const csvText = await fetch("data/cooperative_countries.csv").then(response => response.text());
  cooperativeRows = vega.read(csvText, { type: "csv", parse: { eligible_games: "number" } });
  document.getElementById("map-period").addEventListener("change", selectMapPeriod);
  document.getElementById("reset-maps").addEventListener("click", function () {
    document.getElementById("map-period").value = "All";
    selectMapPeriod();
  });

  const downloads = document.getElementById("download-list");
  charts.forEach(function (chart) {
    const row = document.createElement("p");
    const label = document.createTextNode("Chart " + chart.id + ": ");
    const data = document.createElement("a");
    data.href = "data/" + chart.data + ".csv";
    data.textContent = "CSV";
    data.download = "";
    const spec = document.createElement("a");
    spec.href = "js/charts/" + chart.file + ".vg.json";
    spec.textContent = "JSON";
    row.append(label, data, document.createTextNode(" / "), spec);
    if (chart.id === "04") {
      const nodes = document.createElement("a");
      nodes.href = "data/network_nodes.csv";
      nodes.textContent = "node CSV";
      nodes.download = "";
      row.append(document.createTextNode(" / "), nodes);
    }
    downloads.appendChild(row);
  });
  // Mark ready only after all charts and controls have been initialised.
  document.body.dataset.ready = "true";
}

let resizeTimer;
window.addEventListener("resize", function () {
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(function () { ["04", "07", "15"].forEach(fitVegaChart); }, 150);
});
startPage().catch(function (error) { console.error("Page setup", error); });
