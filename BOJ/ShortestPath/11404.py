from sys import stdin
Read = stdin.readline
INF = int(1e9)

n = int(Read())
m = int(Read())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, Read().split())
    if c < graph[a][b] :
        graph[a][b] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0

        print(graph[i][j], end=' ')
    print()