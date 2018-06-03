# question: http://hsin.hr/2007/regional/juniors/tasks.pdf

import sys
import bisect

N, H = map(int, sys.stdin.readline().rstrip().split())
Obstacle = [sys.stdin.readline() for _ in range(N)]
Obstacle = list(map(int, Obstacle))
Roots = [i for i in range(1, H+1)]

Obstacle_a = Obstacle[0::2]
Obstacle_b = Obstacle[1::2]

Obstacle_a.sort()
Obstacle_b.sort()

# print(Obstacle)
# print(Obstacle_a)
# print(Obstacle_b)
# print(Roots)

for i in range(1, H+1):
    index_a = N//2 - bisect.bisect_right(Obstacle_a, H-i)
    index_b = N//2 - bisect.bisect_right(Obstacle_b, i-1)
    # print(index_a, index_b)
    Roots[i-1] = (index_b + index_a)

# Roots[0] = Roots[H-1] = N//2

result = min(Roots)
# print(Roots, result)
count = Roots.count(result)


# 높이 필요 (root)에 대한
print(result, count)