phone = input()
mapping = [
    ['A','B','C', 3],
    ['D','E','F', 4],
    ['G','H','I', 5],
    ['J','K','L', 6],
    ['M','N','O', 7],
    ['P','Q','R','S', 8],
    ['T','U','V', 9],
    ['W','X','Y','Z', 10]
]
result = 0
for i in phone:
    for j in mapping:
        if i in j:
            result += j[-1]
            break
print(result)