# def person_is_seller(name):
#     return name[-1] == 'm'
#     # 사람 이름의 맨 마지막 알파벳이 'm'일 경우에는 찾는 사람.
#
#
# graph = {"you": ["alice", "bob", "claire"]}
#
# # example to how to apply graph in python code
# # For implement to graph, we can use Hash Table (dictionary)
# # graph = {"you": ["alice", "bob", "claire"]}
# graph["bob"] = ["anuj", "peggy"]
# graph["alice"] = ["peggy"]
# graph["claire"] = ["thom", "jonny"]
# graph["anuj"] = []
# graph["peggy"] = []
# graph["thom"] = []
# graph["jonny"] = []
#
# # 최단 경로 탐색을 위해서는 자료구조인 Queue가 사용된다.
# # 한 큐에 대해 여러 번 반복될 수 있기 때문에 중복 처리를 확실하게 해야 한다. 만일 그렇지 않다면 무한 루프의 위험.
# # from collections import deque
# # search_queue = deque()
# # search_queue += graph["you"]
# #
# # while search_queue:
# #     person = search_queue.popleft()
# #     if person_is_seller(person):
# #         print(person + "is a mango seller!")
# #         return True
# #     else:
# #         search_queue += graph[person]
# #
# # return False
#
# # 실제 코드
# from collections import deque
#
#
# def search(name):
#     search_queue = deque()
#     search_queue += graph["you"]
#     searched = []
#
#     while search_queue:
#         person = search_queue.popleft()
#         if not person in searched:
#             if person_is_seller(person):
#                 print(person + " is a mango seller")
#                 return True
#             else:
#                 search_queue += graph[person]
#                 searched.append(person)
#     return False
#
#
# search("you")


# 인접행렬을 사용하는 방법 [O(V^2)]
# from collections import deque
# v, e = map(int, input().split())
#
# Map = [[0 for _ in range(v+1)] for _ in range(v+1)]
# visited = [False for _ in range(v+1)]
#
#
# def BFS(start):
#     d = deque()
#     d.appendleft(start)
#     visited[start] = True
#
#     while d:
#         temp = d.popleft()
#         print(str(temp) + " ")
#
#         for i in range(1, v+1):
#             if Map[temp][i] == 0 or visited[i]:
#                 continue
#             d.append(i)
#             visited[i] = True
#
#
# for _ in range(e):
#     x, y = map(int, input().split())
#
#     Map[x][y] = Map[y][x] = 1
#
# BFS(1)


# 인접리스트를 사용하는 방법 [O(V+E)]
from collections import deque

v, e = map(int, input().split())
Map = {}
visited = [False for _ in range(v+1)]

for i in range(v+1):
    Map[i] = []


def BFS(start):
    d = deque()
    d.appendleft(start)
    visited[start] = True

    while d:
        temp = d.popleft()
        print(temp, Map.get(temp))
        for t in Map.get(temp):
            if visited[t]:
                continue
            visited[t] = True
            d.append(t)


for i in range(e):
    x, y = map(int, input().split())

    Map[x].append(y)
    Map[y].append(x)

print(Map)
BFS(1)