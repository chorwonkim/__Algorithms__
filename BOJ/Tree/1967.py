from sys import stdin
from collections import deque
Read = stdin.readline
n = int(Read())
graph = [[] for _ in range(n)]

# for _ in range(n-1):
#     x, y, z = map(int, Read().split())
#
#     graph[x-1].extend((y-1, z))
#     graph[y-1].extend((x-1, z))
#
# print(graph)
#
#
# def func_1967(start, node):
#     d = deque(start)
#
#     while d:
#         root = d.popleft()
#         length = d.popleft()
#
#         if visited[root]:
#             node += 1
#             continue
#
#         visited[root] += length
#         visited_path[node].append(root)
#
#         for sub in graph[root]:
#             d.append(sub)
#
#
# visited = [1] + [0 for _ in range(n-1)]
# visited_path = [[] for _ in range(n)]
# func_1967(graph[0], 0)
# print(visited)
# print(visited_path)

# for _ in range(n-1):
#     x, y, z = map(int, Read().split())
#
#     graph[x-1].extend((y-1, z))
#
# print(graph)
#
#
# def func_1967(start):
#     d = deque(start)
#
#     while d:
#         root = d.popleft()
#         length = d.popleft()
#
#         visited[root] += length
#
#
# visited = [1] + [0 for _ in range(n-1)]
# for i in range(n):
#     func_1967(graph[i])
# print(visited)


# for _ in range(n-1):
#     x, y, z = map(int, Read().split())
#
#     graph[x-1].extend((y-1, z))
#     graph[y-1].extend((x-1, z))
#
# print(graph)
#
#
# def func_1967(start, node):
#     d = deque(start)
#
#     while d:
#         root = d.popleft()
#         length = d.popleft()
#
#         if root > node:
#             visited[root] += length
#         else:
#             visited[node] += visited[root]
#
#
# visited = [0 for _ in range(n)]
#
# for i in range(n):
#     func_1967(graph[i], i)
#
# print(visited)


for _ in range(n-1):
    x, y, z = map(int, Read().split())
    graph[x-1].extend((x-1, y-1, z))
    graph[y-1].extend((y-1, x-1, z))


def func_1967(start):
    d = deque(graph[start])
    visited[start] = True

    while d:
        node = d.popleft()
        root = d.popleft()
        length = d.popleft()

        if visited[root]:
            visited_path[node] += visited_path[root]
            continue

        visited[root] = True
        visited_path[root] += length

        for sub in graph[root]:
            d.append(sub)


visited_path = [0 for _ in range(n)]
visited = [False for _ in range(n)]
func_1967(0)

temp = max(visited_path)
t1 = visited_path.index(temp)

visited_path = [0 for _ in range(n)]
visited = [False for _ in range(n)]
func_1967(t1)
print(max(visited_path))
