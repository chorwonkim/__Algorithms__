from sys import stdin
Read = stdin.readline

n = int(Read())
cards = list(map(int, Read().split()))
m = int(Read())
numbers = list(map(int, Read().split()))

cards.sort()

for number in numbers:
    start = 0
    end = n-1
    result = False

    while start <= end:
        mid = (start+end) // 2

        if cards[mid] == number:
            result = True
            break
        elif cards[mid] > number:
            end = mid-1
        else:
            start = mid+1

    if result:
        print(1, end=' ')
    else:
        print(0, end=' ')