import sys
Read = sys.stdin.readline

for _ in range(int(Read())):
    N = bin(int(Read()))

    for i in range(len(N)):
        if N[len(N)-1-i] == '1':
            print(i, end=' ')