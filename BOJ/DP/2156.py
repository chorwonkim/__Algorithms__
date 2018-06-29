from sys import stdin
Read = stdin.readline
N = int(Read())
items = [0 for _ in range(N)]
dp = [0 for _ in range(N)]

for i in range(N):
    items[i] = int(Read().rstrip())

if N == 1 or N == 2:
    print(sum(items))
    exit()

dp[0] = items[0]
dp[1] = max(dp[0] + items[1], items[1])
dp[2] = max(items[0] + items[2], items[1] + items[2], dp[1])

for i in range(3, N):
    dp[i] = max(dp[i-1], dp[i-3] + items[i-1] + items[i], dp[i-2] + items[i])

print(max(dp))
