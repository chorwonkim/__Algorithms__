import sys
Read = sys.stdin.readline

string1 = Read().rstrip()
result = [-1 for _ in range(26)]
result_index = 0

for character in string1:
    i = ord(character) - ord('a')
    if result[i] == -1:
        result[i] = result_index
    result_index += 1

for item in result:
    print(item, end=" ")