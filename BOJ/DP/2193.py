from sys import stdin
Read = stdin.readline

N = int(Read())
count = 0


def func_2193(x):
    prev, curr = 1, 1
    while x > 0:
        yield prev
        prev, curr = curr, prev + curr
        x -= 1


for item in func_2193(N):
    count += 1

    if count == N:
        print(item)