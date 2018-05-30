import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    x, y = sys.stdin.readline().rstrip().split()
    x, y = int(x), int(y)
    print(x+y)