from itertools import combinations_with_replacement

S, k = input().split()
S = list(S)
S.sort()
result = combinations_with_replacement(S, int(k))

for item in result:
    temp = (item[i] for i in range(len(item)))

    print(''.join(temp))