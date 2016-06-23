
'''
This module handles the rendering of noobcraft.
'''

import math

from noobcraft.rendering.primitiverenderer import PrimitiveRenderer
from noobcraft.rendering.rectangle import Rectangle

class Renderer(PrimitiveRenderer):
    '''
    This class represents a world in noobcraft.
    '''
    def __init__(self):
        pass

    def drawTerrain(self, ctx, r, game):
        self.fillRectangle(ctx, r, [0.2, 0.8, 0.2])

    def drawPlayers(self, ctx, r, game):
        for playerId, player in enumerate(game.players):
            self.drawText(ctx, r.x, r.y + 20 * playerId, player.name, player.color)

    def drawUnits(self, ctx, r, game):
        for player in game.players:
            for unit in game.world.unitsOf(player):
                self.fillCircle(ctx, 400 + 200 * unit.x, 300 + 200 * unit.y, math.sqrt(unit.size), player.color)

    def draw(self, game, ctx):
        self.setFont(ctx, 'Arial', 14)

        r = Rectangle(0, 0, ctx.canvas.width-10, ctx.canvas.height-10)
        self.drawTerrain(ctx, r, game)
        self.drawUnits(ctx, r, game)

        r = r.offset(5, 20)
        self.drawPlayers(ctx, r, game)