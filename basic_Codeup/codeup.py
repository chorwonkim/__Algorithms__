# 6001
# print("Hello")

# 6002
# print("Hello World")

# 6003
# print("Hello")
# print("World")

# 6004
# print("'Hello'")

# 6005
# print('"Hello World"')

# 6006
# print("\"!@#$%^&*()\'")

# 6007
# print("\"C:\\Download\\\'hello\'.py\"")

# 6008
# print("print(\"Hello\\nWorld\")")

# 6009
# print(input())

# 6010
# print(int(input()))

# 6011
# print(float(input()))

# 6012
# a = input()
# b = input()
# print(a)
# print(b)

# 6013
# a = input()
# b = input()
# print(b)
# print(a)

# 6014
# a = input()
# for _ in range(0, 3):
#     print(a)

# 6015
# a, b = input().split()
# print(a)
# print(b)

# 6016
# a, b = input().split()
# print(b, a)

# 6017
# a = input()
# print(a, a, a)

# 6018
# a, b = input().split(':')
# print(a, b, sep=':')

# 6019
# y, m, d = input().split('.')
# print(d,m,y,sep='-')

# 6020
# a, b = input().split('-')
# print(a, b, sep='')

# 6021
# a = input()
# for i in a:
#     print(i)

# 6022
# s = input()
# print(s[0:2], s[2:4], s[4:6])

# 6023
# _, m, _ = input().split(':')
# print(m)

# 6024
# a, b = input().split()
# print(a, b, sep='')

# 6025
# a, b = map(int, input().split())
# print(a+b)

# 6026
# a = float(input())
# b = float(input())
# print(a+b)

# 6027
# print("%x" % int(input()))

# 6028
# print("%X" % int(input()))

# 6029
# a = int(input(), 16)
# print("%o" % a)

# 6030
# print(ord(input()))

# 6031
# 정수 입력 받고, 유니코드 문자로 변환
# print(chr(int(input())))

# 6032
# print(-int(input()))

# 6033
# a = input()
# print(chr(ord(a)+1))

# 6034
# a, b = map(int, input().split())
# print(a-b)

# 6035
# a, b = map(float, input().split())
# print(a*b)

# 6036
# w, n = input().split()
# print(w*int(n))

# 6037
# n = int(input())
# s = input()
# print(s*n)

# 6038
# a, b = map(int, input().split())
# print(a**b)

# 6039
# a, b = map(float, input().split())
# print(a**b)

# 6040
# a, b = map(int, input().split())
# print(a//b)

# 6041
# a, b = map(int, input().split())
# print(a%b)

# 6042
# a = float(input())
# print(format(a, ".2f"))

# 6043
# a, b = map(float, input().split())
# print(format(a/b, ".3f"))

# 6044
# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
# print(format(a/b, ".2f"))

# 6045
# a, b, c = map(int, input().split())
# temp = a+b+c
# print(temp, format(temp/3, ".2f"))

# 6046
# n = int(input())
# print(n<<1)

# 6047
# a, b = map(int, input().split())
# print(a<<b)

# 6048~51
# a, b = map(int, input().split())
# print(a<b)

# 6052
# a = int(input())
# print(bool(a))

# 6053
# a = bool(int(input()))
# print(not a)

# 6054
# a, b = map(int, input().split())
# print(bool(a) and bool(b))

# 6055
# a, b = map(int, input().split())
# print(bool(a) or bool(b))

# 6056
# a, b = map(int, input().split())
# a = bool(a)
# b = bool(b)
# print((a and (not b)) or ((not a) and b))
# print(((not a) or b) and (a or (not b)))

# 6057
# a, b = map(int, input().split())
# a = bool(a)
# b = bool(b)
# print(((not a) or b) and (a or (not b)))

# 6058
# a, b = map(int, input().split())
# print(not (bool(a) or bool(b)))

# 6059
# a = int(input())
# print(~a)

# 6060
# a, b = map(int, input().split())
# print(a & b)

# 6061
# 비트단위 연산은 빠른 계산이 필요한 그래픽처리에서도 효과적으로 사용
# a, b = map(int, input().split())
# print(a | b)

# 6062
# a, b = map(int, input().split())
# print(a ^ b)

# 6063
# a, b = map(int, input().split())
# print(a if a>=b else b)

# 6064
# a, b, c = map(int, input().split())
# print((a if a<=b else b) if ((a if a<=b else b)<=c) else c)

# 6065
# a, b, c = map(int, input().split())

# if a % 2 == 0:
#     print(a)

# if b % 2 == 0:
#     print(b)

# if c % 2 == 0:
#     print(c)

# 6066
# a = map(int, input().split())
# for i in a:
#     if i % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# 6067
# a = int(input())
# if a < 0:
#     if a % 2 == 0:
#         print("A")
#     else:
#         print("B")
# else:
#     if a % 2 == 0:
#         print("C")
#     else:
#         print("D")

# 6068
# a = int(input())
# if a >= 90:
#     print("A")
# elif a >= 70 and a <= 89:
#     print("B")
# elif a >= 40 and a <= 69:
#     print("C")
# else:
#     print("D")

# 6069
# a = input()
# if a == 'A':
#     print("best!!!")
# elif a == 'B':
#     print("good!!")
# elif a == 'C':
#     print("run!")
# elif a == 'D':
#     print("slowly~")
# else:
#     print("what?")

# 6070
# a = int(input())
# if a // 3 == 1:
#     print("spring")
# elif a // 3 == 2:
#     print("summer")
# elif a // 3 == 3:
#     print("fall")
# else:
#     print("winter")

# 6071
# while True:
#     a = int(input())
#     if a == 0:
#         break
#     else:
#         print(a)

# 6072
# a = int(input())
# while a != 0:
#     print(a)
#     a = a-1

# 6073
# a = int(input())
# while a > 0:
#     a = a-1
#     print(a)

# 6074
# a = ord(input())
# temp = ord('a')

# while temp <= a:
#     print(chr(temp), end=' ')
#     temp += 1

# 6075~6
# a = int(input())
# for i in range(a+1):
#     print(i)

# 6077
# a = int(input())
# result = 0
# for i in range(a+1):
#     if i % 2 == 0:
#         result += i
# print(result)

# 6078
# a = ''
# while a != 'q':
#     a = input()
#     print(a)

# 6079
# a = int(input())
# result = 0
# temp = 0
# while True:
#     result += temp
#     if result >= a:
#         break
#     temp += 1
# print(temp)

# 6080
# a, b = map(int, input().split())
# for i in range(1,a+1):
#     for j in range(1, b+1):
#         print(i, j)

# 6081
# temp = input()
# a = int(temp, 16)

# for i in range(1, 16):
#     print("%X" % a, "*%X" % i, "=%X" % (a*i), sep='')

# 6082
