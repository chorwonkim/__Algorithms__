from sys import stdin
Read = stdin.readline

N = int(Read())
L = int(Read())
result = 0
computers = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(L):
    a, b = map(int, Read().split())

    computers[a-1][b-1] = computers[b-1][a-1] = 1


# Floyd-Warshar Algorithm

for k in range(N):
    for i in range(N):
        for j in range(N):
            if computers[i][k] and computers[k][j]:
                computers[i][j] = 1


for i in range(1, N):
    if computers[0][i]:
        result += 1
    else:
        continue

print(result)
