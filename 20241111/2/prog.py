from math import *


class Triangle:
    def __init__(self, point1, point2, point3):
        self.points = (tuple(point1), tuple(point2), tuple(point3))

    def __abs__(self):
        x1, y1 = self.points[0]
        x2, y2 = self.points[1]
        x3, y3 = self.points[2]

        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

    def __bool__(self):
        return abs(self) > 0

    def __lt__(self, other):
        return abs(self) < abs(other)

    def contains(self, point):
        return isclose(
            abs(self),
            abs(Triangle(self.points[0], self.points[1], point))+
            abs(Triangle(self.points[2], self.points[1], point))+
            abs(Triangle(self.points[0], self.points[2], point))
        )

    def __contains__(self, other):
        return (
            self.contains(other.points[0])
            and self.contains(other.points[1])
            and self.contains(other.points[2]) and bool(self)
        ) or not other

    def __and__(self, other):
        return (
            self.contains(other.points[0])
            or self.contains(other.points[1])
            or self.contains(other.points[2])
            or other.contains(self.points[0])
            or other.contains(self.points[1])
            or other.contains(self.points[2])
        ) and bool(other) and bool(self)


import sys

exec(sys.stdin.read())

