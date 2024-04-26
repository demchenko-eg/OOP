from math import log

def t2d(x, eps):
    sum_terms = 0
    term = x
    k = x
    while abs(term) > eps:
        sum_terms += term
        k += 2
        term = (x ** k) / k
    return 2 * sum_terms


x = float(input('Введіть значення х: '))
eps = float(input('Введіть точність у вигляді десяткового дробу: '))
print(f'Обчислене значення {t2d(x, eps)}')
t = log((1 + x) / (1 - x))
print(f'Точне значення {t}')