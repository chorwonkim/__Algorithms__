from collections import deque
from sys import stdin
Read = stdin.readline

n, m, k, x = map(int, Read().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, Read().split())
    graph[a-1].append(b-1)

length = [-1] * n
length[x-1] = 0

def bfs(start):
    queue = deque([start])

    while queue:
        temp = queue.popleft()

        for i in graph[temp]:
            if length[i] == -1:
                length[i] = length[temp] + 1
                queue.append(i)


bfs(x-1)

check = False
for i in range(n):
    if length[i] == k:
        print(i+1)
        check = True

if not check:
    print(-1)