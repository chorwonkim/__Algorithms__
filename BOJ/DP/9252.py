first_string = input()
second_string = input()
result = [[0 for _ in range(len(second_string)+1)] for _ in range(len(first_string)+1)]
result_string = [["" for _ in range(len(second_string)+1)] for _ in range(len(first_string)+1)]

# for i in range(len(first_string)):
#     result_string[0][i+1] = first_string[i]

# print(result_string)
for i in range(len(first_string)):
    for j in range(len(second_string)):
        if first_string[i] == second_string[j]:
            result[i+1][j+1] = result[i][j] + 1
            result_string[i+1][j+1] = result_string[i][j] + first_string[i]
        else:
            result[i+1][j+1] = max(result[i+1][j], result[i][j+1])

            if result[i+1][j] > result[i][j+1]:
                result_string[i+1][j+1] = result_string[i+1][j]
            else:
                result_string[i+1][j+1] = result_string[i][j+1]

print(max(result[len(first_string)]))
# print(result)
print(result_string[-1][-1])