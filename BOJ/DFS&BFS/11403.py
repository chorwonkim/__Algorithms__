from sys import stdin
Read = stdin.readline

N = int(Read())
G = [list(map(int, Read().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if G[i][k] and G[k][j]:
                G[i][j] = 1

for i in range(N):
    for j in range(N):
        print(G[i][j], end=' ')
    print()