# 기본 정렬문제, sort/sorted() 쓰지 말고 정렬하기
"""
반복문을 통해 각각의 차수에 min()을 구합니다.  --> min(arr)
이전 차수에 min()으로 나왔던 것은 제외합니다.   --> arr.pop(0)
"""


def solution1(arr):
    res = []
    for i in range(len(arr)):
        idx = arr.index(min(arr))
        res.append(arr.pop(idx))
    return res


def solution2(arr):
    """
        solution1의 답안을 개선합니다.
        min, index 함수를 따로 사용하기에 O(N^3)이 소모됩니다.
        --> for문을 통해 min을 구함과 동시에 idx를 구합니다.
    """
    idx = 0
    res = []
    for i in range(len(arr)):
        mn = 99999
        for j in range(len(arr)):
            if mn > arr[j]:
                mn = arr[j]
                idx = j
        res.append(arr.pop(idx))
    return res


def solution3(arr):
    """
        solution2의 답안을 개선합니다.
        solution2는 여전히 O(n^2)이
    """
    idx = 0
    res = []
    for i in range(len(arr)):
        mn = 99999
        for j in range(len(arr)):
            if mn > arr[j]:
                mn = arr[j]
                idx = j
        res.append(arr.pop(idx))
    return res


import heapq

def solution3(arr):
    """
        solution2의 답안을 개선합니다.
        solution2는 여전히 O(n^2)이다.
        heap_sort를 통해 O(N*logN)을 구현한다.
    """

    heapq.heapify(arr)
    res = []
    while arr:
        r = heapq.heappop(arr)
        res.append(r)
    return res


if __name__ == "__main__":
    arr = [2, 7, 4, 3, 8]

    # print(solution1(arr))
    # print(solution2(arr))
    print(solution3(arr))