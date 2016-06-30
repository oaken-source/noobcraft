
'''
This module represents the game.
'''

from noobcraft.gameobjects.world import World


class Game(object):
    '''
    This class represents a noobcraft game.
    '''
    def __init__(self):
        self.actors = []
        self.world = World(game=self)

    def addActor(self, actor):
        self.actors.append(actor)

    def start(self):
        self.world.placeStarters(self.actors)

    def update(self):
        for actor in self.actors:
            actor.act(self.world)
        self.world.update()

    def run(self):
        self.start()
        while not self.over:
            self.update()

    @property
    def over(self):
        return self.world.age >= 1000
