from sys import stdin
Read = stdin.readline

N = int(input())
items = [0 for _ in range(26)]
result = ''

for _ in range(N):
    name = input()
    items[ord(name[0])-97] += 1

for i in range(26):
    if items[i] >= 5:
        result += chr(i+97)


if result:
    print(result)
else:
    print("PREDAJA")