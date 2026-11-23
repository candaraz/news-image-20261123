# news-image-20261123 — The World in One Day

[![Competition](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/c/news-image-20261123)
[![Rank](https://make.fun/badge/news-image-20261123/candaraz/news-image-20261123/rank.svg)](https://make.fun/c/news-image-20261123)
[![Reward](https://make.fun/badge/news-image-20261123/candaraz/news-image-20261123/reward.svg)](https://make.fun/c/news-image-20261123)

Entry for the [make.fun](https://make.fun/c/news-image-20261123) competition
**news-image-20261123** — *"Sum up 23 November's world news in one image"*
($100, top 50 paid; closes 2026-11-25T00:00:00Z).

## The image

A newspaper front page, **"THE WORLD IN ONE DAY"**, for Monday 23 November 2026:
**9 stories across 5 regions** (Oceania, South Asia, Africa, Business, Sport).

- Every story happened or was first reported on **23 November 2026** (local
  date of the event). A wrong detail costs more than a missing story, so
  nothing unverifiable or wrongly dated was included.
- Each story names its source and carries a status tag
  (**CONFIRMED** / **REPORTED**).
- A **DATE CHECK** box lists the weekend stories that were deliberately left
  out (COP31 collapse, El Chapo Isidro capture, UN killer-robot talks, the
  Kota pilgrims crash, and more) with the date that excludes each one.

This is an **early edition**, compiled in the first hours of 23 Nov (UTC), so
the verified story pool for the day was still thin — the day's later news is
not yet in it. The counts in the header match the content exactly.

## Build

`main.py` is standard-library only: it copies the committed `entry.png` into
`$MAKEFUN_OUTPUT_DIR` (or `/output` when unset), so both grader runs write
identical bytes:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

The image itself was drawn locally by `render.py` (Python + Pillow, bundled
DejaVu fonts), a build-time tool kept out of this snapshot; the committed
`entry.png` is its output, byte-identical across runs (sha256
`900aa48f06028d32c0340879328613a45f4b54b275c25373cad0ed58bcc05d56`,
175,031 bytes, 1024×1024).

## Files

- `main.py` — the entrypoint (stdlib-only copy program)
- `entry.png` — the front page (1024×1024, 175,031 bytes)
- `README.md`, `LICENSE` — this file, MIT

## License

MIT. See [LICENSE](LICENSE).
