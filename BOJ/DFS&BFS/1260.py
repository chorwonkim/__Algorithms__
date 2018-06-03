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


import sys
sys.setrecursionlimit(10000000)

N, M, V = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(1002)]

for _ in range(M):
    S, E = map(int, sys.stdin.readline().rstrip().split())
    graph[S].append(E)
    graph[E].append(S)

for item in graph:
    item.sort()


def DFS(root):
    if visited[root]:
        return
    visited[root]=1
    print(root, end=' ')
    for sub in graph[root]:
        DFS(sub)


def BFS(root):
    queue = [root]
    while queue:
        root = queue.pop(0)
        if visited[root]:continue
        visited[root]=1
        print(root, end=' ')
        for sub in graph[root]:
            queue.append(sub)


visited = [0 for _ in range(1002)]
DFS(V)
print()
visited = [0 for _ in range(1002)]
BFS(V)
