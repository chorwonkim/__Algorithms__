# x = int(input())
# number = int(input())
# result = []
# for i in range(x):
#     result.append(number % 10)
#     number = number // 10
#
# print(result)
# print(sum(result))

x = int(input())
numbers = input()
result = 0
for number in numbers:
    # 어짜피 숫자만 들어올 것을 알기에..
    result += int(number)

print(result)
