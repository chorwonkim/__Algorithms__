from sys import stdin
Read = stdin.readline
result = 0

for _ in range(int(Read())):
    result += int(Read())-1

print(result+1)