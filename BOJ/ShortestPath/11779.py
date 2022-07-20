import heapq
from sys import stdin
Read = stdin.readline
INF = int(1e9)

n = int(Read())
m = int(Read())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, Read().split())
    graph[a].append((b, c))

start, end = map(int, Read().split())
path = [[] for _ in range(n+1)]
path[start].append(start)
    
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
                path[i[0]] = []
                for p in path[now]:
                    path[i[0]].append(p)
                path[i[0]].append(i[0])
                
dijkstra(start)

print(distance[end])
print(len(path[end]))
print(" ".join(map(str, path[end])))