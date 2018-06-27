from sys import stdin
Read = stdin.readline

chessMap = [list(map(str, Read().rstrip())) for _ in range(8)]
result = 0
for i in range(8):
    for j in range(8):
        if i % 2: # 홀수행
            if j % 2: # 홀수열이 하얀칸
                if chessMap[i][j] == 'F':
                    result += 1

        else: # 짝수행
            if not j % 2: # 짝수열이 하얀칸
                if chessMap[i][j] == 'F':
                    result += 1

print(result)