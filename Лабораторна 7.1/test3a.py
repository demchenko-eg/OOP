def t3a(n):
    sum_value = 0
    for i in range(2, n + 1):
        sum_value += 1 / (i * (i - 1))
    return sum_value

n = int(input())
print(t3a(n))
