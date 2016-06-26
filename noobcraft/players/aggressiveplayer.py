
'''
This module contains the demo players created for noobcraft.
'''

import random

from noobcraft.players.player import Player

class AggressivePlayer(Player):
    '''
    This demo player just does nothing.
    '''
    def randomDirection(self):
        return [ random.uniform(-1, 1), random.uniform(-1, 1) ]

    def act(self, world):
        for unit in world.unitsOf(self):
            closestEnemy = unit.closestEnemy()
            if closestEnemy is None:
                unit.moveTowards(self.randomDirection(), 1)
            else:
                unit.moveTowards([closestEnemy.x - unit.x, closestEnemy.y - unit.y], 1)
