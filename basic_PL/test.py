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

# 2609
# import sys
# input = sys.stdin.readline
# a, b = map(int, input().split())
# x = 1
# if b < a:
#     a, b = b, a

# for i in range(2, a+1):
#     if a % i == 0 and b % i == 0:
#         x = i

# print(x)
# print(x * (a//x) * (b//x))

# 2748
# n = int(input())
# a, b = 0, 1
# result = 0

# if n == 1:
#     result = 1
# else:
#     for _ in range(n-1):
#         result = a+b
#         a, b = b, result

# print(result)

# 10984
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     temp, result = 0, 0
#     for _ in range(int(input())):
#         a, b = map(float, input().split())

#         temp += a
#         result += a*b

#     print(int(temp), round(result/temp, 1))

# 10833
# import sys
# input = sys.stdin.readline
# remain = 0
# for _ in range(int(input())):
#     student, apple = map(int, input().split())

#     remain += apple % student

# print(remain)

# 2442
# n = int(input())

# for i in range(1, n+1):
#     print(' '*(n-i) + '*'*(2*i-1))

# 2443
# n = int(input())

# for i in range(1, n+1):
#     print(' ' * (i-1) + '*' * (2*(n-i)+1))

# 2444
# n = int(input())

# for i in range(1, n+1):
#     print(' ' * (n-i) + '*' * (2*i-1))

# for i in range(2, n+1):
#     print(' ' * (i-1) + '*' * (2*(n-i)+1))

# 9325
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     s = int(input())

#     for _ in range(int(input())):
#         q, p = map(int, input().split())
#         s += (q*p)

#     print(s)

# 2010
# import sys
# input = sys.stdin.readline
# n = int(input())

# result = 0
# for i in range(n):
#     tap = int(input())
#     if i != n-1:
#         tap -= 1
    
#     result += tap

# print(result)

# 5522
# x = 0
# for _ in range(5):
#     x += int(input())
# print(x)

# 10178
# for _ in range(int(input())):
#     c, v = map(int, input().split())

#     print("You get %d piece(s) and your dad gets %d piece(s)." % (c//v, c%v))

# 9295
# for i in range(1, int(input())+1):
#     a, b = map(int, input().split())
#     print("Case %d: %d" % (i, a+b))

# 10569
# from sys import stdin
# input = stdin.readline
# for _ in range(int(input())):
#     v, e = map(int, input().split())
#     print(2-v+e)

# 2921
# n = int(input())
# result = 0
# for i in range(1, n+1):
#     result += ((3*i*(i+1))//2)
# print(result)

# 2522
# n = int(input())
# for i in range(1, n+1):
#     print(' ' * (n-i) + '*'*(i))

# for i in range(1, n):
#     print(' ' * i + '*'*(n-i))

# 10871
# from sys import stdin
# input = stdin.readline
# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# for i in a:
#     if i < x:
#         print(i, end=' ')

# 10872
# def factorial(n):
#     if n <= 0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# n = int(input())
# print(factorial(n))

# 2523
# n = int(input())
# for i in range(1, n+1):
#     print('*'*(i))

# for i in range(1, n):
#     print('*'*(n-i))

# 2445
# n = int(input())
# for i in range(1, n+1):
#     print('*'*i + ' '*(n-i) + ' '*(n-i) + '*'*i)

# for i in range(1, n):
#     print('*'*(n-i) + ' '*i + ' '*i + '*'*(n-i))

# 1978
# n = int(input())
# x = list(map(int, input().split()))

# for i in x:
#     if i == 1:
#         n -= 1
#         continue

#     for j in range(2, i):
#         if i % j == 0:
#             n -= 1
#             break

# print(n)

# 2446
# 오른쪽 공백에 대한 출력 형식 잘못됨 오류 발생
# n = int(input())

# for i in range(1, n+1):
#     print(' '*(i-1) + '*'*(2*(n-i)+1))

# for i in range(1, n):
#     print(' '*(n-i-1) + '*'*(2*i+1))

# 2581
# m = int(input())
# n = int(input())
# result = []

# for i in range(m, n+1):
#     checker = False
#     if i == 1:
#         continue

#     for j in range(2, i):
#         if i % j == 0:
#             checker = True
#             break
    
#     if not checker:
#         result.append(i)

# if len(result) == 0:
#     print(-1)
# else:
#     print(sum(result))
#     print(result[0])

# 2475
# temp = list(map(int, input().split()))
# result = 0
# for i in temp:
#     result += i ** 2

# print(result % 10)

# 9085
# for _ in range(int(input())):
#     _ = int(input())
#     temp = sum(list(map(int, input().split())))

#     print(temp)

# 10797
# date = int(input())
# cars = list(map(int, input().split()))
# result = 0
# for i in cars:
#     if i % 10 == date:
#         result += 1
# print(result)

# 2506
# input()
# temp = 0
# ans = list(input().split())
# result = 0

# for i in ans:
#     if i == '0':
#         checker = False
#     else:
#         checker = True

#     if checker:
#         temp += 1
#         result += temp
#     else:
#         temp = 0

# print(result)

# 2455
# result = temp = 0
# for _ in range(4):
#     a, b = map(int, input().split())
#     temp = temp + b - a
#     if result < temp:
#         result = temp
# print(result)

# 10995
# n = int(input())

# for i in range(n):
#     if i % 2 != 0:
#         for j in range(2*n):
#             if j % 2 != 0:
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#     else:
#         for j in range(2*n):
#             if j % 2 != 0:
#                 print(' ', end='')
#             else:
#                 print('*', end='')

#     print()

# 10991
# n = int(input())

# for i in range(n):
#     print(' '*(n-i-1), end='')

#     for j in range(2*i+1):
#         if j % 2 == 0:
#             print('*', end='')
#         else:
#             print(' ', end='')

#     print()

# 2908
# a, b = map(str, input().split())
# a = a[::-1]
# b = b[::-1]
# if int(a) > int(b):
#     print(a)
# else:
#     print(b)

# 2460
# temp = result = 0
# for _ in range(10):
#     a, b = map(int, input().split())
#     temp = temp + b - a

#     if result < temp:
#         result = temp
# print(result)

# 2577
# a = int(input())
# b = int(input())
# c = int(input())
# temp = str(a*b*c)
# result = [0] * 10
# for i in temp:
#     result[int(i)] += 1

# for i in result:
#     print(i)

# 2592
# result = dict()
# temp = 0
# for i in range(10):
#     x = int(input())
#     temp += x
#     if x not in result.keys():
#         result[x] = 1
#     else:
#         result[x] += 1
# print(temp//10)
# x = [i for i, j in result.items() if j == max(result.values())]
# print(x[0])

# 2711
# for _ in range(int(input())):
#     a, b = input().split()
#     temp = list(b)
#     temp.pop(int(a)-1)
#     print(''.join(temp))

# 2953
# result = count = 0
# for i in range(5):
#     temp = 0
#     x = list(input().split())
#     for j in x:
#         temp += int(j)
#     if result < temp:
#         count = i+1
#         result = temp
# print(count, result)

# 1292 -1
# a, b = map(int, input().split())
# seq = []
# for i in range(1, 46):
#     for j in range(i):
#         seq.append(i)
# print(sum(seq[a-1:b]))

# 1292 -2 - 처음부터 하나씩 더해가는 방법...
# def easy(n):
#     s = 0
#     num, cnt = 1, 1
#     while True:
#         for _ in range(num):
#             if cnt == n+1:
#                 break
#             s += num
#             cnt += 1
#         num += 1
#         if cnt == n+1:
#             break
#     return s

# a, b = map(int, input().split())
# print(easy(b) - easy(a-1))

# 3052
# result = set()
# for _ in range(10):
#     a = int(input())
#     result.add(a % 42)
# print(len(result))

# 3460
# for _ in range(int(input())):
#     n = int(input())
#     result = []

#     while True:
#         if n < 2:
#             result.append(n)
#             break
        
#         result.append(n % 2)
#         n = n // 2
    
#     for i in range(len(result)):
#         if result[i] == 1:
#             print(i, end=' ')

# 10807
# from sys import stdin
# input = stdin.readline
# _ = int(input())
# x = list(input().split())
# v = input().rstrip()  # 문자열 비교시 개행문자 포함되서 실제 비교시 다르다고 나옴
# result = 0
# for i in x:
#     if i == v:
#         result += 1
# print(result)

# 10818 - 1
# from sys import stdin
# input = stdin.readline
# input()
# x = list(map(int, input().split()))
# print(min(x), max(x))

# 10818 - 2 # short time ; 채점 도구에서 동작하는 것 같음
# from sys import stdin
# _, *arr = map(int, stdin.read().split())
# print(min(arr), max(arr))

# 5054
# from sys import stdin
# input = stdin.readline
# for _ in range(int(input())):
#     input()
#     arr = list(map(int, input().split()))
#     arr.sort()
#     result = 0
#     for i in arr:
#         if result == 0:
#             result = i
#         else:
#             result += (i-result)
#     result += (arr[-1] - arr[0] * 2)
#     print(result)

# 2822 // I think this code is not clean
# result = []
# for i in range(1, 9):
#     result.append((int(input()), i))
# result.sort()
# temp = 0
# x = []
# for i, j in result[3:]:
#     temp += i
#     x.append(j)
# print(temp)
# for j in sorted(x):
#     print(j, end=' ')

# 2822 - Reference
# quizs = [int(input()) for i in range(8)]
# result = []
# temp = 0
# for i in sorted(quizs, reverse=True)[:5]:
#     result.append(quizs.index(i))
#     temp += i
# print(temp)
# for i in sorted(result):
#     print(i+1, end=' ')

# 2750
# x = sorted([int(input()) for _ in range(int(input()))])
# for i in x:
#     print(i)

# 2752
# n = list(map(int, input().split()))
# for i in sorted(n):
#     print(i, end=' ')

# 5543
# ham = 2001
# drink = 2001
# for _ in range(3):
#     temp = int(input())
#     if temp < ham:
#         ham = temp
# for _ in range(2):
#     temp = int(input())
#     if temp < drink:
#         drink = temp
# print(ham+drink-50)

# 2587
# x = [int(input()) for _ in range(5)]
# print(sum(x)//5)
# print(sorted(x)[2])

# 1427
# x = list(input())
# print(''.join(sorted(x, reverse=True)))

# 2309  // using combinations
# from itertools import combinations
# x = [int(input()) for _ in range(9)]
# comb = list(combinations(x, 7))

# for i in comb:
#     temp = 0
#     for j in i:
#         temp += j
#     if temp == 100:
#         for j in sorted(i):
#             print(j)
#         break

# 2309  // not combinations
# x = sorted(int(input()) for _ in range(9))
# for i in x:
#     for j in x:
#         if i+j == sum(x)-100:
#             x.remove(i)
#             x.remove(j)
#             break
# for i in x:
#     print(i)

# 9076
# for _ in range(int(input())):
#     x = sorted(list(map(int, input().split())))
#     if x[3]-x[1] >= 4:
#         print("KIN")
#     else:
#         print(sum(x[1:4]))

# 2902
# x = input().split('-')
# for i in x:
#     print(i[0], end='')

# 5800
# for i in range(int(input())):
#     k, *x = map(int, input().split())
#     temp = 0
#     x = sorted(x)
#     for p in range(len(x)-1):
#         if x[p+1] - x[p] > temp:
#             temp = x[p+1] - x[p]
#     print("Class %d" %(i+1))
#     print("Max %d, Min %d, Largest gap %d" % (x[-1], x[0], temp))

# 11047
# from sys import stdin
# input = stdin.readline
# n, k = map(int, input().split())
# coins = []
# for _ in range(n):
#     coins.append(int(input()))

# count = 0
# while k != 0:
#     if coins[-1] > k:
#         coins.pop()
#         continue
#     else:
#         count += (k // coins[-1])
#         k = (k % coins[-1])

# print(count)

# 1357
# x, y = input().split()
# x, y = x[::-1], y[::-1]
# print(int(str(int(x)+int(y))[::-1]))

# 10987
# x = input()
# # temp = ['a','e','i','o','u']
# temp = 'aeiou' # 굳이 리스트로 만들어서 사용할 필요 없음
# count = 0
# for i in x:
#     if i in temp:
#         count += 1
# print(count)

# 4458
# for _ in range(int(input())):
#     # Capitalize 쓰면 맨 앞글자만 대문자, 나머지 소문자로 망함
#     # Title은 And, of와 같은 접속사, 전치사도 대문자로 만들기에 망함
#     x = str(input())
#     x = x[0].upper() + x[1:]
#     print(x)

# 11654
# print(ord(input()))

# 11720
# input()
# print(sum(list(map(int, input()))))

# 11721
# x = input()
# for i in range(len(x)//10+1):
#     print(x[i*10:i*10+10])

# 10821
# print(len(input().split(',')))

# 10808
# s = input()
# result = [0 for _ in range(26)]
# for i in s:
#     result[ord(i)-97] += 1
# for i in result:
#     print(i, end=' ')

# s = input()
# result = [0 for _ in range(26)]  # 갯수 조심!!!
# for i in s:
#     result[ord(i)-97] += 1
# print(' '.join(map(str, result)))

# 1157 1. dictionary - slow
# result = dict()
# string = input().lower()
# for i in string:
#     if i in result:
#         result[i] += 1
#     else:
#         result[i] = 1
# x = list(result.values())
# if x.count(max(x)) >= 2:
#     print('?')
# else:
#     for key, value in result.items():
#         if value == max(x):
#             print(key.upper())

# 1157 2. fast method
# n = input().upper()
# temp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# result = []
# for i in temp:
#     result.append(n.count(i))

# if  result.count(max(result)) > 1:
#     print("?")
# else:
#     print(temp[result.index(max(result))])

# 9086
# for _ in range(int(input())):
#     x = input()
#     print(x[0] + x[-1])

# 5218
# for _ in range(int(input())):
#     a, b = input().split()
#     print("Distances:", end='')
#     for i in range(len(a)):
#         x, y = ord(a[i]), ord(b[i])
#         if y >= x:
#             print(" %d" % (y-x), end='')
#         else:
#             print(" %d" % (y+26-x), end='')
#     print()

# 11365
# while True:
#     x = input()

#     if x == "END":
#         break
#     else:
#         print(x[::-1])

# 11170 1. 숫자 입력 받은 후 하나하나 세는 방법
# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     count = 0
#     for i in range(n, m+1):
#         for j in str(i):
#             if j == '0':
#                 count += 1
#     print(count)

# 11170 2. 아예 처음부터 모든 종류에 대해서 입력
# result = [1] # 0일때는 1개
# for i in range(1, 1000001):
#     result.append(result[-1] + str(i).count('0')) # 이전 숫자까지의 0의 개수에 현재 수 추가
# result.append(0)
# for _ in range(int(input())):
#     a, b = map(int, input().split())
#     print(result[b] - result[a-1])

# 11665
# x = list(input())
# result = ""
# for i in x:
#     if 'A' <= i <= 'Z':
#         if ord(i) + 13 > 90:
#             result += chr(ord(i)-13)
#         else:
#             result += chr(ord(i)+13)
#     elif 'a' <= i <= 'z':
#         if ord(i) + 13 > 122:
#             result += chr(ord(i)-13)
#         else:
#             result += chr(ord(i)+13)
#     else:
#         result += i
# print(result)

# # Combinations not itertools
# def combination(arr, n):
#     result = []
#     if n == 0:
#         return [[]]

#     for i in range(len(arr)):
#         temp = arr[i]
#         for rest in combination(arr[i+1:], n-1):
#             result.append([temp] + rest)

#     return result

# print(combination([0,1,2,3], 2))


# # Permutation not itertools
# def permutation(arr, n):
#     result = []

#     if n == 0:
#         return [[]]

#     for i in range(len(arr)):
#         temp = arr[i]
#         for rest in permutation(arr[:i] + arr[i+1:], n-1):
#             result.append([temp] + rest)

#     return result

# print(permutation([0,1,2,3], 3))

# def binary_search(array, target, start, end):
#     if start > end:
#         return None

#     mid = (start+end) // 2

#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1)
#     else:
#         return binary_search(array, target, mid+1, end)

# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start+end) // 2

#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid-1
#         else:
#             start = mid+1

#     return None

# n, m = map(int, input().split())
# rices = list(map(int, input().split()))
# rices.sort()

# start = 0
# end = max(rices)

# result = 0
# while start <= end:
#     total = 0
#     mid = (start+end) // 2

#     for x in rices:
#         if x > mid:
#             total += (x-mid)

#     if total < m:
#         end = mid-1
#     else:
#         result = mid
#         start = mid+1

# print(result)

n = int(input())
numbers = list(map(int, input().split()))

start, end = 0, len(numbers)
result = -1
while start <= end:
    mid = (start + end) // 2

    if numbers[mid] == mid:
        result = mid
        break
    elif numbers[mid] >= mid:
        end = mid-1
    else:
        start = mid+1

print(result)