from sys import stdin
Read = stdin.readline


def union_find(i):
    if i == checker[i]:
        return i

    checker[i] = union_find(checker[i])
    return checker[i]


for _ in range(int(Read())):
    N, M = map(int, Read().split())
    Map = [[0,0] for _ in range(M)]
    checker = [i for i in range(N+1)]
    result = 0

    for i in range(M):
        Map[i][0], Map[i][1] = map(int, Read().split())

    for i in range(M):
        temp1 = union_find(Map[i][0])
        temp2 = union_find(Map[i][1])

        if temp1 == temp2:
            continue

        checker[temp1] = temp2
        result += 1

    print(result)