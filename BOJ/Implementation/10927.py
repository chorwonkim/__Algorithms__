import hashlib
str = input()
result = hashlib.md5(str.encode()).hexdigest()
print(result)