# 1-3, 10171
# x = '''\    /\\
#  )  ( ')
# (  /  )
#  \(__)|'''

# print(x)

# 1-11, 2588
# x = int(input())
# y = input()

# for i in y[::-1]:
#     print(x * int(i))

# print(x*int(y))

# 2-1, 1330
# a, b = map(int, input().split())

# if a < b:
#     print("<")
# elif a > b:
#     print(">")
# else:
#     print("==")

# 2-4, 14681
# x = int(input())
# y = int(input())

# if x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# else:
#     print(4)

# 2-5, 2884
# H, M = map(int, input().split())

# if M < 45:
#     M = M + 15
#     H = H - 1

#     if H < 0:
#         H = H + 24

#     print(H, M)
# else:
#     print(H, M-45)

# 3-4, 15552
# import sys
# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     A, B = map(int, input().split())
#     print(A+B)

# 5-1, 10818
# N = int(input())
# x = list(map(int, input().split()))
# x.sort()
# print(x[0], x[-1])

# 5-2, 2562
# import sys
# input = sys.stdin.readline
# temp = 0
# count = 0

# for i in range(9):
#     x = int(input())
    
#     if temp < x:
#         temp = x
#         count = i

# print(temp)
# print(count+1)

# 5-4, 3052
# x = [int(input()) for _ in range(10)]
# result = set()
# for i in x:
#     result.add(i % 42)
# print(len(result))

# print(len({int(i)%42 for i in open(0)}))
# 해당 코드를 IDE에서 수행할 경우, 마지막 값으로 ctrl + z와 같은 키 입력 필요

# 6-2, 4673
## set으로 푸는 경우
# member = set(i for i in range(10001))
# # set(range(1, 10001)) can possible
# result = set()

# for i in range(10001):
#     for j in str(i):
#         i += int(j)
#     result.add(i)

# for i in sorted(member - result):
#     print(i)

## 함수로 푸는 경우
# def Kaprekar(n) -> int:
#     x = 0
#     for i in str(n):
#         x += int(i)

#     return n+x

# result = set(range(1, 10001))
# temp = set()

# for i in range(10001):
#     temp.add(Kaprekar(i))

# ans = result - temp

# for i in sorted(ans):
#     print(i)

# 6-3, 1065
# # not using Func
# N = int(input())

# result = 0
# # 함수로 만들려면 해당 부분을 옮기면 됨. 
# for i in range(1, N+1):
#     if i < 100:
#         result += 1
#     else:
#         temp = list(map(int, str(i)))
#         if temp[1] - temp[0] == temp[2] - temp[1]:
#             result += 1

# print(result)