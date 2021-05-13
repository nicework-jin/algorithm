"""
프로그래머스, 타겟넘버

dfs의 파라미터로 주어진 리스트를 반복적으로 전달하기 싫었음.
따라서 class를 생성하여 numbers와 target 값을 기억하도록 함.
"""

class Answer():
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target
        self.cnt = 0

    def dfs(self, L, number):
        if L == len(self.numbers):
            if number == target:
                self.cnt += 1
            return
        else:
            self.dfs(L + 1, number - numbers[L])
            self.dfs(L + 1, number + numbers[L])


def solution(numbers, target):
    res = Answer(numbers, target)
    res.dfs(0, 0)
    return res.cnt

if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3

    print(solution(numbers, target))
