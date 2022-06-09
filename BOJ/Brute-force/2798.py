from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

x = combinations(cards, 3)
result = m
for i in x:
    temp = sum(i)

    if temp > m:
        continue
    elif temp == m:
        result = 0
        break
    else:
        if result > m - temp:
            result = m - temp

print(m-result)