def youngSik(a, b):
    if a >= 30:
        return youngSik(a-30, b+10)
    else:
        return b+10


def minSik(a, b):
    if a >= 60:
        return minSik(a-60, b+15)
    else:
        return b+15


N = int(input())
times = list(map(int, input().split()))
result_A = 0
result_B = 0

for time in times:
    result_A += youngSik(time, 0)
    result_B += minSik(time, 0)

# print(type(result_A), type(result_B))
# print(result_A, result_B)
# 출력 형식 주의 필요
if result_A > result_B:
    print("M", result_B)
elif result_A < result_B:
    print("Y", result_A)
elif result_A == result_B:
    print("Y", "M", result_A)



