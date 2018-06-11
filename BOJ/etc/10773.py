import sys
from collections import deque

Read = sys.stdin.readline
d = deque()

for _ in range(int(Read())):
    x = int(Read())
    if x == 0:
        d.pop()
    else:
        d.append(x)

print(sum(d))