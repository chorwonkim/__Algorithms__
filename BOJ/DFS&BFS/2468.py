import sys
Read = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(Read())
Map = [list(map(int, Read().split())) for _ in range(N)]
count = 0
result = 1


def func_2468(x, y, k):
    if Map_checker[x][y] or Map[x][y] <= k:
        return

    Map_checker[x][y] = True

    for i, j in zip([1,0,-1,0],[0,1,0,-1]):
        dx = x + i
        dy = y + j

        if 0 <= dx <= N-1 and 0 <= dy <= N-1:
            if not Map_checker[dx][dy]:
                func_2468(dx, dy, k)

    return


for k in range(1, 101):

    count = 0

    Map_checker = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if Map[i][j] > k and not Map_checker[i][j]:
                func_2468(i, j, k)
                count += 1

    result = max(result, count)

print(result)

