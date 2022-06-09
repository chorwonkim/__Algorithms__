import sys
sys.setrecursionlimit(1000000)

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
    

def dfs(y, x):
    graph[y][x] = 1
    global count
    count += 1

    for i, j in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
        nx = x + i
        ny = y + j

        if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == 0:
            dfs(ny, nx)

result = []
count = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            count = 0
            dfs(i, j)
            result.append(count)
        
print(len(result))
print(*sorted(result))