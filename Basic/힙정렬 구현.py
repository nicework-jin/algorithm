# 잘 모르겠다.
"""
- 힙 정렬은 완전 이진트리를 기본으로 한다
    - 완전 이진트리란, 루트 노드부터 시작해서 왼쪽/오른쪽 노드로 자식 노드가 하나씩 들어가는 자료구조를 말한다.
    - 트리 중간이 비어있지 않은 것이 특징이다.

[힙 정렬 구현]
들어가기 전에, 컨셉을 기억한다.
- *heapify한다.
    - 정렬되지 않은 주어진 리스트에서 heap tree 구성할 때 아래와 같은 공식이 성립한다.
    - "부모 노드 = (자식노드 인덱스-1) // 2"

- *힙 노드가 붕괴되면, 크기를 줄여가면서 반복적으로 heapify한다.
    - 자식 노드 중 큰 것(작은 것)을 고르고
    - 큰 것을 부모 노드와 교환한다.

* heapify란, 부모 노드는 자식 노드보다 크도록(작도록) 구성한다
* 힙 노드 붕괴란, 부모 노드보다 자식 노드가 큰 것을 의미한다.
"""
import random


def heapify(end):
    for i in range(end-1, 0, -1):
        root = (i - 1) // 2
        if arr[root] < arr[i]:
            arr[root], arr[i] = arr[i], arr[root]


def solution():
    end = len(arr)

    # heapSort
    for i in range(end, 0, -1):
        arr[0], arr[end - 1] = arr[end - 1], arr[0]
        end -= 1
        heapify(end)
        print(arr, end)







if __name__ == "__main__":
    arr = [7, 6, 5, 8, 3, 5, 9, 1, 6]
    solution()