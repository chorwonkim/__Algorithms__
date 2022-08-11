eq = input().split('-')

number = []

for i in eq:
    sum = 0
    temp = i.split('+')

    for j in temp:
        sum += int(j)

    number.append(sum)

result = number[0]
for i in number[1:]:
    result -= i
print(result)