
'''
This module handles the rendering of noobcraft.
'''

import math

from browser import html
from noobcraft.rendering.rectangle import Rectangle
from noobcraft.rendering.character import Character

class RPGTheme():    
    '''
    This class represents a world in noobcraft.
    '''
    def __init__(self):
        self.tilewidth = 48
        self.tileheight = 48
        self.terrainImage=html.IMG('', src='assets/grass.png')
        self.characters = []
        self.characters.append(Character(0))

    def drawTerrain(self, renderer, r, game, elapsedSeconds):
        for x in range(r.x, r.x + r.w, self.tilewidth):
            for y in range(r.y, r.y + r.h, self.tileheight):
                renderer.drawImageNow(self.terrainImage, 0, 0, 48, 48, x, y, 48, 48)

    def drawActors(self, renderer, r, game, elapsedSeconds):
        for i, actor in enumerate(game.actors):
            text = "%s's %s" % (actor.creator, actor.name)
            renderer.drawTextNow(r.x, r.y + 20 * i, text, actor.primary_color)

    def drawUnits(self, renderer, r, game, elapsedSeconds):
        for unit in game.world.units:
            self.characters[unit.characterModel].draw(renderer, 400 + 200 * unit.x, 300 + 200 * unit.y, unit, elapsedSeconds)

    def draw(self, renderer, game, elapsedSeconds):
        renderer.setFont('Arial', 14)

        r = Rectangle(0, 0, renderer.width-10, renderer.height-10)
        self.drawTerrain(renderer, r, game, elapsedSeconds)
        self.drawUnits(renderer, r, game, elapsedSeconds)
        renderer.flush()

        r = r.offset(5, 20)
        self.drawActors(renderer, r, game, elapsedSeconds)
