from sys import stdout

N = int(input())


def func_1914(number, a, b, c):
    if number == 1:
        stdout.write(str(a) + " " + str(c) + "\n")
        return

    func_1914(number-1, a, c, b)
    stdout.write(str(a) + " " + str(c) + "\n")
    func_1914(number-1, b, a, c)


if N > 20:
    print((2**N)-1)
else:
    print((2 ** N) - 1)
    func_1914(N, 1, 2, 3)