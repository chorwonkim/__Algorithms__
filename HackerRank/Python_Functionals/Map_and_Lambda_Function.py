import sys

cube = lambda x: x**3


def fibonacchi(n):
    result = [0, 1]

    if n == 0:
        result = []
    elif n == 1:
        result = [0]

    for i in range(2, n):
        result.append(result[i-1] + result[i-2])

    return result


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())

    print(list(map(cube, fibonacchi(n))))