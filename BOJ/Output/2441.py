N = int(input())

for i in range(1, N+1):
    a = "*" * (N-i+1)
    print(a.rjust(N))