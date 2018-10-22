# import sys
# from collections import deque
#
# graph = {}
#
# N, M, V = map(int, sys.stdin.readline().rstrip().split())
#
# for i in range(1, int(N)+1):
#     graph[str(i)] = []
#
# for _ in range(int(M)):
#     vertex, edge = map(str, sys.stdin.readline().rstrip().split())
#     graph[vertex].append(edge)
#     graph[edge].append(vertex)
#
#
# def DFS(graph, root):
#     stack = [root]
#     visited = []
#
#     while stack:
#         outputFromStack = stack.pop()
#         if outputFromStack not in visited:
#             visited.extend(outputFromStack)
#
#             inputToStack = list(set(graph[outputFromStack]) - set(visited))
#             inputToStack.sort(reverse=True)
#             stack.extend(inputToStack)
#
#     return ' '.join(visited)
#
#
# def BFS(graph, root):
#     queue = deque()
#     queue += graph[root]
#     visited = [root]
#
#     while queue:
#         outputFromQueue = queue.popleft()
#         if not outputFromQueue in visited:
#             queue += graph[outputFromQueue]
#             visited.extend(outputFromQueue)
#
#     return ' '.join(visited)
#
#
# print(DFS(graph, V))
# print(BFS(graph, V))


# import sys
# sys.setrecursionlimit(10000000)
#
# N, M, V = map(int, sys.stdin.readline().rstrip().split())
# graph = [[] for _ in range(1002)]
#
# for _ in range(M):
#     S, E = map(int, sys.stdin.readline().rstrip().split())
#     graph[S].append(E)
#     graph[E].append(S)
#
# for item in graph:
#     item.sort()
#
#
# def DFS(root):
#     if visited[root]:
#         return
#     visited[root]=1
#     print(root, end=' ')
#     for sub in graph[root]:
#         DFS(sub)
#
#
# def BFS(root):
#     queue = [root]
#     while queue:
#         root = queue.pop(0)
#         if visited[root]:continue
#         visited[root]=1
#         print(root, end=' ')
#         for sub in graph[root]:
#             queue.append(sub)
#
#
# visited = [0 for _ in range(1002)]
# DFS(V)
# print()
# visited = [0 for _ in range(1002)]
# BFS(V)

from collections import deque

N, M, V = map(int, input().split())
Map = [[0 for _ in range(N)] for _ in range(N)]
d = deque()

for i in range(M):
    S, E = map(int, input().split())

    Map[S-1][E-1] = Map[E-1][S-1] = 1


def dfs(root):
    visited_dfs[root] = 1
    for i in range(N):
        if Map[root][i] and not visited_dfs[i]:
            print(i+1, end=" ")
            dfs(i)


def bfs(root):
    d.append(root)
    while d:
        root = d.popleft()
        if visited_bfs[root]:
            continue
        visited_bfs[root] = 1
        print(root+1, end=" ")

        for i in range(N):
            if Map[root][i] and not visited_bfs[i]:
                d.append(i)


visited_dfs = [0 for _ in range(N)]
print(V, end=" ")
dfs(V-1)
visited_bfs = [0 for _ in range(N)]
queue = [0 for _ in range(N)]
bfs(V-1)
