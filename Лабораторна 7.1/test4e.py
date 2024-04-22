def minor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]

def det(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        det = 0
        for j in range(n):
            det += ((-1) ** j) * matrix[0][j] * det(minor(matrix, 0, j))
        return det


n = int(input("Введіть порядок матриці: "))
a = int(input("Введіть значення  параметра а: "))

matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j] = a
        elif abs(i - j) == 1:
            matrix[i][j] = 1
for row in matrix:
    print(row)
print(det(matrix))