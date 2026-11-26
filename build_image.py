#!/usr/bin/env python3
"""Build entry.png: a one-page newspaper front page summing up the world news
of Thursday 26 November 2026, for the make.fun bounty news-image-20261126.

Local build tool only (uses PIL). The submitted entry program is main.py,
which copies this pre-rendered image; the sandbox never runs this file.

Stories (all reported 26 Nov 2026, cross-checked across Reuters, SCMP,
Moneycontrol, Economic Times and Manila Times world pages):
- CPTPP/ASEAN/EU trade chiefs meet in Vietnam hours after the US proposed
  new tariffs on 14 trading partners (China, Japan, EU among them) - Reuters.
- Kim Jong Un makes a rare public show of nuclear warheads - KCNA via press.
- Fuel tanker crash/fire on Cairo's ring highway kills at least 30.
- Leaked Russian registry records suggest 700,000+ Russian war dead in Ukraine.
- Police free hostages seized in a Colombia supermarket after a failed raid.
- A major storm postpones New York's Thanksgiving parade; king tides hit
  the California coast.
- Nearly 2,000 migrants reach Spain's Canary Islands in a record day.
"""
from PIL import Image, ImageDraw, ImageFont
import glob

W = H = 1024
PAPER = (247, 243, 234)
INK = (18, 20, 26)
RED = (178, 34, 40)
GREY = (96, 98, 104)
PANEL = (255, 253, 247)
RULE = (30, 30, 34)

SERIF_B = glob.glob('/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf')[0]
SANS_B = glob.glob('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')[0]
SANS = glob.glob('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')[0]


def font(path, size):
    return ImageFont.truetype(path, size)


img = Image.new('RGB', (W, H), PAPER)
d = ImageDraw.Draw(img)


def text_cx(cx, y, s, fnt, fill=INK):
    d.text((cx, y), s, font=fnt, fill=fill, anchor='ma')


def wrap(s, fnt, maxw):
    words, lines, cur = s.split(), [], ''
    for w_ in words:
        t = (cur + ' ' + w_).strip()
        if d.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


# ---------- masthead ----------
d.rectangle([0, 0, W, 8], fill=RED)
text_cx(W // 2, 20, 'THE WORLD TODAY', font(SERIF_B, 66))
d.line([36, 106, W - 36, 106], fill=RULE, width=4)
d.line([36, 113, W - 36, 113], fill=RULE, width=1)
text_cx(W // 2, 122, 'THURSDAY · 26 NOVEMBER 2026', font(SANS_B, 38), fill=RED)
d.line([36, 174, W - 36, 174], fill=RULE, width=1)

# ---------- lead story ----------
LY, LH = 188, 248
d.rectangle([36, LY, W - 36, LY + LH], fill=PANEL, outline=RULE, width=2)
d.text((58, LY + 14), 'TRADE', font=font(SANS_B, 23), fill=RED)
for i, line in enumerate(wrap('TRADE BLOCS HUDDLE IN VIETNAM AS U.S. FIRES NEW TARIFF SALVO',
                              font(SANS_B, 40), W - 116)):
    d.text((58, LY + 48 + i * 49), line, font=font(SANS_B, 40), fill=INK)
sub = ('Washington proposes duties on 14 partners — China, Japan and the EU '
       'among them — as Asia-Pacific and ASEAN ministers open talks in Vietnam.')
for i, line in enumerate(wrap(sub, font(SANS, 24), W - 116)):
    d.text((58, LY + 158 + i * 30), line, font=font(SANS, 24), fill=GREY)

# ---------- story cards ----------
cards = [
    ('NORTH KOREA', RED,
     'Kim parades nuclear warheads in rare display',
     'KCNA shows Kim Jong Un inspecting warheads after Trump talks were snubbed.'),
    ('EGYPT', (196, 110, 20),
     'Tanker blaze kills at least 30 near Cairo',
     'A fuel truck overturned and caught fire on the ring highway around the capital.'),
    ('UKRAINE WAR', (52, 84, 150),
     'Leak points to 700,000+ Russian war dead',
     'Leaked civil-registry records expose the scale of Moscow\u2019s battlefield losses.'),
    ('COLOMBIA', (24, 120, 84),
     'Police free hostages after supermarket raid',
     'Gunmen seized shoppers in a failed armoured-car heist; officers freed them.'),
    ('UNITED STATES', (90, 70, 160),
     'Storm halts New York\u2019s Thanksgiving parade',
     'Severe weather disrupts the holiday as king tides batter the California coast.'),
    ('SPAIN', (20, 130, 150),
     'Nearly 2,000 migrants reach Canaries in a day',
     'A record single-day arrival by boat on Spain\u2019s Canary Islands.'),
]
GX, GY = 36, 452
CW, CH = (W - 72 - 16) // 2, 158
for idx, (kicker, kc, head, body) in enumerate(cards):
    x = GX + (idx % 2) * (CW + 16)
    y = GY + (idx // 2) * (CH + 12)
    d.rectangle([x, y, x + CW, y + CH], fill=PANEL, outline=RULE, width=2)
    d.rectangle([x, y, x + 10, y + CH], fill=kc)
    d.text((x + 24, y + 10), kicker, font=font(SANS_B, 20), fill=kc)
    for i, line in enumerate(wrap(head, font(SANS_B, 26), CW - 44)):
        d.text((x + 24, y + 37 + i * 31), line, font=font(SANS_B, 26), fill=INK)
    for i, line in enumerate(wrap(body, font(SANS, 19), CW - 44)):
        d.text((x + 24, y + 106 + i * 23), line, font=font(SANS, 19), fill=GREY)

# ---------- footer ----------
FY = GY + 3 * CH + 2 * 12 + 14
d.line([36, FY, W - 36, FY], fill=RULE, width=2)
text_cx(W // 2, FY + 10, 'One day · One picture · The world\u2019s news of 26 November 2026',
        font(SANS_B, 22))

img.save('/home/hatch/workspace/makefun/entries/news-image/entry.png', optimize=True)
print('saved entry.png', img.size)
