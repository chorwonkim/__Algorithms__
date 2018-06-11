from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
d = deque()

for _ in range(N):
    string = list(map(str, sys.stdin.readline().rstrip().split()))

    if string[0] == "push":
        d.append(string[1])
    elif string[0] == "pop":
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif string[0] == "size":
        print(len(d))
    elif string[0] == "empty":
        if d:
            print(0)
        else:
            print(1)
    elif string[0] == "front":
        if d:
            print(d[0])
        else:
            print(-1)
    elif string[0] == "back":
        if d:
            print(d[-1])
        else:
            print(-1)