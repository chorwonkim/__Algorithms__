N, X = map(int, input().split())
temp = []

for i in range(X):
    temp.append(list(map(float, input().split())))

result = list(zip(*temp))

for item in result:
    print(sum(item)/X)