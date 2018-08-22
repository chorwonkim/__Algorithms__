S = input()
pikachu = ["pi", "ka", "chu"]
result = True

for item in pikachu:
    if item in S:
        continue
    else:
        result = False
        break


if not result:
    print("NO")
else:
    print("YES")