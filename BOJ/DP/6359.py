for _ in range(int(input())):
    n = int(input())
    count = 0

    checker = [True for _ in range(n)]

    for i in range(2, n+1):  # n에 따른 횟수
        for j in range(n):  # 방 번호
            if ((j+1) % i) == 0:
                checker[j] = (not checker[j])

    for item in checker:
        if item:
            count += 1

    print(count)