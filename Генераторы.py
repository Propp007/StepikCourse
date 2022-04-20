## 6.6
## Словарь по списку оценок
## 2 неудовлетворительно удовлетворительно хорошо отлично
# lst = input().split()
# p = int(lst.pop(0))
# d = {key: value for key, value in enumerate(lst, p)}
# print(d[4])

## Список уникальных машин, вывести количество
# lst_in = ['А323ГД', 'Д456ВВ', 'Б001ББ', 'Д456ВВ', 'С111СС']
# print(len(set(lst_in)))

## Количество слов в строке, длина которых не менее 3 символов
# s = set(w for w in input().lower().split() if len(w) >=3)
# print(len(s))

## Количество уникальных слов в строке
# line = input().lower().split()
# s = set(line) # Необязательно, множество для уникальности слов
# d = {w : line.count(w) for w in s}
# print(s)
# print(d['и'] if 'и' in d else 0)

## Спискок книг по авторам
lst_in = ['Пушкин: Сказака о рыбаке и рыбке', 'Есенин: Письмо к женщине', 'Тургенев: Муму', 'Пушкин: Евгений Онегин', 'Есенин: Русь']
listed = [entry.split(": ") for entry in lst_in]
print (listed)
# d = {}
# for entry in listed:
#     name = entry[0]
#     book = {entry[1]}
#     if not name in d:
#         d[name] = book
#     else:
#         d[name] = d[name].union(book)
# print(d)
s = {book[1] for book in listed}
d = {author[0]: {book[1] for book in listed if book[0] == author[0]} for author in listed}

print(s)
print(d)