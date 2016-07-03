
'''
This module provides utilities to describe objects in R^2.
'''

import math
from collections import namedtuple


class Vec2(namedtuple('Vec2', ('x', 'y'))):
    '''
    This class represents a vector in R^2.
    '''

    def __new__(cls, x=0, y=0, direction=None, magnitude=1):
        '''
        constructor - can be invoked with x, y or direction and magnitude
        '''
        if direction is not None:
            x = magnitude * math.cos(direction)
            y = magnitude * math.sin(direction)
        return super(Vec2, cls).__new__(cls, x, y)

    def __abs__(self):
        '''
        produce the magnitude of the vector as absolute value
        '''
        return math.hypot(self.x, self.y)

    def __add__(self, other):
        '''
        produce the sum of two vectors
        '''
        return type(self)(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        '''
        produce the difference of two vectors
        '''
        return type(self)(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        '''
        produce the product of a vector and a scalar or the dot product of two vectors
        '''
        if isinstance(other, type(self)):
            return self.x * other.x + self.y * other.y
        return type(self)(self.x * other, self.y * other)

    def __div__(self, other):
        '''
        produce the quotient of a vector and a scalar (python2)
        '''
        return type(self)(self.x.__div__(other), self.y.__div__(other))

    def __truediv__(self, other):
        '''
        produce the true quotient of a vector and a scalar (python3)
        '''
        return type(self)(self.x.__truediv__(other), self.y.__truediv__(other))

    def __floordiv__(self, other):
        '''
        produce the floored quotient of a vector and scalar (python3)
        '''
        return type(self)(self.x.__floordiv__(other), self.y.__floordiv__(other))

    def normalized(self):
        '''
        produce a vector with the same direction and a magnitude of 1
        '''
        return self / abs(self)
