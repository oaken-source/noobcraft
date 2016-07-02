
'''
This module handles the rendering of noobcraft.
'''

import math

class PrimitiveRenderer(object):
    '''
    This class represents a world in noobcraft.
    '''
    def __init__(self):
        pass

    def setFont(self, ctx, name, size):
        self.fontName = name
        self.fontSize = size
        ctx.font = str(size) + 'px ' + name

    def setColor(self, ctx, rgb):
        ctx.fillStyle = 'rgba(' + str(math.floor(rgb[0] * 255)) + ',' + str(math.floor(rgb[1] * 255)) + ',' + str(math.floor(rgb[2] * 255)) + ',255)'
        ctx.strokeStyle = ctx.fillStyle

    def fillCircle(self, ctx, x, y, r, rgb1, rgb2):
        self.setColor(ctx, rgb1)
        ctx.beginPath()
        ctx.arc(x, y, r, 0, 2 * math.pi)
        self.setColor(ctx, rgb2)
        ctx.fill()

    def drawRectangle(self, ctx, r, rgb):
        self.setColor(ctx, rgb)
        ctx.beginPath()
        ctx.rect(r.x, r.y, r.w, r.h)
        ctx.stroke()

    def fillRectangle(self, ctx, r, rgb):
        self.setColor(ctx, rgb)
        ctx.beginPath()
        ctx.rect(r.x, r.y, r.w, r.h)
        ctx.fill()

    def drawText(self, ctx, x, y, text, rgb):
        self.setColor(ctx, rgb)
        ctx.fillText(text, x, y)

    def drawImage(self, ctx, x, y, img):
        ctx.drawImage(img, x, y);

    def drawImageX(self, ctx, img, sx, sy, sw, sh, dx, dy, dw, dh):
        ctx.drawImage(img, sx, sy, sw, sh, dx, dy, dw, dh)
        
