# pypy3로 컴파일함..
# 실제로 Python 3에서도 통과시키기 위한 리펙토링 필요.

N = int(input())

result = [i for i in range(100001)]

for i in range(2, N+1):
    for j in range(2, i):
        if j*j > i:
            break

        result[i] = min(result[i], result[i-j*j]+1)

print(result[N])