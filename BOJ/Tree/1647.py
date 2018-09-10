# Memory Exceed
# from sys import stdin
# Read = stdin.readline
#
#
# class Node:
#     def __init__(self, a, b, weight):
#         self.a = a
#         self.b = b
#         self.weight = weight
#
#
# N, M = map(int, Read().split())
# temp = [Node(0,0,0) for _ in range(M)]
# checker = [i for i in range(N+1)]
# result = 0
# count = 0
#
# for i in range(M):
#     temp[i].a, temp[i].b, temp[i].weight = map(int, Read().split())
#
# temp.sort(key=lambda node: node.weight)
#
#
# def union_find(i):
#     if i == checker[i]:
#         return i
#
#     checker[i] = union_find(checker[i])
#     return checker[i]
#
#
# for i in range(M):
#     if count == N-2:
#         break
#
#     temp1 = union_find(temp[i].a)
#     temp2 = union_find(temp[i].b)
#
#     if temp1 == temp2:
#         continue
#
#     checker[temp1] = temp2
#
#     result += temp[i].weight
#     count += 1
#
# print(result)

from sys import stdin
Read = stdin.readline

N, M = map(int, Read().split())
temp = [[0, 0, 0] for _ in range(M)]
checker = [i for i in range(N+1)]
result = 0
count = 0

for i in range(M):
    temp[i][0], temp[i][1], temp[i][2] = map(int, Read().split())

temp.sort(key=lambda x: x[-1])

def union_find(i):
    if i == checker[i]:
        return i

    checker[i] = union_find(checker[i])
    return checker[i]


for i in range(M):
    if count == N-2:
        break

    temp1 = union_find(temp[i][0])
    temp2 = union_find(temp[i][1])

    if temp1 == temp2:
        continue

    checker[temp1] = temp2

    result += temp[i][2]
    count += 1

print(result)