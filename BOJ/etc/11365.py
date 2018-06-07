import sys
Read = sys.stdin.readline
while True:
    string = Read().rstrip()
    if string == "END":
        break
    else:
        print(string[::-1])
