
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

    def tick(self):
        for unit in self.units:
            unit.tick()
        self.age += 1

    def unitsOf(self, player):
        result = []
        for unit in self.units:
            if unit.player == player:
                result.append(unit)
        return result
