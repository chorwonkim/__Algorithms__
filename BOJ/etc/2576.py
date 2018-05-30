values = []

for i in range(7):
    x = int(input())
    if x % 2 != 0:
        values.append(x)
    else:
        continue


if not values:
    print(-1)
else:
    values.sort()
    print(sum(values))
    print(values[0])

