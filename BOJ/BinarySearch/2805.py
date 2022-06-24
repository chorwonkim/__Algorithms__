from sys import stdin
Read = stdin.readline

n, m = map(int, Read().split())
trees = list(map(int, Read().split()))
trees.sort()

start = 0
end = trees[-1]
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in trees:
        if i > mid:
            total += (i - mid)

    if total < m:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)