from math import factorial

def t3b(x, epsilon):
    sum_terms = 0
    term = 1
    k = 0
    while True:
        sum_terms += term
        term = (((-1) ** k) * (x ** (2 * k + 1))) / (factorial(k) * (2 * k + 1))
        if abs(term) < epsilon:
            break
        k += 1
    return sum_terms, k + 1


x = float(input('Введіть значення х: '))
eps = float(input('Введіть точність у вигляді десяткового дробу: '))
t = t3b(x, eps)
print(f'Обчислене значення: {t[0]}')
print(f'Кількість обчислених членів: {t[1]}')