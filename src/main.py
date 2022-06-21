from classes import *

point1 = Point(0, 3)
point2 = Point(4, 0)
point3 = Point(0, 0)
circle = Circle(10, point1)
triangle = Triangle(point1, point2, point3)
square = Square(point1, point2)

list_of_figures = [circle, triangle, square]

for i in list_of_figures:
    i.__str__
    print('Perimeter ', i.perimeter)
    print('Square', i.square)
    print()
