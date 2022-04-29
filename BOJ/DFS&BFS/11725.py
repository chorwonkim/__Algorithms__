# DFS는 시간 초과

# import sys
# Read = sys.stdin.readline
# sys.setrecursionlimit(2500)

# n = int(Read())
# graph = [[] for _ in range(n)]
# result = [0] * n
# visited = [False] * n

# for _ in range(n-1):
#     x, y = map(int, Read().split())
#     graph[x-1].append(y-1)
#     graph[y-1].append(x-1)

# def dfs(graph, v, visited):
#     visited[v] = True

#     for i in graph[v]:
#         if not visited[i]:
#             result[i] = v
#             dfs(graph, i, visited)

# dfs(graph, 0, visited)

# for i in result[1:]:
#     print(i+1)

import sys
from collections import deque
Read = sys.stdin.readline

n = int(Read())
graph = [[] for _ in range(n)]
result = [0] * n
visited = [False] * n

for _ in range(n-1):
    x, y = map(int, Read().split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        temp = queue.popleft()
        for i in graph[temp]:
            if not visited[i]:
                queue.append(i)
                result[i] = temp
                visited[i] = True

bfs(graph, 0, visited)

for i in result[1:]:
    print(i+1)