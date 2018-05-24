# 1번째로 생각한 방법
# Knapsack과 다른 부분은 값어치가 없는 문제
# 그래서 조합을 생각했는데, 이로 발생하는 리스트의 메모리 양을 초과하는 문제.

# import itertools
#
# N, C = map(int, input().split())
# items = []
#
# while True:
#     try:
#         items += map(int, input().split())
#     except:
#         break
#
# result = 0
#
# for i in range(1, N+1):
#     temp = list(itertools.combinations(items, i))
#     print(temp)
#     print("AAAA")
#
#     for j in temp:
#         if sum(j) <= C:
#             result += 1
#         else:
#             continue
#
# print(result+1)

# 두 번째 방법.
# 직접 더하고 나서 비교
import bisect

N, C = map(int, input().split())
items = []

while True:
    try:
        items += map(int, input().split())
    except:
        break

# 원소들의 대한 모든 합을 구하는 함수
def func_1450(start, end, temp, items_case):
    if start == end:
        items_case += [temp]
        return

    func_1450(start + 1, end, temp + items[start], items_case)
    func_1450(start + 1, end, temp, items_case)


StartToHalf = []
LastToHalf = []

func_1450(0, N//2, 0, StartToHalf)
func_1450(N//2, N, 0, LastToHalf)

LastToHalf.sort()

result = 0

for i in StartToHalf:
    index = bisect.bisect_right(LastToHalf, C-i)
    result += index

print(result)