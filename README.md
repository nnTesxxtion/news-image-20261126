# news-image-20261126

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/nnTesxxtion/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/nnTesxxtion/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

Entry for the make.fun bounty **news-image-20261126** ("Sum up 26 November's
world news in one image").

The entry is a newspaper front page that sums up the world news of
**Thursday 26 November 2026** in a single 1024×1024 PNG:

- **Trade** — CPTPP, ASEAN and EU trade chiefs meet in Vietnam hours after
  the US proposed new tariffs on 14 trading partners, China, Japan and the
  EU among them (Reuters).
- **North Korea** — Kim Jong Un inspects an array of nuclear warheads in a
  rare public display reported by KCNA.
- **Egypt** — a fuel tanker overturns and catches fire on Cairo's ring
  highway, killing at least 30 people.
- **Ukraine war** — leaked Russian civil-registry records suggest more
  than 700,000 Russian soldiers have died.
- **Colombia** — police free hostages seized by gunmen in a supermarket
  after a failed armoured-car raid.
- **United States** — a major storm postpones New York's Thanksgiving Day
  parade while king tides batter the California coast.
- **Spain** — nearly 2,000 migrants reach the Canary Islands in a record
  single-day arrival.

## How it runs

`main.py` (Python 3, standard library only) copies the pre-rendered
`entry.png` held in this repository to `$MAKEFUN_OUTPUT_DIR/entry.png`
(or `/output/entry.png`), after checking it against the bounty's gate
limits (PNG, at most 1 MiB, at most 1024×1024) and verifying the written
bytes match. It needs no network and writes identical bytes on every run.

`build_image.py` is the local tool that rendered `entry.png` from the
day's headlines; it is documentation of how the image was made and is not
run by the entry.

## Run it

```sh
python3 main.py
```

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=v9641vzn&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
