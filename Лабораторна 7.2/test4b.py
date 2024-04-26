def t4b(x, eps):
    a1 = x
    an = (16 + x) / (1 + abs(a1 ** 3))
    while abs(an - a1) > eps:
        a1 = an
        an = (16 + x) / (1 + abs(a1 ** 3))
    return an

x = float(input("Введіть дійсне число x: "))
eps = float(input("Введіть точність у вигляді десяткового дробу: "))
print(f"Границя послідовності a_n з точністю {eps}: {t4b(x, eps)}")