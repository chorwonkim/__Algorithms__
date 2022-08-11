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

n, m, k = map(int, Read().split())
plants = list(map(int, Read().split()))
parent = [0] * (n+1)

for i in range(n+1):
    if i in plants:
        continue
    parent[i] = i

edges = []
result = 0

for _ in range(m):
    a, b, c = map(int, Read().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)