import sys
sys.setrecursionlimit(1000000)
Read = sys.stdin.readline

N, M = map(int, Read().split())
cheese = [list(map(int, Read().split())) for _ in range(N)]
result = 0


def checking_cheese():
    count = 0
    for i in range(N):
        for j in range(M):
            if cheese[i][j] == 1 or cheese[i][j] == 2:
                cheese[i][j] = 1
                count += 1
            else:
                cheese[i][j] = 0

    print(cheese)
    return count == 0


def func_2638(x, y):
    cheese[x][y] = -1

    for i, j in zip([1, 0, -1, 0], [0, 1, 0, -1]):
        dx = x + i
        dy = y + j

        if 0 <= dx < N and 0 <= dy < M:
            if cheese[dx][dy] > 0:
                cheese[dx][dy] += 1
            elif cheese[dx][dy] == 0:
                func_2638(dx, dy)


while not checking_cheese():
    func_2638(0, 0)
    print(cheese)
    print("AAAA")
    result += 1

print(result)