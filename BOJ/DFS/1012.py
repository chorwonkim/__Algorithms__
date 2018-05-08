import sys
sys.setrecursionlimit(100000)

# RunTime Error..
# bug_dx = [0, 1, 0, -1]
# bug_dy = [1, 0, -1, 0]
#
# Land = []
# Zed = []
#
#
# def func_1012(y, x):
#     Zed[y][x] = True
#
#     # EWSN 4 direction
#     for i in range(4):
#         changed_x = x + bug_dx[i]
#         changed_y = y + bug_dy[i]
#
#         if x >= 0 and y >= 0 and changed_x < M and changed_y < N:
#             if Land[changed_y][changed_x] == 1 and (not Zed[changed_y][changed_x]):
#                 func_1012(changed_y, changed_x)
#
#
# testCase = int(input())
#
# for i in range(testCase):
#     Land.clear()
#     Zed.clear()
#     M, N, K = map(int, input().split())
#
#     for r in range(N):
#         Land.append([0]*M)
#         Zed.append([False]*M)
#
#     result = 0
#
#     # input the data that where are chinese cabbages.
#     for j in range(K):
#         cabbage_x, cabbage_y = map(int, input().split())
#
#         Land[cabbage_y][cabbage_x] = 1
#
#     for p in range(N):
#         for q in range(M):
#             if Land[p][q] == 1 and (not Zed[p][q]):
#                 func_1012(p, q)
#                 result += 1
#
#     print(result)

def func_1012(x, y):
    global Land
    Land[x][y] = 0

    if x-1>=0 and Land[x-1][y] == 1:
        func_1012(x-1, y)

    if x+1 < N and Land[x+1][y] == 1:
        func_1012(x+1, y)

    if y-1 >= 0 and Land[x][y-1] == 1:
        func_1012(x, y-1)

    if y+1 < M and Land[x][y+1] == 1:
        func_1012(x, y+1)


testCase = int(input())
result = [0 for i in range(testCase)]

for i in range(testCase):
    M, N, K = map(int, input().split())
    Land = [[0 for b in range(M)] for a in range(N)]

    for j in range(K):
        x, y = map(int, input().split())
        Land[y][x] = 1

    for a in range(N):
        for b in range(M):
            if Land[a][b] == 1:
                func_1012(a, b)
                result[i] += 1

print('\n'.join(map(str, result)))
