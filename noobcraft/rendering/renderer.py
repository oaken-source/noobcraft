
'''
This module handles the rendering of noobcraft.
'''

import math

from noobcraft.rendering.rectangle import Rectangle

class Renderer(object):
    '''
    This class represents a world in noobcraft.
    '''
    def __init__(self):
        self.toDraw = []
        self.fontSize = 14
        self.zoom = 1
        self.offsetX = 0
        self.offsetY = 0
        self.transforming = True

    def setCtx(self, ctx):
        self.ctx = ctx

    def flush(self):
        self.toDraw = sorted(self.toDraw, key=lambda x: x[0])
        for todo in self.toDraw:
            todo[1](*todo[2])
        self.toDraw = []

    @property
    def width(self):
        return self.ctx.canvas.width

    @property
    def height(self):
        return self.ctx.canvas.height

    def setFont(self, name, size):
        self.fontName = name
        if self.transforming:
            self.fontSize = size * self.zoom
        else:
            self.fontSize = size
        self.ctx.font = str(self.fontSize) + 'px ' + name

    def setColor(self, rgb):
        self.ctx.fillStyle = 'rgba(' + str(math.floor(rgb[0] * 255)) + ',' + str(math.floor(rgb[1] * 255)) + ',' + str(math.floor(rgb[2] * 255)) + ',255)'
        self.ctx.strokeStyle = self.ctx.fillStyle

    # real drawing

    def fillCircleNow(self, x, y, r, rgb1, rgb2):
        self.setColor(rgb1)
        self.ctx.beginPath()
        if self.transforming:
            self.ctx.arc((x + self.offsetX)*self.zoom, (y + self.offsetY)*self.zoom, r * self.zoom, 0, 2 * math.pi)
        else:
            self.ctx.arc(x, y, r, 0, 2 * math.pi)
        self.setColor(rgb2)
        self.ctx.fill()

    def drawRectangleNow(self, r, rgb):
        if self.transforming:
            r = r.offset(self.offsetX, self.offsetY).zoom(self.zoom)
        self.setColor(rgb)
        self.ctx.beginPath()
        self.ctx.rect(r.x, r.y, r.w, r.h)
        self.ctx.stroke()

    def fillRectangleNow(self, r, rgb):
        if self.transforming:
            r = r.offset(self.offsetX, self.offsetY).zoom(self.zoom)
        self.setColor(rgb)
        self.ctx.beginPath()
        self.ctx.rect(r.x, r.y, r.w, r.h)
        self.ctx.fill()

    def drawTextNow(self, x, y, text, rgb):
        self.setColor(rgb)
        if self.transforming:
            self.ctx.fillText(text, (x + self.offsetX)*self.zoom, (y + self.offsetY)*self.zoom)
        else:
            self.ctx.fillText(text, x, y)

    def drawImageNow(self, img, sx, sy, sw, sh, dx, dy, dw, dh):
        if self.transforming:
            r = Rectangle(dx, dy, dw, dh).offset(self.offsetX, self.offsetY).zoom(self.zoom)
        self.ctx.drawImage(img, sx, sy, sw, sh, r.x, r.y, r.w, r.h)

    # will not be drawn until flush is called

    def fillCircle(self, x, y, r, rgb1, rgb2):
        self.toDraw.append([y - r, self.fillCircleNow, [x, y, r, rgb1, rgb2]])

    def drawRectangle(self, r, rgb):
        self.toDraw.append([r.y, self.drawRectangleNow, [r, rgb]])

    def fillRectangle(self, r, rgb):
        self.toDraw.append([r.y, self.fillRectangleNow, [r, rgb]])

    def drawText(self, x, y, text, rgb):
        self.toDraw.append([y, self.drawTextNow, [x, y, text, rgb]])

    def drawImage(self, img, sx, sy, sw, sh, dx, dy, dw, dh):
        self.toDraw.append([dy, self.drawImageNow, [img, sx, sy, sw, sh, dx, dy, dw, dh]])
