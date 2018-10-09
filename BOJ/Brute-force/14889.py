from sys import stdin
from itertools import combinations
Read = stdin.readline

N = int(Read())
status = [list(map(int, Read().split())) for _ in range(N)]

# start and link team
case_set = list(combinations(range(N), N//2))
length = len(case_set)//2

start = case_set[0:length]
link = case_set[:length-1:-1]
result = 10000

print(start)
print(link)

# for item in start:
#     temp_start = 0
#     temp_link = 0
#
#     after_case = list(combinations(item, 2))
#
#     for i, j in after_case:
#         print(i, j)
#         temp_start += (status[i][j] + status[j][i])
#
#         # N-i-1 서로 대칭 아님, i랑
#         temp_link += (status[N-i-1][N-j-1] + status[N-j-1][N-i-1])
#
#     print(temp_start, temp_link)
#     temp = abs(temp_start - temp_link)
#
#     if result > temp:
#         result = temp
#
#     print(result, "AAA")
#
# print(result)

for item, item2 in zip(start, link):
    temp_start = 0
    temp_link = 0

    after_start = combinations(item, 2)
    after_link = combinations(item2, 2)

    for i, j in after_start:
        temp_start += status[i][j] + status[j][i]

    for i, j in after_link:
        temp_link += status[i][j] + status[j][i]

    temp = abs(temp_start - temp_link)

    if result > temp:
        result = temp

print(result)