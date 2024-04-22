def t3b(n):
    sum_value = 0
    for i in range(1, n + 1):
        sum_value += ((-1) ** i) * (i - 1) / i
    return sum_value

n = int(input())
print(t3b(n))
