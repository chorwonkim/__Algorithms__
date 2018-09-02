from sys import stdin

Read = stdin.readline

N, M = map(int, Read().split())
relation = [[1000000 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y = map(int, Read().split())

    relation[x-1][y-1] = 1
    relation[y-1][x-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if relation[i][j] > (relation[i][k] + relation[k][j]):
                relation[i][j] = relation[i][k] + relation[k][j]

result = 0
indexing = 0
checker = 10000

for item in relation:
    temp = sum(item)

    if checker > temp:
        checker = temp
        result = indexing

    indexing += 1

print(result+1)