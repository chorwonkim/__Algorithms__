for _ in range(int(input())):
    k = int(input())
    n = int(input())

    graph = [[0] * n for _ in range(k+1)]
    
    for i in range(n):
        graph[0][i] = i+1
    
    for i in range(k+1):
        graph[i][0] = 1

    for i in range(1, k+1):
        for j in range(1, n):
            graph[i][j] = graph[i][j-1] + graph[i-1][j]

    print(graph[-1][-1])