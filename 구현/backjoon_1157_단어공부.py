"""
백준, 1157 단어공부
대문자 변환 -> 알파벳별 사용된 횟수 -> 가장 많이 사용된 알파벳 리턴
* 가장 많이 사용된 알파벳이 2개 이상이면 ? 리턴
"""

import sys

# sys.stdin = open("C:/Users/JIn/PycharmProjects/coding_Test/input.txt", "rt")


def get_most_used_alphabet(used_number_alphabet_dict):
    most_used_num = max(used_number_alphabet_dict.values())
    most_used_alphabet = ''
    for alphabet, number in used_number_alphabet_dict.items():
        if most_used_num == number:
            if most_used_alphabet != '':
                return '?'
            most_used_alphabet = alphabet
    return most_used_alphabet


def count_used_number_alphabet(word):
    used_num_alphabet_dict = {}
    for i in range(len(word)):
        used_num_alphabet_dict[word[i]] = used_num_alphabet_dict.get(word[i], 0) + 1
    return used_num_alphabet_dict


def make_upper_case(word):
    return list(map(lambda x: x.upper(), word))


def answer(word):
    upper_cased_word_list = make_upper_case(word)
    used_number_alphabet_dict = count_used_number_alphabet(upper_cased_word_list)
    return get_most_used_alphabet(used_number_alphabet_dict)


if __name__ == "__main__":
    word = input()
    print(answer(word))
