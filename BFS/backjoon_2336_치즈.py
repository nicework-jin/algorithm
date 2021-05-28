import sys
from collections import deque


INPUT = sys.stdin.readline
N, M = map(int, INPUT().split())
BOARD = [list(map(int, INPUT().split())) for _ in range(N)]
DIRECTION = ((0, -1), (0, 1), (-1, 0), (1, 0))


def cheese_to_air(loc_list):
    for x, y in loc_list:
        BOARD[y][x] = 0


def bfs():
    """ 공기에 닿아 있는 치즈의 좌표들을 구한 뒤, 리스트 형식로 리턴.

    * bfs로 구현 됐음
    - continue 조건: (1)좌표상 범위 (2)방문했던 좌표 (3)치즈를 만났을 때
    """
    outside_cheese_loc_list = []
    visited = [[0] * M for _ in range(N)]
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            next_x = x + DIRECTION[i][0]
            next_y = y + DIRECTION[i][1]
            if (0 > next_x or next_x >= M) or (0 > next_y or next_y >= N):
                continue

            if visited[next_y][next_x] == 1:
                continue

            visited[next_y][next_x] = 1

            if BOARD[next_y][next_x] == 1:
                outside_cheese_loc_list.append((next_x, next_y))
                continue

            q.append((next_x, next_y))
    return outside_cheese_loc_list


def solution():
    """ 공기와 닿은 치즈의 개수가 0이 될 때 까지 넓이 우선 탐색을 반복적으로 수행함.

    while문 종료 후에 반복 수행된 횟수(hour)와 1시간 전 치즈의 개수를 출력(print)함.
    """
    hour = 0
    while outside_cheeses := bfs():
        hour += 1
        cheese_to_air(outside_cheeses)
        cheese_num_1hour_ago = len(outside_cheeses)
    print(hour)
    print(cheese_num_1hour_ago)


if __name__ == '__main__':
    solution()
