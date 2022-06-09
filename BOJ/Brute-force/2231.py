n = input()
checker = False
result = 0
for i in range(int(n)-len(n)*9, int(n)):
    temp = result = i

    for j in range(len(n)-1, 0, -1):
        result += temp // (10**j)
        temp %= (10**j)

    result += temp

    if result == int(n):
        checker = True
        result = i
        break

if checker:
    print(result)
else:
    print(0)