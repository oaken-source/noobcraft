
'''
This module contains the demo players created for noobcraft.
'''


class Player(object):

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def act(self, world):
        raise NotImplementedError('override this method in your player.')


class InactivePlayer(Player):
    '''
    This demo player just does nothing.
    '''

    def act(self, world):
        pass


