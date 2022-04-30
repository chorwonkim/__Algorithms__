from sys import stdin
Read = stdin.readline

n = int(Read().rstrip())
result = 0

for _ in range(n):
    word = Read().rstrip()
    checker = []
    cont = False

    for i in word:
        if i not in checker:
            checker.append(i)
            cont = True
        else:
            if checker[-1] == i:
                cont = True
            else:
                cont = False
                break

    if cont:
        result += 1

print(result)