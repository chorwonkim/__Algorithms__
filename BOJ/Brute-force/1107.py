import sys

Read = sys.stdin.readline
button = [str(i) for i in range(0,10)]

N = Read().rstrip()
M = int(Read())

for item in Read().split():
    button.remove(item)

result = abs(int(N)-100)

for i in range(int(N),-1,-1):
    checking = True

    for j in str(i):
        if j in button:
            continue
        else:
            checking = False
            break

    if checking:
        result = min(result, int(N)-i+len(str(i)))
        break

for i in range(int(N), (int(N)+10)*10):
    checking = True

    for j in str(i):
        if j in button:
            continue
        else:
            checking = False
            break

    if checking:
        result = min(result, i-int(N)+len(str(i)))
        break

print(result)