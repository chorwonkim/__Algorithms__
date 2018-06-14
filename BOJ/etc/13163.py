import sys
Read = sys.stdin.readline

for _ in range(int(Read())):
    first, *args = map(str, Read().split())

    print("god" + "".join(args))
