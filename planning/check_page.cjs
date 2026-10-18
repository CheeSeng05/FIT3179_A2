// Development-only browser check. The website does not depend on this script.
const { chromium } = require('C:/Users/User/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs = require('fs');
const { spawn } = require('child_process');
const assert = require('assert');

(async function () {
  const server = spawn('C:/Users/User/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe',
    ['-m', 'http.server', '8003', '--bind', '127.0.0.1'], { windowsHide: true, stdio: 'ignore' });
  server.unref();
  process.on('exit', () => server.kill());
  await new Promise(resolve => setTimeout(resolve, 1000));
  const browser = await chromium.launch({ headless: true, executablePath: 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe' });
  const page = await browser.newPage({ viewport: { width: 1366, height: 900 } });
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  page.on('console', message => { if (message.type() === 'error' || message.type() === 'warning') errors.push(message.text()); });
  await page.goto('http://127.0.0.1:8003/', { waitUntil: 'networkidle' });
  await page.waitForFunction(() => document.body.dataset.ready === 'true', { timeout: 30000 });
  console.log(JSON.stringify(await page.evaluate(() => ({
    chartCount: document.querySelectorAll('.vis-container svg').length,
    failed: [...document.querySelectorAll('.chart-error')].map(element => element.parentElement.id),
    horizontalOverflow: document.documentElement.scrollWidth > innerWidth,
    charts: [...document.querySelectorAll('.vis-container')].map(element => ({ id: element.id, svg: !!element.querySelector('svg'), width: Math.round(element.getBoundingClientRect().width), svgWidth: element.querySelector('svg')?.getAttribute('width') }))
  })), null, 2));
  console.log('BROWSER ERRORS:', JSON.stringify(errors));
  assert.equal(await page.locator('.vis-container svg').count(), 15);
  assert.equal(await page.locator('.chart-error').count(), 0);
  assert.equal(await page.locator('.chart-layout').count(), 12);
  const expectedPairs = [['vis02', 'vis03'], ['vis05', 'vis06'], ['vis12', 'vis13']];
  const desktopPairs = await page.locator('.chart-row').evaluateAll(rows => rows.map(row => {
    return [...row.querySelectorAll('.vis-container')].map(chart => {
      const box = chart.getBoundingClientRect();
      return { id: chart.id, x: box.x, y: box.y, width: box.width };
    });
  }));
  console.log('RELATED PAIRS:', JSON.stringify(desktopPairs));
  assert.deepEqual(desktopPairs.map(pair => pair.map(chart => chart.id)), expectedPairs);
  for (const pair of desktopPairs) {
    assert(Math.abs(pair[0].y - pair[1].y) < 2, 'Paired plots need aligned top edges');
    assert(pair[1].x > pair[0].x + pair[0].width, 'Related charts need separate columns');
    assert(pair.every(chart => chart.width >= 550), 'Each paired figure needs readable width');
  }
  assert.equal(await page.locator('.chart-row .map-block').count(), 0, 'Maps must keep their own rows');
  assert.equal(await page.locator('#download-list a').count(), 31, 'All static CSV and JSON downloads remain available');
  assert.deepEqual(await page.locator('.role-legend-title text').evaluateAll(elements => elements.filter(element => element.textContent.includes('…')).map(element => element.textContent)), [], 'Legend headings must remain fully readable');
  const mapSizes = await page.evaluate(() => ['08', '09', '10'].map(id => {
    const container = document.getElementById('vis' + id);
    const shapes = container.querySelector('g.mark-shape.role-mark');
    return { id, width: container.clientWidth, worldWidth: shapes?.getBoundingClientRect().width,
      fullWidth: container.closest('article').classList.contains('map-block') };
  }));
  console.log('MAP SIZES:', JSON.stringify(mapSizes));
  for (const map of mapSizes) {
    assert(map.fullWidth && map.width > 1000, 'All maps must span the page');
    assert(map.worldWidth >= map.width * .85, 'The actual world geometry must fill the map');
  }
  const checkTreemap = async () => page.locator('#vis07').evaluate(container => {
    const labels = [...container.querySelectorAll('.mark-text.role-mark text')];
    const tiles = [...container.querySelectorAll('.mark-rect.role-mark path')];
    return labels.map((label, index) => {
      const a = label.getBoundingClientRect(), b = tiles[index].getBoundingClientRect();
      return { text: label.textContent, fits: a.left >= b.left && a.right <= b.right && a.top >= b.top && a.bottom <= b.bottom };
    });
  });
  const desktopLabels = await checkTreemap();
  console.log('TREEMAP LABELS:', JSON.stringify(desktopLabels));
  assert(desktopLabels.length === 12 && desktopLabels.every(label => label.fits && !label.text.includes('…')), 'All publisher labels must fit their tiles');
  assert(desktopLabels.some(label => label.text.includes('Pegasus') && label.text.includes('Spiele')));
  const bodyStyles = await page.locator('.chart-note p, .map-notes p').evaluateAll(elements => elements.map(element => ({
    colour: getComputedStyle(element).color, size: parseFloat(getComputedStyle(element).fontSize)
  })));
  assert(bodyStyles.every(style => style.colour === 'rgb(39, 49, 58)' && style.size >= 18), 'Body explanations need a consistent readable colour and size');
  const notes = await page.locator('.chart-note').evaluateAll(elements => elements.map(element => element.innerText.trim().split(/\s+/).length));
  assert(notes.every(count => count <= 22), 'Side notes must remain concise, rather than filling whitespace with prose');
  // Exercise the actual brush with pointer input, rather than only setting its signal.
  await page.locator('#vis01').scrollIntoViewIfNeeded();
  const line = await page.locator('#vis01 .mark-line path').first().boundingBox();
  await page.mouse.move(line.x + line.width * .65, line.y + 50);
  await page.mouse.down();
  await page.mouse.move(line.x + line.width * .85, line.y + 50, { steps: 12 });
  await page.mouse.up();
  await page.waitForTimeout(200);
  const years = await page.evaluate(() => [views['02'].signal('start_year'), views['03'].signal('end_year')]);
  console.log('BRUSH:', JSON.stringify(await page.evaluate(() => ({ selection: views['01'].signal('year_brush'), label: document.getElementById('year-selection').textContent }))), 'YEARS:', years, 'LINE:', line);
  assert(years[0] > 1950 && years[1] < 2025 && years[1] > years[0], 'The year brush must update both linked charts');
  await page.locator('#reset-years').click();
  assert.equal(await page.evaluate(() => views['02'].signal('start_year')), 1950);
  await page.mouse.move(line.x + line.width * .5, line.y + 50);
  await page.mouse.down();
  await page.mouse.move(line.x + line.width * .5 + 2, line.y + 50);
  await page.mouse.up();
  await page.waitForTimeout(150);
  const narrowYears = await page.evaluate(() => [views['02'].signal('start_year'), views['03'].signal('end_year')]);
  assert(narrowYears[0] <= narrowYears[1], 'A narrow brush cannot create a backwards year range');
  await page.locator('#reset-years').click();
  await page.locator('#map-period').selectOption('2010s');
  assert.deepEqual(await page.evaluate(() => [views['08'].signal('publication_period'), views['09'].signal('publication_period')]), ['2010s', '2010s']);
  await page.locator('#reset-maps').click();
  await page.locator('#vis11 .mark-rect.role-mark path').first().click({ position: { x: 20, y: 10 } });
  const selected = await page.evaluate(() => [views['11'].signal('selected_game'), views['13'].signal('selected_game')]);
  assert(selected[0] > 0 && selected[0] === selected[1], 'Selecting a rank cell must highlight matching complexity dots');
  await page.locator('#clear-game').click();
  assert.equal(await page.evaluate(() => views['13'].signal('selected_game')), 0);
  await page.locator('#vis11 .mark-text.role-mark text').first().click();
  assert.equal(await page.evaluate(() => views['13'].signal('selected_game')), selected[0]);
  await page.locator('#clear-game').click();
  const profileId = await page.locator('#profile-game option').nth(1).getAttribute('value');
  await page.locator('#profile-game').selectOption(profileId);
  assert.equal(await page.evaluate(() => views['15'].signal('selected_profile')), Number(profileId));
  assert((await page.locator('#profile-details').textContent()).includes('minutes'));
  const longProfileLines = await page.locator('#profile-details').evaluate(element => element.innerText.split('\n').filter(line => line.trim().split(/\s+/).length > 9));
  assert.deepEqual(longProfileLines, [], 'Winner explanations must use at most nine words per line');
  await page.locator('#profile-game').selectOption('0');
  console.log('PASS: year brush/reset, publisher period/reset, linked game selection/reset, award profile selection.');
  await page.screenshot({ path: 'planning/website-desktop.png', fullPage: true });
  for (let index = 0; index < 5; index++) {
    await page.locator('.story-section').nth(index).screenshot({ path: 'planning/website-section-' + (index + 1) + '.png' });
  }
  await page.locator('.page-header').screenshot({ path: 'planning/website-header.png' });
  for (const id of ['07', '08', '09', '10']) {
    await page.locator('#vis' + id).locator('xpath=ancestor::article').screenshot({ path: 'planning/website-chart-' + id + '.png' });
  }
  await page.locator('.page-footer details').first().evaluate(element => { element.open = true; });
  const longExplanations = await page.locator('p, .source-list li').evaluateAll(elements => elements
    .filter(element => element.getClientRects().length)
    .flatMap(element => element.innerText.split('\n').filter(line => line.trim().split(/\s+/).length > 9)));
  assert.deepEqual(longExplanations, [], 'Written explanations must use at most nine words per line');
  await page.locator('.page-footer details').first().evaluate(element => { element.open = false; });
  await page.locator('#data-methods').evaluate(element => { element.open = true; });
  const longMethodLines = await page.locator('#data-methods li').evaluateAll(elements => elements.flatMap(element => element.innerText.split('\n').filter(line => line.trim().split(/\s+/).length > 9)));
  assert.deepEqual(longMethodLines, [], 'Expanded methods must retain short lines too');
  await page.locator('#data-methods').evaluate(element => { element.open = false; });
  assert((await page.locator('#vis14').innerText()).includes('40.9%'), 'The cooperative winner annotation must render');
  assert((await page.locator('#vis14').innerText()).includes('10.7%'), 'The cooperative catalogue annotation must render');
  await page.setViewportSize({ width: 1024, height: 768 });
  await page.waitForTimeout(600);
  const laptopPairsStack = await page.locator('.chart-row').evaluateAll(rows => rows.every(row => {
    const articles = [...row.querySelectorAll('article')].map(article => article.getBoundingClientRect());
    return Math.abs(articles[0].x - articles[1].x) < 2 && articles[1].y > articles[0].bottom;
  }));
  assert(laptopPairsStack, 'Pairs must stack on narrower screens');
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, 'Laptop horizontal overflow');
  const laptopLabels = await checkTreemap();
  assert(laptopLabels.every(label => label.fits), 'Publisher labels must fit on laptops too');
  await page.setViewportSize({ width: 390, height: 844 });
  await page.waitForTimeout(600);
  console.log('MOBILE:', JSON.stringify(await page.evaluate(() => ({ overflow: document.documentElement.scrollWidth > innerWidth, width: document.documentElement.scrollWidth }))));
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, 'Phone horizontal overflow');
  const mobileLabels = await checkTreemap();
  console.log('MOBILE TREEMAP:', JSON.stringify(mobileLabels));
  assert(mobileLabels.every(label => label.fits), 'Publisher labels must fit on phones too');
  await page.screenshot({ path: 'planning/website-mobile.png', fullPage: true });
  await page.locator('.story-section').nth(3).screenshot({ path: 'planning/website-mobile-rankings.png' });
  await page.locator('.story-section').nth(4).screenshot({ path: 'planning/website-mobile-awards.png' });
  await page.locator('#vis11').screenshot({ path: 'planning/website-mobile-rank-chart.png' });
  await page.locator('#vis04').screenshot({ path: 'planning/website-mobile-network.png' });
  await page.locator('#vis07').screenshot({ path: 'planning/website-mobile-treemap.png' });
  assert.deepEqual(errors, [], 'Browser errors or warnings');
  fs.writeFileSync('planning/browser-errors.json', JSON.stringify(errors, null, 2));
  await browser.close();
  server.kill();
})().catch(error => { console.error(error); process.exit(1); });
