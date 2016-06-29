
import math
from collections import namedtuple


class Vec2(namedtuple('Vec2', ('x', 'y'))):

    def __new__(cls, x=0, y=0, direction=None, magnitude=1):
        if direction is not None:
            x = magnitude * math.cos(direction)
            y = magnitude * math.sin(direction)
        return super(Vec2, cls).__new__(cls, x, y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __add__(self, other):
        return type(self)(self.x.__add__(other.x), self.y.__abs__(other.y))

    def __sub__(self, other):
        return type(self)(self.x.__sub__(other.x), self.y.__sub__(other.y))

    def __mul__(self, other):
        if isinstance(other, type(self)):
            return self.x * other.x + self.y * other.y
        return type(self)(self.x.__mul__(other), self.y.__mul__(other))

    def __div__(self, other):
        return type(self)(self.x.__div__(other), self.y.__div__(other))

    def __truediv__(self, other):
        return type(self)(self.x.__truediv__(other), self.y.__truediv__(other))

    def __floordiv__(self, other):
        return type(self)(self.x.__floordiv__(other), self.y.__floordiv__(other))
