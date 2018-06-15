for _ in range(3):
    arr = input().split()
    temp = arr.count('1')

    if temp == 0:
        print('D')
    elif temp == 1:
        print('C')
    elif temp == 2:
        print('B')
    elif temp == 3:
        print('A')
    else:
        print('E')
