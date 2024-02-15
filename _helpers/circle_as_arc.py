import math as m

def circle_as_arc(radius, center=(0,0)):
    center_x,center_y = center
    print(center_x,type(center_x))
    print(center_y,type(center_y))
    print(radius,type(radius))
    print(f'<path id="upper" d="M{center_x - radius:.3f},{center_y:.3f} A{radius:.3f},{radius:.3f} 0 0 1 {center_x + radius:.3f} {center_y:.3f}" />')
    print(f'<path id="lower" d="M{center_x - radius:.3f},{center_y:.3f} A{radius:.3f},{radius:.3f} 0 0 -1 {center_x + radius:.3f} {center_y:.3f}" />')

