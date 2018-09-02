from sys import stdin
from collections import deque

Read = stdin.readline

n = int(Read())
relations = {}
for i in range(1, n+1):
    relations[i] = []

# relations = [[0 for _ in range(n+1)] for _ in range(n+1)]
result = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]

A, B = map(int, Read().split())

for _ in range(int(Read())):
    x, y = map(int, Read().split()) # x는 y의 부모
    relations[x].append(y)
    relations[y].append(x)


def func_2644(start):
    d = deque()
    d.appendleft(start)
    visited[start] = True

    while d:
        temp = d.popleft()

        for t in relations.get(temp):
            if visited[t]:
                continue

            d.append(t)
            visited[t] = True

            result[t] = result[temp] + 1


func_2644(A)
if result[B] == 0:
    print(-1)
else:
    print(result[B])

# for _ in range(int(Read())):
#     x, y = map(int, Read().split()) # x는 y의 부모
#     relations[x][y] = relations[y][x] = 1
#
#
# def func_2644(start):
#     d = deque()
#     d.appendleft(start)
#
#     while d:
#         temp = d.popleft()
#
#         for i in range(1, n+1):
#             if relations[temp][i] == 0 or result[i]:
#                 continue
#             result[i] = result[temp] + 1
#             d.append(i)
#
#
# func_2644(A)
# if result[B] == 0:
#     print(-1)
# else:
#     print(result[B])