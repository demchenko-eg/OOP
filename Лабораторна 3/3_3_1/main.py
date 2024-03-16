from Circle import Circle
from Cone import Cone
from Parallelogram import Parallelogram
from Rectangle import Rectangle
from RectangularParallelepiped import RectangularParallelepiped
from QuadrangularPyramid import QuadrangularPyramid
from Ball import Ball
from SquarePyramid import SquarePyramid
from Trapeze import Trapeze
from Triangle import Triangle
from TriangularPyramid import TriangularPyramid
from TriangularPrism import TriangularPrism


def read_figures(filename):
    figures = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split()
            figure_name = data[0]
            parameters = list(map(float, data[1:]))
            if 0 in parameters:
                continue
            if figure_name == 'Triangle':
                if parameters[0] < parameters[1] + parameters[2] or parameters[1] < parameters[0] + parameters[2] or parameters[2] < parameters[1] + parameters[0]:
                    continue
                figures.append(Triangle(*parameters))
            elif figure_name == 'Rectangle':
                figures.append(Rectangle(*parameters))
            elif figure_name == 'Trapeze':
                figures.append(Trapeze(*parameters))
            elif figure_name == 'Parallelogram':
                figures.append(Parallelogram(*parameters))
            elif figure_name == 'Circle':
                figures.append(Circle(*parameters))
            elif figure_name == 'Ball':
                figures.append(Ball(*parameters))
            elif figure_name == 'TriangularPyramid':
                figures.append(TriangularPyramid(*parameters))
            elif figure_name == 'QuadrangularPyramid':
                figures.append(QuadrangularPyramid(*parameters))
            elif figure_name == 'RectangularParallelepiped':
                figures.append(RectangularParallelepiped(*parameters))
            elif figure_name == 'Cone':
                figures.append(Cone(*parameters))
            elif figure_name == 'TriangularPrism':
                if parameters[0] < parameters[1] + parameters[2] or parameters[1] < parameters[0] + parameters[2] or parameters[2] < parameters[1] + parameters[0]:
                    continue
                figures.append(TriangularPrism(*parameters))
            elif figure_name == 'SquarePyramid':
                figures.append(SquarePyramid(*parameters))
    return figures


def solve_task(filename):
    figures = read_figures(filename)
    with open("results_2.txt", "a") as file:
        file.write(filename + "\n")
        for figure in figures:
            file.write("Figure: " + type(figure).__name__ + "\n")
            file.write("Dimension: " + str(figure.dimension()) + "\n")
            if figure.dimension() == 3:
                file.write("Side surface area: " + str(figure.squareSurface()) + "\n")
                file.write("Base area: " + str(figure.squareBase()) + "\n")
                file.write("Volume: " + str(figure.volume()) + "\n")
                file.write("Height: " + str(figure.height()) + "\n")
                if type(figure).__name__ == 'RectangularParallelepiped' or type(figure).__name__ == 'TriangularPrism':
                    file.write("Total surface area: " + str(figure.square()) + "\n")
                # print("Периметр:", None)
                # print("Площа:", None)
            if figure.dimension() == 2:
                file.write("Petimeter: " + str(figure.perimetr()) + "\n")
                file.write("Area: " + str(figure.square()) + "\n")
                # print("Площа бічної поверхні:", None)
                # print("Площа основи:", None)
                # print("Об'єм:", None)
                # print("Висота:", None)
            file.write("\n")

if __name__ == '__main__':
    with open("results_2.txt", "w") as file:
        file.write("")

    solve_task('input01.txt')
    solve_task('input02.txt')
    solve_task('input03.txt')
