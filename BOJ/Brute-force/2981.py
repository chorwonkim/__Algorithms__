# 100% TLE
# N = int(input())
# numbers = [0 for _ in range(N)]
#
# for i in range(N):
#     numbers[i] = int(input())
#
# numbers.sort()
#
# result = []
#
# for i in range(2, numbers[0]+1):
#     checker = [False for i in range(numbers[0] + 1)]
#     for item in numbers:
#         M = item % i
#
#         if checker[M]:
#             continue
#         else:
#             break
#
#     if checker.count(True) == 1:
#         result.append(i)
#
#
# print(result)

import math

N = int(input())
numbers = [0 for _ in range(N)]

for i in range(N):
    numbers[i] = int(input())

numbers.sort()
result = []

value = numbers[N-1]-numbers[0]
result.append(value)

for i in range(2, int(math.sqrt(value))+1):
    if value % i == 0:
        if i == (value // i):
            result.append(i)
        else:
            result.append(i)
            result.append(value // i)

result.sort()

for item in result:
    checker = True
    temp = numbers[0] % item

    for x in numbers:
        if x % item != temp:
            checker = False
            break

    if checker:
        print(item, end=' ')
