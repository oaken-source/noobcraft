
'''
This module handles the rendering of noobcraft.
'''

import math

from browser import html
from noobcraft.rendering.primitiverenderer import PrimitiveRenderer
from noobcraft.rendering.rectangle import Rectangle
from noobcraft.rendering.character import Character

class Renderer(PrimitiveRenderer):    
    '''
    This class represents a world in noobcraft.
    '''
    def __init__(self):
        self.tilewidth = 48
        self.tileheight = 48
        self.terrainImage=html.IMG('', src='assets/grass.png')
        self.characters = []
        self.characters.append(Character(0))

    def drawTerrain(self, ctx, r, game, elapsedSeconds):
        for x in range(r.x, r.x + r.w, self.tilewidth):
            for y in range(r.y, r.y + r.h, self.tileheight):
                self.drawImage(ctx, x, y, self.terrainImage)

    def drawActors(self, ctx, r, game, elapsedSeconds):
        for i, actor in enumerate(game.actors):
            text = "%s's %s" % (actor.creator, actor.name)
            self.drawText(ctx, r.x, r.y + 20 * i, text, actor.primary_color)

    def drawUnits(self, ctx, r, game, elapsedSeconds):
        for unit in game.world.units:
            self.characters[unit.characterModel].draw(ctx, 400 + 200 * unit.x, 300 + 200 * unit.y, unit, elapsedSeconds)
            #self.fillCircle(ctx, 400 + 200 * unit.x, 300 + 200 * unit.y, math.sqrt(unit.size), unit.owner.primary_color, unit.owner.secondary_color)

    def draw(self, game, ctx, elapsedSeconds):
        self.setFont(ctx, 'Arial', 14)

        r = Rectangle(0, 0, ctx.canvas.width-10, ctx.canvas.height-10)
        self.drawTerrain(ctx, r, game, elapsedSeconds)
        self.drawUnits(ctx, r, game, elapsedSeconds)

        r = r.offset(5, 20)
        self.drawActors(ctx, r, game, elapsedSeconds)
