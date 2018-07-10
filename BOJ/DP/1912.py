from sys import stdin
Read = stdin.readline

n = int(Read())
numbers = input().split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

result = [0 for _ in range(n)]

for i in range(n):
    result[i] = max(result[i-1] + numbers[i], numbers[i])

print(max(result))