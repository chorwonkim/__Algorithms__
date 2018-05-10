N = int(input())
prices = [0] + list(map(int, input().split()))
result = [0] * (N+1)

for i in range(1, N+1):
    for j in range(1, i+1):
        result[i] = max(prices[j]+result[i-j], result[i])

print(result[N])
