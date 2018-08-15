# X, Y = map(int, input().split())
#
# Z1 = (Y * 100) // X
# result = 0
#
# if Z1 >= 99:
#     result = -1
# else:
#     for i in range(1, X+1):
#         Z2 = ((Y+i) * 100) // (X+i)
#
#         if Z1 != Z2:
#             result = i
#             break
#
# print(result)

X, Y = map(int, input().split())

Z1 = (Y * 100) // X
result = 0

if Z1 >= 99:
    result = -1
else:
    temp = Z1 + 1

    result = (X * temp - 100 * Y - 1) // (100 - temp) + 1

print(result)