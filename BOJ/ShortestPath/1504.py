# python 시간 초과, pypy3 틀린 상태
import heapq
from sys import stdin
Read = stdin.readline
INF = int(1e9)

n, e = map(int, Read().split())
graph = [[] for _ in range(n+1)]
distance = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, Read().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start][start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[start][now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[start][i[0]]:
                distance[start][i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

for i in range(1, n):
    dijkstra(i)

v1, v2 = map(int, Read().split())
result = distance[1][v1] + distance[v1][v2] + distance[v2][n]
if result >= INF:
    print(-1)
else:
    print(result)