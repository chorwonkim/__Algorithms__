import sys
Read = sys.stdin.readline
N, K = map(int, Read().split())
Based = Read().split()

for i in range(len(Based)):
    Based[i] = int(Based[i])

Based.sort()

print(Based[K-1])
