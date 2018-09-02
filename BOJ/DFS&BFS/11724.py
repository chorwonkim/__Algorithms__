from sys import stdin
from collections import deque
Read = stdin.readline

N, M = map(int, Read().split())
Map = {}
visited = [False for _ in range(N+1)]
result = 0

for i in range(1, N+1):
    Map[i] = []

for _ in range(M):
    x, y = map(int, Read().split())

    Map[x].append(y)
    Map[y].append(x)


def func_11724(start):
    d = deque()
    d.appendleft(start)
    visited[start] = True

    while d:
        temp = d.popleft()

        for t in Map.get(temp):
            if visited[t]:
                continue

            d.append(t)
            visited[t] = True

    global result
    result += 1


for i in range(1, N+1):
    if visited[i]:
        continue

    func_11724(i)

print(result)
