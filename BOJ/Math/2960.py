A, B = map(int, input().split())
value_set = [i for i in range(2, A+1)]
result = []

while len(result) < B:
    # 나눌 값 정하기
    sacrifice_value = value_set[0]

    for value in value_set:
        if value % sacrifice_value == 0:
            value_set.remove(value)
            result.append(value)

        if len(result) == B:
            break

print(result[B-1])