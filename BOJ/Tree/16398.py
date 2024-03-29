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
parent = [0] * (n+1)
graph = [[0] * (n+1) for _ in range(n+1)]
edges = []
result = 0

for i in range(1, n+1):
    data = list(map(int, Read().split()))
    for j in range(1, n+1):
        graph[i][j] = data[j-1]

for i in range(1, n+1):
    for j in range(i):
        if graph[i][j] != 0:
            edges.append((graph[i][j], i, j))

for i in range(1, n+1):
    parent[i] = i

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)