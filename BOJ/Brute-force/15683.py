N, M = map(int, input().split())
office = []

for i in range(N):
    office.append(list(map(int, input().split())))

def CCTV(number, y, x):
    global office

    if number == 1:
        pass
    elif number == 2:
        pass
    elif number == 3:
        pass
    elif number == 4:
        pass
    elif number == 5:
        pass

for i in range(N):
    for j in range(M):
        CCTV(office[i][j], j, i)
