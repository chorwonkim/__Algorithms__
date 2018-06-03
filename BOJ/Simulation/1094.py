X = int(input())
result = 0
while X > 0:
    X = (X-1)&X
    result += 1
print(result)