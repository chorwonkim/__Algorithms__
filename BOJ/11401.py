"""
[Reference]
http://sexycoder.tistory.com/67
http://koosaga.com/entry/이항계수-nCr-mod-p-계산하기
"""

m = 1000000007


def defined_exp(x, y):
    temp = 1
    while y > 0:
        if (y % 2) == 1:
            temp *= x
            y -= 1
            temp %= m
        x *= x
        x %= m
        y /= 2
    return temp


N, K = map(int, input().split())

r1 = 1
r2 = 1

for i in range(1, N+1):
    r1 *= i
    r1 %= m

for i in range(1, K+1):
    r2 *= i
    r2 %= m

for i in range(1, N-K+1):
    r2 *= i
    r2 %= m

r2 = defined_exp(r2, m-2)
r2 %= m

r1 *= r2
r1 %= m

print(r1)