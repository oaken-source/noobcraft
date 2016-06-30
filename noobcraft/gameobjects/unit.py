
'''
This module defines the game objects present in noobcraft.
'''

import math

from noobcraft.util.geometry import Vec2


class Unit(object):
    '''
    This class represents a unit of control for the players.
    '''
    def __init__(self, owner, world):
        self.owner = owner
        self.world = world

        self.pos = Vec2(0, 0)
        self.speed = 0.01
        self.size = 10

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]

    def update(self):
        self.size = self.size + math.pow(self.size, 0.2)

    def moveTowards(self, targetPosition, speedFactor):
        speedFactor = max(0, min(1, speedFactor)) # should be 0..1

        # movement vector, not normalized
        v = targetPosition - self.pos
        dv = abs(v)

        if dv < speedFactor * self.speed:    # target is super close
            speedFactor = dv    # so we wont need to make the full move, just dv
            self.pos = targetPosition
        else:
            # offset position by normalized movement vector * speedFactor
            self.pos = self.pos + v * (speedFactor * self.speed / dv)

        self.size = self.size - speedFactor * math.pow(self.size, 0.1)
        if self.size <= 0:
            self.world.removeUnit(self)

    def inRange(self, other):
        return abs(self.pos - other.pos) <= ( math.sqrt(self.size) + math.sqrt(other.size) ) / 200

    def attack(self, other):
        if not self.inRange(other):
            return False
        force = min(10, self.size, other.size)

        other.size -= force
        self.size -= force

        if other.size <= 0:
            self.world.removeUnit(other)
        if self.size <= 0:
            self.world.removeUnit(self)
