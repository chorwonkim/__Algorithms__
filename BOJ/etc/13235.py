import sys

string = sys.stdin.readline().rstrip()


def func_13235(string):
    reverse_string = string[::-1]

    if reverse_string == string:
        return True
    else:
        return False


if func_13235(string):
    print("true")
else:
    print("false")