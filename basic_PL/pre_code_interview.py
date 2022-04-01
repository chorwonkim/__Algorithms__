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
s = list(map(int, input()))
result = 0
for i in s:
    if i <= 1 or result <= 1:
        result += i
    else:
        result *= i
print(result)