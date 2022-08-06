from collections import deque
from sys import stdin
Read = stdin.readline

n, m = map(int, Read().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, Read().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = [0] * (n+1)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append((i, 1))
            result[i] = 1

    while q:
        now, count = q.popleft()
        result[now] = count

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append((i, count+1))

    for i in result[1:]:
        print(i, end=' ')

topology_sort()