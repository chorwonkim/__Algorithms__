croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
words = input()
count = 0
checker = False

for item in croatian:
    count += words.count(item)

print(count, len(words))
print(len(words)-count)