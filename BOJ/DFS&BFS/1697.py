import sys
import queue
Read = sys.stdin.readline


class Node:
    def __init__(self, location, count):
        self.location = location
        self.count = count


N, K = map(int, Read().split())
result = 0
q = queue.Queue()
q.put(Node(N, 0))
visited = [False for _ in range(100001)]


def func_1697(n):
    while not q.empty():
        p = q.get()
        x = p.location
        time = p.count

        if x == K:
            return time

        for j in [1,-1,2]:
            if j == 2:
                moving = x * j
            else:
                moving = x + j

            if 0 <= moving <= 100000:
                if not visited[moving]:
                    q.put(Node(moving, time+1))
                    visited[moving] = True


print(func_1697(N))
