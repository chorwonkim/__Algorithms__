import sys
Read = sys.stdin.readline

n, m = map(int, Read().split(':'))


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


temp = gcd(n, m)

print(str(n//temp) + ":" + str(m//temp))
