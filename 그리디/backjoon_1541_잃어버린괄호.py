import sys

INPUT = sys.stdin.readline    # 10+01-1+1


def solution():
    """ 주어진 식에 적절히 괄호를 쳐서 최소 값으로 계산하여 리턴한다.
    """
    exp = INPUT().split('-')

    numbers = []
    for x1 in exp:
        x2 = x1.split('+')

        count = 0
        for num in x2:
            count += int(num)

        numbers.append(count)
    return numbers[0] - sum(numbers[1:])
print(solution())
