from manim import *
from manim_slides import Slide

import math

DOTCOLOR = WHITE

def plotDotTL(s):
    dot = Dot(color=DOTCOLOR).to_corner(UL).scale(0.1)
    s.play(FadeIn(dot), run_time=0.1)
    s.play(FadeOut(dot), run_time=0.1)


def fun(x):
    return math.sqrt(x*x*x - 3*x + 3)


def fun2(x):
    return (x*x*x - 3*x + 3)


def getEC_points():
    points = []
    cnt = 0
    for i in range(9, -3, -1):
        cnt += 1
        points.append([i, fun(i), 0])

    for i in range(cnt-1, -1, -1):
        points.append([points[i][0], -points[i][1], 0])

    return points