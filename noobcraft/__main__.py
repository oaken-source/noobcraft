
'''
This is the entry point of noobcrafts cli mode.
'''

from noobcraft.game import Game
from noobcraft.actors.demo import LazyActor, RandomActor, BerserkActor

if __name__ == '__main__':
    '''
    Executed when invoked from command line.
    '''
    game = Game()

    game.addActor(LazyActor())
    game.addActor(RandomActor())
    game.addActor(BerserkActor())

    game.run()
