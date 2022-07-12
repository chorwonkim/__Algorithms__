# Dijkstra method using PriorityQueue(HeapQ)
import heapq
from sys import stdin
Read = stdin.readline
INF = int(1e9)

n, m, x = map(int, Read().split())
graph = [[] for _ in range(n+1)]
result = [0] * (n+1)

for _ in range(m):
    a, b, c = map(int, Read().split())
    graph[a].append((b, c))

def dijkstra(start, x):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[x]

for i in range(1, n+1):
    result[i] = dijkstra(i, x)

for i in range(1, n+1):
    result[i] += dijkstra(x, i)

print(max(result))