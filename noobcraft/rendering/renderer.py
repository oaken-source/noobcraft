
'''
This module handles the rendering of noobcraft.
'''

import math

from browser import html
from noobcraft.rendering.primitiverenderer import PrimitiveRenderer
from noobcraft.rendering.rectangle import Rectangle

class Renderer(PrimitiveRenderer):
    '''
    This class represents a world in noobcraft.
    '''
    def __init__(self):
        self.terrainImage=html.IMG('', src='assets/grass.png')
        pass

    def drawTerrain(self, ctx, r, game):
        for x in range(r.x, r.x + r.w, 48):
            for y in range(r.y, r.y + r.h, 48):
                self.drawImage(ctx, x, y, self.terrainImage)
        #self.fillRectangle(ctx, r, [0.2, 0.8, 0.2])

    def drawActors(self, ctx, r, game):
        for i, actor in enumerate(game.actors):
            text = "%s's %s" % (actor.creator, actor.name)
            self.drawText(ctx, r.x, r.y + 20 * i, text, actor.primary_color)

    def drawUnits(self, ctx, r, game):
        for unit in game.world.units:
            self.fillCircle(ctx, 400 + 200 * unit.x, 300 + 200 * unit.y, math.sqrt(unit.size), unit.owner.primary_color, unit.owner.secondary_color)

    def draw(self, game, ctx):
        self.setFont(ctx, 'Arial', 14)

        r = Rectangle(0, 0, ctx.canvas.width-10, ctx.canvas.height-10)
        self.drawTerrain(ctx, r, game)
        self.drawUnits(ctx, r, game)

        r = r.offset(5, 20)
        self.drawActors(ctx, r, game)
