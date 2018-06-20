import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
result = []
i = 1

while i**2 <= N:
    if i**2 >= M:
        result.append(i**2)
    i += 1

if not result:
    sys.stdout.write("-1\n")
else:
    sys.stdout.write(str(sum(result)) + "\n")
    sys.stdout.write(str(result[0]) + "\n")