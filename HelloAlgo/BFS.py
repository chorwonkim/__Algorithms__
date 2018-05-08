def person_is_seller(name):
    return name[-1] == 'm'
    # 사람 이름의 맨 마지막 알파벳이 'm'일 경우에는 찾는 사람.


graph = {"you": ["alice", "bob", "claire"]}

# example to how to apply graph in python code
# For implement to graph, we can use Hash Table (dictionary)
# graph = {"you": ["alice", "bob", "claire"]}
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# 최단 경로 탐색을 위해서는 자료구조인 Queue가 사용된다.
# 한 큐에 대해 여러 번 반복될 수 있기 때문에 중복 처리를 확실하게 해야 한다. 만일 그렇지 않다면 무한 루프의 위험.
# from collections import deque
# search_queue = deque()
# search_queue += graph["you"]
#
# while search_queue:
#     person = search_queue.popleft()
#     if person_is_seller(person):
#         print(person + "is a mango seller!")
#         return True
#     else:
#         search_queue += graph[person]
#
# return False

# 실제 코드
from collections import deque


def search(name):
    search_queue = deque()
    search_queue += graph["you"]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search("you")