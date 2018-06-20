from sys import stdin
import bisect
Read = stdin.readline
T = int(Read())
for _ in range(T):
    N = int(Read())

    numbers1 = Read().split()

    for i in range(len(numbers1)):
        numbers1[i] = int(numbers1[i])

    M = int(Read())

    numbers2 = Read().split()

    for i in range(len(numbers2)):
        numbers2[i] = int(numbers2[i])

    numbers1.sort()
    for item in numbers2:
        if bisect.bisect(numbers1, item) != bisect.bisect_left(numbers1, item):
            print(1)
        else:
            print(0)


# a = [4,1,5,2,3]
# b = [1,3,7,9,5]
#
# import bisect
# b.sort() -> [1,3,5,7,9]
# for item in a:
#     x = bisect.bisect(b, item)
#     y = bisect.bisect_left(b, item)
#     z = bisect.bisect_right(b, item)
#     print(x, y, z, str(item))
# 결과값: 2 2 2 4
#       1 0 1 1
#       3 2 3 5
#       1 1 1 2
#       2 1 2 3