import sys
Read = sys.stdin.readline
X = int(Read())
n = 1

while (n**2 + n) < X*2:
    n += 1

temp = X - ((n-1)**2 + (n-1)) // 2

if n % 2 != 0:
    result_a = n-temp+1
    result_b = temp
else:
    result_a = temp
    result_b = n-temp+1

result = str(result_a) + '/' + str(result_b)

print(result)