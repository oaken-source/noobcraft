
import math


class Vec2(tuple):

    def __new__(cls, *args, direction=None, magnitude=1):
        if direction is not None:
            v = (magnitude * math.cos(direction), magnitude * math.sin(direction))
            return super(Vec2, cls).__new__(cls, v)
        else:
            return super(Vec2, cls).__new__(cls, [i for i in args])

    def __add__(self, other):
        return Vec2(*[self[i] + other[i] for i in range(len(self))])

    def __sub__(self, other):
        return Vec2(*[self[i] - other[i] for i in range(len(self))])

    def __mul__(self, other):
        if isinstance(other, Vec2):
            raise NotImplementedError('cross product is not implemented')
        return Vec2(*[self[i] * other for i in range(len(self))])

    def __abs__(self):
        return math.hypot(self[0], self[1])
