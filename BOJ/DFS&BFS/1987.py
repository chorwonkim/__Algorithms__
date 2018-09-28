R, C = map(int, input().split())

Map = [list(map(str, input())) for _ in range(R)]
visited = [0 for _ in range(26)]
result = []


def func_1987(x, y):
    visited[ord(Map[x][y])-65] = 1

    for i, j in zip([-1,0,1,0],[0,-1,0,1]):
        dx = x + i
        dy = y + j

        if 0 <= dx < C and 0 <= dy < R:
            if not visited[ord(Map[dx][dy])-65]:
                func_1987(dx, dy)
                result.append(Map[dx][dy])


func_1987(0, 0)

