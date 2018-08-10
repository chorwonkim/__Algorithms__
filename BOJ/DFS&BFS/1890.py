import sys
sys.setrecursionlimit(100000)

N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
result = 0
dp[0][0] = 1


# N = 100이기에 시간 초과의 가능성 존재
# def func_1890(x, y):
#     if x == N-1 and y == N-1:
#         global result
#         result += 1
#
#     moving = Map[x][y]
#
#     if moving:
#         for i, j in zip([moving, 0], [0, moving]):
#             dx = x + i
#             dy = y + j
#
#             if dx < N and dy < N:
#                 func_1890(dx, dy)
#
#
# func_1890(0, 0)
# print(result)

# 결국 생각한게 DP....
for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1 and Map[i][j] == 0:
            continue

        moving = Map[i][j]

        for x, y in zip([moving, 0], [0, moving]):
            dx = i + x
            dy = j + y

            if dx < N and not y:
                dp[dx][j] += dp[i][j]

            if dy < N and not x:
                dp[i][dy] += dp[i][j]


print(dp[N-1][N-1])