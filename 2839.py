N = int(input())

x = N//5
y = N//3

result = N

for i in range(x+1):
    for j in range(y+1):
        if (5*i + 3*j) == N:
            if result > (i+j):
                result = (i+j)
            else:
                continue

if result == N:
    print(-1)
else:
    print(result)