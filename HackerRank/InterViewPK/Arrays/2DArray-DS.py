def hourglassSum(arr):
    answer = -100
    for i in range(4):
        for j in range(4):
            result = 0

            result += arr[i][j] + arr[i][j+1] + arr[i][j+2]
            result += arr[i+1][j+1]
            result += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            if answer < result:
                answer = result

    return answer


arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

print(hourglassSum(arr))