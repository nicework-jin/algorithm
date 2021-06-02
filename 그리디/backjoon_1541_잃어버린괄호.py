import sys
INPUT = sys.stdin.readline    # 10+01-1+1


def solution(exp):
    """ 주어진 식에 적절히 괄호를 쳐서 최소 값으로 계산하여 리턴한다.
    """
    numbers = [sum(map(int, x1.split('+'))) for x1 in exp.split('-')]
    return numbers[0] - sum(numbers[1:])

print(solution(INPUT()))
