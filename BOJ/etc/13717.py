import sys
Read = sys.stdin.readline

N = int(Read())
Ps = [0 for _ in range(N)]
result = [0 for _ in range(N)]

for i in range(N):
    Ps[i] = Read()
    need, have = map(int, Read().split())

    while have >= need:
        result[i] += 1
        have = have - need + 2


print(sum(result))
print(Ps[result.index(max(result))])
