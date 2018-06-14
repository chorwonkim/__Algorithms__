from itertools import permutations
import sys
Read = sys.stdin.readline

N, M = map(int, Read().split())
for item in permutations(range(1, N+1), M):
    for x in item:
        print(x, end=" ")
    print()
