from Equation import Equation
from QuadraticEquation import QuadraticEquation
from BiQuadraticEquation import BiQuadraticEquation


def read_equations(filename):
    equations = []
    with open(filename, 'r') as file:
        coeffs = []
        for line in file:
            line = line.strip()
            coeffs = list(map(float, line.split()))
            if len(coeffs) == 2:
                equations.append(Equation(coeffs[0], coeffs[1]))
            elif len(coeffs) == 3:
                equations.append(QuadraticEquation(coeffs[0], coeffs[1], coeffs[2]))
            elif len(coeffs) == 5:
                equations.append(BiQuadraticEquation(coeffs[0], coeffs[2], coeffs[4]))
    return equations


def solve_task(filename):
    with open("results_1.txt", "a") as file:
        file.write(f"{filename}\n")
        min_s = 0
        min_eq = []
        max_s = 0
        max_eq = []
        equations = read_equations(filename)
        for equation in equations:
            file.write("Equation:\n")
            equation.show(file)
            solutions = equation.solve()
            if solutions == Equation.INF:
                file.write("It has many solutions\n")
            elif len(solutions) == 0:
                file.write("There are no solutions\n")
            elif len(solutions) == 1:
                if solutions[0] > max_s:
                    max_s = solutions[0]
                    max_eq.clear()
                    max_eq.append(equation)
                elif solutions[0] < min_s:
                    min_s = solutions[0]
                    min_eq.clear()
                    min_eq.append(equation)
                file.write("It has a unique solution:\n")
                file.write(str(solutions[0]) + "\n")
            else:
                file.write("It has solutions:\n")
                for solution in solutions:
                    file.write(str(solution) + "\n")
            file.write("\n")
        file.write("The largest single solution has the equation:\n")
        max_eq[0].show(file)
        file.write("\n")
        file.write("The smallest unique solution has the equation:\n")
        min_eq[0].show(file)
        file.write("\n")

if __name__ == "__main__":
    with open("results_1.txt", "w") as file:
        file.write("")

    solve_task("input01.txt")
    solve_task("input02.txt")
    solve_task("input03.txt")
