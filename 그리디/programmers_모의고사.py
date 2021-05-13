"""
프로그래머스, 모의고사

반복되는 패턴의 원소들은 나누기(%)로 처리하여 호출한다.
예를 들어, [1,2,3,4,5]가 주어졌을 때 0~1000에 해당하는 인덱스를 출력해야 한다면 => idx % len([1, 2, 3, 4, 5])
"""


def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score_by_person = {'1': 0, '2': 0, '3': 0}
    for i in range(len(answers)):
        if answers[i] == one[i % 5]:
            score_by_person['1'] += 1
        if answers[i] == two[i % 8]:
            score_by_person['2'] += 1
        if answers[i] == three[i % 10]:
            score_by_person['3'] += 1

    max_score = max(score_by_person.values())
    res = []
    for k, v in score_by_person.items():
        if max_score == v:
            res.append(int(k))
    return res

if __name__ == "__main__":
    answer = [1, 2, 3, 4, 5]
    answer = [1, 3, 2, 4, 2]
    print(solution(answer))
