import sys
Read = sys.stdin.readline

for _ in range(int(Read())):
    N, M = map(int, Read().split())
    classroom = [Read() for _ in range(N)]
    num = [[0 for _ in range(M)] for _ in range(N)]
    acnt = 0
    bcnt = 0

    for i in range(N):
        for j in range(M):
            if classroom[i][j] == 'x':
                continue
            if j % 2:
                num[i][j] = acnt
                acnt += 1
            else:
                num[i][j] = bcnt
                bcnt += 1

    adj = [[] for _ in range(acnt)]
    for i in range(N):
        for j in range(M):
            if classroom[i][j] == 'x':
                continue
            if j % 2:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 1]:
                        nx = i + dx
                        ny = j + dy
                        if 0 <= nx < N and 0 <= ny < M and classroom[nx][ny] == '.':
                            adj[num[i][j]].append(num[nx][ny])

    vis = [0] * acnt
    match = [-1] * bcnt
    vcnt = 0

    def dfs(cur):
        if vis[cur] == vcnt:
            return 0
        vis[cur] = vcnt
        for nxt in adj[cur]:
            if match[nxt] == -1 or dfs(match[nxt]):
                match[nxt] = cur
                return 1
        return 0


    matched = 0
    for i in range(acnt):
        vcnt += 1
        matched += dfs(i)
    print(acnt + bcnt - matched)