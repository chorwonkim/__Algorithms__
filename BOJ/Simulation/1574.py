M = int(input())

cups = [i for i in range(3)]

for _ in range(M):
    x, y = map(int, input().split())

    temp1 = cups.index(x-1)
    temp2 = cups.index(y-1)

    cups[temp1], cups[temp2] = cups[temp2], cups[temp1]

print(cups[0]+1)