N, J, H = map(int, input().split())
result = 0
while J != H:
    J = J//2 + J%2
    H = H//2 + H%2
    result += 1
print(result)