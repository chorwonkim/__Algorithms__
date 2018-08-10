def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


print(fact(5))

def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)

print(fibo(5))


def fibo_2(x):
    prev, curr = 0, 1

    for _ in range(x):
        yield prev
        prev, curr = curr, prev + curr


print(list(fibo_2(5)))