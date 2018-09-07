from sys import stdin
Read = stdin.readline


class Node:
    def __init__(self, a, b, weight):
        self.a = a
        self.b = b
        self.weight = weight


N = int(Read())
M = int(Read())
result = 0

temp = [Node(0,0,0) for _ in range(M)]
checker = [i for i in range(N+1)]

for i in range(M):
    temp[i].a, temp[i].b, temp[i].weight = map(int, Read().split())

# sorted(temp, key=lambda node: node.weight)
temp.sort(key=lambda node: node.weight)


def union_find(i):
    if i == checker[i]:
        return i

    checker[i] = union_find(checker[i])
    return checker[i]


for i in range(M):
    # print(temp[i].a, temp[i].b)
    temp1 = union_find(temp[i].a)
    temp2 = union_find(temp[i].b)

    if temp1 == temp2:
        continue

    checker[temp1] = temp2

    result += temp[i].weight

print(result)