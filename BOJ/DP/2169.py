from sys import stdin
Read = stdin.readline

N, M = map(int, Read().split())
Map = [list(map(int, Read().split())) for _ in range(N)]
dp = [[-101 for _ in range(M)] for _ in range(N)]
tmp = [[0 for _ in range(M)] for _ in range(2)]
cases = [(0, -1), (0, 1), (1, 0)]

dp[0][0] = Map[0][0]

# for i in range(N):
#     for j in range(M):
#         for x, y in cases:
#             dx = i + x
#             dy = j + y
#
#             if 0 <= dx <= N-1 and 0 <= dy <= M-1 and not Map_checker[dx][dy]:
#                 dp[dx][dy] = max(dp[i][j] + Map[dx][dy], dp[dx][dy])
#
#         Map_checker[i][j] = True
#
# print(dp)

# 첫 줄은 오른쪽으로만 이동 가능 (맵의 최상단)
for i in range(1, M):
    dp[0][i] = dp[0][i-1] + Map[0][i]

for i in range(1, N):
    for j in range(M):  # 구하려는 행의 윗 부분을 대입
        tmp[0][j] = tmp[1][j] = dp[i-1][j] + Map[i][j]

    for j in range(1, M):  # 위쪽에서의 값이랑 왼쪽에서의 값
        tmp[0][j] = max(tmp[0][j], tmp[0][j-1] + Map[i][j])

    for j in range(M-2, -1, -1):  # 위쪽에서의 값이랑 오른쪽에서의 값
        tmp[1][j] = max(tmp[1][j], tmp[1][j+1] + Map[i][j])

    for j in range(M):   # 위, 왼, 오 중 큰 두 개는 위의 두 반복문으로 골랐기에 최종적으로 비교하면 된다.
        dp[i][j] = max(tmp[0][j], tmp[1][j])

print(dp[N-1][M-1])
