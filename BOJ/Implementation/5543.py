burgers = [int(input()) for _ in range(3)]
drinks = [int(input()) for _ in range(2)]
result = 4000

for burger in burgers:
    for drink in drinks:
        temp = burger + drink - 50

        if result > temp:
            result = temp

print(result)