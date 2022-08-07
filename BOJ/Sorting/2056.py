from collections import deque
from sys import stdin
Read = stdin.readline

n = int(Read())
indegree = [0] * (n+1)
times = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    data = list(map(int, Read().split()))
    times[i] = data[0]

    for j in data[2:]:
        indegree[i] += 1
        graph[j].append(i)

dp = [0] * (n+1)

def topology_sort():
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = times[i]

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[now]+times[i], dp[i])
            if indegree[i] == 0:
                q.append(i)

topology_sort()

print(max(dp))