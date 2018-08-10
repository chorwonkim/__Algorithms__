from collections import deque


def rotLeft(a, d):
    q = deque(a)

    q.rotate(-d)

    return list(q)


nd = input().split()
n = int(nd[0])
d = int(nd[1])

a = list((map(int, input().rstrip().split())))

result = rotLeft(a, d)

print(result)