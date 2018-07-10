from collections import deque
from sys import stdout

N, M = map(int, input().split())
d = deque(range(1, N+1))
result = []

while d:
    d.rotate(-M)
    result.append(str(d.pop()))

answer = '<' + ", ".join(result) + '>'

print(answer)