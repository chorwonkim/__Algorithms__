history_0 = [1, 0, 1]
history_1 = [0, 1, 1]


def fibo(n):
    length = len(history_0)

    if length <= n:
        for i in range(length, n+1):
            history_0.append(history_0[i-1] + history_0[i-2])
            history_1.append(history_1[i - 1] + history_1[i - 2])

    print(history_0[n], history_1[n])


for i in range(int(input())):
    fibo(int(input()))

