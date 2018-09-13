import sys
Read = sys.stdin.readline

m, n = map(int, Read().split())
checker = [i for i in range(m+1)]


def union_find(number):
    if number == checker[number]:
        return number

    checker[number] = union_find(checker[number])
    return checker[number]


for i in range(n):
    a, b, c = map(int, Read().split())

    temp1 = union_find(b)
    temp2 = union_find(c)

    if a == 0:
        checker[temp1] = temp2
    elif a == 1:
        if temp1 == temp2:
            print("YES")
        else:
            print("NO")