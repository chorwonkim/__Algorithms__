progress = []
number, threshold = map(int, input().split())

progress = list(map(int, input().split()))

for i in progress:
    if i < threshold:
        print(i, end=" ")