# Project Cooum

A realistic, practical model to transform the **Cooum River** in Chennai, from Kesavaram anicut to the Marina mouth (about 65 km, 20 km of it inside the city).

**Interactive map:** https://neeli1628.github.io/Project-Cooum/ (once GitHub Pages is switched on, see below)

## Data labels

Every number and map feature carries one of three labels. Keep them when you add data.

| Label | Meaning |
|---|---|
| **Sourced** | From a public record, with a link |
| **Estimated** | Real thing, but the figure or position is our estimate |
| **Proposal** | This project's idea, not an existing plan |

## The 5 M's (short version)

Details and sources are in [`research/`](research/).

1. **Merits upon successful deploy.** Roughly ₹12,600 to ₹29,400 cr one-time property value uplift, plus ₹190 to ₹825 cr a year in flood losses avoided, health costs avoided and riverfront spending (estimated). A walkable riverfront, water travel, leased shops, bank-top solar (about 14 GWh a year, estimated).
2. **Money required.** ₹735 cr sanctioned for the Integrated Cooum Eco-Restoration Project (sourced, CRRT). Our recommended low-cost package (tanks, recharge wells, check-dam shutters, mouth training walls, treated water as base flow, bank solar) is about ₹180 to 250 cr over 4 years (estimated).
3. **Main causes of the current state.** Untreated sewage outfalls (118 identified in 2014, 41 plugged by Nov 2025, sourced), solid waste, almost no natural flow outside the monsoon, and a sand bar at the mouth made worse by Chennai Port's breakwaters trapping northward drifting sand.
4. **Measures needed.** Plug outfalls and divert sewage; release treated water (Koyambedu) as base flow; training walls at the mouth (~₹70 cr, proposed by WRD); shutters on upstream check dams and inflatable rubber weirs instead of a mouth dam; cleaning robots, an outfall-patrol sensor boat and a thermal drone; public monitoring and feedback.
5. **Maintenance required in future.** Periodic mouth dredging, robot fleet upkeep, sensor calibration, outfall patrols, STP operation, and a value-capture mechanism so land value gains fund upkeep.

## Repository layout

| Folder | What goes here |
|---|---|
| [`research/`](research/) | Research tracks with sources (commercial benefits; river mouth, barrage and power) |
| [`map/`](map/) | Geodata (GeoJSON, KML) and the generator script |
| [`docs/`](docs/) | The GitHub Pages site: interactive Mapbox map |
| [`plan/`](plan/) | The overall plan, phases, budget and timeline |
| [`apps/`](apps/) | Citizen and operator apps (riverfront, water travel, shop leasing) |
| [`robots/`](robots/) | Firmware and CAD for academy teams: cleaning robot, outfall-patrol sensor boat, thermal drone |
| [`monitoring/`](monitoring/) | Water quality sensors, data pipeline and dashboard |
| [`feedback/`](feedback/) | Public reporting and feedback system |
| [`learnings/`](learnings/) | Skills and topics the team needs to learn |

## Publishing the map (GitHub Pages)

Settings, Pages, Source: **Deploy from a branch**, branch `main`, folder `/docs`. Note: Pages on a **private** repository needs a paid GitHub plan (Pro or above). On a free account, make the repo public or keep using the map artifact.

The map uses a Mapbox public token. For production, create a token restricted to `https://neeli1628.github.io` at https://account.mapbox.com/access-tokens/ and replace it in `docs/index.html`.

To update map data, edit `map/tools/gen.py`, run it from `map/tools/`, and copy `map/data/cooum-river-model.geojson` to `docs/data/`.
