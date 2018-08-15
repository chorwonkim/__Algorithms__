from sys import stdin
from collections import deque
Read = stdin.readline

N, M = map(int, Read().split())
Map = [list(map(int, Read().split())) for _ in range(N)]
house = deque()
chicken = deque()
d = deque()
result = 10000000

for i in range(N):
    for j in range(N):
        if Map[i][j] == 1:
            house.append((i, j))
        elif Map[i][j] == 2:
            chicken.append((i, j))


def func_15686(x, d):
    if len(d) == M:
        length = 0

        for i in range(len(house)):
            dx = house[i][0]
            dy = house[i][1]
            temp = 100000000

            for j in range(M):
                ddx = chicken[d[j]][0]
                ddy = chicken[d[j]][1]

                temp = min(temp, abs(dx - ddx) + abs(dy - ddy))

            length += temp

        global result
        if result > length:
            result = length

        return

    for i in range(x, len(chicken)):
        d.append(i)
        func_15686(i+1, d)
        d.pop()


func_15686(0, d)
print(result)