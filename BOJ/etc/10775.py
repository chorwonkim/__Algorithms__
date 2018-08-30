# import sys
# sys.setrecursionlimit(1000000)
# Read = sys.stdin.readline
#
#
# def func_10775(f_airplaines, p):
#     if p == f_airplaines[p]:
#         return p
#     f_airplaines[p] = func_10775(f_airplaines, f_airplaines[p])
#     return f_airplaines[p]
#
#
# G = int(Read())
# P = int(Read())
#
# airplains = [i for i in range(G+P)]
# result = 0
#
# for i in range(P):
#     x = int(Read())
#     location = func_10775(airplains, x)
#
#     if location == 0:
#         break
#
#     airplains[location] = location - 1
#     result += 1
#
# print(result)
#

# Disjoint-set 문제를 해결하기 위한 Union-Find를 Tree를 활용해서 한 번 해보자.