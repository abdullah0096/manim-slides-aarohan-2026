"""
Cryptography Pyramid — Manim-Slides Scene
==========================================

Render:
    manim render piramid.py CryptoPyramid -qh --disable_caching

Present (interactive slide-by-slide):
    manim-slides present CryptoPyramid

The scene builds bottom → top, one tier at a time.
Camera zooms into each new tier as the pyramid narrows toward the apex.
Everything stays inside the triangle boundary.
"""

from manim import *
from manim_slides import Slide


# ─────────────────────────────────────────────────────────────────
#  COLOUR PALETTE
# ─────────────────────────────────────────────────────────────────
BG          = "#000000"
GOLD        = "#D4AA50"
GOLD_BRIGHT = "#F5D87A"
GOLD_DIM    = "#8A6015"
WHITE_T     = "#E8E8E8"
GREY_T      = "#888888"
DARK_GREY   = "#3A3A3A"
DARK_PANEL  = "#0F0F0F"
BITCOIN_ORG = "#F7931A"
ETH_SILVER  = "#C0C0C0"


# ─────────────────────────────────────────────────────────────────
#  TEXT HELPERS  (Manim font_size is in points, ~0.04 manim-units each)
# ─────────────────────────────────────────────────────────────────
def t_gold(s, fs=28, w=NORMAL, col=GOLD_BRIGHT):
    return Text(s, font="GFS Complutum", font_size=fs, weight=w, color=col)

def t_white(s, fs=26, col=WHITE_T):
    return Text(s, font="GFS Complutum", font_size=fs, color=col)

def t_small(s, fs=18, col=GREY_T):
    return Text(s, font="GFS Complutum", font_size=fs, color=col)

def vstack(*items, buf=0.15):
    """Arrange Mobjects top-to-bottom."""
    g = VGroup(*items)
    g.arrange(DOWN, buff=buf)
    return g

def gold_line(p1, p2, sw=2.0):
    return Line(p1, p2, color=GOLD, stroke_width=sw)

def dim_line(p1, p2, sw=0.9):
    return Line(p1, p2, color="#000000", stroke_width=sw)

def dash_vline(x, y0, y1):
    return DashedLine(
        [x, y0, 0], [x, y1, 0],
        color=DARK_GREY, stroke_width=1.2,
        dash_length=0.10, dashed_ratio=0.55,
    )


# ─────────────────────────────────────────────────────────────────
#  PYRAMID GEOMETRY
#
#  Apex   : (0,  4.00)
#  Base   : (±5.5, −3.80)
#  Height : 7.80 units
#
#  hw(y) = 5.5 × (4.0 − y) / 7.8
#
#  Tier boundaries (bottom → top):
#    Y0 = −3.80  base
#    Y1 = −2.40  Math content ─── Hardness (sub-layer of Math)
#    Y2 = −1.40  Math+Hardness ─── Algorithms
#    Y3 = −0.80  algo banner bottom
#    Y4 = −0.20  algo banner top
#    Y5 =  0.50  Algorithms ─── Protocols
#    Y6 =  1.60  Protocols ─── Applications
#    Y7 =  4.00  apex
# ─────────────────────────────────────────────────────────────────
APEX = np.array([0,  4.00, 0])
BL   = np.array([-5.5, -3.80, 0])
BR   = np.array([ 5.5, -3.80, 0])

Y0 = -3.80   # base
Y1 = -2.40   # math content / hardness divider (dashed — sub-layer)
Y2 = -1.40   # math+hardness / algorithms (solid gold)
Y3 = -0.80   # algo banner bottom
Y4 = -0.20   # algo banner top
Y5 =  0.50   # algo / protocols
Y6 =  1.60   # protocols / applications
Y7 =  4.00   # apex

MATH_TINT   = "#0D0D00"    # very subtle warm tint for math zone
LOCK_EMOJI  = "🔒"
KEY_EMOJI   = "🔑"
SHIELD_EMJ  = "🛡"

def hw(y):
    """Half-width of pyramid at height y."""
    return 5.5 * (4.0 - y) / 7.8

def lp(y):
    return np.array([-hw(y), y, 0])

def rp(y):
    return np.array([ hw(y), y, 0])

def tier_div(y, sw=2.5, col=GOLD):
    return Line(lp(y), rp(y), color=col, stroke_width=sw)

def trapezoid(y_bot, y_top, col, opacity=0.08):
    """Filled trapezoid between two Y levels, clipped to pyramid edges."""
    return Polygon(
        lp(y_bot), rp(y_bot), rp(y_top), lp(y_top),
        fill_color=col, fill_opacity=opacity, stroke_width=0,
    )
