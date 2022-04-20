# one=1 two=2 three=3
# d = dict([int(i) if i.isdigit() else i for i in row.split("=")] for row in input().split())
# print(*sorted(d.items()))


# lst_in =  ['5=отлично', '4=хорошо', '3=удовлетворительно']
# d = {}
# for row in lst_in:
#     rs = row.split("=")
#     d[int(rs[0])] = rs[1]
# print(*sorted(d.items()))


# вологда=город house=дом True=1 5=отлично 9=божественно
# d = dict(list(entry.split("=") for entry in input().split()))
# if 'house' in d and 'True' in d and '5' in d:
#     print('ДА')
# else:
#     print('НЕТ')


# лена=имя дон=река москва=город False=ложь 3=удовлетворительно True=истина
# d = dict(list(entry.split("=") for entry in input().split()))
# delete = ['False', '3']
# for i in delete:
#     if i in d:
#         d.pop(i)
# print(*sorted(d.items()))


## Сортировка телефонов в словаре по префиксам +X
## +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
# line = input().split()
#
# d = {}
# lst = [] # Список префиксов
#
# # Составляем список префиксов
# for entry in line:
#     pref = entry[:2]
#     if pref not in lst:
#         lst.append(pref)
#
# # Проверяем номера на префиксы и заносим их в словарь через временный список
# for pref in lst:
#     temp_lst = []
#     for entry in line:
#         if pref in entry:
#             temp_lst.append(entry)
#     d[pref] = temp_lst
#
# print(*sorted(d.items()))

## Не моя сортировка телефонов по префиксам
# lst_in = list(input().split())
# d = {}
# for entry in lst_in:
#     if entry[:2] not in d:
#         d[entry[:2]] = [entry]
#     else:
#         d[entry[:2]] = d[entry[:2]] + [entry]
# print(*sorted(d.items()))

## Ввод телефонных номеров по именам
# lst_in = ['+71234567890 Сергей', '+71234567810 Сергей', '+51234567890 Михаил', '+72134567890 Николай']
#
# d={}
# lst = list(string.split() for string in lst_in)
# for entry in lst:
#     phone = entry[0]
#     name = entry[1]
#     if name not in d:
#         d[name] = [phone]
#     else:
#         d[name] += [phone]
#
# print(*sorted(d.items()))


## Квадратные корни в цикле
# d = {}
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     else:
#         if n not in d:
#             sqr = round(n**.5, 2)
#             d[n] = sqr
#
#         else:
#             sqr = f'значение из кэша: {d[n]}'
#     print(sqr)


## Вывод HTML страниц из кэша
# lst_in = ['ustanovka-i-zapusk-yazyka', 'ustanovka-i-poryadok-raboty-pycharm', 'peremennyye-operator-prisvaivaniya-tipy-dannykh', 'arifmeticheskiye-operatsii', 'ustanovka-i-poryadok-raboty-pycharm']
# d = {}
# for entry in lst_in:
#     if entry not in d:
#         d[entry] = entry
#         text = f'HTML-страница для адреса {entry}'
#     else:
#         text = f'Взято из кэша: HTML-страница для адреса {d[entry]}'
#     print(text)

## Создать словарь из строки
# s = "int= целое число, dict=словарь, list=список, str=строка, bool=булевый тип"
#
# d = dict([[s.strip() for s in entry.split("=")] for entry in s.split(", ")])
# print(d)

# # Словарь из произвольных чисел; ключи только чётные, значения их квадраты
# d = {}
# while True:
#     n = input("Enter number: ")
#     if n.isdigit():
#         n = int(n)
#         if not n % 2:
#             print("Even number")
#             if n not in d:
#                 d[n] = n**2
#
#     else:
#         print("{n} is not a number...")
#     print(d)

## Кодирование в Морзе (русский алфавит)
# L = ''
# morze = {}
# while L != "11":
#     L = input("Введите букву (11 = выход): ")
#     if L == 11:
#         break
#     if L not in morze:
#         code = input(f'"Введите код для буквы{L}:')
#         morze[L] = code
# print(morze)

#morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-...-'}
# line = input().lower()
# l_coded = ([morze[l] + ' ' for l in line])
# s = ''
# for l in l_coded:
#     s += l
#
# print(s.strip())
## Не моё решение
# print(*[morze.get(i) for i in input().upper()])


## Раскодирование строки азбуки Морзе
# morze_rev = {v:k for k, v in morze.items()}
# l = [morze_rev[c] for c in input().split()]
# print(*l, sep='')

# # Упаковка предметов в рюкзак
# # Моё решение
# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10, 'нанохрень': 1}
#
# N = int(input())
# N = N * 1000
#
# # Создаём сортированный список весов
# weights = sorted(things.values(), reverse=True)
#
# w_in_bag = []  # Список весов предметов, которые окажутся в мешке (инвентаре)
# bag = []  # Список предметов в мешке
#
# # Пока общий вес предметов в мешке меньше заявленного, проверяется, войдёт ли в него имеющийся  # самый тяжёлый предмет, если проверка проходит, он помещается в список весов в мешке
# # и одновременно удаляется из общего списка весов, (самым тяжёлым оказывается следующий);
# # если проверка не проходит, самый тяжёлый просто удаляется
#
# while sum(w_in_bag) < N:
#     if len(weights) == 0:
#         break
#     elif max(weights) + sum(w_in_bag) <= N:
#         w_in_bag += [max(weights)]
#         weights.remove(max(weights))
#     else:
#         weights.remove(max(weights))
#
# # Итак, есть список весов предметов, осталось подобрать соответствующие предметы
#
# for w in w_in_bag:
#     for k, v in things.items():
#         if v == w:
#             bag += [k]
#
# print(*bag)

## Не моё решение
# d = {'карандаш': 20,'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,'расческа': 40, 'палатка': 5240, 'брезент': 2130, 'спички': 10, 'котелок': 820}
# mas = int(input()) * 1000
# count = 0
# d1 = {}
# for key, values in d.items():
#     d1[values] = [key]
# for key, values in sorted(d1.items())[::-1]:
#     if mas >= count + key:
#         print(*values, end=" ")
#         count += key