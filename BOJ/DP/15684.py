from collections import deque

N, M, H = map(int, input().split())
d = deque()
Map = [[0 for _ in range(N)] for _ in range(H)]
result = -1


def func_15684():
    for i in range(N):
        x = 0
        y = i

        while x != H:
            if Map[x][y] == 1:
                x, y = x+1, y+1
            elif y-1 >= 0 and Map[x][y-1] == 1:
                x, y = x+1, y-1
            else:
                x = x+1

        if y != i:
            return False

    return True


def make_line(count, start, target):
    global result
    if result != -1:
        return

    if count == target and func_15684():
        result = count
        return

    if count >= target:
        return

    for i in range(start, H*(N-1)):
        x = i // (N-1)
        y = i % (N-1)

        if Map[x][y] == 1:
            continue
        if y-1 >= 0 and Map[x][y-1] == 1:
            continue
        if y+1 < N-1 and Map[x][y+1] == 1:
            continue

        Map[x][y] = 1

        make_line(count+1, i+1, target)

        Map[x][y] = 0

    return


for _ in range(M):
    a, b = map(int, input().split())
    Map[a-1][b-1] = 1

for j in range(4):
    make_line(0, 0, j)
    if result != -1:
        break

print(result)