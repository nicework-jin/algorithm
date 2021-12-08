"""
퀵정렬,
 (1) 피벗값을 정하고 (주로 맨 앞: 0번 인덱스)
 (2) 왼쪽-> 오른쪽 방향: 피벗 값보다 큰 최초 값을 찾는다.
 (3) 오른쪽 -> 왼쪽 방향: 피벗 값보다 작은 최초 값 찾는다.
 (4) 2와 3번에서 찾아진 idx 순서가 역순(ex: 4,6)이라면 4번 인덱스와 피벗 인덱스와 교환한다
 (5) 역순이 아니라면, 왼->오 idx와 오_>왼 idx의 값을 교환한다.

 idx : 0 1 2 3 4 5 6 7 8 9
      [5 7 9 0 3 1 6 4 2 8] --> 피벗 5: 1번, 8번 선택 // 정방향이므로 교환
      [5 2 4 0 3 1 6 9 7 8]
      [5 2 4 0 3 1 6 9 7 8] --> 6번, 5번 선택 // 역방향이므로, 더 작은 값을 가지는 값과 피벗 값교환
      [1 2 4 0 3 {5} 6 9 7 8] ---> 5를 기준으로 왼쪽 오른쪽 나뉨. 0번과 7번을 각각 피벗으로 가짐.
                                   여기부터는 왼쪽만 진행하겠음..
     [1 2 4 0 3] 일때
     1 0 4 2 3
     0 {1} 4 2 3
     0 {1} 2 {4} 3
"""


def quick_sort(start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return

    pivot = start  # 피벗은 첫 번째 원소
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]

        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(start, right - 1)
    quick_sort(right + 1, end)


if __name__ == '__main__':
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    quick_sort(0, len(array) - 1)
    print(array)

