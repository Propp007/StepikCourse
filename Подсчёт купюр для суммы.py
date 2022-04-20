n = int(input())
# money = [64, 32, 16, 8, 4, 2, 1]
money = [5000, 2000, 1000, 500, 200, 100, 50, 10, 5, 2, 1]

for m in money:
    int_sum = n // m
    if int_sum !=0:
        print(f'{m}\t: {int_sum}')
    n = n % m


