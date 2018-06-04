import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    convenience = int(sys.stdin.readline().rstrip())
    convenience += 2

    location_x = [0 for _ in range(convenience)]
    location_y = [0 for _ in range(convenience)]
    whole_map = [[0 for _ in range(convenience)] for _ in range(convenience)]

    for j in range(convenience):
        location_x[j], location_y[j] = map(int, sys.stdin.readline().rstrip().split())

    for p in range(convenience):
        for q in range(convenience):
            length = abs(location_x[p] - location_x[q]) + abs(location_y[p] - location_y[q])
            if length <= 1000:
                whole_map[p][q] = whole_map[q][p] = 1

    for x in range(convenience):
        for y in range(convenience):
            for z in range(1, convenience):
                if whole_map[y][x] and whole_map[x][z]:
                    whole_map[y][z] = whole_map[z][y] = 1

    print("happy" if whole_map[0][convenience-1] else "sad")