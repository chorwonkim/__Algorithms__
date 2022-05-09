import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

result = []
count = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    graph[x][y] = -1
    global count
    count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            dfs(nx, ny)

    # for i, j in zip([-1,1,0,0], [0,0,-1,1]):
    #     nx = x + i
    #     ny = y + j

    #     if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
    #         dfs(nx, ny)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            count = 0
            dfs(i, j)
            result.append(count)

print(len(result))
if len(result) == 0:
    print(0)
else:
    print(max(result))

# from collections import deque

# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]

# result = []
# count = 0

# def bfs(x, y):
#     global count
#     queue = deque()
#     queue.append((x, y))
#     graph[x][y] = -1
#     count = 1

#     while queue:
#         x, y = queue.popleft()
        
#         for i, j in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
#             nx = x + i
#             ny = y + j

#             if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
#                 count += 1
#                 queue.append((nx, ny))
#                 graph[nx][ny] = -1

# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 1:
#             bfs(i, j)
#             result.append(count)

# print(len(result))
# if len(result) == 0:
#     print(0)
# else:
#     print(max(result))