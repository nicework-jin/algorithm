import sys
from itertools import combinations

INPUT = sys.stdin.readline


def solution():
    """  최소 값을 갖는 생성자를 리턴한다.

    *  245      ->  245 + (2 + 4 + 5)
    *  생성자(M) ->  분해합(N)

    (1) 1 ~ n-1 해당하는 범위의 값에 대해 각각 분해합을 구한다.
    (2) 최초로 발견되는 생성자를 답으로 리턴한다. 답이 없으면, 0을 리턴한다.
    """
    for x in range(1, n := int(INPUT())):
        if (get_m := x + sum(map(int, str(x)))) == n:
            return get_m
    return 0


if __name__ == '__main__':
    print(solution())
