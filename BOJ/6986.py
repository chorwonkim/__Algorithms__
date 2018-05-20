N, K = map(int, input().split())

scores = []

for i in range(N):
    scores.append(float(input()))

scores.sort()

# 1e-9는 float의 부동소수점 문제로 인해서 추가를 해줘야 한다.
# 자세한 내용은 질문에 잘 나와있으니 정리..
print("%.2f" % (sum(scores[K:N-K])/(N-(K*2))+1e-9))
print("%.2f" % (((scores[K]+scores[N-K-1])*K+sum(scores[K:N-K]))/N+1e-9))