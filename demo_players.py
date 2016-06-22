
'''
This module contains the demo players created for noobcraft.
'''

from noobcraft import Player


class InactivePlayer(Player):
    '''
    This demo player just does nothing.
    '''

    def act(self, world):
        pass


