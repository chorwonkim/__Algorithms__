from itertools import combinations

while True:
    k, *S = map(int, input().split())

    if not k:
        break

    cases = combinations(S, 6)

    for item in cases:
        result = ""
        for j in item:
            result += (str(j) + " ")

        print(result)

    print()
