# 메모리 초과.
import sys

N, K = [int(x) for x in sys.stdin.readline().split()]
Based = [int(x) for x in sys.stdin.readline().split()]
Based.sort()

print(Based[K-1])
