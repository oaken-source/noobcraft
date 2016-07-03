
'''
This module handles the visual themes of noobcraft.
'''

import math

from browser import html
from noobcraft.rendering.rectangle import Rectangle
from noobcraft.rendering.character import Character

class BasicTheme():    

    def __init__(self):
        pass

    def drawTerrain(self, renderer, r, game, elapsedSeconds):
        renderer.fillRectangleNow(r, [0, 0.8, 0])

    def drawUnits(self, renderer, r, game, elapsedSeconds):
        for unit in game.world.units:
            renderer.fillCircleNow(400 + 200 * unit.x, 300 + 200 * unit.y, math.sqrt(unit.size), [0, 0, 0], unit.owner.primary_color)

    def drawActors(self, renderer, r, game, elapsedSeconds):
        for i, actor in enumerate(game.actors):
            text = "%s's %s" % (actor.creator, actor.name)            
            renderer.drawTextNow(r.x, r.y + 22 * i, text, actor.primary_color)

    def draw(self, renderer, game, elapsedSeconds):
        renderer.setFont('Arial', 14)

        r = Rectangle(0, 0, renderer.width, renderer.height)
        self.drawTerrain(renderer, r, game, elapsedSeconds)
        self.drawUnits(renderer, r, game, elapsedSeconds)
        renderer.flush()

        r = r.offset(5, 20)
        renderer.transforming = False
        renderer.setFont('Arial', 16)
        self.drawActors(renderer, r, game, elapsedSeconds)
        renderer.transforming = True

class RPGTheme(BasicTheme):    

    def directionMap(self, unit):
        if abs(unit.direction) <= 45: # up
            return 3
        if 45 < unit.direction and unit.direction < 135: # left
            return 2
        if -135 < unit.direction and unit.direction < -45: # right
            return 1
        return 0 # down

    def loadImages(self):
        self.terrainImage=html.IMG('', src='assets/rpg-theme/grass.png')
        self.characters.append(Character('assets/rpg-theme/characters/character-model-0.png', 48, 48, 2, self.directionMap))

    def __init__(self):
        self.tilewidth = 48
        self.tileheight = 48
        self.characters = []
        self.loadImages()

    def drawTerrain(self, renderer, r, game, elapsedSeconds):
        for x in range(r.x, r.x + r.w, self.tilewidth):
            for y in range(r.y, r.y + r.h, self.tileheight):
                renderer.drawImageNow(self.terrainImage, 0, 0, 48, 48, x, y, 48, 48)

    def drawUnits(self, renderer, r, game, elapsedSeconds):
        for unit in game.world.units:
            self.characters[unit.characterModel].draw(renderer, 400 + 200 * unit.x, 300 + 200 * unit.y, unit, elapsedSeconds)

class RealisticTheme(RPGTheme):    

    def directionMap(self, unit):
        if abs(unit.direction) <= 22.5: # N
            return 3
        if 22.5 < unit.direction and unit.direction <= 67.5: # NE
            return 7
        if 67.5 < unit.direction and unit.direction <= 112.5: # E
            return 2
        if 112.5 < unit.direction and unit.direction <= 157.5: # SE
            return 6
        if -157.5 < unit.direction and unit.direction <= -112.5: # SW
            return 4
        if -112.5 < unit.direction and unit.direction <= -67.5: # W
            return 1
        if -67.5 < unit.direction and unit.direction <= -22.5: # NW
            return 5
        return 0 # S
    
    def loadImages(self):
        self.terrainImage=html.IMG('', src='assets/realistic-theme/ground.png')
        self.characters.append(Character('assets/realistic-theme/characters/character-model-0-running.png', 128, 128, 7, self.directionMap))