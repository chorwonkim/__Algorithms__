from sys import stdin

Read = stdin.readline

T, length = map(int, Read().split())
Map = [[0 for _ in range(100)] for _ in range(100)]

values = list(map(int, Read().split()))
values_A = values[0::2]
values_B = values[1::2]

for x, y in zip(values_A, values_B):
    Map[x][y] = 1

# Case#1. Floyd
# for k in range(100):
#     for i in range(100):
#         for j in range(100):
#             if Map[i][k] and Map[k][j]:
#                 Map[i][j] = Map[j][i] = 1
#
#
# if Map[0][99]:
#     print(1)
# else:
#     print(0)

