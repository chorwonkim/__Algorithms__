# 스택에 들어있는 막대보다 다음 막대보다 크거나 같으면 그냥 넣고,
# 아니면 다음에 넣을 막대보다 큰 막대들을 뺀 후에 계산하고, 스택에 넣기

from collections import deque
from sys import stdin

Read = stdin.readline
N = int(Read())
items = [0 for _ in range(N)]
d = deque()
result = 0

for i in range(N):
    items[i] = int(Read())

    while d and items[d[-1]] > items[i]:
        temp = d.pop()
        p = i

        if d:
            p -= d[-1] + 1

        cmp = items[temp] * p
        result = max(result, cmp)

    d.append(i)

while d:
    temp = d.pop()
    p = N

    if d:
        p -= d[-1] + 1

    cmp = items[temp] * p
    result = max(cmp, result)

print(result)