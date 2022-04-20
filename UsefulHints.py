# n = int(input())
# t = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
# print(t[n-1])

# k = int(input())
# lst = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
# print(lst[k % 7 - 1])
#
# a, b, c = map(int, input().split())

##
# m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
# sharp = [0, 3]
#
# prea = "#" if a-1 in sharp else ""
# preb = "#" if b-1 in sharp else ""
# prec = "#" if c-1 in sharp else ""
#
# print(prea + m[a - 1], preb + m[b - 1], prec + m[c - 1])

## Определение длины каждого слова из списка через пробелы
# print(*map(len, input().split()))

# У if тоже есть свой else
# n = int(input())
# for i in range(2, n):
#     if n % i == 0:
#         print('НЕТ')
#         break
# else:
#     print('ДА')


# Возвести в квадрат вводимые через пробел числа
# 8 -11 4 3 6
# print(*[int(i)**2 for i in input().split()])

## Подсчёт суммы чисел от 0 до 9
# sum = 0
# t = [] # List of all sums with their respective indices
# for n in range(0, 10):
#     sum +=n
#     t.append(sum)
#     print(f'For {n} sum = {sum}')
# print(t)
#
# probe = int(input("Enter your number: "))
# i = 0
# while t[i] < probe:
#     i+=1
# print(f'Max amount of numbers is {i}.')


## Список всех делителей числа
# n = int(input())
# lst = [x for x in range(1, n+1) if n%x == 0]
# print(*lst)

## Список городов и населения
# line = input().split()
# lst1 = [n if i%2==0 else int(n) for i, n in enumerate(line)]
# print(lst1)
#
# # Var 2
# line = input().split()
# lst1 = [[line[i-1]]+ [int(line[i])] for i in range(1, len(line),2)]
# print(lst1)


## Ввод в несколько строк
# text = ""
# while True:
#     x = input()
#     if x:
#         text += x + "\n"
#     else:
#         break
