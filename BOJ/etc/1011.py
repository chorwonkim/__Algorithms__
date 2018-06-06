import sys
Read = sys.stdin.readline

for _ in range(int(Read())):
    x, y = map(int, Read().split())

    result = 0
    light_year = 1
    distance = y-x
    while distance:
        if distance > light_year * 2:
            result += 2
            distance -= light_year * 2
            light_year += 1

        else:
            temp = distance // light_year
            distance -= temp * light_year
            result += temp
            light_year -= 1

    print(result)
