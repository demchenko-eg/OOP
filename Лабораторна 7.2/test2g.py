from math import sqrt

def t2g(x, eps):
    sum_terms = 1
    term = 1
    k = 1
    while True:
        term *= ((2 * k - 1) / (2 * k)) * x
        sum_terms += term
        if abs(term) < eps:
            break
        k += 1
    return sum_terms


x = float(input('Введіть значення х: '))
eps = float(input('Введіть точність у вигляді десяткового дробу: '))
print(f'Обчислене значення {t2g(x, eps)}')
print(f'Точне значення {sqrt(1+x)}')