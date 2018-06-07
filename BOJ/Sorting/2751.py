import sys
Read = sys.stdin.readline
N = int(Read())
result = [0 for _ in range(N)]

for i in range(N):
    result[i] = int(Read())

result.sort()

for i in range(N):
    print(result[i])