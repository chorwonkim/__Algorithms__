N = int(input())

result = 0
numbers = [0 for _ in range(3)]

for i in range(1, N+1):
    if i < 100:
        result = i
    elif i == 1000:
        break
    else:
        temp = 0
        time = i

        while time > 0:
            numbers[temp] = time % 10
            time = time // 10
            temp += 1

        if numbers[0] - numbers[1] == numbers[1] - numbers[2]:
            result += 1

print(result)