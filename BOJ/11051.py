# DP인 줄 알았는데 아니였음...ㅠ (중복연산 존재)

x, y = map(int, input().split())

for row in range(x+1):
    clearList = 1

    resultList = [clearList]
    # 계산 횟수 때문에 그런 것 같다.
    # 이 코드의 경우에는 첫 항부터 마지막 항까지 계속해서 진행되기 때문에 해당 사항이 없다.
    for i in range(row):
        clearList = clearList * (row - i) * 1 / (i+1)
        resultList.append(int(clearList))

    if row == x:
        print(resultList[y] % 10007)


# DP를 활용한 방법

N, R = map(int, input().split())

result = [[0 for i in range(1001)] for j in range(1001)]
result[0][0] = result[1][0] = result[1][1] = 1
for i in range(2, 1001):
    for j in range(0, i+1):
        if i == j or j == 0:
            result[i][j] = 1
        elif result[i][j] == 0:
            result[i][j] = result[i-1][j-1] + result[i-1][j]

print(result[N][R] % 10007)