import math

from browser import html
from noobcraft.rendering.rectangle import Rectangle

class Character():
    '''
    This class represents a world in noobcraft.
    '''
    def __init__(self, imageSource, tileW, tileH, maxFrameIndex, directionMap):
        self.image = html.IMG('', src=imageSource)
        self.directionMap = directionMap

        self.tileW = tileW
        self.tileHalfW = tileW / 2
        self.tileH = tileH
        self.tileHalfH = tileH / 2

        self.frameUpdateDelay = 0.3
        self.elapsedSinceLastFrameUpdate = 0
        self.frameIndex = 1
        self.maxFrameIndex = maxFrameIndex

    def update(self, elapsedSeconds):
        self.elapsedSinceLastFrameUpdate += elapsedSeconds
        if self.elapsedSinceLastFrameUpdate > self.frameUpdateDelay:
            self.elapsedSinceLastFrameUpdate -= self.frameUpdateDelay
            self.frameIndex += 1
            if self.frameIndex > self.maxFrameIndex:
                self.frameIndex = 0

    def draw(self, renderer, x, y, unit, elapsedSeconds):
        self.update(elapsedSeconds)
        if not unit.isMoving:
            frame = 1
        else:
            frame = self.frameIndex
        renderer.drawImage(
            self.image,
            frame * self.tileW, self.directionMap(unit) * self.tileH, self.tileW, self.tileH, # source
            x - self.tileHalfW, y - self.tileHalfH, self.tileW, self.tileH # destination
        )
        renderer.drawRectangle(Rectangle(x - self.tileW * 0.4, y - self.tileHalfH - 4, self.tileW * 0.8, 4), [0, 0, 0])
        renderer.fillRectangle(Rectangle(x - self.tileW * 0.4, y - self.tileHalfH - 3, min(math.sqrt(unit.size), self.tileW * 0.8), 2), [0.8, 0, 0])
