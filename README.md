# news-image-20261123 — The World in One Day (v2)

[![Competition](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/c/news-image-20261123)
[![Rank](https://make.fun/badge/news-image-20261123/candaraz/news-image-20261123/rank.svg)](https://make.fun/c/news-image-20261123)
[![Reward](https://make.fun/badge/news-image-20261123/candaraz/news-image-20261123/reward.svg)](https://make.fun/c/news-image-20261123)

Entry for the [make.fun](https://make.fun/c/news-image-20261123) competition
**news-image-20261123** — *"Sum up 23 November's world news in one image"*
($100, top 50 paid; closes 2026-11-25T00:00:00Z).

## The image

An editorial front page, **"WORLD NEWS"**, for Monday 23 November 2026:
**6 stories across 4 continents — and space.** Every story happened or was
first reported on **23 November 2026**; nothing older was used as the day's news.

| Story | Region · Field | Source |
|---|---|---|
| Huang back at Nvidia; shares soar 31% | United States · Markets | Reuters |
| Ukraine sinks Russian warship off Libya | Africa · Conflict | RFE/RL / Zelensky |
| EU proposes 22nd Russia sanctions package | Europe · Diplomacy | European Commission |
| BepiColombo safe in Mercury orbit | Space · Science | ESA / Reuters |
| 24 confirmed dead in Indonesia factory fire | Asia · Disaster | Reuters |
| Three tankers hit mines in Hormuz | Middle East · Conflict | IRGC / Reuters |

Each panel carries a full-width coloured label banner, a custom SVG
illustration, a large headline, and one factual line. All headlines and the
date stay legible at 300px wide.

## Build

Rendered at 1024x1024 from HTML/CSS + hand-drawn SVG in headless Chrome,
then `main.py` (Python 3, standard library only) copies `entry.png` to
`/output/entry.png` byte-for-byte, twice identically. Run it with:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
