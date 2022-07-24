from sys import stdin
import heapq
Read = stdin.readline
INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    n = int(Read())
    if n == 0:
        break

    graph = [list(map(int, Read().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]

    q = []
    distance[0][0] = graph[0][0]
    heapq.heappush(q, (distance[0][0], 0, 0))

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    print(distance[n-1][n-1])