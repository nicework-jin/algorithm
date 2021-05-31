import sys
from itertools import combinations
# sys.stdin = open('input.txt', 'r')

INPUT = sys.stdin.readline


def solution():
    # 카드 세 장의 합(x)이 가장 큰 값을 리턴한다. (조건: x <= m)

    num_cards, m = map(int, INPUT().split())
    cards = map(int, INPUT().split())

    sum_3_each_cards = (a + b + c for a, b, c in combinations(cards, 3))

    res = -1
    for x in sum_3_each_cards:
        if x == m:
            return x
        if x > m:
            continue
        res = max(res, x)
    return res


if __name__ == '__main__':
    print(solution())
