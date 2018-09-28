from sys import stdin
Read = stdin.readline

N = int(Read())
students = list(map(int, Read().split()))

B, C = map(int, Read().split())
result = 0

for i in range(N):

    if students[i] < B:
        students[i] = 0
    else:
        students[i] = students[i] - B

    result += 1

    # C로 메꾸기
    result += (students[i] // C)
    if (students[i] % C) > 0:
        result += 1

print(result)