from itertools import product

N, M = map(int, input().split())
line = [i for i in range(1, N+1)]

for item in product(line, repeat=M):
    temp = ''
    for i in item:
        temp += (str(i) + " ")

    print(temp)