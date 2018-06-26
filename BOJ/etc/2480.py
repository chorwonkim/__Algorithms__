from sys import stdin
Read = stdin.readline

a, b, c = map(int, Read().split())

if a == b:
    if b == c:
        print(10000+a*1000)
    else:
        print(1000 + a*100)
else:
    if b == c or a == c:
        print(1000 + c*100)
    else:
        print(max(a,b,c) * 100)