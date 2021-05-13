"""
프로그래머스, 가장큰수

숫자를 문자 타입으로 정렬 시 주의사항
(1) ['3', '30']에서 '30' > '3'이다. => '허용된 원소 길이-1' 만큼 반복수를 넣어서 해결한다.
  - 주어진 길이가 1000인 경우 333, 303030
  - '허용된 원소 길이 - 1'인 이유는 [9, 991]의 경우, 2배수 늘리면 여전히 99 < 991991이기 때문이다.
  
(2) ['0','0']에서 ''.join(['0','0'])은 '00'이다.
"""

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x: x+x[-1], reverse=True)
    return str(int(''.join(numbers)))

if __name__ == "__main__":
    # numbers = [6, 10, 2]
    numbers = [3, 30, 34, 5, 9]
    print(solution(numbers))
