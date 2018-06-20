import sys
# bisect는 sorting 선행 필요!!
Read = sys.stdin.readline
Write = sys.stdout.write

N = int(Read())
An = Read().split()
M = int(Read())
for _ in range(M):
    i, j, k = map(int, Read().split())
    result = 0
    temp = [int(x) for x in An[i-1:j]]
    # temp.sort()
    # O(nlogn)이라서 sort 하면 안될 것 같다.
    # 소팅 과정에서 기수정렬 사용? (O(kn) [k는 자릿수] 이니깐?)
    # 하나씩 비교하는 것도 시간 초과..
    for item in temp:
        if item > k:
            result += 1
        else:
            continue

    print(result)