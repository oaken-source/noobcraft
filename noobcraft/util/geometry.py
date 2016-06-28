
import math
from collections import namedtuple


class Vec2(namedtuple('Vec2', ('x', 'y'))):

    def __new__(cls, *args, direction=None, magnitude=1):
        if direction is not None:
            x = magnitude * math.cos(direction)
            y = magnitude * math.sin(direction)
            return super(Vec2, cls).__new__(cls, x, y)
        else:
            return super(Vec2, cls).__new__(cls, *args)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __add__(self, other):
        return type(self)(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return type(self)(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, type(self)):
            return self.x * other.x + self.y * other.y
        return type(self)(self.x * other, self.y * other)

    def __div__(self, other):
        return type(self)(self.y / other, self.y / other)
