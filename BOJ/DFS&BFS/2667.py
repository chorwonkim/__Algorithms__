import sys
sys.setrecursionlimit(1000000)
Read = sys.stdin.readline

N = int(Read())
Map = [list(map(int, Read().rstrip())) for _ in range(N)]
visited = [[-1 for _ in range(N)] for _ in range(N)]
count = 0
numbers = []
result = []


def func_2667(x, y):
    Map[x][y] = -1
    visited[x][y] = count

    for i, j in zip([-1, 0, 1, 0], [0, -1, 0, 1]):
        dx = x + i
        dy = y + j

        if 0 <= dx < N and 0 <= dy < N:
            if Map[dx][dy] == 1:
                func_2667(dx, dy)


for i in range(N):
    for j in range(N):
        if Map[i][j] == 1:
            func_2667(i, j)
            result.append(count)

        count += 1


# print(visited, result)

print(len(result))
for item in result:
    temp = 0
    for i in range(N):
        temp += (visited[i].count(item))

    numbers.append(temp)

numbers.sort()
for item in numbers:
    print(item)