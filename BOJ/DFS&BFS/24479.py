import sys
sys.setrecursionlimit(1000000)
Read = sys.stdin.readline

n, m, r = map(int, Read().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, Read().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, v):
    global count
    visited[v] = count
    count += 1
    graph[v].sort()

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i)


visited = [0] * (n+1)
count = 1
dfs(graph, r)

for i in range(n):
    print(visited[i+1])