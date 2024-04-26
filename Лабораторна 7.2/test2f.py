def t2f(x, eps):
    sum_terms = 0
    term = 1
    k = 0 
    while abs(term) > eps:
        sum_terms += term
        k += 2
        term = ((-1) ** (k % 2)) * (x ** k)
    return sum_terms


x = float(input('Введіть значення х: '))
eps = float(input('Введіть точність у вигляді десяткового дробу: '))
print(f'Обчислене значення {t2f(x, eps)}')
t = 1 / (1 + x ** 2)
print(f'Точне значення {t}')