eq = input()
stands = ['-', '+']
for i in eq:
    temp = ''
    if i not in stands:
        temp += i
    else:
        temp = int(temp)
