
'''
This is the entry point of noobcrafts cli mode.
'''

from noobcraft.game import Game
from noobcraft.players.inactiveplayer import InactivePlayer

if __name__ == '__main__':
    '''
    Executed when invoked from command line.
    '''
    game = Game()

    game.addPlayer(InactivePlayer('Player1', [1, 0, 0]))
    game.addPlayer(InactivePlayer('Player2', [0, 1, 0]))
    game.addPlayer(InactivePlayer('Player3', [0, 0, 1]))
    game.addPlayer(InactivePlayer('Player4', [1, 1, 0]))
    game.addPlayer(InactivePlayer('Player5', [1, 0, 1]))

    game.start()
    while True:
        game.update()
