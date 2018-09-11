from sys import stdin, stdout
while True:
    N, M = map(int, stdin.readline().split())

    if N == 0 and M == 0:
        break

    stdout.write("Yes" + "\n") if N > M else stdout.write("No" + "\n")