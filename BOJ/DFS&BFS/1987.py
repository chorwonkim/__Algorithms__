# # 시간 초과 (DFS)

# from sys import stdin
# Read = stdin.readline

# r, c = map(int, Read().rstrip().split())
# graph = []

# for _ in range(r):
#     # graph.append(list(Read()))
#     graph.append(Read())

# points = set()
# result = 0

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def dfs(x, y, temp):
#     global result
#     result = max(result, temp)
    
#     # for i, j in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
#     #     nx = x + i
#     #     ny = y + j

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
        
#         if 0 <= nx < r and 0 <= ny < c and not graph[nx][ny] in points:
#             points.add(graph[nx][ny])
#             dfs(nx, ny, temp+1)
#             points.remove(graph[nx][ny])

# points.add(graph[0][0])
# dfs(0, 0, 1)
# print(result)

# BFS로 풀었을 때 (Ref. https://github.com/Floodnut)
from sys import stdin
Read = stdin.readline

r, c = map(int, Read().split())
graph = []

for _ in range(r):
    graph.append(list(Read().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

visited = {(0, 0, graph[0][0])}
while visited:
    x, y, temp = visited.pop()

    result = max(result, len(temp))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in temp:
            visited.add((nx, ny, temp+graph[nx][ny]))

print(result)