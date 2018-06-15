import sys
Read = sys.stdin.readline
N, M = map(int, Read().split())
cows_want = [[] for _ in range(N)]


def dfs(x):
    if cows[x] == count:
        return 0
    cows[x] = count
    for item in cows_want[x]:
        if rooms[item-1] == -1 or dfs(rooms[item-1]):
            rooms[item-1] = x
            return 1
    return 0


for i in range(N):
    first, *args = map(int, Read().split())

    cows_want[i] = args

cows = [0] * N
rooms = [-1] * M
count = 0
matched = 0

for i in range(N):
    count += 1
    matched += dfs(i)

print(matched)