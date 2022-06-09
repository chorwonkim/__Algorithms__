from sys import stdin
Read = stdin.readline

n = int(Read())
graph = []

for _ in range(n):
    x, y = map(int, Read().split())
    graph.append((x, y))

graph.sort()

for i, j in graph:
    print(i, j)