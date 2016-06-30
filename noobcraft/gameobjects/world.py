
'''
This module defines the world of noobcraft.
'''

import math

from noobcraft.gameobjects.unit import Unit
from noobcraft.util.geometry import Vec2


class World(object):
    '''
    This class represents a world in noobcraft.
    '''
    def __init__(self, game):
        self.game = game

        self.age = 0
        self.units = []

    def placeStarters(self, actors):
        n = len(actors)

        for i in range(n):
            unit = Unit(owner=actors[i], world=self)
            unit.pos = Vec2(direction=2 * math.pi * i / n)
            self.units.append(unit)

    def update(self):
        for unit in self.units:
            unit.update()
        self.age += 1

    def removeUnit(self, unit):
        self.units.remove(unit)
