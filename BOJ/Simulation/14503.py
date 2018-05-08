robot_dr = [-1, 0, 1, 0]
robot_dc = [0, 1, 0, -1]
Map = []
Zed = []

N, M = map(int, input().split())
robot_r, robot_c, robot_d = map(int, input().split())

for i in range(N):
    temp = list(map(int, input().split()))
    Map.append(temp)
    Zed.append([False]*M)


def trial(r, c, d):
    result = 0

    if not Zed[r][c]:
        result += 1
        Zed[r][c] = True

    moved = False

    for i in range(4):
        d -= 1
        if d < 0:
            d = 3

        changed_r = r + robot_dr[d]
        changed_c = c + robot_dc[d]

        if (not Zed[changed_r][changed_c]) and (not Map[changed_r][changed_c]):
            result += trial(changed_r, changed_c, d)

            moved = True
            break

    if not moved:
        back_d = d + 2
        if back_d > 3:
            back_d %= 4

        changed_r = r + robot_dr[back_d]
        changed_c = c + robot_dc[back_d]

        if Map[changed_r][changed_c] == 0:
            result += trial(changed_r, changed_c, d)

    return result


print(trial(robot_r, robot_c, robot_d))