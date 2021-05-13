"""
프로그래머스, 더 맵게

모든 스코빌 지수가 K 이상이 될 때 까지 반복해서 섞는다 => 섞는 최소 횟수 리턴
- 섞은 스코빌 지수 = 스코빌 젤 낮은거 + (스코빌 젤 낮은거보다 하나 높은거 * 2)

## 기존 list 자료형을 heapq로 바꿀 때, heapify라는 함수가 있음.
"""
import heapq


def solution(scoville, k):
    heapq.heapify(scoville)

    time = 0
    while scoville:
        r = heapq.heappop(scoville)
        if r >= k:
            break
        if scoville:
            heapq.heappush(scoville, r + heapq.heappop(scoville)*2)
            time += 1
    else:
        return -1
    return time

if __name__ == "__main__":
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    print(solution(scoville, K))