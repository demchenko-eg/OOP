from Rectangle import Rectangle

class SquarePyramid(Rectangle):
    def __init__(self, a, h):
        super().__init__(a, a)
        self.h = h
    def volume(self):
        return 1 / 3 * self.squareBase() * self.h