
'''
This module defines the game objects present in noobcraft.
'''

import math


class Unit(object):
    '''
    This class represents a unit of control for the players.
    '''
    def __init__(self, player):
        self.player = player
        self._x = 0.0
        self._y = 0.0
        self.speed = 0.01
        self.size = 10

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def position(self):
        return (self._x, self._y)

    @position.setter
    def position(self, value):
        self._x = value[0]
        self._y = value[1]

    def update(self):
        self.size = self.size + math.pow(self.size, 0.2)

    def distanceTo(self, target):
        return math.hypot(target.x - self.x, target.y - self.y)

    def moveTowards(self, targetPosition, speedFactor):
        speedFactor = max(0, min(1, speedFactor)) # should be 0..1

        # movement vector, not normalized
        v = (targetPosition[0] - self.x, targetPosition[1] - self.y)
        dv = math.sqrt(v[0] * v[0] + v[1] * v[1])  # length of the vector

        if dv < speedFactor:    # target is super close
            speedFactor = dv    # so we wont need to make the full move, just dv

        # offset position by normalized movement vector * speedFactor
        self.x = self.x + v[0] / dv * speedFactor * self.speed
        self.y = self.y + v[1] / dv * speedFactor * self.speed

        self.size = self.size - speedFactor * math.pow(self.size, 0.19)
