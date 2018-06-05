from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
d = deque()

for _ in range(N):
    string = list(map(str, sys.stdin.readline().rstrip().split()))

    if string[0] == "append":
        d.append(string[1])
    elif string[0] == "appendleft":
        d.appendleft(string[1])
    elif string[0] == "pop":
        d.pop()
    elif string[0] == "popleft":
        d.popleft()

for item in d:
    print(item, end=' ')
