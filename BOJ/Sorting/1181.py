N = int(input())
result = []

for i in range(N):
    result.append(input())

# 중복 제거를 위한
result = list(set(result))

# 정렬
result.sort(key=str.lower)
result.sort(key=len)

for i in result:
    print(i)
