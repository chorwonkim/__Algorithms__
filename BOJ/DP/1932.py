n = int(input())
x = []

for i in range(n):
    x.append(list(map(int, input().split(' '))))

    for j in range(len(x)):

        if i == 0:
            break

        if j == 0:
            x[i][j] += x[i-1][j]
        elif j == len(x)-1:
            x[i][j] += x[i-1][j-1]
        else:
            x[i][j] += max(x[i-1][j-1], x[i-1][j])

print(max(x[n-1]))
