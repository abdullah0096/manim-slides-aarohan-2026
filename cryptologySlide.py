"""
Cryptology — Manim Slides Moving-Camera Scene (Vertical Tree)
=============================================================

Run (low quality preview):
    manim -pql plaground2.py CryptologySlides

Run with manim-slides:
    manim-slides render plaground2.py CryptologySlides
    manim-slides CryptologySlides

Requires: manim >= 0.18, manim-slides
"""

from manim import *
from manim_slides import Slide

# ══════════════════════════════════════════════════════════════════════════════
#  PALETTE — dark background, soft pastel nodes
# ══════════════════════════════════════════════════════════════════════════════
BG = "#0D1117"

# Root
ROOT_FILL      = "#1B2838"
ROOT_STROKE    = "#58A6FF"
ROOT_TEXT      = "#FFFFFF"

# Cryptography branch — soft lavender / purple tones
CRYPTO_FILL    = "#2D2047"
CRYPTO_STROKE  = "#B392F0"
CRYPTO_TEXT    = "#E2D9F3"

CRYPTO_C1      = "#3B2867"
CRYPTO_C2      = "#44307A"
CRYPTO_C3      = "#4D388D"
CRYPTO_C4      = "#5640A0"
CRYPTO_C5      = "#5F48B3"

LEAF_FILL      = "#221B3A"
LEAF_STROKE    = "#9B8EC4"
LEAF_TEXT      = "#D5CCE8"

# Cryptanalysis branch — soft cyan / teal tones
ANAL_FILL      = "#1A3040"
ANAL_STROKE    = "#56D4B0"
ANAL_TEXT      = "#C8F0E4"

ANAL_C1        = "#1D4A5A"
ANAL_C2        = "#205566"
ANAL_C3        = "#236072"
ANAL_C4        = "#266B7E"

ANAL_LEAF_FILL   = "#152A35"
ANAL_LEAF_STROKE = "#7ECBB5"
ANAL_LEAF_TEXT   = "#BDE8DB"

# Connectors
CONN_ROOT      = "#4A5568"
CONN_CRYPTO    = "#9B7AD8"
CONN_ANAL      = "#4DB89A"


# ══════════════════════════════════════════════════════════════════════════════
#  HELPER FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════

def make_node(lines, width, height, fill, stroke, text_color,
              font_size=20, bold_first=False, radius=0, stroke_w=2.0):
    """Create a rounded-rectangle node with Text labels."""
    if isinstance(lines, str):
        lines = [lines]
    rect = RoundedRectangle(
        corner_radius=radius,
        width=width, height=height,
        fill_color=fill, fill_opacity=0.92,
        stroke_color=stroke, stroke_width=stroke_w,
    )
    texts = VGroup()
    for i, line in enumerate(lines):
        w = BOLD if (i == 0 and bold_first) else NORMAL
        texts.add(Text(line, font_size=font_size, color=text_color, weight=w))
    texts.arrange(DOWN, buff=0.06)
    texts.move_to(rect)
    if texts.width  > width  - 0.22: texts.scale((width  - 0.22) / texts.width)
    if texts.height > height - 0.18: texts.scale((height - 0.18) / texts.height)
    return VGroup(rect, texts)


def make_leaf_node(lines, width, height, fill, stroke, text_color,
                   font_size=18, radius=0, stroke_w=2.0):
    """Create a rounded-rectangle leaf node with Tex (LaTeX) labels."""
    if isinstance(lines, str):
        lines = [lines]
    rect = RoundedRectangle(
        corner_radius=radius,
        width=width, height=height,
        fill_color=fill, fill_opacity=0.92,
        stroke_color=stroke, stroke_width=stroke_w,
    )
    # Build bullet list as a single Tex object
    items = VGroup()
    for line in lines:
        item = Tex(r"\textbullet~" + line, font_size=font_size, color=text_color)
        items.add(item)
    items.arrange(DOWN, buff=0.10, aligned_edge=LEFT)
    items.move_to(rect)
    if items.width  > width  - 0.30: items.scale((width  - 0.30) / items.width)
    if items.height > height - 0.22: items.scale((height - 0.22) / items.height)
    return VGroup(rect, items)


def elbow_down(parent, child, color=WHITE, sw=1.5):
    """Elbow connector: bottom of parent → top of child (vertical tree)."""
    mid_y = (parent.get_bottom()[1] + child.get_top()[1]) / 2
    p0 = parent.get_bottom()
    p1 = np.array([p0[0],              mid_y, 0])
    p2 = np.array([child.get_top()[0], mid_y, 0])
    p3 = child.get_top()
    return VGroup(
        Line(p0, p1, color=color, stroke_width=sw),
        Line(p1, p2, color=color, stroke_width=sw),
        Line(p2, p3, color=color, stroke_width=sw),
    )