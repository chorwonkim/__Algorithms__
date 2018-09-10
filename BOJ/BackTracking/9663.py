import sys
sys.setrecursionlimit(1000000)
N = int(input())
col = [i for i in range(N+1)]
result = 0


def queens(i):
    if i > N:
        global result
        result += 1
    else:
        for j in range(1, N+1):
            col[j] = i
            if promising(i):
                queens(i+1)
            else:
                col[i] = 0


def promising(i):
    for j in range(1, i):
        if col[j] == col[i]:
            return False

        if abs(col[j] - col[i]) == abs(j-i):
            return False

    return True


queens(0)
print(result)