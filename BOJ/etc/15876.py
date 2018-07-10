n, k = map(int, input().split())
count = 0
number = 0
temp = ""

while count < 5:
    temp += str(bin(number))[2:]

    if len(temp) > n*(count+1):
        print(temp[count*n+k-1])
        count += 1

    number += 1