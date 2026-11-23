#!/usr/bin/env python3
"""Render the 23 November 2026 world-news poster (1024x1024 PNG).

Run:  python3 render.py            -> writes entry.png beside this file
Uses only Pillow + the DejaVu fonts shipped with most Linux systems.
The graded entrypoint is main.ts, which copies the rendered entry.png
to $MAKEFUN_OUTPUT_DIR/entry.png. This script is kept in the repo so
anyone can regenerate the image from source.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 242, 231)
INK = (17, 17, 17)
RED = (185, 28, 28)
DARKRED = (127, 29, 29)
BLUE = (29, 78, 216)
TEAL = (13, 116, 128)
AMBER = (180, 83, 9)
GREEN = (21, 101, 52)
GREY = (87, 83, 78)
LIGHT = (255, 255, 255)
PANEL = (255, 255, 255)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, max_w, leading=None):
    lines = wrap(draw, text, fnt, max_w)
    lh = leading or int(fnt.size * 1.22)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


def kicker(draw, x, y, label, colour):
    f = font(FB, 21)
    w = int(draw.textlength(label, font=f)) + 22
    draw.rounded_rectangle([x, y, x + w, y + 32], radius=4, fill=colour)
    draw.text((x + 11, y + 4), label, font=f, fill=LIGHT)
    return w


def panel(draw, x, y, w, h):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10,
                           fill=PANEL, outline=(210, 205, 192), width=2)


def main():
    im = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(im)

    # ---- top black bar: the date, unmissable -------------------------------
    d.rectangle([0, 0, W, 62], fill=INK)
    d.text((24, 12), "MONDAY, 23 NOVEMBER 2026", font=font(FB, 32), fill=LIGHT)
    d.text((W - 24 - d.textlength("ONE DAY  •  ONE IMAGE", font=font(FB, 24)), 18),
           "ONE DAY  •  ONE IMAGE", font=font(FB, 24), fill=(251, 191, 36))

    # ---- masthead ------------------------------------------------------------
    d.text((24, 74), "THE WORLD IN ONE IMAGE", font=font(FB, 58), fill=INK)
    d.text((24, 140), "Seven stories that defined the day — from Antalya to Seoul.",
           font=font(FR, 24), fill=GREY)
    d.line([24, 178, W - 24, 178], fill=INK, width=3)

    # ---- HERO: COP31 collapses ----------------------------------------------
    x, y, w, h = 24, 192, 976, 218
    panel(d, x, y, w, h)
    d.rounded_rectangle([x, y, x + 320, y + h], radius=10, fill=RED)
    d.rounded_rectangle([x + 300, y, x + 320, y + h], radius=0, fill=RED)
    d.text((x + 26, y + 28), "NO", font=font(FB, 88), fill=LIGHT)
    d.text((x + 26, y + 122), "DEAL", font=font(FB, 88), fill=LIGHT)
    kicker(d, x + 350, y + 18, "CLIMATE  •  ANTALYA, TURKEY", RED)
    d.text((x + 350, y + 62), "COP31 COLLAPSES",
           font=font(FB, 46), fill=INK)
    text_block(d, x + 350, y + 118,
               "Climate talks end with no deal — fossil-fuel wording "
               "stripped out, EU and ~130 nations reject the pact. "
               "Longest COP ever; first collapse since 2009.",
               font(FR, 23), INK, 600, leading=29)

    # ---- Row 2: Hormuz | USA -------------------------------------------------
    y2, h2 = 426, 218
    # Hormuz
    x, w = 24, 476
    panel(d, x, y2, w, h2)
    kicker(d, x + 18, y2 + 16, "WAR  •  STRAIT OF HORMUZ", DARKRED)
    d.text((x + 18, y2 + 58), "TANKERS HIT", font=font(FB, 40), fill=INK)
    text_block(d, x + 18, y2 + 108,
               "Three tankers struck Fri–Sat; attacks at their highest "
               "level since the Iran war began. Trump threatens to sink "
               "Iranian ships that force the US blockade.",
               font(FR, 21), INK, w - 36, leading=27)
    # USA
    x, w = 524, 476
    panel(d, x, y2, w, h2)
    kicker(d, x + 18, y2 + 16, "USA  •  MIDTERMS", BLUE)
    d.text((x + 18, y2 + 56), "258", font=font(FB, 64), fill=BLUE)
    text_block(d, x + 170, y2 + 62,
               "DEMOCRATS WIN BIGGEST HOUSE MAJORITY SINCE 1992",
               font(FB, 21), INK, w - 188, leading=27)
    text_block(d, x + 18, y2 + 140,
               "Hubbard beats Foxx in N. Carolina by 330 votes after a "
               "recount — 44 seats flipped.",
               font(FR, 19), INK, w - 36, leading=25)

    # ---- Row 3: Ukraine | Markets | Indonesia --------------------------------
    y3, h3, w3 = 660, 196, 312
    # Ukraine
    x = 24
    panel(d, x, y3, w3, h3)
    kicker(d, x + 16, y3 + 14, "UKRAINE", TEAL)
    d.text((x + 16, y3 + 54), "BOY, 7, ALIVE", font=font(FB, 30), fill=INK)
    text_block(d, x + 16, y3 + 92,
               "David is pulled from rubble after 14 hours in Dymer, "
               "near Kyiv, after a Russian drone strike. At least 9 killed.",
               font(FR, 19), INK, w3 - 32, leading=24)
    # Markets
    x = 356
    panel(d, x, y3, w3, h3)
    kicker(d, x + 16, y3 + 14, "MARKETS", AMBER)
    d.text((x + 16, y3 + 52), "AI ROUT", font=font(FB, 30), fill=INK)
    d.text((x + 16, y3 + 86), "KOSPI −5.8%", font=font(FB, 30), fill=AMBER)
    text_block(d, x + 16, y3 + 124,
               "Seoul slides as AI sell-off spreads. Samsung, "
               "SK Hynix −6%; Nasdaq −5.3% Fri.",
               font(FR, 19), INK, w3 - 32, leading=23)
    # Indonesia
    x = 688
    panel(d, x, y3, w3, h3)
    kicker(d, x + 16, y3 + 14, "INDONESIA", DARKRED)
    d.text((x + 16, y3 + 54), "FACTORY FIRE", font=font(FB, 30), fill=INK)
    text_block(d, x + 16, y3 + 92,
               "24 body bags removed from a candy factory fire in "
               "Banten. Dozens of workers still missing.",
               font(FR, 19), INK, w3 - 32, leading=24)

    # ---- Sport strip -----------------------------------------------------------
    y4, h4 = 872, 104
    panel(d, 24, y4, 976, h4)
    kicker(d, 42, y4 + 14, "SPORT", GREEN)
    d.text((42, y4 + 52), "Liverpool 4–0 Man Utd — Pochettino's debut is a nightmare.",
           font=font(FB, 22), fill=INK)
    d.text((42, y4 + 82), "Yoro sent off, 8'. Szoboszlai, Wirtz, Ngumoha, Munoz score. "
           "Verstappen wins Las Vegas GP.",
           font=font(FR, 18), fill=GREY)

    # ---- footer ------------------------------------------------------------------
    d.line([24, 992, W - 24, 992], fill=(210, 205, 192), width=2)
    d.text((24, 1000), "Sources: CNN, Reuters, BBC, AP, UKMTO  •  Also: Nepal PM in Delhi; "
           "Mayon erupts; Belgium airports shut; Paolo Bulgari dies, 89.",
           font=font(FR, 15), fill=GREY)

    im.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png", im.size)


if __name__ == "__main__":
    main()
