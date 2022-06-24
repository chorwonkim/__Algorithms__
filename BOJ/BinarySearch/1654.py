from sys import stdin
Read = stdin.readline

k, n = map(int, Read().split())
lines = []
for _ in range(k):
    lines.append(int(Read().rstrip()))

lines.sort()

start = 1
end = (1<<31)-1
result = 0

while start <= end:
    total = 0
    mid = (start+end) // 2

    for i in lines:
        total += i // mid

    if total < n:
        end = mid-1
    else:
        result = max(result, mid)
        start = mid+1

print(result)