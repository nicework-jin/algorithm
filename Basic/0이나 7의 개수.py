def solution1(arr):
    one = arr.count(0)
    seven = arr.count(7)
    return one + seven


def solution2(arr):
    cnt = 0
    for n in arr:
        if n == 0 or n == 7:
            cnt += 1
    return cnt


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 0, 7, 7, 7, 7, 7, 0]
    print(solution1(arr))
    print(solution2(arr))
