"""
프로그래머스, 소수찾기

['1', '2']이 주어졌을 때 dfs로 모든 조합을 탐색하기 위해 애썼다. 
원하는 결과는 [1, 2, 12, 21]이다.

음..

dfs로 구할 수가 없나? --> 대안으로 itertools 라이브러리의 permutations 사용했음.
"""

from itertools import permutations

def is_prime_number(n):
    if n < 2:
        return False

    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    number_list = list(numbers)
    answer = []
    for i in range(1, len(numbers)+1):
        permutation_list = list(map(''.join, permutations(number_list, i)))
        for permutation in permutation_list:
            number = int(permutation)
            if is_prime_number(number):
                answer.append(number)
    return len(set(answer))
