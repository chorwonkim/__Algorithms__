N = int(input())

result = [1, 3]

if N == 1:
    print(result[1])
else:
    for i in range(2, N + 1):
        result.append((result[i-1] * 2 + result[i-2]) % 9901)
    #     result.append((result[i-1]*2) % 9901 + (result[i-2]) % 9901)로 할 경우에는 틀렷다고 나오는데
    #     결괏값의 차이가 아닌 메모리 점유나 시간이 오래 걸리는 경우일 것 같다... (이렇게 추측중)

    print(result[N])
