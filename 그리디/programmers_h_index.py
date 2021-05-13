"""
프로그래머스, h-index

h-index에서 h 구하는 조건: 최대 인용 횟수(h)로부터 역순으로 가감하며, 인용된 논문의 개수 >= h인 최초의 h
"""


def solution(citations):
    h = max(citations)
    citations.sort(reverse=True)
    while h >= 0:
        more_than_h = 0
        for i in range(len(citations)):
            if h <= citations[i]:
                more_than_h += 1
            else:
                break
        if h <= more_than_h:
            return h
        h -= 1

if __name__ == "__main__":
    # 3
    citations = [3,0,6,1,5]
    print(solution(citations))
