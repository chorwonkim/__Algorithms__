from itertools import combinations
N = range(1, int(input())+1)
string = list(map(str, input().split()))
K = int(input())

temp = combinations(N, K)
count = 0
ans = 0

for item in temp:
    ans += 1
    for x in item:
        if string[x-1] is 'a':
            count += 1
            break


print("%.4f" % (count/ans))
