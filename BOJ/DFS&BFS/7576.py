# from sys import stdin
# from collections import deque
# Read = stdin.readline

# M, N = map(int, Read().split())
# boxes = [list(map(int, Read().rstrip().split())) for _ in range(N)]
# visited = [[-1 for _ in range(M)] for _ in range(N)]
# checker = True

# q = queue.Queue()
# for i in range(N):
#     for j in range(M):
#         if boxes[i][j] == 1:
#             visited[i][j] = 0
#             q.put([i, j])
#         elif boxes[i][j] == 0 and checker:
#             checker = False
#
#
# def func_7576():
#     while not q.empty():
#         for _ in range(q.qsize()):
#             p = q.get()
#
#             for j in range(4):
#                 y, x = p[0] + [1,0,-1,0][j], p[1] + [0,-1,0,1][j]
#
#                 if 0 <= x <= M-1 and 0 <= y <= N-1:
#                     if boxes[y][x] == 0 and visited[y][x] == -1:
#                         boxes[y][x] = 1
#                         visited[y][x] = visited[p[0]][p[1]] + 1
#                         q.put([y, x])
#
#
# def last_check():
#     result = 1
#
#     for i in range(N):
#         for j in range(M):
#             if boxes[i][j] == 0:
#                 print(-1)
#                 return
#
#             if visited[i][j] > result:
#                 result = visited[i][j]
#
#     print(result)
#
#
# if checker:
#     print(0)
# else:
#     func_7576()
#     last_check()


# M, N = map(int, Read().split())
# boxes = [list(map(int, Read().rstrip().split())) for _ in range(N)]
# visited = [[-1 for _ in range(M)] for _ in range(N)]
# checker = True
# d = deque()

# for i in range(N):
#     for j in range(M):
#         if boxes[i][j] is 1:
#             d.append((j, i))


# def func_7576(d):
#     d_temp = deque()
#     d_temp.extend(d)
#     temp = deque()
#     result = 0

#     while d_temp:
#         a = d_temp.popleft()
#         for i, j in zip([1,0,-1,0],[0,1,0,-1]):
#             x = i + a[0]
#             y = j + a[1]

#             if 0<= x <M and 0 <= y < N:
#                 if boxes[y][x] is 0:
#                     temp.append((x,y))
#                     boxes[y][x]=1
#         if not d_temp:
#             d_temp.extend(temp)
#             temp.clear()
#             result+=1
#     return result-1


# xcv = func_7576(d)

# for i in boxes:
#     if 0 in i:
#         print(-1)
#         exit()

# print(xcv)

from collections import deque

m, n = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
queue = deque()
check_zero = False

def bfs():    
    while queue:
        x, y = queue.popleft()
        
        for i, j in zip([-1,1,0,0], [0,0,-1,1]):
            nx = x + i
            ny = y + j
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == -1:
                    continue
                    
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

                    
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))
        elif graph[i][j] == 0 and check_zero:
            check_zero = False

if check_zero:
    print(0)
else:
    bfs()
    
    check_zero_two = False
    temp = -100
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                check_zero_two = True
                break
            elif graph[i][j] > temp:
                temp = graph[i][j] - 1
    
    if check_zero_two:
        print(-1)
    else:
        print(temp)