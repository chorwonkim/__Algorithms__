import sys

temp = str(int(sys.stdin.readline().rstrip()) * int(sys.stdin.readline().rstrip()) * int(sys.stdin.readline().rstrip()))

for i in range(10):
    print(temp.count(str(i)))