from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

graph = [[-1] * n for _ in range(n)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    while queue:
        p, q = queue.popleft()

        if p == r2 and q == c2:
            break

        for i in range(6):
            nx = p + dx[i]
            ny = q + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == -1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[p][q] + 1

bfs(r1, c1)

print(graph[r2][c2])