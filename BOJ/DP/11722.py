from sys import stdin
Read = stdin.readline

N = int(Read())
items = list(map(int, Read().split()))
result = [0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        print(items[i], i, items[j], j)
        if items[i] < items[j]:
            result[i] = max(result[i], result[j] + 1)
            # result[i] += 1
        # print(result, "AAA")

print(max(result)+1)