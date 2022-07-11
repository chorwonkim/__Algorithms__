# 3-1
# n = 1260
# count = 0

# coins = [500, 100, 50, 10]

# for coin in coins:
#     count += n // coin
#     n %= coin

# print(count)

# 3-2
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()
# first = data[n-1]
# second = data[n-2]

# count = int(m / (k+1)) * k
# count += m % (k+1)

# result = 0
# result += (count) * first
# result += (m-count) * second
# print(result)

# 3-3
# n, m = map(int, input().split())
# cards = [list(map(int, input().split())) for _ in range(n)]

# temp=result=101
# for i in range(n):
#     if min(cards[i]) < temp:
#         temp = min(cards[i])
#     else:
#         result = min(cards[i])
# print(result)

# 3-4 --1
# n, k = map(int, input().split())
# count = 0
# while True:
#     if n % k != 0:
#         n -= 1
#     else:
#         n = n // k
#     count += 1
#     # 일일이 1씩 빼는 방법은 N이 100억 이상일 경우, 시간 초과 발생 가능

#     if n == 1:
#         break
# print(count)

# 3-4 --2
# n, k = map(int, input().split())
# count = 0
# while True:
#     temp = (n // k) * k # n이 k로 나누어질 때까지의 필요한 -1 갯수 구하기
#     count += (n-temp)
#     n = temp

#     if n < k:
#         break

#     count += 1
#     n //= k

# count += (n-1)
# print(count)

# 4-1
# n = int(input())
# x, y = 1, 1
# plan = input().split()
# print(plan, type(plan))

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']

# for p in plan:
#     for i in range(len(move_types)):
#         if p == move_types[i]:
#             nx = x+dx[i]
#             ny = y+dy[i]

#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue

#     x, y = nx, ny

# print(x, y)

# 4-3
# loc = input()
# loc_row = int(loc[1])
# loc_colume = int(ord(loc[0])) - int(ord('a')) + 1

# steps = [(-2,-1), (-1,-2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# result = 0
# for step in steps:
#     next_row = loc_row + step[0]
#     next_col = loc_colume + step[1]

#     if 1 <= next_row <= 8 and 1 <= next_col <= 8:
#         result += 1

# print(result)

# 4-4
# n, m = map(int, input().split())
# a, b, d = map(int, input().split())
# mapp = [list(map(int, input().split())) for _ in range(n)]
# users = [[0]*m for _ in range(n)]
# users[a][b] = 1

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# def turn_left():
#     global d
#     d -= 1

#     if d == -1:
#         d = 3

# count = 1
# turn = 0

# while True:
#     turn_left()
#     nx = a + dx[d]
#     ny = b + dy[d]

#     if users[nx][ny] == 0 and mapp[nx][ny] == 0:
#         users[nx][ny] = 1
#         a = nx
#         b = ny
#         count += 1
#         turn = 0
#         continue
#     else:
#         turn += 1

#     if turn == 4:
#         nx = a - dx[d]
#         ny = b - dy[d]

#         if mapp[nx][ny] == 0:
#             a = nx
#             b = ny
#         else:
#             break

#         turn = 0

# print(count)

# 11-1
# n = int(input())
# advent = list(map(int, input().split()))
# advent.sort()
# result = 0
# count = 0

# for i in advent:
#     count += 1

#     if count >= i:
#         result += 1
#         count = 0

# print(result)

# 11-2
# s = list(map(int, input()))
# result = 0
# for i in s:
#     if i <= 1 or result <= 1:
#         result += i
#     else:
#         result *= i
# print(result)

# 11-3
# s = list(input())
# count_1 = count_0 = 0
# if s[0] == '0':
#     count_0 += 1
# else:
#     count_1 += 1
#
# for i in range(1, len(s)-1):
#     if s[i+1] != s[i]:
#         if s[i+1] == '0':
#             count_0 += 1
#         else:
#             count_1 += 1
#
# print(min(count_0, count_1))

# 11-4
# n = int(input())
# coins = list(map(int, input().split()))
# coins.sort()
#
# target = 1
# for i in coins:
#     if target < i:
#         break
#
#     target += i
# print(target)

# 11-5 -1
# n, m = map(int, input().split())
# balls = list(map(int, input().split()))
# result = 0
#
# for i in range(n):
#     for j in range(i, n):
#         if balls[j] != balls[i]:
#             result += 1
# print(result)

# 11-5 -2
# n, m = map(int, input().split())
# balls = list(map(int, input().split()))
# array = [0] * (m+1)
#
# for i in balls:
#     array[i] += 1
#
# result = 0
# for i in range(1, m+1):
#     n -= array[i]
#     result += array[i] * n
# print(result)

# 12-1 (boj 18406)

# 12-2
# middle = []
# numbers = []
# for i in list(input()):
#     if 65 <= ord(i) <= 90:
#         middle.append(i)
#     else:
#         numbers.append(int(i))
# print(''.join(sorted(middle)) + ''.join(str(sum(numbers))))

# 12-3 (programmers 문자열 압축, 60057)
# s = input()
# result = []
# if len(s) == 1:
#     result.append(1)
#
# for i in range(1, (len(s) // 2)+1):
#     b = ''
#     count = 1
#     temp = s[:i]
#
#     for j in range(i, len(s), i):
#         if temp == s[j:i+j]:
#             count += 1
#         else:
#             if count != 1:
#                 b = b + str(count) + temp
#             else:
#                 b = b + temp
#             temp = s[j:j+i]
#             count = 1
#
#     if count != 1:
#         b = b + str(count) + temp
#     else:
#         b = b + temp
#
#     result.append(len(b))
#
# print(min(result))

# 12-4 (programmers 자물쇠와 열쇠, 60059)
# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# temp = [[0]*key_length for _ in range(key_length)]
# # # 90도 회전
# # for i in range(key_length):
# #     for j in range(key_length):
# #         temp[j][key_length-1-i] = key[i][j]
#
# # # 180도 회전
# # for i in range(key_length):
# #     for j in range(key_length):
# #         temp[key_length-1-i][key_length-1-j] = key[i][j]
#
# # # 270도 회전
# # for i in range(key_length):
# #     for j in range(key_length):
# #         temp[key_length-1-j][i] = key[i][j]
# print(temp)

# def rotate(key, d):
#     n = len(key)
#     temp = [[0]*n for _ in range(n)]

#     if d % 4 == 1:
#         for i in range(n):
#             for j in range(n):
#                 temp[j][n-1-i] = key[i][j]
#     elif d % 4 == 2:
#         for i in range(n):
#             for j in range(n):
#                 temp[n-1-i][n-1-j] = key[i][j]
#     elif d % 4 == 3:
#         for i in range(n):
#             for j in range(n):
#                 temp[n-1-j][i] = key[i][j]
#     else:
#         for i in range(n):
#             for j in range(n):
#                 temp[i][j] = key[i][j]

#     return temp

# def check(append_lock):
#     n = len(append_lock) // 3
#     for i in range(n, n*2):
#         for j in range(n, n*2):
#             if append_lock[i][j] != 1:
#                 return False
#     return True

# def solution(key, lock):
#     key_length = len(key)
#     lock_length = len(lock)

#     append_lock = [[0] * lock_length * 3 for _ in range(lock_length * 3)]
#     for i in range(lock_length):
#         for j in range(lock_length):
#             append_lock[lock_length + i][lock_length + j] = lock[i][j]

#     for i in range(lock_length * 2):
#         for j in range(lock_length * 2):
#             for d in range(4):
#                 rotate_key = rotate(key, d)

#                 for x in range(key_length):
#                     for y in range(key_length):
#                         append_lock[i + x][j + y] += rotate_key[x][y]

#                 if check(append_lock):
#                     return True

#                 for x in range(key_length):
#                     for y in range(key_length):
#                         append_lock[i + x][j + y] -= rotate_key[x][y]

#     return False

# print(solution(key, lock))

# 8-2
# x = int(input())

# d = [0] * 30001

# for i in range(2, x+1):
#     d[i] = d[i-1]+1

#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)
    
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)

#     if i % 5 == 0:
#         d[i] = min(d[i], d[i // 5] + 1)

# print(d[x])

# 8-3
# n = int(input())
# cargo = list(map(int, input().split()))

# d = [0] * 100
# d[0] = cargo[0]
# d[1] = max(cargo[0], cargo[1])

# for i in range(2, n):
#     d[i] = max(d[i-1], d[i-2] + cargo[i])

# print(d[n-1])

# 8-5
# n, m = map(int, input().split())
# coins = []
#
# for _ in range(n):
#     coins.append(int(input()))
#
# d = [10001] * (m+1)
# d[0] = 0
#
# for i in range(n):
#     for j in range(coins[i], m+1):
#         if d[j-coins[i]] != 10001:
#             d[j] = min(d[j], d[j-coins[i]]+1)
#
# if d[m] == 10001:
#     print(-1)
# else:
#     print(d[m])

# 16-1
# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     io = list(map(int, input().split()))
#     mines = []
#     for i in range(n):
#         mines.append(io[i * m:i * m + m])
#     d = [[0] * m for _ in range(n + 2)]

#     for i in range(1, n + 1):
#         d[i][0] = mines[i - 1][0]

#     for j in range(1, m):
#         for i in range(1, n + 1):
#             d[i][j] = mines[i - 1][j] + max(d[i - 1][j - 1], d[i][j - 1], d[i + 1][j - 1])

#     result = 0
#     for i in range(1, n+1):
#         if result < d[i][m-1]:
#             result = d[i][m-1]
#     print(result)

# # simple Dijkstra
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split())
# start = int(input())
# graph = [[] for i in range(n+1)]
# visited = [False] * (n+1)
# distance = [INF] * (n+1)

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))

# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1, n+1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i

#     return index

# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True

#     for j in graph[start]:
#         distance[j[0]] = j[1]

#     for i in range(n-1):
#         now = get_smallest_node()
#         visited[now] = True

#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost

# dijkstra(start)

# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("INFINITY")
#     else:
#         print(distance[i])

# Reform dijkstra (heapq)
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])