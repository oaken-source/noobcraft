
'''
This module contains the demo players created for noobcraft.
'''

import random

from noobcraft.players.player import Player


class AggressivePlayer(Player):
    '''
    This demo player attacks its nearest neighbor.
    '''
    def act(self, world):
        for unit in world.unitsOf(self):
            closestEnemy = unit.closestEnemy()
            if closestEnemy is None:
                unit.moveTowards(unit.pos + Vec2(direction=random.uniform(0, 2 * math.pi)), 1)
            else:
                if unit.inRange(closestEnemy):
                    unit.attack(closestEnemy)
                else:
                    unit.moveTowards(closestEnemy.pos, 1)
