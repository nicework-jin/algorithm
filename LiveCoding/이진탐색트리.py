"""
이진탐색트리는 항상 O(logN)를 보장한다.
"""


def solution(s, e):
    if s >= e:
        return None

    mid = (s + e) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return solution(s, mid - 1)

    else:
        return solution(e, mid + 1)


if __name__ == '__main__':
    target = 4
    arr = [1, 2, 4, 8, 10, 12, 14, 16, 18, 20, 22]
    print(solution(0, len(arr)-1))