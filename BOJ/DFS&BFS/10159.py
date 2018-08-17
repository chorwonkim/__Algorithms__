from sys import stdin
Read = stdin.readline

N = int(Read())
M = int(Read())
result = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a, b = map(int, Read().split())

    result[a-1][b-1] = 1


for k in range(N):
    for i in range(N):
        for j in range(N):
            if result[i][k] and result[k][j]:
                result[i][j] = 1


for i in range(N):
    count = -1
    for j in range(N):
        if (not result[i][j]) and (not result[j][i]):
            count += 1

    print(count)
