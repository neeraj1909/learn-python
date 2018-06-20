class Point(object):
    """Represents a point in 2-D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("Point = (%s, %s)" % (self.x, self.y))


blank = Point(3.0, 4.0)
blank.print_point()
