from sys import stdin
Read = stdin.readline

T = int(Read())


def func_10451(x):
    visited[x] = True

    if not visited[Permutation[x]-1]:
        func_10451(Permutation[x]-1)


for _ in range(T):
    N = int(Read())

    visited = [False for _ in range(N)]

    Permutation = list(map(int, Read().split()))

    result = 0

    for i in range(N):
        if not visited[i]:
            func_10451(i)
            result += 1

    print(result)