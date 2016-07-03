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

    def center(self):
        return [self.x + self.w / 2, self.y + self.h / 2]

    def zoom(self, factor):
        if factor is 1:
            return Rectangle(self.x, self.y, self.w, self.h)
        else:
            return Rectangle(self.x * factor, self.y * factor, self.w * factor, self.h * factor)

    def shrinkCenter(self, margin):
        return Rectangle(self.x + margin/2, self.y + margin/2, self.w - margin, self.h - margin)