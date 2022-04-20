## Var 1.1
# row = [[1, 0, 0, 0, 0],
#        [0, 0, 1, 0, 1],
#        [0, 0, 0, 0, 0],
#        [0, 1, 0, 1, 0],
#        [0, 0, 0, 0, 0]]
#
# for i in range(5):
#     for j in range(4):
#         if row[i][j] == 1 and row[i][j] == row[i][j + 1]:
#             print(f"Match row {i} index {j} horizontally")
# for i in range(4):
#     for j in range(5):
#         if row[i][j] == 1 and row[i][j] == row[i + 1][j]:
#             print(f"Match row {i} index {j} vertically")
# for i in range(4):
#     for j in range(4):
#         if row[i][j] == 1 and row[i][j] == row[i+1][j + 1]:
#             print(f"Match row {i} index {j} diagonally lower")
#
# for i in range(1,5):
#     for j in range(4):
#         if row[i][j] == 1 and row[i][j] == row[i - 1][j + 1]:
#             print(f"Match row {i} index {j} diagonally higher")


## Var 1.2, сдача
# lst_in = [[1, 0, 0, 0, 0],
#           [0, 0, 1, 0, 1],
#           [0, 0, 0, 0, 0],
#           [0, 1, 0, 1, 0],
#           [0, 0, 0, 0, 0]]
# answer = "ДА"
# for i in range(5):
#     for j in range(4):
#         if lst_in[i][j] == 1 and lst_in[i][j] == lst_in[i][j + 1]:
#             answer ="НЕТ"
# for i in range(4):
#     for j in range(5):
#         if lst_in[i][j] == 1 and lst_in[i][j] == lst_in[i + 1][j]:
#             answer ="НЕТ"
# for i in range(4):
#     for j in range(4):
#         if lst_in[i][j] == 1 and lst_in[i][j] == lst_in[i+1][j + 1]:
#             answer ="НЕТ"
#
# for i in range(1,5):
#     for j in range(4):
#         if lst_in[i][j] == 1 and lst_in[i][j] == lst_in[i - 1][j + 1]:
#             answer ="НЕТ"
#
# print(answer)

# Var 2.0, Сдача прошла
lst_in = [[1, 0, 0, 0, 0],
          [0, 0, 1, 0, 1],
          [0, 0, 0, 0, 0],
          [0, 1, 0, 1, 0],
          [0, 0, 0, 0, 0]]

answer = "ДА"
for row in range(4):
    for item in range(4):
        sum =(lst_in[row][item] + lst_in[row + 1][item] + lst_in[row][item + 1] + lst_in[row + 1][item + 1])
        if  sum > 1:
            print(lst_in[row][item], sum)
            answer = "НЕТ"

print(answer)
