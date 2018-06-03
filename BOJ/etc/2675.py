import sys

T = sys.stdin.readline().rstrip()

for i in range(int(T)):
    R, S = sys.stdin.readline().rstrip().split()
    S = list(S)

    for character in S:
        print(character * int(R), end='')

    if i == int(T)-1:
        break
    else:
        print()