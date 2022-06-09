for _ in range(int(input())):
    h, w, n = map(int, input().split())
    first, second = 0, 0
    if n % h == 0:
        first = (n//h)
        second = h
    else:
        first = (n//h) + 1
        second = (n%h)

    print(second * 100 + first)
