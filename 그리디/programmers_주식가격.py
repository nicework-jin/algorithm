def solution(prices):
    prices_length = len(prices)
    seconds_list = [0] * prices_length

    for i in range(prices_length - 1):
        curr_price = prices[i]
        for j in range(i+1, prices_length):
            seconds_list[i] += 1
            if curr_price > prices[j]:
                break
    return seconds_list


if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]
    print(solution(prices))