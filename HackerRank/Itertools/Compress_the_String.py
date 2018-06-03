import sys
from itertools import groupby

string1 = sys.stdin.readline().rstrip()

for i, j in groupby(string1):
    x = '(' + str(list(j).count(i)) + ', ' + str(i) + ')'
    print(x, end=' ')