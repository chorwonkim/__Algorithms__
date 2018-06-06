import sys
Read = sys.stdin.readline

n = int(Read())
dp = [1, 0, 3] + [0 for _ in range(n-2)]

for i in range(4, n+1, 2):
    dp[i] = 3 * dp[i-2]
    for j in range(4, i+1, 2):
        dp[i] += 2 * dp[i-j]

print(dp[n])