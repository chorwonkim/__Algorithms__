N = int(input())
count = 0
start = 666

while count < N:

    if str(start).count('666') >= 1:
        count += 1

    start += 1

print(start-1)