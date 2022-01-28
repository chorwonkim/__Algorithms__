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
while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    if b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")