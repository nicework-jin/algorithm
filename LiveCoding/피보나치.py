"""
n번째 피보나치 수열? >>>  [1 1 2 3 5 8 13 21]
n = 7이면, 13
n = 8이면, 21
"""


def solution1(n):
    if n == 1 or n == 2:
        return 1

    a = 1
    b = 1
    for i in range(1, n):
        a, b = b, a + b
    return a


def solution2(n):
    if n == 1 or n == 2:
        return 1
    return solution2(n-2) + solution2(n-1)


if __name__ == '__main__':
    n = 8
    print(solution1(n))
    print(solution2(n))