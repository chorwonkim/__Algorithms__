import heapq
from sys import stdin
Read = stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
solve_count = 0

while True:
    T = int(Read())
    solve_count += 1
    if T == 0:
        break

    graph = []
    for _ in range(T):
        graph.append(list(map(int, Read().split())))

    distance = [[INF] * T for _ in range(T)]

    x, y = 0, 0
    distance[x][y] = graph[x][y]
    q = [(graph[x][y], x, y)]

    while q:
        dist, next_x, next_y = heapq.heappop(q)
        if distance[next_x][next_y] < dist:
            continue

        for i in range(4):
            nx = next_x + dx[i]
            ny = next_y + dy[i]

            if 0 <= nx < T and 0 <= ny < T:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    print("Problem " + str(solve_count) + ": " + str(distance[T-1][T-1]))