from sys import stdin
Read = stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(Read())
m = int(Read())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(n):
    data = list(map(int, Read().split()))

    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i+1, j+1)

cities = list(map(int, Read().split()))

result = parent[cities[0]]
checker = True
for i in cities[1:]:
    if result != parent[i]:
        checker = False
        break

if checker:
    print("YES")
else:
    print("NO")