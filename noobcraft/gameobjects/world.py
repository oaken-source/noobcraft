
'''
This module defines the world of noobcraft.
'''

import math

class World(object):
    '''
    This class represents a world in noobcraft.
    '''
    def __init__(self, starters):
        self.age = 0

        n = len(starters)
        a = 2 * math.pi / n
        l = 1 / (2 * math.sin(a / 2))

        for i in range(n):
            starters[i].position = (l * math.cos(i * a), l * math.sin(i * a))

        self.units = starters

    def update(self):
        for unit in self.units:
            unit.update()
        self.age += 1

    def unitsOf(self, player):
        return [ unit for unit in self.units if unit.player == player ]

    def closestEnemyTo(self, unit):
        return min(self.units, key=lambda candidate: candidate.distanceTo(unit))
