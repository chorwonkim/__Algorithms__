from sys import stdin
Read = stdin.readline

V, E = map(int, Read().split())
temp = [[0,0,0] for _ in range(E)]
checker = [i for i in range(V+1)]
result = 0

for i in range(E):
    temp[i][0], temp[i][1], temp[i][2] = map(int, Read().split())

temp.sort(key=lambda x: x[-1])


def union_find(i):
    if i == checker[i]:
        return i

    checker[i] = union_find(checker[i])
    return checker[i]


for i in range(E):
    temp1 = union_find(temp[i][0])
    temp2 = union_find(temp[i][1])

    if temp1 == temp2:
        continue

    checker[temp1] = temp2
    result += temp[i][2]

print(result)