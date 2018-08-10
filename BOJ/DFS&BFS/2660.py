from sys import stdin
Read = stdin.readline

N = int(Read())
friends = [[N*100 for _ in range(N)] for _ in range(N)]
scores = [0 for _ in range(N)]

for i in range(N):
    friends[i][i] = 1

while True:
    a, b = map(int, Read().split())

    if a == -1 and b == -1:
        break

    friends[a-1][b-1] = friends[b-1][a-1] = 1


for k in range(N):
    for i in range(N):
        for j in range(N):
            if friends[i][j] > (friends[i][k] + friends[k][j]):
                friends[i][j] = (friends[i][k] + friends[k][j])

# print(friends)


for i in range(N):
    scores[i] = max(friends[i])

score = min(scores)
number = scores.count(score)

print(score, number)
for i in range(N):
    if scores[i] == score:
        print(i+1, end=' ')