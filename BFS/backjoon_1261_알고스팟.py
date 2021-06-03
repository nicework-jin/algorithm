# [백준, 1261] 알고스팟 (BFS 가중치 주기: 메모리 초과 코드와 비교) 글 적음 : https://gaza-anywhere-coding.tistory.com/143

import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
INPUT = sys.stdin.readline
DIRECTION = ((0, 1), (0, -1), (1, 0), (-1, 0))


def solution():
    m, n = map(int, INPUT().split())
    board = [list(map(int, INPUT().rstrip())) for _ in range(n)]
    visited = [[-1] * m for _ in range(n)]

    visited[0][0] = 0
    q = deque([[0, 0]])
    while q:
        x, y = q.popleft()

        for i in range(4):
            next_x = x + DIRECTION[i][0]
            next_y = y + DIRECTION[i][1]

            if (0 > next_x or next_x >= m) or (0 > next_y or next_y >= n):
                continue

            if visited[next_y][next_x] != -1:
                continue

            if board[next_y][next_x] == 0:
                visited[next_y][next_x] = visited[y][x]
                q.appendleft([next_x, next_y])
            else:
                visited[next_y][next_x] = visited[y][x] + 1
                q.append([next_x, next_y])
    return visited[n-1][m-1]
print(solution())
