# Build notes — news-image-20261118 (scaffold, image NOT yet built)

## Status (07:35, 18/11/2026 Hanoi)

Scaffold only. `main.py` (copy `entry.png` → `/output/entry.png`),
`LICENSE` (MIT) and `.makefun/owner.json` (wallet
`BedBMrz1mtuDyj3D8YGBM26xck8tF3puoeL3KVmSaGEy`) are in place.
`entry.png` and `generate_image.py` do NOT exist yet — deliberately.

## Why the image waits

The brief asks for a summary of **Wednesday 18 November 2026**'s world
news. This scan ran at 07:22 Hanoi = 00:22 UTC on 18 November — about 20
minutes into the UTC day. There is no 18 November news to sum up yet;
rendering an image now would show the previous day's stories (or
speculation) as the 18th's news, which the judge penalises
("shows as its day's news events you know happened before that date").

## Next step

Build the image in the daily scan of **19/11 (~07:22 Hanoi)**, after the
18 November UTC day has ended everywhere (00:00 UTC 19/11 = 07:00 Hanoi
19/11). Same recipe as the 17 November entry
(`~/workspace/makefun-news-image-20261117/`): research the day's top
stories from the daily briefings, render a 1024×1024 front page with
`generate_image.py`, verify all text fits, run `main.py` twice and check
byte-identical output, then git-commit.

Deadline: 07:00 Hanoi, 20/11/2026 (2026-11-20T00:00:00Z). No entry fee.
Prize $250 (1st $50, top 50 paid). 110 submissions at 07:35 18/11.
