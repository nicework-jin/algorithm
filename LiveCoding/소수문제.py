def solution(n):
    """
    소수는 1과 자기 자신으로만 나눠지는 수다.
    """
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for number in numbers:
        print(solution(number), number)