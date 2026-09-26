# 🐥 Swarmlings

**English** ・ [繁體中文](README.zh-TW.md)

**▶ Play in your browser: https://shanchiehchiu.github.io/swarmlings/**

A pixel-art virtual-pet game that quietly turns into a civilization simulator. You find one fuzzy creature in a meadow. There is plenty of fruit and water, so it lives on its own — and multiplies. Feed, wash, play with and pet them if you like, or just watch. Give them time and they build roads, houses, farms, a market and a dock, discover fire and writing, raise generations, bury their elders… and finally raise a monument, **wake up, and start watching you**.

Single HTML file, zero dependencies, no build step. Open `index.html` and play. UI in English and Traditional Chinese (auto-detected, switch in the menu).

![demo](docs/demo.gif)

_A single creature becomes a village in about 15 seconds of time-lapse (roads, farms, seasons, generations)._

![settlement](docs/settlement.png)

| | |
|---|---|
| ![winter](docs/winter-filter.png) | ![inspect](docs/inspect.png) |

## What is in it

- **Hands-off by default.** They eat fruit, bathe, chat and reproduce without you. Your care is a bonus, not a requirement.
- **Procedural worlds.** Every game has a different map (lakes, forests, rocks, three palettes). Share one with `?seed=26`.
- **A planned settlement.** Radial + ring roads grow outward from the plaza; buildings fill the lots along them ring by ring. Landmarks sit near the plaza, farms on the outskirts, docks on the shore.
- **Seasons.** Spring blossoms, summer green, autumn leaves, winter snow and frozen lakes. Water level rises and falls with the seasons.
- **Farming that works.** Crops are sown in spring, ripen in autumn, frost in winter.
- **Buildings and jobs.** Huts, houses, campfire, farm, library, monument, well, storehouse, mill, market, dock — plus farmers and fishers.
- **Generations.** Parents, children, elders with white hair, gravestones in a graveyard, funerals.
- **Events.** Droughts, bountiful harvests, meteor showers, auroras, festivals.
- **Wildlife.** Fish in the lakes, birds in the sky, rabbits that hop away from you.
- **Inspect anything.** Click a creature, building, tree, rock, grave or animal for an info card. A **Filter** panel outlines every match (e.g. all farmers, all ripe farms).
- **World history.** A timeline of everything important that happened, with stats.
- **Terrain tool.** Plant trees, place rocks, dig ponds, fill water.
- **Achievements & records** saved in your browser, plus nine different endings.
- **Sound.** Rain, wind, birds, crickets and a seasonal pentatonic melody, all synthesized live with WebAudio (no audio files).
- **Zoom & pan** with the wheel, right-drag, pinch or keyboard. Time speeds up to 100×.
- **Everything is pixel art**, including the UI, drawn in code (only external asset: a pixel font, see below).

## Controls

| | |
|---|---|
| `1`–`6` | Feed · Wash · Play · Pet · Look · Terrain |
| `F` / `H` | Filter panel / World history |
| `Space` | Pause |
| Wheel, `+` `-`, `0` | Zoom in / out / reset |
| Right-drag, arrows, WASD | Pan |
| Menu | Music, sound, language, reset |

URL parameters: `?lang=en` · `&seed=26` · `&speed=30` · `&intro=0`

## Run locally

```
open index.html      # macOS; or just double-click the file
```

## Credits & notes

- All art, dialogue, questions and endings are original and drawn/written in code.
- Inspired by the fictional virtual-pet game in *Black Mirror* S7 "Plaything" (care → reproduce → emergent society → they start watching you). **This project is not affiliated with that show or its makers.**
- Font: [Cubic 11](https://github.com/ACh-K/Cubic-11) (SIL OFL 1.1, `tools/Cubic11-OFL.txt`). The 2.8 MB font is subset to the glyphs the game uses (~40 KB) by `tools/build-font.py` and embedded as base64 so the game stays a single offline file. After changing game text, rebuild with:

```
python3 -m venv .venv && .venv/bin/pip install fonttools brotli
.venv/bin/python tools/build-font.py
```

## License

Code: MIT (see `LICENSE`). Font: SIL OFL 1.1.
