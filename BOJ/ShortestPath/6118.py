import heapq
from sys import stdin
Read = stdin.readline
INF = int(1e9)

n, m = map(int, Read().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, Read().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
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

dijkstra(1)

length = max(distance[1:])
result = 0
count = 0
for i in range(1, n+1):
    if distance[i] == length:
        result = i
        break

for i in range(1, n+1):
    if distance[i] == length:
        count += 1

print(result, length, count)

