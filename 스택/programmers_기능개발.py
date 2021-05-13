"""
프로그래머스, 기능개발

- 맨 앞 공정의 진도가 100이 되면, 이미 진도가 끝난 연결된 뒷 공정과 함께 배포됨
- 배포된 개수를 리스트에 담아서
- 모든 공정이 종료되면 정답 리턴

: 리스트 pop(0) 했을 때의 시간복잡도를 개선하기 위해 progresses와 sppeds에 역순을 취했음.
"""


def solution(progresses, speeds):
    answer = []
    progresses = progresses[::-1]
    speeds = speeds[::-1]

    while progresses:
        while progresses[-1] < 100:
            for i in range(len(progresses)):
                progresses[i] = progresses[i] + speeds[i]

        cnt = 0
        while progresses and progresses[-1] >= 100:
            progresses.pop()
            # speeds.pop()  it is not necessary.
            cnt += 1
        answer.append(cnt)
    return answer

if __name__ == "__main__":
    # progresses = [93, 30, 55]
    # speeds = [1, 30, 5]
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    solution(progresses, speeds)
