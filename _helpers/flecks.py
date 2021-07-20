#!/bin/env python3

# just modify for each use... simple helper for flecked patterns

from random import random
WIDTH=100
HEIGHT=100
RADIUS=4

for x in range(80):
    print(f'<circle cx="{random()*WIDTH}" cy="{random()*HEIGHT}" r="{random()*RADIUS}" fill="gold" />')

