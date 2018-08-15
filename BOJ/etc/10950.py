# 10950
import sys
Read = sys.stdin.readline

# for _ in range(int(Read())):
#     a = list(map(int, Read().split()))
#     print(sum(a))


# 10953

# for _ in range(int(Read())):
#     a = list(map(int, Read().split(',')))
#     print(sum(a))


# 11021

# for i in range(int(Read())):
#     a = list(map(int, Read().split()))
#     print("Case #%d: %d" % (i+1, sum(a)))


# 11022
#
# for i in range(int(Read())):
#     a = list(map(int, Read().split()))
#     print("Case #%d: %d + %d = %d" % (i+1, a[0], a[1], sum(a)))


# 15873

temp = Read().rstrip()
result = 0
buffer = False

for item in temp[::-1]:
    if buffer:
        result += 10
        buffer = False
    else:
        if item == str(0):
            buffer = True
            continue

        result += int(item)

print(result)
