#!/bin/env python

# this program will be expanded later, but for now
# just draw the star I need.


from math import sin,cos,radians

def star(sides,outer,inner):
   print('<polygon points="')
   angle = radians(360.0 / sides)
   half  = angle/2 
   for s in range(sides):
      print(f'{outer*cos(s*angle)},{outer*sin(s*angle)} ')
      print(f'{inner*cos(half+s*angle)},{inner*sin(half+s*angle)} ')
   print('''">
   <desc>???</desc>
</polygon>''')

if __name__ == '__main__':
   import argparse as ap
   parser = ap.ArgumentParser(description='draws polygons.')
   parser.add_argument('--type','-t', default="star",
                       help='the type of polygon to draw')
   parser.add_argument('--sides', '-s', type=int, default=5,
                       help='the number of sides')
   parser.add_argument('--dimensions', '-d', nargs=2, type=float, 
                       help='the outer and inner dimensions')
   args = parser.parse_args()
   star(args.sides,args.dimensions[0],args.dimensions[1])

# vim: expandtab:sw=3
