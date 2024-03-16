from Rectangle import Rectangle

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
    def dimension(self):
        return 3
    def squareSurface(self):
        return None
    def squareBase(self):
        return None
    def height(self):
        return None
    def square(self):
        return 2 * self.a * self.b + 2 * self.b * self.c + 2 * self.a * self.c
    def volume(self):
        return self.a * self.b * self.c