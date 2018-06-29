# from sys import stdin
# Read = stdin.readline
# n = int(Read())
#
#
# def fib():
#     prev, curr = 0, 1
#     while True:
#         yield curr
#         prev, curr = curr, prev+curr
#
#
# f = fib()
#
# for _ in range(n):
#     result = next(f)
#
# if n == 0:
#     print(0)
# elif n == 1:
#     print(1)
# else:
#     print(result)


# N = int(input())
#
# def fib():
#     prev, curr = 0, 1
#     while True:
#         yield curr
#         prev, curr = curr, prev+curr
#
#
# f = fib()
#
# for _ in range(N):
#     result = next(f)
#
# if N == 0:
#     print(0)
# elif N == 1:
#     print(1)
# else:
#     print(result % 1000000)

# 문제 번호 2920
# 위의 피보나치와는 아무런 상관없는데 그냥 테스트 용으로 사용함... lol
x = input().split()
is_sorted_ascend = (sorted(x) == x)
is_sorted_descend = (sorted(x, reverse=True) == x)

if is_sorted_ascend:
    print("ascending")
elif is_sorted_descend:
    print("descending")
else:
    print("mixed")