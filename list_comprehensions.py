## Формирование матрицы нулей с единицами по диагонали
# n = int(input())
# lst = [[1 if x == y else 0 for x in range(n)] for y in range(n)]
# [print(*row) for row in lst]

## Формирование матрицы нулей с единицами по диагонали//Чужое решение
# n = int(input())
# [print(*[0]*i + [1] + [0]*(n-i-1)) for i in range(n)]

## Формирование матрицы с рядами чисел
# n = int(input())
# lst = [[x for y in range(n)] for x in range(n)]
# [print(*row) for row in lst]