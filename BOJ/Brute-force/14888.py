from sys import stdin
from itertools import permutations

Read = stdin.readline

N = int(Read())
A = list(map(int, Read().split()))
symbols = list(map(int, Read().split()))
equation = []
max_value = -1000000000
min_value = 1000000000

for i in range(4):
    count = symbols[i]
    for j in range(count):
        if i == 0:
            equation.append('+')
        elif i == 1:
            equation.append('-')
        elif i == 2:
            equation.append('*')
        elif i == 3:
            equation.append('//')

setting = permutations(equation, N-1)

for item in setting:
    temp = str(A[0])

    for i in range(N-1):
        if int(temp) < 0 and item[i] == '//':
            temp = str(int(temp) * -1)
            temp = str(eval((temp + item[i] + str(A[i + 1]))))
            temp = str(int(temp) * -1)
        else:
            temp = str(eval((temp + item[i] + str(A[i+1]))))

    result = eval(temp)
    if max_value < result:
        max_value = result

    if min_value > result:
        min_value = result

print(max_value)
print(min_value)