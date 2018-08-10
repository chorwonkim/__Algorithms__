T = int(input())
result = [[1 for _ in range(31)] for _ in range(31)]

for i in range(30):
    for j in range(1, i+1):
        result[i+1][j] = result[i][j] + result[i][j-1]

for _ in range(T):
    N, M = map(int, input().split())

    print(result[M][N])