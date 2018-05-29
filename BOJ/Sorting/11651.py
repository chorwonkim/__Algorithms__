Coordinates = []

for i in range(int(input())):
    Coordinates.append(tuple(map(int, input().split())))

Coordinates.sort(key=lambda x: (x[1], x[0]))

for x, y in Coordinates:
    print(x, y)