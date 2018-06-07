import sys
Read = sys.stdin.readline
while True:
    a, b = map(int, Read().split())
    if a == 0 and b == 0:
        break
    else:
        print(a + b)