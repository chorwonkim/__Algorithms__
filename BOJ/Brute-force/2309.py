import sys
from itertools import combinations
Read = sys.stdin.readline
hobits = [0 for _ in range(9)]

for i in range(9):
    hobits[i] = int(Read())

result = combinations(hobits, 7)

for item in result:
    if sum(item) == 100:
        x = sorted(list(map(int, item)))
        print("\n".join(str(i) for i in x))
