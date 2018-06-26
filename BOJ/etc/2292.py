from sys import stdin
Read = stdin.readline

N = int(Read().rstrip())
result = 1
i = 1

while True:
    temp = N - result
    if temp > 0:
        result += 6 * i
        i += 1
    else:
        break

print(i)