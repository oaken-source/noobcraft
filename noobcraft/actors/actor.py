
'''
This module contains the abstract actor in the world of noobcraft.
'''

class Actor(object):
    '''
    This is the abstract actor class. All actors should inherit from it.
    '''

    @property
    def name(self):
        '''
        each actor needs a name - this property should produce it
        '''
        raise NotImplementedError('override this method in your actor.')

    @property
    def creator(self):
        '''
        this property should produce the name of whoever created the actor.
        '''
        raise NotImplementedError('override this method in your actor.')

    @property
    def primary_color(self):
        '''
        this property should produce the primary color of the actor for rendering
        '''
        raise NotImplementedError('override this method in your actor.')

    @property
    def secondary_color(self):
        '''
        this property should produce the secondary color of the actor for rendering
        '''
        raise NotImplementedError('override this method in your actor.')

    def act(self, world):
        '''
        this method is invoked once per round to allow your actor to choose its actions
        '''
        raise NotImplementedError('override this method in your actor.')
