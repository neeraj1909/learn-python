"""
Write a function called draw_rect that takes a Turtle object and a Rectangle and uses
the Turtle to draw the Rectangle. See Chapter 4 for examples using Turtle objects.

Write a function called draw_circle that takes a Turtle and a Circle and draws the
Circle.
"""

from turtle import *


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

def draw_rect(bob, rectangle):
    turtle.pu()
    bob.setposition(rectangle.corner.x, rectangle.corner.y)
    turtle.pd()
    for _ in range(2):
        bob.forward(width)
        bob.lt(90)
        bob.forward(height)
        bob.lt(90)
    return


bob = turtle.Turtle()

width = 60
height = 100
corner = Point(10, 10)
rectangle = Rectangle(width, height, corner)

print(draw_rect(bob, rectangle))




def draw_circle(bob, circle):
    turtle.pu()
    bob.setposition(circle.center.x + circle.radius, circle.center.y)
    turtle.pd()
    bob.circle(circle.radius)



if __name__ == '__main__':
    bob = turtle.Turtle()

    width = 60
    height = 100
    corner = Point(10, 10)
    rectangle = Rectangle(width, height, corner)

    print(draw_rect(bob, rectangle))


    x = turtle.Turtle()
    center = Point(0, 0)
    radius = 20
    circle = Circle(center, radius)

    print(draw_circle(x, circle))
