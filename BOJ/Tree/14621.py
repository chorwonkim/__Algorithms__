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


v, e = map(int, input().split())
parent = [0] * (v + 1)
parent_class = [0] * (v + 1)

data = list(map(str, input().split()))

for i in range(len(data)):
    if data[i] == "M":
        parent_class[i + 1] = 1

edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if parent_class[a] == parent_class[b]:
        continue

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

# 사이클 확인은 해결에 영향 X, 결국 부모 노드를 가지는 애가 없느냐를 확인해야 했음 (맞나..?)
checker = True
for i in range(2, v + 1):
    if parent[i] == i:
        checker = False

if checker:
    print(result)
else:
    print(-1)