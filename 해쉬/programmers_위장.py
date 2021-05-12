'''
프로그래머스, 위장

위장할 수 있는 조합의 수를 리턴
'''
def solution(clothes):
    number_per_clothes_type = {}
    for _, type in clothes:
        number_per_clothes_type[type] = number_per_clothes_type.get(type, 0) + 1

    res = 1
    for v in number_per_clothes_type.values():
        res *= (v + 1)
    return res - 1

if __name__ == '__main__':
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))
