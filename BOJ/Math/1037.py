N = int(input())
items = list(map(int, input().split()))

items.sort()

print(items[0] * items[-1])