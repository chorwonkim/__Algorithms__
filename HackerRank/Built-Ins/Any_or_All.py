# N = int(input())
# nums = map(int, input().split())
# # print(all([x>0 for x in nums]) and any([int(str(x)[::-1]) is x for x in nums]))
# #
# # print(all([x>0 for x in nums]))
# # print(any([int(str(x)[::-1]) is x for x in nums]))
#
# # print(all(x>0 for x in nums))
# print(list(int(str(x)[::-1]) is x for x in nums))

N, nums=int(input()), input().split()
print((all(int(i)>0 for i in nums))and(any(i==i[::-1] for i in nums)))