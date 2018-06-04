import sys

T = int(sys.stdin.readline().rstrip())
result = [1, 2, 4]

for i in range(T):
    target = int(sys.stdin.readline().rstrip())

    for j in range(len(result), target):
        result.append(result[j-1] + result[j-2] + result[j-3])

    print(result[target-1])
