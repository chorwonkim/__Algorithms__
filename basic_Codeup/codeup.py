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
a, b = map(int, input().split())
print(a & b)