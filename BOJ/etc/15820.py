from sys import stdin
Read = stdin.readline

s1, s2 = map(int, Read().split())

for _ in range(s1):
    t1, ans = map(int, Read().split())

    if t1 != ans:
        print("Wrong Answer")
        exit()

for _ in range(s2):
    t2, ans = map(int, Read().split())

    if t2 != ans:
        print("Why Wrong!!!")
        exit()

print("Accepted")