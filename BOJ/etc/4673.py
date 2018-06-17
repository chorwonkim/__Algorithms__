x = set(i for i in range(1, 10001))
temp = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    temp.add(i)
result = sorted(x-temp)
for i in result:
    print(i)