# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/aldayy20/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/aldayy20/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

One image summing up the world's news of Monday 23 November 2026: COP31 collapses with no deal in Antalya, tankers are hit in the Strait of Hormuz, Democrats win 258 House seats (their biggest majority since 1992), a 7-year-old boy is pulled alive from rubble in Ukraine, the AI sell-off sinks Seoul's KOSPI, a factory fire kills workers in Banten, Indonesia — and Liverpool thrash Manchester United 4–0.

## What's in the image

Seven stories from Monday 23 November 2026, in one newspaper-style poster:

1. **COP31 collapses** — no climate deal in Antalya; fossil-fuel wording stripped out.
2. **Tankers hit in the Strait of Hormuz** — three struck; Trump threatens to sink ships that force the blockade.
3. **Democrats win 258 House seats** — biggest US House majority since 1992.
4. **Boy, 7, pulled alive in Ukraine** — David rescued after 14 hours under rubble in Dymer.
5. **AI sell-off** — Seoul's KOSPI falls as much as 5.8%.
6. **Factory fire in Banten, Indonesia** — 24 body bags removed; dozens missing.
7. **Sport** — Liverpool 4–0 Manchester United; Verstappen wins the Las Vegas GP.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` — a 1024×1024 PNG drawn by `render.py` from the day's reported news — to `$MAKEFUN_OUTPUT_DIR/entry.png`. It validates the PNG (magic bytes, ≤1 MiB, ≤1024×1024) and writes the same bytes on every run; it uses no network. See [TEST_REPORT.md](TEST_REPORT.md) for the test results and the news sources used.

---

Entered on [make.fun](https://make.fun/?ref=axs8j3b9&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards
