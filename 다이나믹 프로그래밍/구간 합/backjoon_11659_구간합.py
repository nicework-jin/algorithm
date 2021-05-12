"""
백준, 11659 구간 합 구하기 4

구간 합 알고리즘
(1) 주어진 리스트의 누적합 결과를 리스트(cumulative_sum_list) 1 ~ n의 각 원소에 넣음 (0번 인덱스는 0임).
(2) i ~ j의 구간 합(1 <= i <= j): cumulative_sum_list[j] - commulative_sum_list[i - 1]
"""

import sys

# sys.stdin = open("C:/Users/JIn/PycharmProjects/coding_Test/input.txt", "rt")


def get_cumulative_sum_list(number_list):
    cumulative_sum_list = [0]
    for i in range(len(number_list)):
        cumulative_sum_list.append(cumulative_sum_list[-1] + number_list[i])
    return cumulative_sum_list


def solution():
    n, m = map(int, sys.stdin.readline().split(' '))
    number_list = list(map(int, sys.stdin.readline().split(' ')))

    cumulative_sum_list = get_cumulative_sum_list(number_list)
    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split(' '))
        print(cumulative_sum_list[j] - cumulative_sum_list[i-1])  # get result.

if __name__ == "__main__":
    solution()
