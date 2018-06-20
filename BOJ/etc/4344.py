import sys
for _ in range(int(sys.stdin.readline())):
    student, *args = map(int, sys.stdin.readline().split())
    avg = sum(args) / student
    result = 0

    for item in args:
        if item > avg:
            result += 1
        else:
            continue

    sys.stdout.write("{0:.3f}%\n".format((result/student) * 100))