import sys
sys.setrecursionlimit(10000000)
Read = sys.stdin.readline

while True:
    m, n = map(int, Read().split())

    if m == 0 and n == 0:
        break

    inform = [[0, 0, 0] for _ in range(n)]
    checker = [i for i in range(m + 1)]
    result = 0
    allCost = 0

    for i in range(n):
        a, *b = map(int, Read().split())

        inform[i][0], inform[i][1], inform[i][2] = a, b[0], b[1]
        allCost += b[1]

    inform.sort(key=lambda x: x[-1])


    def union_find(number):
        if number == checker[number]:
            return number

        checker[number] = union_find(checker[number])
        return checker[number]


    for i in range(n):
        temp1 = union_find(inform[i][0])
        temp2 = union_find(inform[i][1])

        if temp1 == temp2:
            continue

        checker[temp1] = temp2
        result += inform[i][2]

    print(allCost - result)