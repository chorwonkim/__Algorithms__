from sys import stdin, stdout
Read = stdin.readline
Write = stdout.write

N = int(Read())
Based = Read().rstrip().split()
checker = [[False for _ in range(N)] for _ in range(N)]

for i in range(len(Based)):
    Based[i] = int(Based[i])

for i in range(N):
    # S, E가 동일한 경우에는 항상 팰린드롬
    checker[i][i] = True

for i in range(N-1):
    if Based[i] == Based[i+1]:
        checker[i][i+1] = True

for i in range(2, N):
    for j in range(N-i):
        if Based[j] == Based[j+i] and checker[j+1][j+i-1]:
            checker[j][j+i] = True

M = int(Read())

for i in range(M):
    S, E = map(int, Read().split())

    if checker[S-1][E-1]:
        Write("1")
    else:
        Write("0")

    if i != M-1:
        Write("\n")
