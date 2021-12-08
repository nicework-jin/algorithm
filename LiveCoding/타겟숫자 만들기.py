"""
배열에 들어있는 숫자를 이용해서 타겟 숫자 만들기

    Target : 5

    idx   0 1 2
    value 1 2 4

모든 경우의 수 탐 색 ==> DFS
0 1
0 2
1 2
           0                  x               L == 0
        1     x           1      x            L == 1
     2    x  2   x     2    x  2   x          L == 2
                                              L == 3
"""


def solution(L, v):
    if L == 3:
        if target == v:
            print(target)
        return

    else:
        solution(L + 1, v + arr[L])
        solution(L + 1, v)


if __name__ == '__main__':
    target = 5
    arr = [1, 2, 4]
    solution(0, 0)
