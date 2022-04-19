n = list(input())
base = len(n)//2
first = [int(i) for i in n[:base]]
second = [int(i) for i in n[base:]]
if sum(first) == sum(second):
    print("LUCKY")
else:
    print("READY")