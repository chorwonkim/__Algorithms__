import operator

problems = {}

for i in range(8):
    problems[i] = int(input())

result = sorted(problems.items(), key=operator.itemgetter(1), reverse=True)
summary = []
number = 0

for i in range(5):
    number += result[i][1]
    summary.append(str(result[i][0] + 1))

summary.sort()
print(number)
print(' '.join(summary))