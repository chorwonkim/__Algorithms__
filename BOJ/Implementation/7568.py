n = int(input())
member = []

for _ in range(n):
    x, y = map(int, input().split())
    member.append((x, y))

for i in member:
    temp = 1

    for j in member:
        if i[0] < j[0] and i[1] < j[1]:
            temp += 1

    print(temp, end=' ')