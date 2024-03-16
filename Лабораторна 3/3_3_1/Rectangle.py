from Figure import Figure

class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__(dim=2)
        self.a = a
        self.b = b
    def perimetr(self):
        return 2 * (self.a + self.b)
    def square(self):
        return self.a * self.b