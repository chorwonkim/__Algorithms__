# 1789
# S = int(input())
# n = 1

# while n * (n+1) / 2 <= S:
#     n += 1
# print(n-1)

    
# 2753
# x = int(input())
# if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
#     print(1)
# else:
#     print(0)

# 10039
# result = 0
# for _ in range(5):
#     x = int(input())
#     if x < 40:
#         result += 40
#     else:
#         result += x
# print(result//5)

# 1934
# for _ in range(int(input())):
#     a, b = map(int, input().split())

#     if b < a:
#         a, b = b, a
    
#     temp = 1
#     for i in range(2, a+1):
#         if a % i == 0 and b % i == 0:
#             temp = i

#     if temp == 1:
#         print(a*b)
#     else:
#         print(temp * (a//temp) * (b//temp))

# for _ in range(int(input())):
#     a, b = map(int, input().split())
#     x, y = a, b

#     while a % b != 0:
#         a, b = b, a % b

#     print(x * y // b)

# 2480
# a, b, c = map(int, input().split())
# x = set([a, b, c])

# if len(x) == 1:
#     print(10000 + a * 1000)
# elif len(x) == 2:
#     if a == b:
#         print(1000 + a * 100)
#     elif b == c:
#         print(1000 + b * 100)
#     else:
#         print(1000 + a * 100)
# else:
#     print(100 * max(x))

# 4101
# while True:
#     a, b = map(int, input().split())

#     if a == b == 0:
#         break

#     if a > b:
#         print("Yes")
#     else:
#         print("No")

# 10156
# k, n, m = map(int, input().split())
# result = k*n - m
# if result < 0:
#     print(0)
# else:
#     print(result)

# 3009
# x = []
# y = []
# result_x = result_y = 0
# for _ in range(3):
#     a, b = map(int, input().split())
#     x.append(a)
#     y.append(b)

# for i in range(3):
#     if x.count(x[i]) == 1:
#         result_x = x[i]
    
#     if y.count(y[i]) == 1:
#         result_y = y[i]

# print(result_x, result_y)

# a1, b1 = map(int, input().split())
# a2, b2 = map(int, input().split())
# a3, b3 = map(int, input().split())
# a4 = b4 = 0

# if a1 == a2:
#     a4 = a3
# elif a2 == a3:
#     a4 = a1
# elif a1 == a3:
#     a4 = a2

# if b1 == b2:
#     b4 = b3
# elif b2 == b3:
#     b4 = b1
# elif b1 == b3:
#     b4 = b2

# print(a4, b4)

# 2476
# result = 0
# for _ in range(int(input())):

#     a, b, c = map(int, input().split())
#     temp = 0
#     if a == b == c:
#         temp = 10000 + a * 1000
#     elif a == b:
#         temp = 1000 + a*100
#     else:
#         if b == c or a == c:
#             temp = 1000 + c*100
#         else:
#             temp = max(a,b,c) * 100

#     if temp > result:
#         result = temp

# print(result)

# 2884
# h, m = map(int, input().split())

# if m < 45:
#     if h <= 0:
#         h += 24

#     h -= 1
#     m += 15
# else:
#     m -= 45

# print(h, m)

# 7567
# x = input()
# temp = x[0]
# result = 10
# for i in x[1:]:
#     if temp == '(':
#         if i == '(':
#             result += 5
#         else:
#             result += 10
#     else:
#         if i == '(':
#             result += 10
#         else:
#             result += 5

#     temp = i

# print(result)

# 5063
# for _ in range(int(input())):
#     r, e, c = map(int, input().split())

#     if r < e-c:
#         print("advertise")
#     elif r == e-c:
#         print("does not matter")
#     else:
#         print("do not advertise")

# 10102
# V = int(input())
# vote = [i for i in input() if i == 'A']
# result = len(vote)

# if V - result > result:
#     print("B")
# elif V - result == result:
#     print("Tie")
# else:
#     print("A")

# 10988
# x = input()
# x_reverse = x[::-1]
# result = 1
# for i in range(len(x)):
#     if x[i] == x_reverse[i]:
#         continue
#     else:
#         result = 0
#         break

# print(result)

# 5086
# while True:
#     a, b = map(int, input().split())

#     if a == 0 and b == 0:
#         break

#     if b % a == 0:
#         print("factor")
#     elif a % b == 0:
#         print("multiple")
#     else:
#         print("neither")

# 5717
# while True:
#     a, b = map(int, input().split())

#     if a == 0 and b == 0:
#         break

#     print(a+b)

# 9610
# q1 = q2 = q3 = q4 = axis = 0
# for _ in range(int(input())):
#     a, b = map(int, input().split())

#     if a == 0 or b == 0:
#         axis += 1
#     elif a < 0:
#         if b > 0:
#             q2 += 1
#         else:
#             q3 += 1
#     else:
#         if b > 0:
#             q1 += 1
#         else:
#             q4 += 1

# print("Q1:", q1)
# print("Q2:", q2)
# print("Q3:", q3)
# print("Q4:", q4)
# print("AXIS:", axis)

# 8958
# for _ in range(int(input())):
#     x = input()
#     temp = False
#     count = result = 0

#     for i in x:
#         if i == "O":
#             temp = True
#             count += 1
#         else:
#             count = 0

#         result += count

#     print(result)

# 9506
# while True:
#     x = int(input())
#     result = []

#     if x == -1:
#         break

#     for i in range(1, x):
#         if x % i == 0:
#             result.append(i)

#     if sum(result) == x:
#         temp = str(x) + " = "
#         for i in result:
#             if x // 2 == i:
#                 temp += str(i)
#             else:
#                 temp += (str(i) + " + ")
#         print(temp)
#     else:
#         print("%d is NOT perfect." % x)

# 9506 - others
# while True:
#     r = int(input())
#     if r < 1:
#         break
#     n = [i for i in range(1, r) if r % i == 0]
#     print(r, ['is NOT perfect.', "= " + " + ".join(map(str, n))][sum(n)==r])

# 10162
# T = int(input())
# a=b=c=0

# while T:
#     if T % 10 != 0:
#         break

#     if T >= 300:
#         a += 1
#         T -= 300
#     elif T >= 60:
#         b += 1
#         T -= 60
#     else:
#         c += 1
#         T -= 10

# if T % 10 != 0:
#     print(-1)
# else:
#     print(a, b, c)

# 10103
# import sys
# input = sys.stdin.readline
# x=y=100
# for _ in range(int(input())):
#     a, b = map(int, input().split())

#     if a < b:
#         x -= b
#     elif a > b:
#         y -= a

# print('\n'.join([str(x), str(y)]))

# 10214
# import sys
# input = sys.stdin.readline
# for _ in range(int(input())):
#     y=k=0

#     for _ in range(9):
#         a, b = map(int, input().split())
#         y += a
#         k += b

#     if y > k:
#         print("Yonsei")
#     elif y < k:
#         print("Korea")
#     else:
#         print("Draw")

# 1977
# import sys
# input = sys.stdin.readline
# result = []
# i = 1

# M = int(input())
# N = int(input())

# while i ** 2 <= N:
#     if i ** 2 >= M:
#         result.append(i**2)
#     i += 1

# if not result:
#     print("-1")
# else:
#     print(sum(result))
#     print(result[0])

# 11098
# import sys
# input = sys.stdin.readline
# for _ in range(int(input())):
#     p = int(input())
#     c, name = 0, ''
#     for _ in range(p):
#         temp_c, temp_name = input().split()
#         temp_c = int(temp_c)

#         if c < temp_c:
#             c = temp_c
#             name = temp_name

#     print(name)

# 5635
# import sys
# input = sys.stdin.readline
# min_name, max_name = '', ''
# min_age, max_age = 1000, 0
# min_age_month, min_age_day = 1000, 0
# max_age_month, max_age_day = 1000, 0

# for _  in range(int(input())):
#     a, b, c, d = input().split()
#     temp_age = 2011 - int(d)
#     check_min, check_max = False, False

#     if min_age > temp_age:
#         check_min = True
#     elif min_age == temp_age:
#         if min_age_month > int(c):
#             check_min = True
#         elif min_age_month == int(c):
#             if min_age_day > int(b):
#                 check_min = True

#     if max_age < temp_age:
#         check_max = True
#     elif max_age == temp_age:
#         if max_age_month > int(c):
#             check_max = True
#         elif max_age_month == int(c):
#             if max_age_day > int(b):
#                 check_max = True

#     if check_max:
#         max_age = temp_age
#         max_age_month = int(c)
#         max_age_day = int(b)
#         max_name = a

#     if check_min:
#         min_age = temp_age
#         min_age_month = int(c)
#         min_age_day = int(b)
#         min_name = a

# print(min_name)
# print(max_name)

# 1408
# import sys
# input = sys.stdin.readline
# a, b, c = map(int, input().split(':'))
# d, e, f = map(int, input().split(':'))
# start = c + b*60 + a*60*60
# fin = f + e*60 + d*60*60
# if start > fin:
#     fin += (24*60*60)

# result = fin-start
# print("%02d:%02d:%02d" % (result//3600, result%3600//60, result%60))

# 2501
# n, k = map(int, input().split())
# result = []

# for i in range(1, n+1):
#     if n % i == 0:
#         result.append(i)
    
# if len(result) < k:
#     print(0)
# else:
#     print(result[k-1])
