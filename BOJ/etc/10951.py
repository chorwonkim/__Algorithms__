from sys import stdin
Read = stdin.readline

while True:
    temp = Read().rstrip()
    if not temp:
        break

    A, B = map(int, temp.split())
    print(A+B)