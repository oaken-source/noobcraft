class Rectangle(object):
    '''
    This class represents a world in noobcraft.
    '''
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def offset(self, x, y):
        return Rectangle(self.x + x, self.y + y, self.w, self.h)

    def shrinkCenter(self, margin):
        return Rectangle(self.x + margin/2, self.y + margin/2, self.w - margin, self.h - margin)