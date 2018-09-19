for t in range(1, int(input())+1):
    N, number = map(str, input().split())

    temp = str(bin(int(number, 16)))
    # print(temp)

    if number[0] >= '8':
        print("#" + str(t) + " " + temp[2:])
    else:
        print("#" + str(t) + " " + temp[0] + temp[2:])