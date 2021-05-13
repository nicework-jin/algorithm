from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * (bridge_length + 1))
    truck_weights = truck_weights[::-1]
    left_trucks = len(truck_weights)

    time = 1
    while left_trucks > 0:
        if truck_weights and truck_weights[-1] + sum(bridge) <= weight:
            bridge[0] = truck_weights.pop()
        bridge.appendleft(bridge.pop())
        time += 1

        if bridge[-1] > 0:
            bridge[-1] = 0
            left_trucks -= 1
    return time



if __name__ == "__main__":
    bridge_length = 2
    weight = 10
    truck_weight = [7, 4, 5, 6]

    bridge_length = 100
    weight = 100
    truck_weight = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    #
    bridge_length = 100
    weight = 100
    truck_weight = [10]
    print(solution(bridge_length, weight, truck_weight))
