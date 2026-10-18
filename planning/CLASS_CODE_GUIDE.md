# Class code and this webpage

| File | Purpose | Class reference |
| --- | --- | --- |
| `index.html` | Text, chart containers, buttons, menus and source links. | Week 9 `5_multiple_charts_html/index.html`. |
| `css/styles.css` | Fonts, colours, spacing and responsive columns. | Week 9 `5_multiple_charts_html/css/styles.css`. Our column rules are custom CSS; the example uses Pure.css. |
| `js/vega_lite_vis.js` | Embed each chart and connect controls. | Week 9 `vegaEmbed(...).then(function (result) {...})`; Week 7 `events.js` for ordinary functions and event listeners. |
| `js/charts/*.vg.json` | Data paths, marks, encodings, tooltips and chart parameters. | Class Vega-Lite examples. Charts 04, 07 and 15 use Vega for their more specialised layouts. |

`loadChart` repeats one embed pattern for the fifteen entries in `charts`.
The returned `result.view` is stored in `views` by chart number.
Once every chart has loaded, `connectControls` attaches its event listeners.

The following are extensions to the examples and need understanding:

- `signal(name, value)` changes a parameter declared in a chart JSON.
- `runAsync()` asks Vega to redraw after the change.
- `addSignalListener` receives the selected year range from chart 01.
- The selected years filter charts 02 and 03.
- The publication dropdown filters maps 08 and 09 together.
- Selecting a game in chart 11 highlights its dots in 13.
- The winner dropdown highlights a profile in chart 15.
- `fitChart` changes map heights and explicit Vega widths on resize.
- `fetch` reads prepared metadata for menu options and short captions.

The chart JSON still performs filtering and rendering; JavaScript passes
control values between the separate charts. The class demo exposes
`result.view`, but does not implement these exact connections.

The layout pairs 02/03, 05/06 and 12/13 on wider screens. At 1,200 pixels
or less, CSS stacks these pairs. Maps always have their own full-width row.
Short notes sit beside single charts and below paired charts.

These references explain the implementation; they do not guarantee marks.
