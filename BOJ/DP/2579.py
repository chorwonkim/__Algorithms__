import sys
Read = sys.stdin.readline
N = int(Read())
stairs = [int(Read().rstrip()) for _ in range(N)]
dp = [0 for _ in range(N)]

dp[0] = stairs[0]
dp[1] = max(dp[0] + stairs[1], stairs[1])
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, N):
    dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])

print(dp[N-1])