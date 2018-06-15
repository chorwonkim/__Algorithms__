# Memory exceed. N <= 10000000

N = int(input())
x = sum((i for i in range(1, N)))
y = sum((i for i in map(int, input().split())))
print(y-x)