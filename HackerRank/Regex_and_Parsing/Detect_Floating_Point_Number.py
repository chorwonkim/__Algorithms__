import re

for i in range(int(input())):
    K = input()

    if bool(re.match("\\+", K)) or bool(re.match("\\-", K)) or bool(re.search(".", K)):
        print(K)
    else:
        print("not")

