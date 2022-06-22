from sys import stdin
Read = stdin.readline

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2

        if array[mid] == target:
            return mid+1
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None


n = int(Read())
numbers = list(map(int, Read().split()))
numbers.sort()
m = int(Read())
for i in list(map(int, Read().split())):
    if binary_search(numbers, i, 0, n-1):
        print(1)
    else:
        print(0)

    