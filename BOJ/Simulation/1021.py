from sys import stdin
from collections import deque

Read = stdin.readline
N, M = map(int, Read().split())
d = deque()
result = 0

for i in range(1, N+1):
    d.append(i)

# print(d)
for item in map(int, Read().split()):
    location = d.index(item)

    if location == 0:
        d.popleft()
        continue

    left = location-1
    right = len(d)-location
    # print(left, right, item, location)

    if left < right:
        for i in range(left+1):
            d.rotate(-1)
            # print(d, "AAA")
            result += 1
        d.popleft()
    else:
        for i in range(right):
            d.rotate()
            # print(d, "BBB")
            result += 1
        d.popleft()

    # print(d, result)

print(result)
