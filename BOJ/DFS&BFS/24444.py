from sys import stdin
from collections import deque
Read = stdin.readline

n, m, r = map(int, Read().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, Read().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(graph, start, count):
    queue = deque([start])
    visited[start] = count

    while queue:
        v = queue.popleft()
        graph[v].sort()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                count += 1
                visited[i] = count


visited = [0] * (n+1)
count = 1
bfs(graph, r, count)

for i in range(n):
    print(visited[i+1])