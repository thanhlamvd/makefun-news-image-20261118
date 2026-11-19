#!/usr/bin/env python3
"""Render the news image for Wednesday 18 November 2026.

Build-time script (runs on the author's machine, not in the grader):
reads the six verified stories below and draws a 1024x1024 newspaper
front page to entry.png. The stories are the day's news as reported on
18 November 2026 by Reuters, AP, AFP, BBC, the Wall Street Journal and
PAHO/CDC (via the daily briefings that collected them). The entry itself
is main.py, which only copies entry.png to /output/entry.png —
deterministic, stdlib-only, no network.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (246, 241, 231)          # newsprint
NAVY = (20, 33, 61)
INK = (26, 26, 26)
GREY = (90, 90, 90)
CARD = (255, 255, 255)
LINE = (200, 192, 175)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to pixel width."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# (tag, tag colour, headline, summary, icon)
STORIES = [
    ("DIPLOMACY", (27, 94, 143),
     "Xi and Putin meet in Shenzhen",
     "China and Russia hold talks a day before the first three-way "
     "summit with Trump, on Thursday at APEC.",
     "flags"),
    ("MIDDLE EAST", (176, 106, 0),
     "Iran hits Kuwait and Bahrain",
     "Tehran says it fired drones at US bases after American strikes "
     "on Qeshm Island; Bahrain says it intercepted them.",
     "radar"),
    ("EUROPE \u00b7 WAR", (178, 34, 34),
     "Kerch bridge arch collapses",
     "Ukraine\u2019s strike brings down part of the bridge to Crimea "
     "for a second day; Russia hits back at Kyiv.",
     "bridge"),
    ("UNITED STATES", (90, 90, 90),
     "Peltola wins Alaska Senate race",
     "Mary Peltola beats Dan Sullivan; Democrats take a 56\u201344 "
     "majority in the incoming Senate.",
     "scale"),
    ("HEALTH", (46, 125, 90),
     "US loses measles-free status",
     "After 26 years, health officials say the US no longer meets "
     "elimination criteria, with 5,400 cases.",
     "chart"),
    ("TECHNOLOGY", (106, 76, 147),
     "Nvidia posts record $115.8B quarter",
     "Revenue doubles from a year ago; the board rules out bringing "
     "Jensen Huang back as chief executive.",
     "chip"),
]


def icon(draw, kind, cx, cy, r, colour):
    """Simple white glyph on a coloured disc."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=colour)
    w = (255, 255, 255)
    if kind == "bridge":
        # deck + two arches + posts
        draw.line([cx - r + 8, cy + 6, cx + r - 8, cy + 6], fill=w, width=4)
        draw.arc([cx - r + 8, cy - r + 12, cx - 4, cy + 10], 180, 360, fill=w, width=4)
        draw.arc([cx + 4, cy - r + 12, cx + r - 8, cy + 10], 180, 360, fill=w, width=4)
        draw.line([cx - r + 12, cy - r + 18, cx - r + 12, cy + 6], fill=w, width=3)
        draw.line([cx + r - 12, cy - r + 18, cx + r - 12, cy + 6], fill=w, width=3)
    elif kind == "radar":
        draw.ellipse([cx - r + 10, cy - r + 10, cx + r - 10, cy + r - 10],
                     outline=w, width=3)
        draw.line([cx, cy, cx + r - 12, cy - r + 16], fill=w, width=3)
        draw.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=w)
        draw.ellipse([cx + r - 18, cy - r + 12, cx + r - 10, cy - r + 20], fill=w)
    elif kind == "flags":
        for i, x in enumerate((cx - 16, cx - 2, cx + 12)):
            draw.line([x, cy - r + 14, x, cy + r - 12], fill=w, width=3)
            draw.rectangle([x, cy - r + 14, x + 12, cy - r + 26], fill=w)
    elif kind == "jet":
        draw.polygon([(cx - r + 10, cy + 8), (cx + r - 8, cy - 12),
                      (cx + r - 14, cy + 2), (cx + 2, cy + 8),
                      (cx - r + 16, cy + 16)], fill=w)
    elif kind == "scale":
        draw.line([cx, cy - r + 12, cx, cy + r - 12], fill=w, width=3)
        draw.line([cx - r + 12, cy - r + 12, cx + r - 12, cy - r + 12],
                  fill=w, width=3)
        draw.polygon([(cx - r + 12, cy - 2), (cx - r + 2, cy - 2),
                      (cx - r + 7, cy + 10)], fill=w)
        draw.polygon([(cx + r - 12, cy - 2), (cx + r - 2, cy - 2),
                      (cx + r - 7, cy + 10)], fill=w)
        draw.line([cx - 8, cy + r - 12, cx + 8, cy + r - 12], fill=w, width=3)
    elif kind == "chart":
        for i, h in enumerate((14, 24, 34)):
            x0 = cx - 18 + i * 14
            draw.rectangle([x0, cy + 16 - h, x0 + 9, cy + 16], fill=w)
    elif kind == "chip":
        # square chip with pins
        draw.rectangle([cx - 14, cy - 14, cx + 14, cy + 14], outline=w, width=3)
        draw.rectangle([cx - 6, cy - 6, cx + 6, cy + 6], fill=w)
        for x in (cx - 8, cx, cx + 8):
            draw.line([x, cy - 20, x, cy - 14], fill=w, width=3)
            draw.line([x, cy + 14, x, cy + 20], fill=w, width=3)
        for y in (cy - 8, cy, cy + 8):
            draw.line([cx - 20, y, cx - 14, y], fill=w, width=3)
            draw.line([cx + 14, y, cx + 20, y], fill=w, width=3)


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    d.rectangle([0, 0, W, 168], fill=NAVY)
    f_kicker = font(FONT_BOLD, 26)
    date_text = "WEDNESDAY, 18 NOVEMBER 2026"
    date_size = 56
    f_date = font(FONT_BOLD, date_size)
    while d.textlength(date_text, font=f_date) > W - 2 * 36 and date_size > 30:
        date_size -= 2
        f_date = font(FONT_BOLD, date_size)
    f_sub = font(FONT_REG, 23)
    d.text((36, 18), "T H E   W O R L D   I N   O N E   D A Y",
           font=f_kicker, fill=(212, 175, 105))
    d.text((36, 52), date_text,
           font=f_date, fill=(255, 255, 255))
    d.text((36, 124), "Six stories that defined the day \u2014 as reported",
           font=f_sub, fill=(190, 200, 220))

    # --- story cards: 2 cols x 3 rows ---
    margin, gutter = 36, 18
    cw = (W - 2 * margin - gutter) // 2
    ch = 246
    top = 188
    f_tag = font(FONT_BOLD, 20)
    f_head = font(FONT_BOLD, 29)
    f_body = font(FONT_REG, 21)
    for i, (tag, colour, head, body, ic) in enumerate(STORIES):
        row, col = divmod(i, 2)
        x0 = margin + col * (cw + gutter)
        y0 = top + row * (ch + gutter)
        d.rectangle([x0, y0, x0 + cw, y0 + ch], fill=CARD, outline=LINE, width=2)
        d.rectangle([x0, y0, x0 + cw, y0 + 7], fill=colour)
        icon(d, ic, x0 + cw - 44, y0 + 48, 30, colour)
        d.text((x0 + 18, y0 + 20), tag, font=f_tag, fill=colour)
        text_w = cw - 36 - 76  # leave room for the icon disc
        y = y0 + 52
        head_lines = wrap(d, head, f_head, text_w)[:2]
        for ln in head_lines:
            d.text((x0 + 18, y), ln, font=f_head, fill=INK)
            y += 36
        y += 4
        body_lines = wrap(d, body, f_body, cw - 36)[:3]
        for ln in body_lines:
            d.text((x0 + 18, y), ln, font=f_body, fill=(60, 60, 60))
            y += 28
        if len(wrap(d, head, f_head, text_w)) > 2 or \
                len(wrap(d, body, f_body, cw - 36)) > 3:
            print("WARNING: text truncated in card", i, tag)

    # --- footer ---
    f_foot = font(FONT_REG, 17)
    d.text((36, 984),
           "Sources: Reuters, AP, AFP, BBC, Wall Street Journal, PAHO/CDC \u2014 as reported on 18 November 2026.",
           font=f_foot, fill=GREY)

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
