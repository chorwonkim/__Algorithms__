import itertools

N = int(input())
K = int(input())
items = []
result = []

for i in range(N):
    items.append(input())

temp = list(itertools.permutations(items, K))

print(temp)
print(len(temp))

for i in temp:
    sum_of_item = ''
    for j in range(K):
        sum_of_item += i[j]
        print(sum_of_item)
    result.append(sum_of_item)

result = set(result)

print(len(result))
