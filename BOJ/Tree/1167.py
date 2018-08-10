from sys import stdin
from collections import deque
Read = stdin.readline

V = int(Read())
Map = [[] for _ in range(V)]

# # 2차원 배열로 생각
# Map = [[0 for _ in range(V)] for _ in range(V)]
#
# for _ in range(V):
#     a, *args, _ = map(int, Read().split())
#
#     for i in range(len(args)//2):
#         Map[a-1][args[i*2]-1] += args[i*2+1]

for _ in range(V):
    a, *args, _ = map(int, Read().split())

    for i in range(len(args)//2):
        Map[a-1].extend((args[i*2], a, args[i*2+1]))


# print(Map)


# 1967번 풀이 참조.
def func_1167(start):
    d = deque(Map[start])
    visited[start] = True

    while d:
        node = d.popleft()
        root = d.popleft()
        value = d.popleft()
        # print(node, value)

        if visited[node-1]:
            visited_path[root-1] += visited_path[node-1]
            continue

        visited[node-1] = True
        visited_path[node-1] += value

        for sub in Map[node-1]:
            d.append(sub)


visited_path = [0 for _ in range(V)]
visited = [False for _ in range(V)]
func_1167(0)

temp = max(visited_path)
t1 = visited_path.index(temp)

visited_path = [0 for _ in range(V)]
visited = [False for _ in range(V)]
func_1167(t1)
print(max(visited_path))
