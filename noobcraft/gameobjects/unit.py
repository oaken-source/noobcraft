
'''
This module defines the game objects present in noobcraft.
'''

class Unit(object):
    '''
    This class represents a unit of control for the players.
    '''
    def __init__(self, player):
        self.player = player
        self.position = (0.0, 0.0)
        self.speed = 1
        self.size = 900

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    def tick(self):
        pass
