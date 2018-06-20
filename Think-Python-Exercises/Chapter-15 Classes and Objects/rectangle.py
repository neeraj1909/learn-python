import copy

class Point:
    """Represents a point in 2-D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    """docstring for Rectangle.

    attributes: width, height, corner.
    """
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner

    def all_corners_of_rectangle(self):
        corner2 = Point(0, 0)
        corner3 = Point(0, 0)
        corner4 = Point(0, 0)
        #corner on right side at same level
        corner2.x = self.corner.x + self.width
        corner2.y = self.corner.y

        #corner just above
        corner3.x = self.corner.x
        corner3.y = self.corner.y + self.height

        #opposite corner
        corner4.x = self.corner.x + self.width
        corner4.y = self.corner.y + self.height

        return ((self.corner.x, self.corner.y), (corner2.x, corner2.y), (corner3.x, corner3.y), (corner4.x, corner4.y))


    def center(self):
        center = Point()
        center.x = self.cornerx + self.width/2
        center.y = self.cornery + self.height/2
        return (center.x, center.y)

    def grow_rectangle(self, rect, dwidth, dheight):
        rect.width += dwidth
        rect.height += dheight

    def move_rectangle(self, rect, dx, dy):
        rect.cornerx += dx
        rect.cornery += dy
        return rect




width = 50
height = 50
corner = Point(100, 100)

box = Rectangle(width, height, corner)


box2 = copy.copy(box)
print("corners of the rectangle are = " + str(box.all_corners_of_rectangle()))
print("corners of the rectangle are = " + str(box2.all_corners_of_rectangle()))

# print("center of the rectangle is= " + str(box.center()))
# print("center of the rectangle is= " + str(box2.center()))

# box.grow_rectangle(box, 50, 50)
# print("corners of rectangle after updation is= " + str(box.all_corners_of_rectangle()))
# print("corners of rectangle after updation is= " + str(box2.all_corners_of_rectangle()))

# box.move_rectangle(box, 50, 50)

# print("corners of rectangle after updation is= " + str(box.all_corners_of_rectangle()))
# print("corners of rectangle after updation is= " + str(box2.all_corners_of_rectangle()))
