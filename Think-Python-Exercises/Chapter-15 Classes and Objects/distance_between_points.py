#write a function called distance_between_points that takes two Points as arguments and
#returns the distance between them

from math import sqrt


class Point(object):
    """Represents a point in 2-D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Distance(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def distance_between_points(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        distance = sqrt(dx**2 + dy**2)
        return distance


d1 = Distance(1,1)
d2 = Point(2,2)

print(d1.distance_between_points(d2))

