T = int(input())
coins = [25, 10, 5, 1]
for _ in range(T):
    c = int(input())
    result = []

    for coin in coins:
        result.append(c // coin)
        c = c % coin

    for i in result:
        print(i, end=' ')
    print()