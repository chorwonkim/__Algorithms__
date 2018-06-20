from sys import stdin


# def read():
#     while True:
#         s = stdin.read(100000)
#         print(s)
#         if not s:
#             return
#         while s[-1] != ' ':
#             extra = stdin.read(1)
#             if not extra:
#                 break
#             s += extra
#
#         yield from map(int, s.split())


# from sys import stdin
#
# N = int(stdin.readline())
#
#
# def read():
#     while True:
#         s = stdin.read(10)
#         if not s:
#             return
#         while s[-1] != ' ':
#             extra = stdin.read(1)
#             if not extra:
#                 break
#             s += extra
#         yield from map(int, s.split())
#
#
# y = read()
# print(y)
# while y:
#     print(next(y))

# def teting():
#     y = input().split()
#     for i in y:
#         print(i, "AAA")
#         yield int(i)
#
#
# f = teting()
# print(f)

from sys import stdin
import os
import psutil
import time

process = psutil.Process(os.getpid())
mem_before = process.memory_info().rss / 1024 / 1024


def read():
    while True:
        s = stdin.read(100000)
        if not s:
            return
        while s[-1] != ' ':
            extra = stdin.read(1)
            if not extra:
                break
            s += extra

        yield from map(int, s.split())


t1 = time.clock()

p = read()
count = 0
for i in p:
    print(i)
    count += 1
    if count > 1000:
        break

t2 = time.clock()
mem_after = process.memory_info().rss / 1024 / 1024
total_time = t2 - t1


print("{}MB".format(mem_before))
print("{}MB".format(mem_after))
print("{:.6f}s".format(total_time))