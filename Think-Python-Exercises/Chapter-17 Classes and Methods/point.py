"""
write an add method for the Point class.

write an add method for Points that works with either a Point object
or a tuple:
• If the second operand is a Point, the method should return a new Point whose x
coordinate is the sum of the x coordinates of the operands, and likewise for the y
coordinates.
• If the second operand is a tuple, the method should add the first element of the
tuple to the x coordinate and the second element to the y coordinate, and return
a new Point with the result
"""


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "%.2d, %.2d" % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return (self.x + other.x, self.y + other.y)
        else:
            return (self.x + other[0], self.y + other[1])


p1 = Point(2, 3)
p2 = Point(3, 3)
print(p1 + p2)

p3 = (4, 4)
print(p1 + p3)
