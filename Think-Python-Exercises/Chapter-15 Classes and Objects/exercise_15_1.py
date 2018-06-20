"""
Write a definition for a class named Circle with attributes center and radius , where
center is a Point object and radius is a number.

Instantiate a Circle object that represents a circle with its center at 150, 100 and
radius 75.

Write a function named point_in_circle that takes a Circle and a Point and returns
True if the Point lies in or on the boundary of the circle.

Write a function named rect_in_circle that takes a Circle and a Rectangle and
returns True if the Rectangle lies entirely in or on the boundary of the circle.

Write a function named rect_circle_overlap that takes a Circle and a Rectangle
and returns True if any of the corners of the Rectangle fall inside the circle. Or as a
more challenging version, return True if any part of the Rectangle falls inside the
circle.
"""
from math import sqrt


class Point(object):
    """Represents a point in 2-D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle (object):
    """docstring for Rectangle.

    attributes: width, height, corner.
    """
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner


class Circle(object):
    """docstring for Circle.

    attributes: center, radius.
    """

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    # def print(self):
    #     return ((self.center.x, self.center.y), self.radius)

    def point_in_circle(self, circle, point):
        dx = point.x - circle.center.x
        dy = point.y - circle.center.y
        distance = sqrt(dx**2 + dy**2)
        return distance <= circle.radius

    def rect_in_circle(self, circle, rectangle):
        if not self.point_in_circle(circle, rectangle.corner):
            return False

        rectangle.corner.x += rectangle.width
        if not self.point_in_circle(circle, rectangle.corner):
            return False

        rectangle.corner.y += rectangle.height
        if not self.point_in_circle(circle, rectangle.corner):
            return False

        rectangle.corner.x -= rectangle.width
        if not self.point_in_circle(circle, rectangle.corner):
            return False

        return True

    def rect_circle_overlap(self, circle, rectangle):
        if self.point_in_circle(circle, rectangle.corner):
            return True

        rectangle.corner.x += rectangle.width
        if self.point_in_circle(circle, rectangle.corner):
            return True

        rectangle.corner.y += rectangle.height
        if self.point_in_circle(circle, rectangle.corner):
            return True

        rectangle.corner.x -= rectangle.width
        if self.point_in_circle(circle, rectangle.corner):
            return True

        return False





center = Point(150, 100)
radius = 75
circle = Circle(center, radius)
# print(circle.print())

# point = Point(200, 100)
# result = circle.point_in_circle(circle, point)
# print(result)
width = 50
height = 50
corner = Point(100, 100)

rectangle = Rectangle(width, height, corner)

result = circle.rect_in_circle(circle, rectangle)
print(result)
