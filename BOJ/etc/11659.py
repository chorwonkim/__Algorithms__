from sys import stdin
Read = stdin.readline

n, m = map(int, Read().split())
numbers = list(map(int, Read().split()))

for _ in range(m):
    i, j = map(int, Read().split())
    print(sum(numbers[i-1:j]))