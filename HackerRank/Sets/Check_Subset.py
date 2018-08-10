for _ in range(int(input())):
    _ = int(input())
    list_A = set(map(int, input().split()))
    _ = int(input())
    list_B = set(map(int, input().split()))

    if list_A.issubset(list_B):
        print("True")
    else:
        print("False")

