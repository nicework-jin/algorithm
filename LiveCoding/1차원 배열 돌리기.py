"""
1차원 배열 돌리기

[1, 2, 3, 4]
[4, 1, 2, 3]
[3, 4, 1, 2]
[2, 3, 4, 1]
[1, 2, 3, 4]

"""


def solution1(arr):
    """
     제자리로 돌아올 때까지 O(N^2)
    """

    arr.insert(0, arr.pop())


def solution2(arr):
    """
     for문을 이용한 풀이

     1 2 3 [4]  뒤에서부터 반복문 돌리면, 맨 뒤에 숫자만 앞으로 보내주면 되니까.
     4 1 2 3
    """
    tmp = arr[-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[i-1] = arr[i-1], arr[i]
    arr[0] = tmp
    print(arr)


from collections import deque


def solution3(arr):
    """
    O(1)
    """
    arr = deque(arr)
    arr.rotate(1)
    print(arr)


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    # solution1(arr)
    # solution2(arr)
    solution3(arr)



