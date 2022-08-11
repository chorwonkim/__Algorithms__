import heapq
from sys import stdin
Read = stdin.readline

n, m = map(int, Read().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, Read().split())
    indegree[b] += 1
    graph[a].append(b)

def topology_sort():
    result = []
    q = []

    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(q, (i, i))

    while q:
        _, now = heapq.heappop(q)
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, (i, i))

    for i in result:
        print(i, end=' ')

topology_sort()