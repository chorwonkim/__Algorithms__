import sys
Read = sys.stdin.readline
sys.setrecursionlimit(10000000)


def func_4963(y, x):
    Map[y][x] = 100

    for p, q in zip([1, -1, 0, 0, 1, 1, -1, -1], [0, 0, 1, -1, 1, -1, 1, -1]):
        di = p + y
        dj = q + x

        if 0 <= di < N and 0 <= dj < M:
            if Map[di][dj] == 1:
                func_4963(di, dj)


while True:
    M, N = map(int, Read().split())
    result = 0

    if not N and not M:
        break

    Map = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        temp = list(map(int, Read().split()))
        for j in range(M):
            Map[i][j] = temp[j]

    for i in range(N):
        for j in range(M):
            if Map[i][j] == 1:
                result += 1
                func_4963(i, j)

    print(result)



