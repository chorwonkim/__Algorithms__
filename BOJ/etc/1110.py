N = [int(input())]
result = 0
while True:
    temp_2 = N[-1]%10
    temp_1 = (N[-1]//10 + N[-1]%10) % 10
    temp = temp_2 * 10 + temp_1
    if temp == N[0]:
        break
    N.append(temp)
print(len(N))
