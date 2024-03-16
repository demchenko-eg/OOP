from Rectangle import Rectangle

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h
    def volume(self):
        return 1 / 3 * self.squareBase() * self.h