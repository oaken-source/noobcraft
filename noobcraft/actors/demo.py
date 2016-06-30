
'''
This module contains the demo actors created for noobcraft.
'''

import math
import random

from noobcraft.actors.actor import Actor
from noobcraft.util.geometry import Vec2


class DemoActor(Actor):
    '''
    This is the base class for the demo actors.
    '''
    @property
    def name(self):
        return type(self).__name__

    @property
    def creator(self):
        return 'NoobCraft'


class LazyActor(DemoActor):
    '''
    This demo actor just does nothing.
    '''
    @property
    def primary_color(self):
        return (0, 0, 0)

    @property
    def secondary_color(self):
        return (0.1, 0.1, 0.1)

    def act(self, world):
        pass


class RandomActor(DemoActor):
    '''
    This demo actor will move its unit around randomly.
    '''
    @property
    def primary_color(self):
        return (0, 1, 0)

    @property
    def secondary_color(self):
        return (0.1, 0.9, 0.1)

    def act(self, world):
        owned = [e for e in world.units if e.owner == self]
        for unit in owned:
            unit.moveTowards(Vec2(direction=random.uniform(0, 2 * math.pi)), 1)


class BerserkActor(DemoActor):
    '''
    This demo actor always attacks its nearest neighbor.
    '''
    @property
    def primary_color(self):
        return (1, 0, 0)

    @property
    def secondary_color(self):
        return (0.9, 0.1, 0.1)

    def act(self, world):
        owned = [e for e in world.units if e.owner == self]
        enemies = [e for e in world.units if e.owner != self]
        for unit in owned:
            enemy = min(enemies, key=lambda v, u=unit: abs(u.pos - v.pos))
            if unit.inRange(enemy):
                unit.attack(enemy)
            else:
                unit.moveTowards(enemy.pos, 1)
