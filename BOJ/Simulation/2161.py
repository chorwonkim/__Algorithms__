from collections import deque
N = int(input())
d = deque(maxlen=N)
for i in range(N):
    d.append(i+1)

# while d:
#     print(d.popleft(), end=" ")
#     d.rotate(-1)

# 2164번의 경우
while len(d) != 1:
    d.popleft()
    d.rotate(-1)

print(d.pop())