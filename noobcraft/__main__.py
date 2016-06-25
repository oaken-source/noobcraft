
'''
This is the entry point of noobcrafts cli mode.
'''

from noobcraft.game import Game
from noobcraft.players.inactiveplayer import InactivePlayer
from noobcraft.players.aggressiveplayer import AggressivePlayer

if __name__ == '__main__':
    '''
    Executed when invoked from command line.
    '''
    game = Game()

    game.addPlayer(InactivePlayer('Player1', [0, 0, 0]))
    game.addPlayer(AggressivePlayer('Player2', [1, 0, 0]))
    game.addPlayer(AggressivePlayer('Player3', [0, 1, 0]))
    game.addPlayer(AggressivePlayer('Player4', [0, 0, 1]))
    game.addPlayer(InactivePlayer('Player5', [1, 1, 0]))
    game.addPlayer(InactivePlayer('Player6', [1, 0, 1]))
    game.addPlayer(AggressivePlayer('Player7', [0, 1, 1]))
    game.addPlayer(InactivePlayer('Player8', [1, 1, 1]))

    game.run()
