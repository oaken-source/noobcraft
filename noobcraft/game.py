
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
        self.world = World(game=self)

    def addPlayer(self, player):
        self.players.append(player)

    def start(self):
        self.world.placeStarters(self.players)

    def update(self):
        for player in self.players:
            player.act(self.world)
        self.world.update()

    def run(self):
        self.start()
        while not self.over:
            self.update()

    @property
    def over(self):
        return self.world.age >= 1000
