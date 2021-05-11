"""
백준, 11000 강의실 배정

(1) 빨리 시작하고, 빨리 끝나는 강의 순서로 정렬한 다음
(2) heapq 알고리즘을 이용하여 바로 시작 가능한 강의실 배정
  - 수업이 끝났으면 기존 강의실
  - 끝난 수업이 없으면 새로운 강의실
"""

import sys
import heapq
# sys.stdin = open("C:/Users/JIn/PycharmProjects/coding_Test/input.txt", "rt")


def get_num_classroom(num_lecture, schedule_list):
    hq = []
    for i in range(num_lecture):
        if hq and hq[0] <= schedule_list[i][0]:
            heapq.heappop(hq)
        heapq.heappush(hq, schedule_list[i][1])
    return len(hq)


def solution():
    num_lecture = int(input())
    schedule_list = []
    for _ in range(num_lecture):
        start_time, end_time = map(int, input().split())
        schedule_list.append((start_time, end_time))

    schedule_list.sort()
    return get_num_classroom(num_lecture, schedule_list)

if __name__ == "__main__":
    print(solution())
