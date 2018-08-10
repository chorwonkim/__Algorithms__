from sys import stdin
Read = stdin.readline

n = int(Read())
m = int(Read())
bigbig_2 = 100000000000

citymapper = [[bigbig_2 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, Read().split())

    if citymapper[a-1][b-1] > c:
        citymapper[a-1][b-1] = c

for i in range(n):
    citymapper[i][i] = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if citymapper[j][k] > citymapper[j][i] + citymapper[i][k]:
                citymapper[j][k] = citymapper[j][i] + citymapper[i][k]

for i in range(n):
    for j in range(n):

        if citymapper[i][j] == bigbig_2:
            print(0, end=' ')
        else:
            print(citymapper[i][j], end=' ')

    print()