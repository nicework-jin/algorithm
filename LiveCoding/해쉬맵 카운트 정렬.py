"""
arr = ['a', 'a', 'b', 'b', 'c', 'd']
각 원소의 합을 구해서 정렬

1. 딕셔너리에 key value 구조로 카운트한다.
2. value를 기준으로 정렬을 수행한다.
"""


def solution(arr):
    each_num = {}
    for alphabet in arr:
        each_num[alphabet] = each_num.get(alphabet, 0) + 1

    sorted_by_num = sorted(each_num.items(), key=lambda x: x[1])
    return list(map(lambda x: x[0], sorted_by_num))


if __name__ == "__main__":
    arr = ['a', 'a', 'b', 'b', 'c', 'd']
    print(solution(arr))