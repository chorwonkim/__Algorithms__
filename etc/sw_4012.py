from sys import stdin
from itertools import combinations

Read = stdin.readline

T = int(Read())

for _ in range(T):
    result = 20000
    N = int(Read())

    foods = [list(map(int, Read().split())) for _ in range(N)]

    occurs = list(combinations([i for i in range(1, N + 1)], N // 2))
    length = len(occurs) // 2

    case_1 = occurs[0:length]
    case_2 = occurs[:length - 1:-1]

    for x, y in zip(case_1, case_2):

        A = 0
        B = 0

        after_1 = combinations(x, 2)
        after_2 = combinations(y, 2)

        for i, j in after_1:
            A += (foods[i-1][j-1] + foods[j-1][i-1])

        for i, j in after_2:
            B += (foods[i-1][j-1] + foods[j-1][i-1])

        temp = abs(A-B)

        if result > temp:
            result = temp

    print(result)

