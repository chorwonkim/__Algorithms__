from sys import stdin
Read = stdin.readline

N, K = map(int, Read().split())
items = list(map(int, Read().split()))
result = -1

for i in range(N):
    total = 0
    vtotal = 0
    count = 0
    for j in range(i, N):
        total += items[j]
        vtotal += (items[j] ** 2)
        count += 1

        if count >= K:
            average = float(total) / count
            average2 = float(vtotal) / count

            # var = average2 - (average ** 2)
            var = (vtotal * count - total ** 2) / float(count ** 2)

            std = (var ** 0.5)

            if result == -1 or std < result:
                result = std

print("%.12f" % result)

# 배울 코드 "randoms"님
# import math
# N,K=map(int,input().split())
# L=list(map(int,input().split()))+[0]
# minE=999999999999
# for k in range(K,N+1):
#     s=sum(L[:k])
#     s2=sum(map(lambda x:x*x,L[:k]))
#     for i in range(k,N+1):
#         M=s/k
#         E=math.pow(((s2*k-s*s)/(k*k)),0.5)
#         if minE>E:
#             minE=E
#         s+=L[i]-L[i-k]
#         s2+=L[i]**2-L[i-k]**2
# print("%.11f"%minE)

# 소수점 오류 (K 이상..)
# for p in range(K, N):
#     for i in range(N-p+1):
#         temp = []
#         for j in range(p):
#             temp.append(decimal.Decimal(items[i + j]))
#
#         # print(temp)
#
#         average = (math.fsum(temp) / float(K))
#         average = decimal.Decimal(average)
#         # print(average)
#
#         vsum = decimal.Decimal(0)
#
#         for x in temp:
#             vsum += ((x - average) ** 2)
#
#         length = decimal.Decimal(float(K))
#         var = vsum / length
#
#         std = var.sqrt()
#
#         # print(std, type(std))
#
#         if result > std:
#             result = std
#
#
# print(result)

# 시간 초과
# temp = K
#
# while N >= temp:
#     for i in range(N-temp+1):
#         total = 0
#         vtotal = 0
#         for j in range(i, temp+i):
#             total += items[j]
#             vtotal += (items[j] ** 2)
#
#         average = total / float(K)
#         average2 = vtotal / float(K)
#
#         var = average2 - (average ** 2)
#
#         if var >= 0.00000000001:
#             std = sqrt(var)
#
#             if result > std:
#                 result = std
#         else:
#             continue
#
#     temp += 1
#
# print(result)
#

# N, K = map(int, Read().split())
# items = [list(map(int, Read().split()))] * N
# power_items = [[0 for _ in range(N)] for _ in range(N)]
# result = 1000000.0
#
# for i in range(N):
#     for j in range(N):
#         power_items[i][j] = (items[i][j] ** 2)
# 답은 틀리다고 하네... ㅅㅂ
# for i in range(N):
#     for j in range(N):
#         total = 0.0
#         vtotal = 0.0
#
#         if K <= j-i+1:
#             total = sum(items[i][i:j+1])
#             vtotal = sum(power_items[i][i:j+1])
#             # print(total, vtotal, i, j)
#
#             average = total / (float(j-i+1) + 1e-100)
#             average2 = vtotal / (float(j-i+1) + 1e-100)
#
#             var = average2 - (average ** 2)
#
#             if var >= 0:
#                 std = sqrt(var)
#                 print(std, i, j, total, vtotal, average, average2)
#                 if result - std > 1e-100:
#                     result = std
#
# print(result)