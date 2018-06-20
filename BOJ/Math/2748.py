from sys import stdin
Read = stdin.readline
n = int(Read())


def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev+curr


f = fib()

for _ in range(n):
    result = next(f)

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    print(result)