for _ in range(int(input())):
    N, M = map(int, input().split())
    t = [0 for _ in range(N)]

    for i in range(N):
        t[i] = int(input())

    t.sort()

    max_time = result = max(t) * M
    min_time = 0
    # time_range = [i for i in range(min_time, max_time+1)]

    while True:

        if max_time < min_time:
            break

        middle = (max_time + min_time) // 2
        checker = 0

        for i in range(N):
            checker += (middle // t[i])

        # print(checker)

        if checker >= M:
            if result > middle:
                result = middle
            max_time = middle - 1
        elif checker < M:
            min_time = middle + 1

    print(result)