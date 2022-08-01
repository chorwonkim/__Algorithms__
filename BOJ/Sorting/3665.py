from collections import deque
from sys import stdin
Read = stdin.readline

t = int(Read())

def topology_sort():
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[n+1-i] == 0:
            q.append(n+1-i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if len(result) != n:
        print("IMPOSSIBLE")
    else:
        for i in result:
            print(i, end=' ')

for _ in range(t):
    n = int(Read())
    last_rank = list(map(int, Read().split()))
    m = int(Read())
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a, b = map(int, Read().split())
        indegree[a] += 1
        graph[b].append(a)

    topology_sort()