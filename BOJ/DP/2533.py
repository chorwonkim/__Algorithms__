import sys
from collections import deque
import os
import psutil
import time
# 메모리 초과로 인해 수정 필요..
sys.setrecursionlimit(1000000)

process = psutil.Process(os.getpid())
mem_before = process.memory_info().rss / 1024 / 1024

Read = sys.stdin.readline
N = int(Read())
# Generator로 바꿀 경우에는 'generator' object is not subscriptable 과 같은 오류가 발생한다.
d = [deque() for _ in range(N)]
visited = [False for _ in range(N)]
result = [[0 for _ in range(2)] for _ in range(N)]

for _ in (range(N-1)):
    u, v = map(int, Read().split())
    d[u-1].append(v)

first = 0

print(d)


def func_2533(x):
    visited[x] = True
    result[x][0] = 0
    result[x][1] = 1

    print(visited)
    print(result)
    temp = d[x]
    mem_middle = process.memory_info().rss / 1024 / 1024
    print("{}".format(mem_middle), "AAAA")
    for item in temp:
        if visited[item-1] == 0:
            func_2533(item-1)
            result[x][0] += result[item-1][1]
            result[x][1] += min(result[item-1][0], result[item-1][1])


func_2533(first)
print(min(result[first][0], result[first][1]))

mem_after = process.memory_info().rss / 1024 / 1024

print("{}".format(mem_before))
print("{}".format(mem_after))
