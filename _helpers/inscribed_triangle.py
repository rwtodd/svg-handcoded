import math as m

def inscribed_triangle(radius,rotate=0):
    """Draw an inscribed triangle in a circle of 
    radius 'radius', roatated 'roate' degrees
    clockwise"""
    vertices = (270, 30, 150)
    def xy(deg):
      rads = m.radians(deg+rotate)
      return f'{radius * m.cos(rads):0.3f},{radius * m.sin(rads):0.3f}'
    print(f'<path d="M{xy(vertices[0])} L{xy(vertices[1])} L{xy(vertices[2])} Z" />')

