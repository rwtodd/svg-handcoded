#!/bin/env python3

# just modify for each use... simple helper for rayed patterns

from random import random
from math import sin,cos,radians

WIDTH=300
HEIGHT=300
STROKE=5
ANGLE=80
COLORS=["#669900", "#ffff66"]

GROUPS=50
for ray in range(GROUPS):
   for cl in COLORS:
      x,y = random()*WIDTH, random()*HEIGHT
      x2,y2 = random()*WIDTH, random()*HEIGHT
      print(f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" stroke="{cl}" stroke-width="{random()*STROKE+0.5}"  />')

