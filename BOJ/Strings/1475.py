import sys
Read = sys.stdin.readline

N = Read().rstrip()
N = N.replace('6', '9')
result = 0

for i in range(10):
    count = N.count(str(i))
    if i == 9:
        count = int(count//2) + count%2

    if result < count:
        result = count

print(result)


# 재귀로 풀려고 했는데 if elif 정상적으로 동작 안하는거 같다... 뭐같다.
# 논리적 생각과 실제 결과가 갈라서 빡침
# number_set = [str(i) for i in range(10)]
# result = 1

# def func_1475(x, setting):
#     temp = []
#     for item in x:
#         if item in setting:
#             if item == '6':
#                 if item in setting:
#                     setting.remove(item)
#                 elif '9' in setting:
#                     setting.remove('9')
#             elif item == '9':
#                 if item in setting:
#                     setting.remove(item)
#                 elif '6' in setting:
#                     setting.remove('6')
#             else:
#                 setting.remove(item)
#         else:
#             temp.append(item)
#
#     if not temp:
#         return
#     else:
#         global result
#         result += 1
#         func_1475(temp, [str(i) for i in range(10) ])


# func_1475(N, number_set)
# print(result)

# x = [0,1,2,3]
#
# for item in x:
#     print(item, x, "AAA")
#     if item < 3:
#         x.pop(0)
#     print(item, x, "BBB")
# """ 다음 코드에 대한 결과값은 다음과 같다. 따라서 for문의 x에 대해서는 건드리지 않는 것이 좋다.
# 0 [0, 1, 2, 3] AAA
# 0 [1, 2, 3] BBB
# 2 [1, 2, 3] AAA
# 2 [2, 3] BBB
# """