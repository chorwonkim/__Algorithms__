#Time exceed
import sys
import queue
sys.setrecursionlimit(1000000)


class Node:
    def __init__(self, location, count):
        self.location = location
        self.count = count


def func_sw_5247():
    while not q.empty():
        p = q.get()
        x = p.location
        time = p.count

        if x == M:
            return time

        for j in [1, -1, 2, -10]:
            if j == 2:
                moving = x * j
            else:
                moving = x + j

            if 0 <= moving < 1000001:
                if not visited[moving]:
                    q.put(Node(moving, time+1))
                    visited[moving] = True


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    result = 0
    q = queue.Queue()
    q.put(Node(N, 0))
    visited = [False for _ in range(1000001)]

    print("#%d %d" % (t, func_sw_5247()))
