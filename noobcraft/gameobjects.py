
'''
This module defines the game objects present in noobcraft.
'''

import math


class Game(object):
    '''
    This class represents a noobcraft game.
    '''
    def __init__(self):
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)

    def run(self):
        self.world = World(
            starters = [ Unit(player) for player in self.players ]
        )

        while not self.over:
            for player in self.players:
                player.act(self.world)
            self.world.tick()

    @property
    def over(self):
        return self.world.age >= 1000


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


class Unit(object):
    '''
    This class represents a unit of control for the players.
    '''
    def __init__(self, player):
        self.player = player
        self.position = (0.0, 0.0)
        self.speed = 1

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    def tick(self):
        pass


