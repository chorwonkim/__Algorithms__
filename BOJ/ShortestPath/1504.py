# 1 -> v1 -> v2 -> n 또는 1 -> v2 -> v1 -> n의 두 가지 경우만 구해주면 됨
# 다익스트라를 굳이 모든 정점에 대해 할 필요 없음
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

v1, v2 = map(int, Read().split())

dijkstra(1)
dijkstra(v1)
dijkstra(v2)

result_1 = distance[1][v1] + distance[v1][v2] + distance[v2][n]
result_2 = distance[1][v2] + distance[v2][v1] + distance[v1][n]
result = 0
if result_1 < result_2:
    result = result_1
else:
    result = result_2

if result >= INF:
    print(-1)
else:
    print(result)