from sys import stdin
from collections import Counter
Read = stdin.readline

n = int(Read().rstrip())
numbers = []

for _ in range(n):
    numbers.append(int(Read().rstrip()))

print(round(sum(numbers) / n))
numbers.sort()
print(numbers[n//2])
count = sorted(Counter(numbers).items(), key=lambda x: (-x[1], x[0]))

if n == 1:
    print(numbers[0])
else:
    if count[0][1] != count[1][1]:
        print(count[0][0])
    else:
        print(count[1][0])

print(numbers[-1] - numbers[0])