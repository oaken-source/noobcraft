
import math

from demo_players import InactivePlayer


class Game(object):

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

    def __init__(self, starters):
        self.age = 0
        self.units = starters

        n = len(starters)
        a = 2 * math.pi / n
        l = 1 / (2 * math.sin(a / 2))

        for i in range(len(self.units)):
            self.units[i].position = (l * math.cos(i * a), l * math.sin(i * a))

    def tick(self):
        self.age += 1


class Unit(object):

    def __repr__(self):
        return '<(%f, %f) - %s>' % (self.x, self.y, self.player.name)

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


if __name__ == '__main__':
    game = Game()
    game.addPlayer(InactivePlayer('Player1', 'red'))
    game.addPlayer(InactivePlayer('Player2', 'blue'))
    game.addPlayer(InactivePlayer('Player3', 'green'))

    game.run()
