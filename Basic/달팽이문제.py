"""
달팽이문제

1    2     3    4    5
16   17    18   19   6
15   24    25   20   7
14   23    22   21   8
13   12    11   10   9

1. (0,0)에서 시작.
2. 수행횟수(k): 5 >> 4 >> 4 >> 3 >> 3 >> 2 >> 2 >> 1 >> 1 >> 0
    - 가로로 움직이고 나서 k-=1 된다.
3. 방향변화 : 열증가 >> 행증가 >> 열감소 >> 행감소 [>> 열증가..]
    - 열/행 둘다 움직이고 증가 / 감소로 바뀜
"""

from collections import deque


def solution(k):
    board = [[0] * k for _ in range(k)]
    n = 0
    x = -1
    y = 0
    num = 1

    while True:
        # 가로로 움직인다
        for _ in range(k):
            n += 1
            x += num
            board[y][x] = n
        k -= 1

        if k == 0:
            break

        # 세로로 움직인다
        for _ in range(k):
            n += 1
            y += num
            board[y][x] = n
        num *= -1
    return board


if __name__ == '__main__':
    k = 5
    board = solution(k)

    for y in range(5):
        for x in range(5):
            print(board[y][x], end=' ')
        print()