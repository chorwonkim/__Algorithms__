# 메모리 초과.
import sys

N, K = [int for x in sys.stdin.readline().split()]
Based = [int for x in sys.stdin.readline().split()]
Based.sort()

print(Based[K-1])
print(sys.getsizeof(Based))