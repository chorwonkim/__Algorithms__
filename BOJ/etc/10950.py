import sys
Read = sys.stdin.readline

for _ in range(int(Read())):
    a = list(map(int, Read().split()))
    print(sum(a))