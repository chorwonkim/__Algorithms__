import sys
sys.setrecursionlimit(1000000)
Read = sys.stdin.readline

N = int(Read())
Map = [list(map(int, Read().rstrip())) for _ in range(N)]
visited = [[-1 for _ in range(N)] for _ in range(N)]
count = 0
numbers = []
result = []


def func_2667(x, y):
    Map[x][y] = -1
    visited[x][y] = count

    for i, j in zip([-1, 0, 1, 0], [0, -1, 0, 1]):
        dx = x + i
        dy = y + j

        if 0 <= dx < N and 0 <= dy < N:
            if Map[dx][dy] == 1:
                func_2667(dx, dy)


for i in range(N):
    for j in range(N):
        if Map[i][j] == 1:
            func_2667(i, j)
            result.append(count)

        count += 1


# print(visited, result)

print(len(result))
for item in result:
    temp = 0
    for i in range(N):
        temp += (visited[i].count(item))

    numbers.append(temp)

numbers.sort()
for item in numbers:
    print(item)

## BFS
# from collections import deque

# n = int(input())

# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input())))
    
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
    
# def bfs(x, y, count):
#     queue = deque()
#     queue.append((x, y))
#     graph[x][y] = count
#     temp = 0
    
#     while queue:
#         x, y = queue.popleft()
        
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
                
#             if graph[nx][ny] == 0:
#                 continue
                
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = count
#                 queue.append((nx, ny))
                
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j] == count:
#                 temp += 1
    
#     return temp
                
# result = []
# count = 2

# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             result.append(bfs(i, j, count))
#             count += 1

# print(len(result))
# result.sort()
# for i in result:
#     print(i)