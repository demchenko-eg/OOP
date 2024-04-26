def t2c(x, eps):
    sum_terms = 0
    term = 1
    k = 0 
    while abs(term) > eps:
        sum_terms += term
        k += 1
        term = ((-1)**k) * (x**k)
    return sum_terms


x = float(input('Введіть значення х: '))
eps = float(input('Введіть точність у вигляді десяткового дробу: '))
print(f'Обчислене значення {t2c(x, eps)}')
print(f'Точне значення {1 / (1 + x)}')