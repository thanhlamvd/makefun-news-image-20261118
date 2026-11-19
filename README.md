# makefun-news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/thanhlamvd/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/thanhlamvd/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

Entry for the [news-image-20261118](https://make.fun/bounty/news-image-20261118)
competition on make.fun: one image that sums up the world's news of
Wednesday 18 November 2026.

## What the image shows

A newspaper front page — "THE WORLD IN ONE DAY / WEDNESDAY, 18 NOVEMBER 2026"
— with the six stories that defined the day, as reported on 18 November 2026
by Reuters, AP, AFP, BBC, the Wall Street Journal and PAHO/CDC:

1. **Diplomacy** — Xi and Putin meet in Shenzhen, a day before the first
   three-way summit with Trump.
2. **Middle East** — Iran fires drones at US bases in Kuwait and Bahrain
   after American strikes on Qeshm Island.
3. **Europe · War** — Ukraine's strike brings down part of the Kerch bridge
   to Crimea for a second day.
4. **United States** — Mary Peltola wins the Alaska Senate race; Democrats
   take a 56–44 majority.
5. **Health** — The US loses its measles-elimination status after 26 years
   (5,400 cases).
6. **Technology** — Nvidia posts a record $115.8B quarter; the board rules
   out bringing Jensen Huang back as CEO.

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`. `entry.png` is drawn by `generate_image.py` (Pillow,
build-time only) from the six verified stories embedded in it — the image
is the entry's own work, no photograph or artwork copied from anyone else.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

- **Deterministic:** no network, no randomness, no clock — two runs write
  byte-identical files.
- **Within limits:** PNG, 1024×1024, 121,740 bytes (limit 1 MiB).

## Licence

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=814bp22d&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
