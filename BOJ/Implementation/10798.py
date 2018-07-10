# items = [[] for _ in range(15)]
# for _ in range(5):
#     temp = list(map(str, input().rstrip()))
#     i = 0
#     for character in temp:
#         items[i].extend(character)
#         i += 1
#
# print(items)
#
# for item in items:
#     print(''.join(item), end='')
#
# print()

result = ''
items = [input() for _ in range(5)]
i = 0
while i < 16:
    for item in items:
        if len(item) > i:
            result += item[i]

    i += 1

print(result)