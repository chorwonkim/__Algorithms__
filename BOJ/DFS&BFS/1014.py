import sys
Read = sys.stdin.readline


def dfs(x):
    if vis[x] == count:
        return 0
    vis[x] = count
    for item in adj[x]:
        if match[item] == -1 or dfs(match[item]):
            match[item] = x
            print(match)
            print(count, matched)
            print(vis)
            return 1
    return


for _ in range(int(Read())):
    N, M = map(int, Read().split())
    classroom = [Read() for _ in range(N)]
    num = [[0 for _ in range(M)] for _ in range(N)]
    even_cnt = 0
    odd_cnt = 0

    for i in range(N):
        for j in range(M):
            if classroom[i][j] == 'x':
                continue
            if j % 2:
                num[i][j] = even_cnt
                even_cnt += 1
            else:
                num[i][j] = odd_cnt
                odd_cnt += 1

    adj = [[] for _ in range(even_cnt)]
    print(num)
    print(adj)

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

    print(adj)

    vis = [0] * even_cnt
    match = [-1] * odd_cnt
    count = 0

    matched = 0
    print(even_cnt)
    for i in range(even_cnt):
        count += 1
        matched += dfs(i)
        print(count, matched, "AAA")
    print(even_cnt + odd_cnt - matched)
