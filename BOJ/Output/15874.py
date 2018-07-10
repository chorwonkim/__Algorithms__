from sys import stdin
Read = stdin.readline

k, lsl = map(int, Read().split())
s = Read().rstrip()

while k >= 26:
    k = k % 26

for x in s:
    temp = ord(x) + k
    if x == '.' or x == ',' or x == ' ':
        print(x, end='')
        continue
    elif x.isupper() and temp > 90:
        temp = temp - 26
    elif x.islower() and temp > 122:
        temp = temp - 26

    print(chr(temp), end='')


# print(ord('A'), ord('Z'))
# print(ord('a'), ord('z'))