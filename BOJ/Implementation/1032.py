# n = int(input())
# x = []
# result = []
# for _ in range(n):
#     x.append(input())
#
# for i in range(len(x[0])):
#     temp = []
#     for j in range(n):
#         temp.append(x[j][i])
#
#     if temp.count(temp[0]) == n:
#         result.append(temp[0])
#     else:
#         result.append('?')
# print(''.join(result))

# 단순히 세 문장이 모두 일치하면 통일
# 하나라도 틀릴 경우 ? 이므로 틀린 경우만 찾으면 되긴함
# n = int(input())
# first = list(input())
#
# for i in range(n-1):
#     other = list(input())
#     for j in range(len(first)):
#         if first[j] != other[j]:
#             first[j] = '?'
# print(''.join(first))