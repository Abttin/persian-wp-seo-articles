#!/usr/bin/env python3
"""Render a Persian (RTL) numbered-cards infographic to WebP + PNG.

Why this exists: WordPress strips inline <svg>, so diagrams must be delivered as image files.

Usage:
  python3 make_infographic.py --title "۷ معیار مهم در راهنمای خرید ..." \
      --items "سازگاری با مدل خودرو,رم و حافظه,پردازنده" \
      --out /mnt/data/my-infographic

Writes <out>.webp and <out>.png. Requires Pillow built with Raqm and a font with Arabic glyphs
(DejaVu Sans is used by default). Always open the PNG afterwards and check the Persian text.
"""
import argparse
import os
import sys
from PIL import Image, ImageDraw, ImageFont, features

import glob
FONT_CANDIDATES = sorted(glob.glob("/mnt/data/*egular*.ttf") + glob.glob("/mnt/data/*Vazir*.ttf") + glob.glob("/mnt/data/*.ttf")) + [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/vazirmatn/Vazirmatn-Regular.ttf",
]
BOLD_CANDIDATES = sorted(glob.glob("/mnt/data/*old*.ttf")) + [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/vazirmatn/Vazirmatn-Bold.ttf",
]
PERSIAN_DIGITS = "۰۱۲۳۴۵۶۷۸۹"


def first_existing(paths):
    for p in paths:
        if os.path.exists(p):
            return p
    sys.exit("No usable font found; pass --font /path/to/font-with-arabic-glyphs.ttf")


def fa_num(n):
    return "".join(PERSIAN_DIGITS[int(c)] for c in str(n))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True)
    ap.add_argument("--items", required=True, help="comma-separated labels, first item appears top-right")
    ap.add_argument("--out", required=True, help="output path without extension")
    ap.add_argument("--font")
    ap.add_argument("--bold-font")
    ap.add_argument("--accent", default="#1e5aa0")
    ap.add_argument("--width", type=int, default=1280)
    args = ap.parse_args()

    RAQM = features.check("raqm")
    if not RAQM:
        try:
            import arabic_reshaper
            from bidi.algorithm import get_display
        except ImportError:
            sys.exit("Pillow lacks Raqm and arabic_reshaper/python-bidi are missing: Persian text would render disconnected.")

    items = [s.strip() for s in args.items.split(",") if s.strip()]
    font_path = args.font or first_existing(FONT_CANDIDATES)
    bold_path = args.bold_font or first_existing(BOLD_CANDIDATES)
    W = args.width
    ft = ImageFont.truetype(bold_path, 46)
    fi = ImageFont.truetype(font_path, 34)
    fn = ImageFont.truetype(bold_path, 40)

    ink, light = (33, 37, 41), (238, 244, 251)
    accent = args.accent
    cw, ch, gap, margin, top = 570, 130, 30, 60, 130
    rows = (len(items) + 1) // 2
    H = top + rows * (ch + gap) + 20

    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)

    def text(x, y, s, font, fill=ink, anchor="mm"):
        if RAQM:
            d.text((x, y), s, font=font, fill=fill, anchor=anchor,
                   direction="rtl", language="fa", features=["-kern"])
        else:
            d.text((x, y), get_display(arabic_reshaper.reshape(s)), font=font, fill=fill, anchor=anchor)

    text(W // 2, 60, args.title, ft, accent)
    xs = [W - margin - cw, W - margin - 2 * cw - 40]  # right column first (RTL reading order)
    for i, label in enumerate(items):
        col, row = i % 2, i // 2
        x0, y0 = xs[col], top + row * (ch + gap)
        d.rounded_rectangle((x0, y0, x0 + cw, y0 + ch), radius=22, fill=light, outline=accent, width=3)
        cx, cy = x0 + cw - 70, y0 + ch // 2
        d.ellipse((cx - 42, cy - 42, cx + 42, cy + 42), fill=accent)
        text(cx, cy - 2, fa_num(i + 1), fn, "white")
        text(cx - 70, cy, label, fi, ink, anchor="rm")

    img.save(args.out + ".webp", quality=90)
    img.save(args.out + ".png", optimize=True)
    print("wrote", args.out + ".webp", "and", args.out + ".png", f"({W}x{H})")


if __name__ == "__main__":
    main()
