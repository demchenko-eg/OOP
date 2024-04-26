from math import factorial, sinh

def t2a(x, eps):
    sum_terms = 0
    term = x
    k = 1  
    while abs(term) > eps:
        sum_terms += term
        k += 2
        term = (x ** k) / factorial(k)
    return sum_terms


x = float(input('Введіть значення х: '))
eps = float(input('Введіть точність у вигляді десяткового дробу: '))
print(f'Обчислене значення {t2a(x, eps)}')
print(f'Точне значення {sinh(x)}')