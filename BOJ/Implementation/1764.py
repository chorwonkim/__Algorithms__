N, M = map(int, input().split())
Hear = []
See = []

for i in range(N):
    Hear.append(input())

for i in range(M):
    See.append(input())

Hear_process = set(Hear)
See_process = set(See)


result = Hear_process.intersection(See_process)

print(len(result))

for item in sorted(result):
    print(item)
