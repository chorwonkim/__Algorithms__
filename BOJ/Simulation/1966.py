from sys import stdin
from collections import deque

Read = stdin.readline

T = int(Read())

for _ in range(T):
    N, M = map(int, Read().split())
    count = 0
    result = -1

    d = deque()
    priority = deque()

    for i in range(1, N+1):
        d.append(i)

    for item in list(map(int, Read().split())):
        priority.append(item)

    while True:
        if result == M+1:
            print(count)
            break

        max_value = max(priority)
        temp = priority.popleft()

        # print(d, priority)

        if temp == max_value:
            result = d.popleft()
            count += 1
        else:
            priority.append(temp)
            d.rotate(-1)
