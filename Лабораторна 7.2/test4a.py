from math import sqrt

def t4a(x, eps):
    a1 = x
    an = sqrt(abs(4 * a1 ** 2 - 2 * x))
    while abs(an - a1) > eps:
        a1 = an
        an = sqrt(abs(4 * a1 ** 2 - 2 * x))
    return an


x = float(input("Введіть дійсне число x: "))
eps = float(input("Введіть точність у вигляді десяткового дробу: "))
print(f"Границя послідовності a_n з точністю {eps}: {t4a(x, eps)}")