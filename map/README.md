# Map and geodata

- `data/cooum-river-model.geojson`: all 64 features (river line, restoration stretch, pilot stretches, outfalls, check dams, weirs, robot docks, shops, solar strips, training walls, tank zone). Each feature has `layer`, `name`, `data` (Sourced / Estimated / Proposal (this project)), `note`, `source`, `source_url`, and sometimes `status`.
- `data/cooum-river-model.kml`: same layers for Google Earth / My Maps.
- `tools/gen.py`: generates the GeoJSON and an offline SVG map (`tools/offline-svg-map.html`) from `tools/template.html`. Run from `map/tools/`.

The river line is hand-traced through geocoded towns and bridges (about 62 km). Trace it from OpenStreetMap before any engineering use.

After regenerating, copy the GeoJSON to `docs/data/` so the website picks it up.
