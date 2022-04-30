from collections import deque

t = int(input())

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(start, end, a, b):
    queue = deque()
    graph[start][end] = 0
    queue.append((start, end))

    while queue:
        x, y = queue.popleft()
        if a == x and b == y:
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == -1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


for _ in range(t):
    l = int(input())
    graph = [[-1] * l for _ in range(l)]

    start, end = map(int, input().split())
    a, b = map(int, input().split())

    bfs(start, end, a, b)

    print(graph[a][b])