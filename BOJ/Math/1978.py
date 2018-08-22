from sys import stdin
Read = stdin.readline

N = int(Read())
numbers = list(map(int, Read().split()))
result = 0

for item in numbers:
    checker = False

    if item == 1:
        continue

    for j in range(2, item):
        if item % j == 0:
            checker = True
            continue

    if not checker:
        result += 1


print(result)