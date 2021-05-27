import sys
# sys.stdin = open("input.txt", "r")

INPUT = sys.stdin.readline


def solution():
    for _ in range(test_case_num := int(INPUT())):
        types = []
        for _ in range(clothes_num := int(INPUT())):
            _, clothes_type = INPUT().split()
            types.append(clothes_type)

        set_types = set(types)

        cnt_per_type = map(lambda x: types.count(x) + 1, set_types)

        res = 1
        for num in cnt_per_type:
            res *= num
        print(res - 1)

if __name__ == "__main__":
    solution()
