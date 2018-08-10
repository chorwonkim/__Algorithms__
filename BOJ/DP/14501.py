N = int(input())
T = [0 for _ in range(16)]
P = [0 for _ in range(16)]
answer = 0
result = [0 for _ in range(22)]

for i in range(N):
    t, p = map(int, input().split())

    T[i] = t
    P[i] = p

for i in range(N):
    result[i+1] = max(result[i+1], result[i])
    result[i+T[i]] = max(result[i+T[i]], result[i] + P[i])

print(result[N])
#
#
# def day_checker(days):
#
#     # 이 방법은 쉬는 타이밍을 가져가는 것이 굉장히 애매해진다.
#     # while True:
#     #     if days + T[days-1] < N:
#     #         temp.append(days)
#     #         days += T[days-1]
#     #         continue
#     #     elif days == N:
#     #         if T[days-1] == 1:
#     #             temp.append(days)
#     #         break
#     #     else:
#     #         break
#     #
#     # return temp
#     pass
#
#
# for i in range(1, N+1):
#     day = i
#     result = 0
#
#     cases = day_checker(day)
#
#     print(cases, i)
#
#     if cases:
#         for item in cases:
#             result += P[item-1]
#
#         print(result)
#
#         if result > answer:
#             answer = result
#
#     temp.clear()
#
# print(answer)

# for i in range(N-1, -1, -1):
#     if i + T[i] >= N+1:
#         result[i] = max(result[i+1], 0)
#         continue
#
#     result[i] = max(result[i + T[i]] + P[i], result[i+1])
#
# print(result[0])
