import sys
Read = sys.stdin.readline
N, M = map(int, Read().split())
notebooks_want = [[] for _ in range(N)]


def dfs(x):
    if people[x] == count:
        return 0
    people[x] = count
    for item in notebooks_want[x]:
        if notebook[item-1] == -1 or dfs(notebook[item-1]):
            notebook[item-1] = x
            return 1
    return 0


for i in range(M):
    first, number = map(int, Read().split())

    notebooks_want[first-1].append(number)

people = [0] * N
notebook = [-1] * M
count = 0
matched = 0

for i in range(N):
    count += 1
    matched += dfs(i)

print(matched)

# 정리를 하자면 이분 매칭으로 풀면 되는 문제.
# 근데 웃긴게 조건이 너무 짜증나게 되어있음. 이도 저도 아닌 느낌
# M 값이 5000 이하라고는 하지만, 결론적으로 각 노드의 숫자는 N을 벗어나지 않는다.
# 할당 받지 못하는 사람을 고려할 필요가 없음. 노트북 번호 제한도 동일하기 때문이다.