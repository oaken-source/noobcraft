
import math

class Game(object):

    def __init__(self):
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)

    def run(self):
        starters = [ Unit(player) for player in self.players ]
        world = World(starters=starters)

        while world.age < 1000:
            for player in self.players:
                player.act(world)
            world.tick()

class World(object):

    def __init__(self, starters):
        self.age = 0
        self.units = starters

        n = len(starters)
        a = 2 * math.pi / n
        l = 1 / (2 * math.sin(a / 2))

        for i in range(len(self.units)):
            self.units[i].x = l * math.cos(i * a)
            self.units[i].y = l * math.sin(i * a)

        print(self.units)

    def tick(self):
        self.age += 1

class Unit(object):

    def __repr__(self):
        return '<(%f, %f) - %s>' % (self.x, self.y, self.player.name)

    def __init__(self, player):
        self.player = player
        self.x = 0.0
        self.y = 0.0

class Player(object):

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def deploy(self, world):
        pass

    def act(self, world):
        raise NotImplementedError()

class InactivePlayer(Player):

    def act(self, world):
        pass

if __name__ == '__main__':
    game = Game()
    game.addPlayer(InactivePlayer('Player1', 'red'))
    game.addPlayer(InactivePlayer('Player2', 'blue'))
    game.addPlayer(InactivePlayer('Player3', 'green'))

    result = game.run()
