import math

from browser import html
from noobcraft.rendering.primitiverenderer import PrimitiveRenderer
from noobcraft.rendering.rectangle import Rectangle

class Character(PrimitiveRenderer):
    '''
    This class represents a world in noobcraft.
    '''
    def __init__(self, id):
    	self.zoom = 1
        self.image = html.IMG('', src='assets/characters/character-model-' + str(id) + '.png')
        self.directionMap = { 'S': 0, 'W': 1, 'E': 2, 'N': 3 }
        
        self.frameUpdateDelay = 0.4
        self.elapsedSinceLastFrameUpdate = 0
        self.frameIndex = 1
        self.maxFrameIndex = 2

    def update(self, elapsedSeconds):
    	self.elapsedSinceLastFrameUpdate += elapsedSeconds
        if self.elapsedSinceLastFrameUpdate > self.frameUpdateDelay:
            self.elapsedSinceLastFrameUpdate -= self.frameUpdateDelay
            self.frameIndex += 1
            if self.frameIndex > self.maxFrameIndex:
                self.frameIndex = 0

    def draw(self, ctx, x, y, unit, elapsedSeconds):
        self.update(elapsedSeconds)
        if not unit.isMoving:
        	frame = 1
        else:
        	frame = self.frameIndex
        self.drawImageX(
        	ctx,
        	self.image, 
        	frame * 48, 
        	self.directionMap[unit.direction] * 48, 
        	48, 
        	48, 
        	x - 24 * self.zoom, 
        	y - 24 * self.zoom, 
        	48 * self.zoom, 
        	48 * self.zoom
    	)
    	self.drawRectangle(ctx, Rectangle(x - 20 * self.zoom, y - 24 * self.zoom - 4, 40 * self.zoom, 4), [0, 0, 0])
    	self.fillRectangle(ctx, Rectangle(x - 20 * self.zoom, y - 24 * self.zoom - 3, min(math.sqrt(unit.size), 40 * self.zoom), 2), [0.8, 0, 0])