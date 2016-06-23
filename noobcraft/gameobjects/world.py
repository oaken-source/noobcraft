
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

    # TODO use a filter instead!!
    def unitsOf(self, player):
        result = []
        for unit in self.units:
            if unit.player == player:
                result.append(unit)
        return result

    # TODO use a filter instead!!
    def closestEnemyTo(self, unit):
        minDistance = 10 # the field is only 1x1
        result = None
        for candidate in self.units:
            if candidate.player != unit.player:
                distance = candidate.distanceTo(unit)
                if distance < minDistance:
                    minDistance = distance
                    result = candidate
        return result
