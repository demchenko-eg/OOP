from Figure import Figure

class Circle(Figure):
    def __init__(self, radius):
        super().__init__(dim=2)
        self.radius = radius
    def perimetr(self):
        return 2 * 3.14 * self.radius
    def square(self):
        return 3.14 * self.radius ** 2