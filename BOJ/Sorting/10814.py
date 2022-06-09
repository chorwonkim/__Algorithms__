from sys import stdin
Read = stdin.readline

n = int(Read())
members = []

for i in range(n):
    age, name = Read().split()
    age = int(age)

    members.append((age, i, name))

members.sort()

for i, _, j in members:
    print(i, j)