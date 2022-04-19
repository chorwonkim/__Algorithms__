# first method
t = int(input())
a=b=c=0
while t >= 10:
    if t >= 300:
        a += (t // 300)
        t = t % 300
        continue

    if t >= 60:
        b += (t // 60)
        t = t % 60
        continue

    if t >= 10:
        c += (t // 10)
        t = t % 10
        continue

if t == 0:
    print(a, b, c)
else:
    print(-1)

# second method
# T = int(input())
# a=b=c=0

# while T:
#     if T % 10 != 0:
#         break

#     if T >= 300:
#         a += 1
#         T -= 300
#     elif T >= 60:
#         b += 1
#         T -= 60
#     else:
#         c += 1
#         T -= 10

# if T % 10 != 0:
#     print(-1)
# else:
#     print(a, b, c)