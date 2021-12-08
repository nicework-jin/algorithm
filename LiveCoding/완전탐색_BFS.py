"""
0은 열린 길, 1은 막힌 길이다.
(0,0)에서 (3,3)으로 가는 최단 걸음 수는?

0 0 0 0
0 1 1 1
0 1 0 0
0 0 0 0

1. (0,0)을 큐에 담는다
2. 큐의 첫 번째 원소가 움직일 수 있는 "모든 방향"으로 "1만큼" 이동한다.
  -  만약 다음 스탭이 막혀(1)있으면 큐에 다음 값을 담지 않는다. board[y][x] == 1
  -  다음 스탭이 이미 왔던 길이면 가지 않는다. tmp[y][x] > 0
"""

from collections import deque


def solution(n):
    direction = ((0, 1), (0, -1), (1, 0), (-1, 0))
    tmp = [[0] * n for _ in range(n)]
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            next_x = x + direction[i][0]
            next_y = y + direction[i][1]
            if 0 <= next_x < n and 0 <= next_y < n:
                if board[next_y][next_x] == 1:
                    continue
                if tmp[next_y][next_x] > 0:
                    continue
                tmp[next_y][next_x] = tmp[y][x] + 1
                q.append((next_x, next_y))
    return tmp[n-1][n-1]


if __name__ == '__main__':
    board = [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0], [0, 0, 0, 0]]
    print(solution(len(board)))