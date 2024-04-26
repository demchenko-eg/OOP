from math import log

def t2b(x, eps):
    sum_terms = 0
    term = x
    k = 1  
    while abs(term) > eps:
        sum_terms += term
        k += 1
        term = ((-1)**k) * (x ** k) / k
    return sum_terms


x = float(input('Введіть значення х: '))
eps = float(input('Введіть точність у вигляді десяткового дробу: '))
print(f'Обчислене значення {t2b(x, eps)}')
print(f'Точне значення {log(1 + x)}')