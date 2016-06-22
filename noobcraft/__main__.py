
'''
This is the entry point of noobcrafts cli mode.
'''

from noobcraft.gameobjects import Game
from noobcraft.players import InactivePlayer


if __name__ == '__main__':
    '''
    Executed when invoked from command line.
    '''
    game = Game()
    game.addPlayer(InactivePlayer('Player1', 'red'))
    game.addPlayer(InactivePlayer('Player2', 'blue'))
    game.addPlayer(InactivePlayer('Player3', 'green'))
    game.run()
