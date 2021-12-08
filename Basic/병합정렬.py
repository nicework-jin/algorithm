import random

"""
병합정렬
[7, 4, 2, 6, 8]
             74268
        742        68
      74    2     6   8
      7  4   2     6   8
  -------------------------
       47  2        68
         247        68
             24678
"""


def merge_sort(s, e):
    if s >= e:
        return

    mid = (s+e) // 2

    merge_sort(s, mid)
    merge_sort(mid+1, e)

    left = s
    right = mid + 1
    tmp = []
    while left <= mid and right <= e:
        if arr[left] <= arr[right]:
            tmp.append(arr[left])
            left += 1

        else:
            tmp.append(arr[right])
            right += 1

    if left <= mid:
        tmp.extend(arr[left:mid+1])
    if right <= e:
        tmp.extend(arr[right:e+1])

    for i in range(len(tmp)):
        arr[s+i] = tmp[i]


def random_list():
    tmp = []
    for _ in range(5):
        n = random.randint(0, 5)
        tmp.append(n)
    return tmp


if __name__ == "__main__":
    arr = random_list()
    merge_sort(0, len(arr) - 1)
    print(arr)