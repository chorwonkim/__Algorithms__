graph = [list(map(str, input().split())) for _ in range(5)]
result = set()


def dfs(x, y, visited):
    visited += graph[x][y]

    if len(visited) == 6:
        result.add(visited)
        return

    for i, j in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
        nx = x + i
        ny = y + j

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, visited)


for i in range(5):
    for j in range(5):
        temp = ''
        dfs(i, j, temp)

print(len(result))