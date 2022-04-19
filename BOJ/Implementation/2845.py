import sys
input = sys.stdin.readline
l, p = map(int, input().split())
party = list(map(int, input().split()))
for i in party:
    print(i-(p*l), end=' ')