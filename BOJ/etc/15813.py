from sys import stdin
Read = stdin.readline

N = int(Read())
name = Read().rstrip()
result = 0

for item in name:
    result += ord(item)-64

print(result)