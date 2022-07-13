import heapq
from sys import stdin
Read = stdin.readline
INF = int(1e9)

n, m, r = map(int, Read().split())
items = [0] + list(map(int, Read().split()))
graph = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, c = map(int, Read().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start, distance):
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

result = 0
for i in range(1, n+1):
    distance = [INF] * (n+1)
    dijkstra(i, distance)

    temp = 0
    for j in range(1, n+1):
        if distance[j] > m:
            continue
        else:
            temp += items[j]
    
    if result < temp:
        result = temp

print(result)