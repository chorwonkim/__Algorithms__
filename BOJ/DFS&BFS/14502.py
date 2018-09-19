import sys
from collections import deque
sys.setrecursionlimit(10000000)

N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
testMap = [[0 for _ in range(M)] for _ in range(N)]

wall = deque()
result = 0

for i in range(N):
    for j in range(M):
        testMap[i][j] = Map[i][j]

        if Map[i][j] == 0:
            wall.append((i, j))


def func_14502(x, y):
    for i, j in zip([1,0,-1,0],[0,1,0,-1]):
        dx = x + i
        dy = y + j

        if 0 <= dx < N and 0 <= dy < M:
            if testMap[dx][dy] == 0:
                testMap[dx][dy] = 2
                func_14502(dx, dy)


# 벽 3개 세우기
for i in range(len(wall)-2):
    for j in range(i+1, len(wall)-1):
        for k in range(j+1, len(wall)):
            build1 = wall[i]
            build2 = wall[j]
            build3 = wall[k]

            for p in range(N):
                for q in range(M):
                    testMap[p][q] = Map[p][q]

            testMap[build1[0]][build1[1]] = 1
            testMap[build2[0]][build2[1]] = 1
            testMap[build3[0]][build3[1]] = 1

            # 바이러스 퍼뜨리기
            for p in range(N):
                for q in range(M):
                    if testMap[p][q] == 2:
                        func_14502(p, q)

            # 안전 영역 찾기
            count = 0
            for p in range(N):
                for q in range(M):
                    if testMap[p][q] == 0:
                        count += 1

            result = max(count, result)

print(result)