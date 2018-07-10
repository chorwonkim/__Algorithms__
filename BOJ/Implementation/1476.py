x, y, z = map(int, input().split())
x_status = False
y_status = False
z_status = False


def func_1476(number, item):
    temp = number % item

    if temp == 0:
        temp = item

    return temp


for i in range(1, 7981):
    x_temp = func_1476(i, 15)
    y_temp = func_1476(i, 28)
    z_temp = func_1476(i, 19)

    if x_temp == x:
        x_status = True
    else:
        continue

    if y_temp == y:
        y_status = True
    else:
        continue

    if z_temp == z:
        z_status = True
    else:
        continue

    if x_status and y_status and z_status:
        break

print(i)