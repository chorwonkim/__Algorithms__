from sys import stdout
from math import sqrt

N = int(input())
numbers = [2,3,5,7]


def checker_prime(number):
    if number < 2:
        return False

    for i in range(2, int(sqrt(number))+1):
        if number % i  == 0:
            return False

    return True


def func_2023(item, n):
    if n == 0:
        stdout.write(str(item) + '\n')

    for i in range(1, 10, 2):
        temp = item * 10 + i
        if checker_prime(temp):
            func_2023(temp, n-1)


for item in numbers:
    func_2023(item, N-1);
