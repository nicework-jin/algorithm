import random
"""
삽입정렬
[7, 4, 2, 6, 8]
7, 4, 2, 6, 8
6, 4, 2, 7, 8
2, 4, 6, 7, 8
2, 4, 6, 7, 8

# 내림차순
- 오른쪽은 이미 정렬되어 있다고 가정한다. arr[-1]
- 0번->4-1번 인덱스로 향하며, 본인보다 큰 숫자가 나오면 교환한다.

# 오름차순
- 오른쪽은 이미 정렬되어 있다고 가정한다. arr[-1]
- 0번->4-1번 인덱스로 향하며, 본인보다 작은 숫자가 나오면 교환한다.
"""


def solution(arr):
    end = len(arr) - 1
    for i in range(end):
        for j in range(i+1, end+1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == "__main__":
    # 정렬이 정상적인지 테스트
    for _ in range(1000):
        arr = []
        for _ in range(5):
            arr.append(random.randint(0, 10))
        if sorted(arr, reverse=True) != solution(arr):
            print(False)
    else:
        print(True)


