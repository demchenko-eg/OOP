import math
from random import randint

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_valid(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a
    def perimeter(self):
        return self.a + self.b + self.c if self.is_valid() else None
    def area(self):
        if not self.is_valid():
            return None
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def perimeter(self):
        return 2 * (self.a + self.b)
    def area(self):
        return self.a * self.b

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    def area(self):
        if self.b == self.a:
            return None
        sqrt = ((self.c ** 2) - (((((self.b - self.a) ** 2) + (self.c ** 2) - (self.d ** 2)) / (2 * (self.b - self.a)))) ** 2)
        if sqrt < 0:
            return None
        return ((self.a + self.b)/2) * math.sqrt(sqrt)

class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
    def perimeter(self):
        return 2 * (self.a + self.b)
    def area(self):
        return self.a * self.h

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def perimeter(self):
        return 2 * math.pi * self.radius
    def area(self):
        return math.pi * (self.radius ** 2)

def read_input(file_path):
    shapes = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            shape_type = parts[0]
            parameters = list(map(float, parts[1:]))
            if shape_type == 'Triangle':
                shapes.append(Triangle(*parameters))
            elif shape_type == 'Rectangle':
                shapes.append(Rectangle(*parameters))
            elif shape_type == 'Trapeze':
                shapes.append(Trapeze(*parameters))
            elif shape_type == 'Parallelogram':
                shapes.append(Parallelogram(*parameters))
            elif shape_type == 'Circle':
                shapes.append(Circle(*parameters))
    return shapes

def max_area_and_perimeter(shapes):
    max_area_shape = None
    max_perimeter_shape = None
    max_area = 0
    max_perimeter = 0
    for shape in shapes:
        area = shape.area()
        perimeter = shape.perimeter()
        if area is not None and area > max_area:
            max_area = area
            max_area_shape = shape
        if perimeter is not None and perimeter > max_perimeter:
            max_perimeter = perimeter
            max_perimeter_shape = shape
    return max_area_shape, max_perimeter_shape

if __name__ == "__main__":
    
    # Через параметри випадкової генерації максимальний периметр
    # і площа в переважній більшості випадків будуть у кола

    N_MAXKEY = 25
    MULT = 4
    Figures = {"Triangle" : 3,
               "Rectangle" : 2,
               "Trapeze" : 4,
               "Parallelogram" : 3, 
               "Circle" : 1, 
               }
    FigureNames = list(Figures.keys())

    def generate(fname, figures_number):
        FUGUGE_COUNT = len(FigureNames)
        with open(fname, "w", encoding='utf-8') as f_out:
            for i in range(figures_number):
                figure = FigureNames[randint(0, FUGUGE_COUNT - 1)]
                print("%30s" % figure, file=f_out, end=" ")

                val_num = Figures[figure]
                for i in range(val_num):
                    val = randint(0, N_MAXKEY)
                    print("%4d" % val, file=f_out, end=" ")
                print(file=f_out)

    generate("input01.txt", 100)
    generate("input02.txt", 500)
    generate("input03.txt", 1000)

    file_paths = ["input01.txt", "input02.txt", "input03.txt"]
    for file_path in file_paths:
        shapes = read_input(file_path)
        max_area_shape, max_perimeter_shape = max_area_and_perimeter(shapes)

        print(f"\nFile: {file_path}")
        print(f"Максимальну площу має фігура: {max_area_shape.__class__.__name__}")
        print(f"Її площа становить {round(max_area_shape.area(), 3)}")
        print(f"Максимальний мериметр має фігура: {max_perimeter_shape.__class__.__name__}")
        print(f"Її периметр становить {round(max_perimeter_shape.perimeter(), 3)}")