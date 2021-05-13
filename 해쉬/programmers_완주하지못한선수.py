# 프로그래머스, 완주하지 못한 선수

def solution(participant, completion):
    not_completed_participant = {}

    for p in participant:
        not_completed_participant[p] = not_completed_participant.get(p, 0) + 1

    for c in completion:
        not_completed_participant[c] -= 1

    for k, v in not_completed_participant.items():
        if v != 0:
            return k

if __name__ == '__main__':
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    print(solution(participant, completion))
