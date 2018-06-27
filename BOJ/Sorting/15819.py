from sys import stdin
Read = stdin.readline

N, M = map(int, Read().split())
result = [i for i in range(N)]

for i in result:
    result[i] = Read().rstrip()

result.sort()

print(result[M-1])