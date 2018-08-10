from collections import deque

N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

d = deque()
count = 0

for i in range(N):
    for j in range(M):
        if Map[i][j] == 2:
            d.append((i, j))


while d:
    #  p, q =
    pass
