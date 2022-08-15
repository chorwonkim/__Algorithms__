t = 1
while True:
    l, p, v = map(int, input().split())
    result = 0

    if l == 0 and p == 0 and v == 0:
        break

    result += (v // p)

    if l - v % p > 0:
        result *= l
        result += (v % p)
    else:
        result *= l
        result += l

    print("Case " + str(t) + ": " + str(result))
    t += 1