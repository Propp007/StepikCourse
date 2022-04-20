# +7(123)456-78-99
# Моё решение
# line = list(input())
# length = len(line)
# chars = ["+", "7", "(", ")", "-", "-"]
# numers = [3, 4, 5, 7, 8, 9, 11, 12, 14, 15]
# digits = []
#
# for i in numers:
#     digits.append(line[i])
#
# line.remove("7")
# for n in digits:
#     line.remove(n)
# line.insert(1, "7")
#
# digitline = "".join(digits)
#
# if not digitline.isdigit() or not line == chars or not length == 16:
#     print("НЕТ")
# else:
#     print("ДА")


# Чужое решение
# s = '+7(xxx)xxx-xx-xx'
# num = input()
# count = 0
# if len(s) == len(num):
#     for i, item in enumerate(num):
#         if s[i] == item or s[i] == 'x' and item.isdigit():
#             count += 1
#
# print('ДА' if count == 16 else 'НЕТ')




