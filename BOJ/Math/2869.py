import math

A, B, V = map(int, input().split())

# 구하려는 날짜가 N일 때, N = d+1
# v <= d(A-B) + A  => A-B가 N 개 있어야 밤이 지난 것이므로.
# (V-A)/(A-B)가 0보다 클 경우에는 무조건 행동을 헸다는 것이다. 즉, 올림을 해줘야 한다.
print(math.ceil((V-A)/(A-B))+1)