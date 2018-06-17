from collections import deque
import sys
Read = sys.stdin.readline

for _ in range(int(Read())):
    order = list(Read().rstrip())
    length = int(Read())
    d = deque(Read().rstrip()[1:-1].split(','))
    if d[0] == '':
        d.popleft()

    rotate_checker = False
    size_checker = False

    for item in order:
        if item == 'R':
            rotate_checker = not rotate_checker
        elif item == 'D':
            if not d:
                sys.stdout.write("error\n")
                size_checker = True
                break
            if rotate_checker:
                d.pop()
            else:
                d.popleft()
        else:
            sys.stdout.write("error\n")
            size_checker = True
            break

    if size_checker:
        continue
    else:
        sys.stdout.write('[')
        while d:

            if rotate_checker:
                if len(d) == 1:
                    sys.stdout.write(d[0])
                else:
                    sys.stdout.write(d[-1] + ',')
                d.pop()
            else:
                if len(d) == 1:
                    sys.stdout.write(d[0])
                else:
                    sys.stdout.write(d[0] + ',')
                d.popleft()

        sys.stdout.write(']\n')