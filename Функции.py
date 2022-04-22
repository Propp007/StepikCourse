# def get_square(x):
#     return x**2
#
#
# N = float(input())
# print(get_square(N))

## Стороны ли это треугольника
# def is_triangle(a, b, c):
#     return True if a+b > c and a+c > b and b+c > a else False
#
#
# print(is_triangle(3, 4, 5))

## Returns True or False
# def is_large(s):
#     return if len (s) < 3


## Список только нечётных
# def is_odd(x):
#     return x % 2
#
#
# l_in = list(map(int, input().split()))
# lst = [n for n in l_in if is_odd(n)]
# print(*lst)

## 7.2 Подвиг 8
# def my_func(l):
#     return (l, len(l))
#
#
# d = dict(my_func(city) for city in input().split())
# a = sorted(d, key=lambda x: d[x])
# print(*a)

## 7.2 Подвиг 9
# def my_func(a, b):
#     return a * b
#
#
# lst = list(map(int, input().split()))
# print( my_func(max(lst), min(lst)))

def make_tag(s, tag="h1"):
    return f"<{tag}>{s}</{tag}>"


text = input()
print(make_tag(text))
print(make_tag(text, tag = "div"))