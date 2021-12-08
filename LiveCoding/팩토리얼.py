"""
팩토리얼

5   (n)
4   (n-1)
3   (n-2)
2   (n-3)
1   (n-4)   ----- 종료지점

공식이 있는 문제는 return 값에 공식을 넣고,
끝나는 지점만 잘 설정해주면 된다.
"""


def solution(n):
    if n == 1:
        return 1
    return n * solution(n-1)


if __name__ == "__main__":
    n = 5
    print(solution(5))