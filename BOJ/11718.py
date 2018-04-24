# for i in range(100):
#     try:
#         a = input()
#     except EOFError as e:
#         e
#     finally:
#         print(a)

string = []
while True:
    try:
        input_data = input()
        if input_data == '':
            break
        else:
            string.append(input_data)
    except EOFError:
        break

for line in string:
    print(line)
