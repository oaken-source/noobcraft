
'''
This module represents the game.
'''

from noobcraft.gameobjects.world import World
from noobcraft.gameobjects.unit import Unit

class Game(object):
    '''
    This class represents a noobcraft game.
    '''
    def __init__(self):
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)

    def start(self):
        self.world = World([ Unit(player) for player in self.players ])

    def update(self):
        if not self.over:
            for player in self.players:
                player.act(self.world)
            self.world.tick()

    @property
    def over(self):
        return self.world.age >= 1000