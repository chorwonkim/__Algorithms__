import sys
Read = sys.stdin.readline
N = int(Read())
scores = list(map(int, Read().rstrip().split()))
result = 0.00

score_max = max(scores)

for score in scores:
    result += (score / score_max) * 100

print("%.2f" % (result/N))