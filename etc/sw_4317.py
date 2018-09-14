# import sys
# sys.setrecursionlimit(1000000)
# Read = sys.stdin.readline
#
# T = int(Read())
# result = 0
#
#
# def func_sw_4317(x, y):
#     count = 0
#     checker = False
#     for i, j in zip([1, 0, 1], [0, 1, 1]):
#         dx = x + i
#         dy = y + j
#
#         if 0 <= dx < H and 0 <= dy < W:
#             if Map[dx][dy] == 1:
#                 break
#
#             visited[dx][dy] = 1
#             count += 1
#
#     if count == 3:
#         checker = True
#
#     return checker
#
#
# for i in range(1, T+1):
#     H, W = map(int, Read().split())
#     Map = [list(map(int, Read().split())) for _ in range(H)]
#
#     for i in range(H):
#         for j in range(W):
#             visited = [[0 for _ in range(W)] for _ in range(H)]
#
#             if Map[i][j] == 0:
#                 if func_sw_4317(i, j):
#                     result += 1
#
#
#     print(result)

import sys
sys.setrecursionlimit(1000000)
Read = sys.stdin.readline

T = int(Read())
result = 0


def func_sw_4317(x, y, count):
    visited[x][y] = 1

    for i, j in zip([1,0,1], [0,1,1]):
        dx = x + i
        dy = y + j

        if 0 <= dx < H and 0 <= dy < W:
            if not visited[dx][dy] and Map[dx][dy] == 0:
                visited[dx][dy] = 1
                count += 1

    if count == 3:
        return 1
    else:
        return 0


for i in range(1, T+1):
    H, W = map(int, Read().split())
    Map = [list(map(int, Read().split())) for _ in range(H)]
    visited = [[0 for _ in range(W)] for _ in range(H)]

    result = 0

    for i in range(H):
        for j in range(W):
            if Map[i][j] == 1:
                continue
            else:
                if visited[i][j]:
                    continue
                result += func_sw_4317(i, j, 0)

    print(result)