import sys
Read = sys.stdin.readline

N = int(Read())
result = [0 for _ in range(10)]
firstPage = 1
temp = 1


def func_1019(x, y):
    while x > 0:
        result[x % 10] += y
        x //= 10


while firstPage <= N:
    while (firstPage % 10) != 0 and firstPage <= N:
        func_1019(firstPage, temp)
        firstPage += 1

    if firstPage > N:
        break

    while (N % 10) != 9 and firstPage <= N:
        func_1019(N, temp)
        N -= 1

    count = N//10 - firstPage//10 + 1

    for i in range(10):
        result[i] += (count * temp)

    firstPage //= 10
    N //= 10
    temp *= 10

for item in result:
    print(item, end=' ')