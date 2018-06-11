import sys
import queue
Read = sys.stdin.readline

N, M = map(int, Read().split())
maze = [list(map(int, Read().rstrip())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
result = 0

q = queue.Queue()
q.put([0, 0])
visited[0][0] = 1

while not q.empty():
    for _ in range(q.qsize()):
        p = q.get()

        if p[0] == N-1 and p[1] == M-1:
            print(result+1)
            break

        for j in range(4):
            y, x = p[0] + [1,0,-1,0][j], p[1] + [0,-1,0,1][j]
            if y > N-1 or x > M-1 or x < 0 or y < 0:
                continue

            if visited[y][x] == 0 and maze[y][x] == 1:
                q.put([y, x])
                visited[y][x] = 1
    result += 1