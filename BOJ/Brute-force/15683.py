import sys
# sys.setrecursionlimit(100000)


class CCTV:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type


N, M = map(int, input().split())

# 이와 같은 List compression의 방식이 append 보다는 훨씬 빠름
office = [[0 for _ in range(M)] for _ in range(N)]
cctvs = []


def TOP(x, y, temp_map):
    for a in range(x - 1, -1, -1):
        if temp_map[a][y] == 6:
            return
        temp_map[a][y] = -1


def BOTTOM(x, y, temp_map):
    for a in range(x + 1, N):
        if temp_map[a][y] == 6:
            return
        temp_map[a][y] = -1


def RIGHT(x, y, temp_map):
    for b in range(y + 1, M):
        if temp_map[x][b] == 6:
            return
        temp_map[x][b] = -1


def LEFT(x, y, temp_map):
    for b in range(y - 1, -1, -1):
        if temp_map[x][b] == 6:
            return
        temp_map[x][b] = -1


def func_15683(n, d, info):
    if n >= cctv_length:
        temp_map = [[0 for _ in range(M)] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                temp_map[i][j] = office[i][j]

        for i in range(cctv_length):
            cctv = cctvs[i]
            dir = info % 10
            info = info // 10

            if cctv.type == 1:
                if dir == 1:
                    TOP(cctv.x, cctv.y, temp_map)
                elif dir == 2:
                    RIGHT(cctv.x, cctv.y, temp_map)
                elif dir == 3:
                    BOTTOM(cctv.x, cctv.y, temp_map)
                elif dir == 4:
                    LEFT(cctv.x, cctv.y, temp_map)
            elif cctv.type == 2:
                if dir == 1:
                    TOP(cctv.x, cctv.y, temp_map)
                    BOTTOM(cctv.x, cctv.y, temp_map)
                elif dir == 2:
                    RIGHT(cctv.x, cctv.y, temp_map)
                    LEFT(cctv.x, cctv.y, temp_map)
            elif cctv.type == 3:
                if dir == 1:
                    TOP(cctv.x, cctv.y, temp_map)
                    RIGHT(cctv.x, cctv.y, temp_map)
                elif dir == 2:
                    RIGHT(cctv.x, cctv.y, temp_map)
                    BOTTOM(cctv.x, cctv.y, temp_map)
                elif dir == 3:
                    BOTTOM(cctv.x, cctv.y, temp_map)
                    LEFT(cctv.x, cctv.y, temp_map)
                elif dir == 4:
                    TOP(cctv.x, cctv.y, temp_map)
                    LEFT(cctv.x, cctv.y, temp_map)
            elif cctv.type == 4:
                if dir == 1:
                    TOP(cctv.x, cctv.y, temp_map)
                    RIGHT(cctv.x, cctv.y, temp_map)
                    LEFT(cctv.x, cctv.y, temp_map)
                elif dir == 2:
                    TOP(cctv.x, cctv.y, temp_map)
                    RIGHT(cctv.x, cctv.y, temp_map)
                    BOTTOM(cctv.x, cctv.y, temp_map)
                elif dir == 3:
                    RIGHT(cctv.x, cctv.y, temp_map)
                    BOTTOM(cctv.x, cctv.y, temp_map)
                    LEFT(cctv.x, cctv.y, temp_map)
                elif dir == 4:
                    BOTTOM(cctv.x, cctv.y, temp_map)
                    LEFT(cctv.x, cctv.y, temp_map)
                    TOP(cctv.x, cctv.y, temp_map)
            elif cctv.type == 5:
                if dir == 1:
                    TOP(cctv.x, cctv.y, temp_map)
                    RIGHT(cctv.x, cctv.y, temp_map)
                    BOTTOM(cctv.x, cctv.y, temp_map)
                    LEFT(cctv.x, cctv.y, temp_map)

        count = 0

        for i in range(N):
            for j in range(M):
                if temp_map[i][j] == 0:
                    count += 1

        global answer
        answer = min(answer, count)
        return

    directions = [0, 4, 2, 4, 4, 1]

    for p in range(1, directions[cctvs[n].type]+1):
        func_15683(n + 1, d * 10, info + d * p)


# Actual lines
for i in range(N):
    lines = list(map(int, sys.stdin.readline().rstrip().split()))

    for j in range(M):
        office[i][j] = lines[j]
        if office[i][j] != 0 and office[i][j] != 6:
            cctvs.append(CCTV(i, j, office[i][j]))

global cctv_length
cctv_length = len(cctvs)
answer = 9999
func_15683(0, 1, 0)

print(answer)