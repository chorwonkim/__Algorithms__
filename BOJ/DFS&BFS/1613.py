# 플로이드, 벨만, 다익스트라 등 정보
# http://koosaga.com/2

from sys import stdin, stdout
Read = stdin.readline
Write = stdout.write

n, k = map(int, Read().split())
whole_case = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(k):
    x, y = map(int, Read().split())

    whole_case[x-1][y-1] = -1
    whole_case[y-1][x-1] = 1


# print(whole_case)
s = int(Read())

for i in range(n):
    for j in range(n):
        for k in range(n):
            if whole_case[j][i] == -1 and whole_case[i][k] == -1:
                whole_case[j][k] = -1
                whole_case[k][j] = 1


# for i in range(n):  # 경유지
#     for j in range(n):  # 시작점
#         for k in range(n):  # 끝점
#             if whole_case[j][k] > whole_case[j][i] + whole_case[i][k]:
#                 whole_case[j][k] = whole_case[j][i] + whole_case[i][k]

# print(whole_case)

for i in range(s):
    case_1, case_2 = map(int, Read().split())

    if whole_case[case_1-1][case_2-1]:
        Write(str(whole_case[case_1-1][case_2-1]))
    else:
        Write("0")

    if not i == s-1:
        Write("\n")
