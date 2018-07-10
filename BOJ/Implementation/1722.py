# # 시간초과. 코드 수정 필요
#
# from itertools import permutations
# N = int(input())
# first, *args = map(int, input().split())
# temp = permutations(range(1, N+1))
# i = 1
# if first == 1:
#     for item in temp:
#         if i >= args[0]:
#             break
#         i += 1
#
#     for x in item:
#         print(x, end=' ')
# else:
#     for item in temp:
#         if list(item) == args:
#             print(i)
#         else:
#             i += 1
#             continue

