# import sys
# import queue
# Read = sys.stdin.readline
#
# N, M = map(int, Read().split())
# maze = [list(map(int, Read().rstrip())) for _ in range(N)]
# visited = [[0 for _ in range(M)] for _ in range(N)]
# result = 0
#
# q = queue.Queue()
# q.put([0, 0])
# visited[0][0] = 1
#
# while not q.empty():
#     for _ in range(q.qsize()):
#         p = q.get()
#
#         if p[0] == N-1 and p[1] == M-1:
#             print(result+1)
#             break
#
#         for j in range(4):
#             y, x = p[0] + [1,0,-1,0][j], p[1] + [0,-1,0,1][j]
#             if y > N-1 or x > M-1 or x < 0 or y < 0:
#                 continue
#
#             if visited[y][x] == 0 and maze[y][x] == 1:
#                 q.put([y, x])
#                 visited[y][x] = 1
#     result += 1


from sys import stdin
from collections import deque

Read = stdin.readline

N, M = map(int, Read().split())

maze = [list(map(int, Read().rstrip())) for _ in range(N)]
result = [[0 for _ in range(M)] for _ in range(N)]


def func_2178(start, end):
    global result
    d = deque()
    d.appendleft((start, end))
    result[start][end] = 1

    while d:
        temp = d.popleft()

        p = temp[0]
        q = temp[1]

        if p == N - 1 and q == M - 1:
            print(result[N-1][M-1])
            break

        for i, j in zip([1, 0, -1, 0], [0, 1, 0, -1]):
            dy = p + i
            dx = q + j
            if 0 <= dy < N and 0 <= dx < M:
                if result[dy][dx] == 0 and maze[dy][dx] == 1:
                    d.append((dy, dx))
                    result[dy][dx] = result[p][q] + 1


func_2178(0, 0)
