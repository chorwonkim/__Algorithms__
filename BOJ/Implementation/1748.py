n = input()
point = len(n)
result = 0
for i in range(1, len(n)+1):
    if point == i:
        result += ((int(n) - 10**(point-1) + 1) * point)
    else:
        result += 9 * (10 ** (i-1)) * i

    # print(i, point, result)
print(result)