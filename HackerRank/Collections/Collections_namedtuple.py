from collections import namedtuple
N = int(input())
Students = namedtuple('Students', input())
result = 0

for _ in range(N):
    a, b, c, d = input().split()
    xyz = Students(a, b, c, d)
    result += int(xyz.MARKS)

print("%.2f" % (result/N))