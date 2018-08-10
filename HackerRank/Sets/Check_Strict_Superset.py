A = set(map(int, input().split()))
checker = True

for _ in range(int(input())):
    B = set(map(int, input().split()))

    if A.issuperset(B):
        continue
    else:
        checker = False

if checker:
    print(checker)
else:
    print(checker)
