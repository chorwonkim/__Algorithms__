from sys import stdin
Read = stdin.readline

n = int(Read())
length = []

x = []
y = []
z = []

for i in range(1, n+1):
    a, b, c = map(int, Read().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

for i in range(n-1):
    length.append((x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
    length.append((y[i+1][0]-y[i][0], y[i][1], y[i+1][1]))
    length.append((z[i+1][0]-z[i][0], z[i][1], z[i+1][1]))

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

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

length.sort()
result = 0

for edge in length:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)