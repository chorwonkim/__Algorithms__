N = int(input())
items = list(map(int, input().split()))
result = 0

for item in items:
    if item == N:
        result += 1

print(result)
