import sys
import copy
from collections import deque

# sys.stdin = open('input.txt', 'r')

INPUT = sys.stdin.readline
DIRECTION = ((0, 1), (0, -1), (1, 0), (-1, 0))
N, M = map(int, INPUT().split())


def count_safe_area(board):
    cnt = 0
    for y in range(N):
        for x in range(M):
            if board[y][x] == 0:
                cnt += 1
    return cnt


def spread_virus(board, virus_zone):
    q = deque(virus_zone)
    while q:
        x, y = q.popleft()

        for i in range(4):
            next_x = x + DIRECTION[i][0]
            next_y = y + DIRECTION[i][1]

            if 0 <= next_x < M and 0 <= next_y < N:
                if board[next_y][next_x] == 0:
                    board[next_y][next_x] = 2
                    q.append([next_x, next_y])


def find_all_cases(board, safe_zone):
    length = len(safe_zone)

    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                tmp_board = copy.deepcopy(board)

                tmp_board[safe_zone[i][1]][safe_zone[i][0]] = 1
                tmp_board[safe_zone[j][1]][safe_zone[j][0]] = 1
                tmp_board[safe_zone[k][1]][safe_zone[k][0]] = 1
                yield tmp_board


def solution():
    """ 벽(1) 세 개를 세워서 바이러스(2)의 확산을 최대한 막습니다. 이 때, 안전 영역(0)의 최대 개수를 출력합니다.

    * 벽 세 개를 세울 수 있는 모든 경우의 수에 대해 아래 알고리즘을 단계별로 수행합니다.
     (1) 벽 세 개를 세울 수 있는 케이스를 생성합니다.
     (2) 바이러스를 퍼뜨립니다.
     (3) 바이러스를 퍼뜨렸을 때 안전 영역의 크기를 구합니다.
     (4) 최대 안전 영역의 크기로 갱신합니다.
     """
    board = [list(map(int, INPUT().split())) for _ in range(N)]
    safe_zone = []
    virus_zone = []
    res = -1

    for y in range(N):
        for x in range(M):
            if board[y][x] == 0:
                safe_zone.append([x, y])
            if board[y][x] == 2:
                virus_zone.append([x, y])

    # 핵심 알고리즘
    for case in find_all_cases(board, safe_zone):
        spread_virus(case, virus_zone)
        res = max(res, count_safe_area(case))
    return res
print(solution())



