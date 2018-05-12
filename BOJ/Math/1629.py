# Exceed Memory.. B번 곱해서 오류가 나는 거겠지
# A, B, C = map(int, input().split())
# result = [A%C]
#
# for i in range(1, B):
#      result.append((result[i-1] * result[i-1]) % C)
#
# print(result[B-1])

A, B, C = map(int, input().split())

def func_1629(A, B, C):
    if B == 0:
        return 1
    elif B == 1:
        return A % C
    elif B % 2 == 0:
        temp = func_1629(A, B/2, C)
        return (temp * temp) % C
    else:
        # N/2를 위한 꼼수
        return (A * func_1629(A, B-1, C)) % C


print(func_1629(A, B, C))