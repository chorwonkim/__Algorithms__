from sys import stdin
Read = stdin.readline
result = [[10], [1], [2,4,8,6], [3,9,7,1], [4,6], [5], [6], [7,9,3,1], [8,4,2,6], [9,1]]

for _ in range(int(Read())):
    a, b = map(str, Read().split())
    a_number, b_number = int(a[-1]), int(b)

    temp = b_number % len(result[a_number])

    print(result[a_number][temp-1])