import sys
sys.setrecursionlimit(100000)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, sys.stdin.readline().rstrip().split())
ice_map = []
ice_map_checker = []
result = 0


def func_2573(p, q):
    ice_map_checker[p][q] = True

    for k in range(4):
        ice_p = p + dx[k]
        ice_q = q + dy[k]

        if (not ice_map_checker[ice_p][ice_q]) and ice_map[ice_p][ice_q]:
            func_2573(ice_p, ice_q)


for i in range(N):
    ice_map.append(list(map(int, sys.stdin.readline().rstrip().split())))

while True:
    block = 0
    ice_map_checker.clear()

    for i in range(N):
        ice_map_checker.append([False] * M)

    for i in range(1, N-1):
        for j in range(1, M-1):
            if ice_map[i][j] and (not ice_map_checker[i][j]):
                block += 1
                func_2573(i, j)

    if block >= 2:
        print(result)
        break
    elif block == 0:
        print(0)
        break

    result += 1

    for i in range(N):
        for j in range(M):
            if (not ice_map_checker[i][j]) and (not ice_map[i][j]):
                for k in range(4):
                    ice_x = i + dx[k]
                    ice_y = j + dy[k]

                    if 0 <= ice_x < N and 0 <= ice_y < M and ice_map[ice_x][ice_y]:
                        ice_map[ice_x][ice_y] -= 1
