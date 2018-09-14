N = int(input())
col = [0] * N
result = 0


def queens(i):
    if i == N:
        global result
        result += 1
    else:
        for j in range(N):
            col[i] = j
            if promising(i):
                queens(i+1)


def promising(i):
    for j in range(i):
        if col[j] == col[i]:
            return False
        if col[j] - col[i] == i-j:
            return False
        if col[i] - col[j] == i-j:
            return False

    return True


queens(0)
print(result)