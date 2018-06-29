from sys import stdin
Read = stdin.readline
# list를 사용할 경우에는 삽입 및 삭제에 O(n)이 사용된다.
# 따라서 총 O(n^2)이 될 수 있으므로 Set 자료구조를 사용했다.
d = set()

for _ in range(int(Read())):
    name, status = map(str, Read().split())

    if status == "enter":
        d.add(name)
    else:
        d.remove(name)

result = list(d)
result.sort(reverse=True)

for item in result:
    print(item)