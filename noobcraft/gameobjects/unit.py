
'''
This module defines the game objects present in noobcraft.
'''

import math


class Unit(object):
    '''
    This class represents a unit of control for the players.
    '''
    def __init__(self, player, world):
        self.player = player
        self.world = world

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

    def closestEnemy(self):
        return min(
            [ unit for unit in self.world.units if unit.player != self.player ],
            key=lambda candidate: self.distanceTo(candidate)
        )

    def moveTowards(self, targetPosition, speedFactor):
        speedFactor = max(0, min(1, speedFactor)) # should be 0..1

        # movement vector, not normalized
        v = (targetPosition[0] - self.x, targetPosition[1] - self.y)
        dv = math.sqrt(v[0] * v[0] + v[1] * v[1])  # length of the vector

        if dv < speedFactor * self.speed:    # target is super close
            speedFactor = dv    # so we wont need to make the full move, just dv
            self.x = targetPosition[0]
            self.y = targetPosition[1]
        else:
            # offset position by normalized movement vector * speedFactor
            self.x = self.x + v[0] / dv * speedFactor * self.speed
            self.y = self.y + v[1] / dv * speedFactor * self.speed

        self.size = self.size - speedFactor * math.pow(self.size, 0.1)
        if self.size <= 0:
            self.world.removeUnit(self)

    def inRange(self, other):
        return self.distanceTo(other) <= ( math.sqrt(self.size) + math.sqrt(other.size) ) / 200

    def attack(self, other):
        if not self.inRange(other) or self.size < 1:
            return False
        force = max(1, min(10, self.size, other.size))

        other.size -= force
        self.size -= force

        if other.size <= 0:
            self.world.removeUnit(other)
        if self.size <= 0:
            self.world.removeUnit(self)
