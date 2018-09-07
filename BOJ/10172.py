# # What the .........
#
# string1 = "|\_/|"
# string2 = "|q p|   /}"
# string3 = "( 0 )" + '"""' + "\\"
# string4 = '|"^"`    |'
# string5 = """||_/=\\\\__|"""
#
# print(string1)
# print(string2)
# print(string3)
# print(string4)
# print(string5)


# A = [[2,7,5],[3,1,1],[2,1,-7],[0,2,1],[1,6,8]]
#
# def solution(S):
#     N = len(S)
#     M = len(S[N-1])
#     row_sum = []
#     col_sum = []
#     row_index = []
#     col_index = []
#     result = 0
#
#     for i in range(N):
#         row_sum.append(sum(S[i]))
#
#     # 3번째 과정
#     for i in range(N):
#         sum1 = sum(row_sum[:i])
#         sum2 = sum(row_sum[i+1:])
#
#         if sum1 == sum2:
#             row_index.append(i)
#
#     # 4번째 과정
#     for i in range(M):
#         temp_col = 0
#         for j in range(N):
#             temp_col += S[j][i]
#
#         col_sum.append(temp_col)
#
#     for i in range(M):
#         sum1 = sum(col_sum[:i])
#         sum2 = sum(col_sum[i+1:])
#
#         if sum1 == sum2:
#             col_index.append(i)
#
#     return len(row_index) * len(col_index)
#
# print(solution(A))




# import sys
# sys.setrecursionlimit(10000000)
#
#
# def solution(S):
#     temp = S.replace("AA", '').replace("BB", '').replace("CC", "")
#
#     if temp == S:
#         return temp
#     else:
#         return solution(temp)
#
#
# solution("ACCAABBC")
# solution("ABCBBCBA")
# solution("BABABA")

# from collections import deque
#
# def solution(A):
#     if not len(A):
#         return 0
#
#     if len(A) == 1:
#         return A[0]
#
#     A.sort()
#     tot = 0
#
#     d = deque()
#
#     for item in A:
#         d.append(item)
#
#     while len(d) > 1:
#         number1 = d.popleft()
#         number2 = d.popleft()
#         tot += (number1 + number2)
#         d.append(tot)
#
#     return tot
#
# A = [100, 250, 1000]
# print(solution(A))