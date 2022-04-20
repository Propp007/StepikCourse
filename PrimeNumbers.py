# Моё решение
# number = int(input())
#
# for n in range(2,number):
#     a = True
#     for j in range(2, n//2 + 1):
#         if n % j != 0:
#             continue
#         elif n % j ==0:
#             a = False
#             break
#
#     if a == True:
#         print(n, end = " ")
#
# n = int(input())
# lst = []
# for i in range(2,n):
#     for j in range(2, i//2+1):
#         if i % j == 0:
#             break
#     else:
#         print(i, end = ' ')




# Другие решения
# n = int(input())
# lst = []
# for i in range(2,n):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         lst.append(i)
# print(*lst)

## С решетом Эратосфена
# n = int(input())
# sieve = [0, 0] + [1] * (n - 2)
# print(sieve)
# for i in range(2, n):
#     if sieve[i]:
#         for j in range(i * i, n, i):
#             sieve[j] = 0
# print(*(i for i, e in enumerate(sieve) if e))

