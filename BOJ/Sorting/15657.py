from itertools import combinations_with_replacement

N, M = map(int, input().split())
line = list(map(int, input().split()))

for item in combinations_with_replacement(sorted(line), M):
    temp = ''
    for i in item:
        temp += (str(i) + " ")

    print(temp)