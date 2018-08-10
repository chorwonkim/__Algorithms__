from collections import defaultdict

d = defaultdict(list)
n, m = map(int, input().split())

for _ in range(n):
    d['A'].append(input())

for _ in range(m):
    d['B'].append(input())

for item in d['B']:

    if d['A'].count(item):
        for i in range(len(d['A'])):
            if d['A'][i] == item:
                print(i + 1, end=' ')
        print()
    else:
        print(-1)