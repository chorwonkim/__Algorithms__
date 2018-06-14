import sys
Read = sys.stdin.readline
N = int(Read())
A = sorted([int(i) for i in Read().split()])
B = sorted([int(i) for i in Read().split()], reverse=True)
print(sum(map(lambda x,y: x * y, A, B)))