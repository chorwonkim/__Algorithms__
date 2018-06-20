import sys
from math import sqrt
Read = sys.stdin.readline
N = int(Read())
n = int(sqrt(N))

for k in range(n+1):
    if k * (k+1) == N-1:
        print(k)
    else:
        continue