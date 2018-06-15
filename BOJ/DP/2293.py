import sys
Read = sys.stdin.readline
n, k = map(int, Read().split())
coins = [int(Read().rstrip()) for _ in range(n)]
dp = [1] + [0] * k

for coin in coins:
    for i in range(k+1):
        if coin <= i:
            dp[i] += dp[i - coin]

print(dp[k])