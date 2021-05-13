from collections import deque


def solution(priorities, location):
    priorities_with_idx = [(priority, idx) for idx, priority in enumerate(priorities)]
    queue = deque(priorities_with_idx)

    cnt = 0
    while True:
        j, j_idx = queue.popleft()

        if any(j < queue[i][0] for i in range(len(queue))):
            queue.append((j, j_idx))
        else:
            cnt += 1
            if j_idx == location:
                return cnt


if __name__ == "__main__":
    # priorities = [2, 1, 3, 2]
    # location = 2

    priorities = [1, 1, 9, 1, 1, 1]
    location = 0

    print(solution(priorities, location))