def check_people(a, b):
    if a > b:
        return a
    else:
        return b

result = 0
temp = 0

for i in range(4):
    Getoff, Geton = map(int, input().split())

    temp -= Getoff
    result = check_people(result, temp)
    temp += Geton
    result = check_people(result, temp)

print(result)