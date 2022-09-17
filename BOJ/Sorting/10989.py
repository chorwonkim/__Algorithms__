from sys import stdin
Read = stdin.readline

n = int(Read())
count = [0] * 10001

# n의 범위가 10,000,000이기에 이를 모두 저장할 리스트를 만들면 메모리 초과

for _ in range(n):
    count[int(Read())] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)