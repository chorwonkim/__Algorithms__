import sys
sys.setrecursionlimit(1000000)

N = int(input())
Map = [list(map(str, input())) for _ in range(N)]
color = 0
allcount = discount = 0


def func_10026(x, y):
    if visited[x][y] or Map[x][y] != color:
        return

    visited[x][y] = True

    for i, j in zip([-1,0,1,0],[0,-1,0,1]):
        dx = x + i
        dy = y + j

        if 0 <= dx < N and 0 <= dy < N:
            func_10026(dx, dy)


visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            allcount += 1
            color = Map[i][j]
            func_10026(i, j)

visited = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if Map[i][j] == 'R':
            Map[i][j] = 'G'


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            discount += 1
            color = Map[i][j]
            func_10026(i, j)

print(allcount, discount)